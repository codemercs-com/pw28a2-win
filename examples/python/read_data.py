#!/usr/bin/env python3
import os
if os.name != "nt":
    raise RuntimeError("This script only runs on Windows!")
import msvcrt
import hid
import sys
import argparse

def get_usb_device_path(vendor_id, interface_number=None):
    """
    Searches for a USB HID device with the given vendor ID and interface number.
    
    Args:
        vendor_id (int): The vendor ID of the device to search for.
        interface_number (int, optional): The interface number of the device to search for.
                                          If None, the first matching device is returned.
    
    Returns:
        str: The path of the found device, or an empty string if nothing was found.
    """
    try:
        for device_dict in hid.enumerate():
            # Filter by vendor ID
            if device_dict.get('vendor_id') != vendor_id:
                continue
            
            # Filter by interface number (if provided)
            if interface_number is not None and device_dict.get('interface_number') != interface_number:
                continue
            
            # Device found — return path
            path = device_dict.get('path')
            if path:
                # Path is a bytes object; convert to string
                if isinstance(path, bytes):
                    return path.decode('utf-8')
                return str(path)
        
        # Nothing found
        return ""
    
    except Exception:
        # On error, return empty string
        return ""

# ---- CLI args ----
parser = argparse.ArgumentParser(description="PhotonWarrior28 HID reader/writer")
parser.add_argument(
    "-a", "--amp",
    type=int,
    choices=range(0, 9),  # only 0..8 allowed
    default=4,
    help="Amplification level (0..8). Default: 4"
)
args = parser.parse_args()

# Device parameters (adjust as needed)
VENDOR_ID = 0x07C0  # 1984 in decimal
INTERFACE_NUMBER = 0  # Interface 0

# Open HID device
js = hid.device()

# Detect path automatically
device_path = get_usb_device_path(VENDOR_ID, INTERFACE_NUMBER)
if not device_path:
    print(f"ERROR: PhotonWarrior28 with Vendor-ID {VENDOR_ID} (0x{VENDOR_ID:04X}) and interface {INTERFACE_NUMBER} not found!")
    print("Available devices:")
    for device_dict in hid.enumerate():
        print(f"  Vendor-ID: {device_dict.get('vendor_id')} (0x{device_dict.get('vendor_id'):04X}), Interface: {device_dict.get('interface_number')}, Product: {device_dict.get('product_string')}")
    sys.exit(1)

print()
print(f"PhotonWarrior28 detected: \033[36m{device_path}\033[0m")
print()
try:
    js.open_path(device_path.encode('utf-8'))
    js.set_nonblocking(True)
except Exception as e:
    print(f"ERROR: Can not open/connect PhotonWarrior28 : {e}")
    sys.exit(1)

def space_pressed() -> bool:
    #Returns True as soon as at least one spacebar press is in the keyboard buffer.
    while msvcrt.kbhit():
        if msvcrt.getch() == b' ':
            return True
    return False

try:
    print("Serial No: \033[35m%s\033[0m" % js.get_serial_number_string())
    print()
    print(f"---SPACEBAR or CTRL+C to exit---")
    print()

    # --- write amplification (1-byte payload: only the level 0..8) ---
    REPORT_ID = 0x00
    amp_value = args.amp  # guaranteed 0..8 by argparse choices

    packet = bytes([REPORT_ID, amp_value])  # exactly 2 bytes total
    packet = packet.ljust(2, b'\x00')  # keeps it at 2 bytes (no-op here)

    try:
        n = js.write(packet)
        if n <= 0:
            print("Write failed or wrote 0 bytes")
    except OSError as e:
        print(f"Write error: {e}")


    #Read once to get the amplification
    report = js.read(64)
    if report:
        btn   = report[4] | (report[5] << 8)
        print(f"Amplification: \033[33m{btn:#06x}\033[0m")

    while True:
        if space_pressed():
            print()
            print("\nSpacebar detected – loop terminated.")
            break
        
        report = js.read(64)
        
        if report:
            data  = report[0] | (report[1] << 8)
            #dummy = report[2] | (report[3] << 8)
            #btn   = report[4] | (report[5] << 8)
            print(f"\rData: \033[32m{data:4d}\033[0m", end='', flush=True)
                  
except KeyboardInterrupt:
    print("\nInterrupted with Ctrl+C – closed cleanly.")
finally:
    js.close()

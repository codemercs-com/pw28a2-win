## PhotonWarrior28A2-USB with python
You can use the PhotonWarrior28A2-USB on Windows with [libusb **hidapi**](https://github.com/libusb/hidapi/releases/tag/hidapi-0.15.0).
To install the *hidapi* package, use **pip**:

```
pip install hidapi
```

After installation, copy hidapi.dll and hidapi.lib into your local Python installation directory, for example:

```
C:\Users\<Username>\AppData\Local\Programs\Python\Python312
```

### Usage: 'read_data.py'
The example code uses the path string to open the correct interface for reading data reports.
Interface 0 is used for reading data; interface 1 is reserved for calibration and production data.
You can set the amplification with the argument **--amp 0..8**. By default, the script uses an amplification of **4**.
```
py .\read_data.py --amp 4
```

#### Terminal color codes
The terminal output uses ANSI color codes for the device path, serial number, amplification, and data.
| Color  | FG normal | BG normal | FG bright | BG bright |
|---|---|---|---|---|
| Black | `\033[30m` | `\033[40m` | `\033[90m` | `\033[100m` |
| Red | `\033[31m` | `\033[41m` | `\033[91m` | `\033[101m` |
| Green | `\033[32m` | `\033[42m` | `\033[92m` | `\033[102m` |
| Yellow | `\033[33m` | `\033[43m` | `\033[93m` | `\033[103m` |
| Blue | `\033[34m` | `\033[44m` | `\033[94m` | `\033[104m` |
| Magenta | `\033[35m` | `\033[45m` | `\033[95m` | `\033[105m` |
| Cyan | `\033[36m` | `\033[46m` | `\033[96m` | `\033[106m` |
| White* | `\033[37m` | `\033[47m` | `\033[97m` | `\033[107m` |

*“White” may appear as light gray depending on your terminal theme.*

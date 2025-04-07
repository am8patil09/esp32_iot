@echo off
setlocal enabledelayedexpansion

:: Set the source directory (the folder containing the .py files you want to upload)
set SOURCE_DIR=./

:: Set the COM port where your ESP32 is connected
set COM_PORT=com6

:: Loop through all .py files in the directory, excluding the batch file
for %%F in (%SOURCE_DIR%\*.py) do (
    :: Skip the batch file itself (if it's in the same directory)
    if "%%~nxF" neq "upload_files.bat" (
        echo Uploading %%F...
        mpremote connect %COM_PORT% cp "%%F" :
    )
)

echo All .py files have been uploaded.
pause

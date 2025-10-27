import subprocess
import time
import sys
import os
import signal

# --- CONFIGURATION ---
APP_PACKAGE = "com.ten.appchamcong"  # 👈 change this to your actual app package name
WAIT_APP_OPEN = 5                    # seconds to wait for app to load
WAIT_SCRCPY_START = 3                # seconds to wait for scrcpy to start

# Coordinates of buttons (adjust as needed)
CHECKIN_BUTTON_COORD = (500, 1600)   # (x, y) of Check In button
CHECKOUT_BUTTON_COORD = (900, 1600)  # (x, y) of Check Out button

# --- FUNCTIONS ---
def run(cmd):
    subprocess.run(cmd, shell=True)

def check_device_connected():
    """Check if Android device is connected via ADB"""
    print("🔍 Checking device connection...")
    result = subprocess.run("adb devices", shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    connected_devices = [line for line in lines[1:] if '\tdevice' in line]

    if not connected_devices:
        print("❌ No Android device connected! Please connect your phone via USB and enable USB debugging.")
        sys.exit(1)
    else:
        print(f"✅ Device connected: {connected_devices[0].split('\t')[0]}")

def start_scrcpy():
    """Start scrcpy in background"""
    print("�️  Starting scrcpy...")
    try:
        # Start scrcpy in background mode
        process = subprocess.Popen("scrcpy", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(WAIT_SCRCPY_START)

        # Check if scrcpy is still running (not crashed)
        if process.poll() is None:
            print("✅ scrcpy started successfully!")
            return process
        else:
            print("❌ scrcpy failed to start!")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting scrcpy: {e}")
        sys.exit(1)

def open_app():
    print("�📱 Opening attendance app...")
    run(f"adb shell monkey -p {APP_PACKAGE} -c android.intent.category.LAUNCHER 1")
    time.sleep(WAIT_APP_OPEN)

def tap(x, y):
    run(f"adb shell input tap {x} {y}")

def cleanup_scrcpy(process):
    """Clean up scrcpy process"""
    if process and process.poll() is None:
        print("🧹 Cleaning up scrcpy...")
        process.terminate()
        time.sleep(1)
        if process.poll() is None:
            process.kill()

# --- MAIN ---
if len(sys.argv) < 2 or sys.argv[1] not in ["checkin", "checkout"]:
    print("Usage:")
    print("  python attendance.py checkin")
    print("  python attendance.py checkout")
    sys.exit(1)

action = sys.argv[1]
scrcpy_process = None

try:
    # Check device connection first
    check_device_connected()

    # Start scrcpy
    scrcpy_process = start_scrcpy()

    # Open the attendance app
    open_app()

    if action == "checkin":
        x, y = CHECKIN_BUTTON_COORD
        tap(x, y)
        print("✅ Checked IN successfully!")

    elif action == "checkout":
        x, y = CHECKOUT_BUTTON_COORD
        tap(x, y)
        print("✅ Checked OUT successfully!")

    # Wait a moment to ensure the tap was registered
    time.sleep(2)

except KeyboardInterrupt:
    print("\n⚠️  Process interrupted by user")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    # Clean up scrcpy process
    if scrcpy_process:
        cleanup_scrcpy(scrcpy_process)

    # Optional: close the app afterward
    # run(f"adb shell am force-stop {APP_PACKAGE}")
    print("🏁 Process completed!")

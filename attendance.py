import subprocess
import time
import sys

# --- CONFIGURATION ---
APP_PACKAGE = "com.ten.appchamcong"  # 👈 change this to your actual app package name
WAIT_APP_OPEN = 5                    # seconds to wait for app to load

# Coordinates of buttons (adjust as needed)
CHECKIN_BUTTON_COORD = (500, 1600)   # (x, y) of Check In button
CHECKOUT_BUTTON_COORD = (900, 1600)  # (x, y) of Check Out button

# --- FUNCTIONS ---
def run(cmd):
    subprocess.run(cmd, shell=True)

def open_app():
    print("📱 Opening attendance app...")
    run(f"adb shell monkey -p {APP_PACKAGE} -c android.intent.category.LAUNCHER 1")
    time.sleep(WAIT_APP_OPEN)

def tap(x, y):
    run(f"adb shell input tap {x} {y}")

# --- MAIN ---
if len(sys.argv) < 2 or sys.argv[1] not in ["checkin", "checkout"]:
    print("Usage:")
    print("  python attendance.py checkin")
    print("  python attendance.py checkout")
    sys.exit(1)

action = sys.argv[1]

open_app()

if action == "checkin":
    x, y = CHECKIN_BUTTON_COORD
    tap(x, y)
    print("✅ Checked IN successfully!")

elif action == "checkout":
    x, y = CHECKOUT_BUTTON_COORD
    tap(x, y)
    print("✅ Checked OUT successfully!")

# Optional: close the app afterward
# run(f"adb shell am force-stop {APP_PACKAGE}")

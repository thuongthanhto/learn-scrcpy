# 📱 Auto Attendance via ADB + scrcpy

Script Python giúp tự động mở ứng dụng chấm công trên điện thoại Android và bấm nút **Check In / Check Out** thông qua `adb`.

---

## ⚙️ Yêu cầu

Trước khi chạy, cần chuẩn bị:

1. **Cài đặt các công cụ cần thiết:**
   - [Python 3](https://www.python.org/downloads/)
   - [ADB (Android Platform Tools)](https://developer.android.com/tools/releases/platform-tools)
   - [scrcpy](https://github.com/Genymobile/scrcpy)

2. **Kết nối thiết bị Android:**
   - Bật **Developer Options** và **USB Debugging** trên điện thoại.
   - Kết nối điện thoại với máy tính qua cáp USB.
   - Kiểm tra kết nối:
     ```bash
     adb devices
     ```
     Nếu thấy thiết bị hiển thị trong danh sách là OK.

---

## 🚀 Cách chạy script

1. Clone hoặc tải file `attendance.py` về.
2. Mở terminal hoặc Command Prompt tại thư mục chứa file.
3. Chạy một trong hai lệnh sau:

   ```bash
   # Chấm công (Check In)
   python attendance.py checkin

   # Ra về (Check Out)
   python attendance.py checkout
   ```

---

## 🧭 Cách xác định tọa độ nút Check In / Check Out

Nếu bạn chưa biết tọa độ của nút chấm công, làm như sau:

1. **Mở app chấm công trên điện thoại qua scrcpy:**

   ```bash
   scrcpy
   ```

2. **Trong cửa sổ terminal, gõ lệnh:**

   ```bash
   adb shell getevent -l
   ```

3. **Nhấp chuột vào nút "Chấm công" trong cửa sổ scrcpy.**

4. **Quan sát terminal** — bạn sẽ thấy các dòng hiển thị giá trị như:

   ```text
   ABS_MT_POSITION_X 00000210
   ABS_MT_POSITION_Y 00000650
   ```

   Đây chính là tọa độ X và Y của vị trí bạn đã bấm.

5. **Lấy hai giá trị này** (chuyển sang số thập phân nếu cần) và cập nhật trong file `attendance.py`:

   ```python
   CHECKIN_BUTTON_COORD = (X, Y)
   CHECKOUT_BUTTON_COORD = (X2, Y2)
   ```



# 🪟 Cách tự động chấm công trên Windows bằng Task Scheduler

## 🔹 1. Tạo 2 file .bat để gọi script Python

Giả sử bạn đã có file `attendance.py` ở thư mục:

```text
C:\attendance\attendance.py
```

Tạo 2 file:

### `checkin.bat`

```batch
@echo off
cd /d "C:\attendance"
python attendance.py checkin
```

### `checkout.bat`

```batch
@echo off
cd /d "C:\attendance"
python attendance.py checkout
```

---

## 🔹 2. Mở Task Scheduler

Bấm **Win + R**, gõ `taskschd.msc`, **Enter**.

---

## 🔹 3. Tạo task Check In (7h sáng)

1. Chọn **Create Task…**

2. **Tab General**
   - **Name:** `Attendance Check-In`
   - Chọn **Run whether user is logged on or not**
   - Tick **Run with highest privileges**

3. **Tab Triggers** → **New…**
   - **Begin the task:** `On a schedule`
   - **Daily, Repeat every:** `1 days`
   - **Start:** `07:00:00`
   - Tick **Enabled**
   - Chọn **Settings** → **Weekly** → **Mon, Tue, Wed, Thu, Fri**

4. **Tab Actions** → **New…**
   - **Action:** `Start a program`
   - **Program/script:** đường dẫn đến `checkin.bat`

     ```text
     C:\attendance\checkin.bat
     ```

5. **Tab Conditions** → bỏ chọn **"Start the task only if the computer is on AC power"** (nếu cần).

6. Nhấn **OK**.

---

## 🔹 4. Tạo task Check Out (5h chiều)

Làm tương tự, chỉ khác:

- **Name:** `Attendance Check-Out`
- **Time:** `17:00:00`
- **Program/script:** `C:\attendance\checkout.bat`
- Lặp lại **thứ 2 → thứ 6**

---

## 🔹 5. Xong ✅

Giờ mỗi ngày máy bạn sẽ tự mở app và tap nút checkin/checkout đúng giờ, **không chạy vào thứ 7 - Chủ nhật**.

---

## 📝 Lưu ý bổ sung

- Đảm bảo điện thoại luôn được kết nối USB với máy tính
- Python và ADB phải được cài đặt và thêm vào PATH
- Kiểm tra task hoạt động bằng cách chạy thử trước khi thiết lập lịch chính thức
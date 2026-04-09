# Logic Analyzer GUI

Phần mềm giao diện phân tích tín hiệu logic (Logic Analyzer) hiệu năng cao, được thiết kế chuyên biệt cho đồ án hệ thống nhúng với giao diện Dark Mode chuẩn kỹ thuật. 
Logic Analyzer này có thể sử dụng kết hợp với bất kỳ vi điều khiển nào (như **Raspberry Pi Pico 2, STM32, Arduino, hay FPGA**), miễn là thiết bị có khả năng gửi dữ liệu qua cổng UART/Serial ảo.

## Tải Ứng dụng ngay (Dành cho Windows) - Không cần cài đặt Code
Nếu bạn muốn gửi phần mềm cho nhóm làm chung, hay lưu trữ để nộp BTL thì không cần cài Python để mở mã nguồn! Thiết kế kho mã nguồn được tự động đóng gói bằng **Github Actions**.

1. Nhấp vào tab **[Actions]** hiển thị ngay trên danh sách các thư mục mã nguồn tại website GitHub này.
2. Click chọn Workflow run có tích nút tick xanh ✅ trên cùng trên danh sách. 
3. Trang thông tin bản build mở ra, bạn cuộn màn hình lăn tay xuống sát tận đáy đến khu vực **Artifacts**.
4. Bấm click tải file nhãn mang tên **`LogicAnalyzer-Windows`**.
5. Giải nén file Zip tải về, bạn sẽ có ngay một con app cực xịn tên `LogicAnalyzer.exe` chạy độc lập. Bấm chạy luôn lập tức!

---

## Tính năng chính
* **Hiển thị thời gian thực xé gió**: Sử dụng sức mạnh vẽ ma trận từ Numpy & `PyQtGraph` (hướng luồng đồ hoạ) để render hàng triệu điểm lấy mẫu mà không gặp tình trạng đơ hình như thường thấy.
* **Hỗ trợ Đa Kênh Linh Hoạt**: Cung cấp cấu hình tùy ý 2, 4, 8, 16, hoặc tăng lên chót vót tới 24 kênh. Chống lại Topic 1 (chạy vi xử lý thông thường) và Topic 2 (FPGA tần số cao). 
* **Simulator Mock Device**: Gắn sẵn module giả lập luồng tín hiệu ở Menu cổng COM mang tên `MOCK (Simulator)`. Hãy bấm nút Capture xem hình ảnh dòng sóng chạy dập dềnh liên hồi mà chưa đòi trang bị mạch thực!
* **Trình phiên dịch luồng tín hiệu 2 Định Dạng**:
   * **Text Format**: Phù hợp cho gỡ lỗi, Board phát các xung như chuỗi serial `"1,0,1,0\n"`.
   * **Binary Format**: Chế độ đẩy băng thông đỉnh. Ghép cọc trạng thái 8 Pin GPIO thành vỏn vẹn 1 Bytes duy nhất lao qua dây vật lý lên máy xử lý!

## Dành cho Sinh Viên Mở Code (Phát triển cục bộ)
Dự án được mã hóa trọn vẹn tại ngôn ngữ Python `(Python 3.8+)`.
Tiến hành Clone Repo này với Terminal:
```bash
# Tạo môi trường độc quyền
python3 -m venv venv
source venv/bin/activate
# (Dành cho Win mở với cmd gõ): venv\Scripts\activate.bat

# Cài đặt nền tảng phụ thuộc
pip install -r requirements.txt

# Bấm máy Logic
python main.py
```

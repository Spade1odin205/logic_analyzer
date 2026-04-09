# Logic Analyzer GUI

Phần mềm giao diện phân tích tín hiệu logic (Logic Analyzer) hiệu năng cao, được thiết kế chuyên biệt cho đồ án hệ thống nhúng với giao diện Dark Mode chuẩn kỹ thuật. 
Logic Analyzer này có thể sử dụng kết hợp với bất kỳ vi điều khiển nào (như **Raspberry Pi Pico 2, STM32, Arduino, hay FPGA**), miễn là thiết bị có khả năng gửi dữ liệu qua cổng UART/Serial ảo.

## Tính năng chính
* **Hiển thị thời gian thực xé gió**: Sử dụng sức mạnh vẽ ma trận từ Numpy & `PyQtGraph` (hướng luồng đồ hoạ) để render hàng triệu điểm lấy mẫu mà không gặp tình trạng đứng hình máy như các phần mềm truyền thống.
* **Hỗ trợ Đa Kênh Linh Hoạt**: Cung cấp cấu hình 2, 4, 8, 16, hoặc lên tới 24 kênh, dễ dàng đối ứng Topic 1 (chạy MCU bình thường) hoặc Topic 2 (FPGA tần số cao). Đầu ra đồ thị sẽ tự động trải dàn và phân luồng!
* **Simulator Mock Device**: Gắn sẵn module giả lập tín hiệu ở cổng COM mang tên `MOCK (Simulator)`. Bạn có thể chạy ngay giao diện, bấm Capture để thấy sóng chạy thử mà chưa cần chạm tay vào làm mạch phần cứng!
* **Trình phiên dịch luồng dữ liệu 2 chế độ**:
   * **Text Format**: Phù hợp cho debug ban đầu, board gửi lên đơn giản như `"1,0,1,0\n"`.
   * **Binary Format**: Chế độ Production tốc độ cao. Dồn trạng thái của 8 kênh GPIO vào 1 Byte nhị phân để bắn lên PC giúp bảo vệ băng thông UART siêu việt!

## Cấu trúc Hệ thống
1. `main.py`: Điểm neo chạy của chương trình và tích hợp giao diện GUI (PyQt6).
2. `main_window.py`: Đóng gói logic đồ họa, thanh công cụ, các biểu đồ (pyqtgraph).
3. `serial_worker.py`: Lớp luồng ngầm (QThread) sử dụng ngắt hệ đệm để giam dữ liệu từ `pyserial`, bảo vệ Thread chính khỏi treo.
4. `data_parser.py`: Lõi phiên dịch frame dữ liệu thô sang các trạng thái logic 0 1 và nhóm nó vào Numpy Array.
5. `mock_device.py`: Vi điều khiển giả lập ngẫu nhiên nhả sóng vuông.

## Cài đặt Môi trường (Installation)
Dự án được viết hoàn toàn trên ngôn ngữ Python.
Yêu cầu: `Python 3.8+`

Mở terminal và gõ các lệnh sau:
```bash
# Ưu tiên tạo môi trường riêng
python3 -m venv venv

# Kích hoạt venv (Trường hợp bạn dùng Linux/MacOS)
source venv/bin/activate
# (Trường hợp bạn dùng Windows): venv\Scripts\activate.bat

# Cài đặt thư viện cần thiết
pip install -r requirements.txt
```

## Chạy Ứng dụng (Run)
Khi venv đang chạy ở terminal, khởi động phần mềm máy hiện sóng qua lệnh:
```bash
python main.py
```

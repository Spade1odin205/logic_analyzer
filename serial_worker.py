import serial
import time
from PyQt6.QtCore import QThread, pyqtSignal

class SerialWorker(QThread):
    data_received = pyqtSignal(bytes)
    error_occurred = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.is_running = False

    def run(self):
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=0.1)
            self.is_running = True
            
            # Continuous reading loop
            while self.is_running:
                if self.serial_conn.in_waiting > 0:
                    # Read up to 4096 bytes per iteration to be fast
                    data = self.serial_conn.read(max(4096, self.serial_conn.in_waiting))
                    if data:
                        self.data_received.emit(data)
                else:
                    # Very short sleep to yield control
                    time.sleep(0.001)
                    
        except Exception as e:
            self.error_occurred.emit(str(e))
        finally:
            if self.serial_conn and self.serial_conn.is_open:
                self.serial_conn.close()

    def stop(self):
        self.is_running = False
        self.wait(1000) # wait up to 1 second for thread to terminate quietly

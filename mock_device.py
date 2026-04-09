from PyQt6.QtCore import QThread, pyqtSignal
import time
import random

class MockWorker(QThread):
    data_received = pyqtSignal(bytes)
    error_occurred = pyqtSignal(str)

    def __init__(self, mode='binary', channels=8, baudrate=115200):
        super().__init__()
        self.mode = mode
        self.channels = channels
        self.baudrate = baudrate
        self.is_running = False
        self.states = [0] * channels

    def run(self):
        self.is_running = True
        
        while self.is_running:
            # Simulate data generation based on mode
            time.sleep(0.01) # generate data every 10ms
            
            # small chance to flip a bit for each channel to simulate logic events
            for i in range(self.channels):
                if random.random() < 0.05:
                    self.states[i] = 1 - self.states[i]
            
            # Pack data
            if self.mode == 'binary':
                val = 0
                for i in range(self.channels):
                    if self.states[i]:
                        val |= (1 << i)
                # duplicate the byte 20 times to simulate fast steady signal
                b = val.to_bytes((self.channels + 7) // 8, byteorder='little')
                if self.is_running:
                    self.data_received.emit(b * 20)
                    
            elif self.mode == 'text':
                line = ",".join(str(s) for s in self.states) + "\n"
                b = (line * 20).encode('utf-8')
                if self.is_running:
                    self.data_received.emit(b)

    def stop(self):
        self.is_running = False
        self.wait(1000)

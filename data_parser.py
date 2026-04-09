import numpy as np

class DataParser:
    def __init__(self, channels=8, mode='binary'):
        self.channels = channels
        self.mode = mode  # 'binary' or 'text'
        self.buffer = bytearray()
        
    def parse(self, raw_data):
        """
        Receives raw bytes from serial.
        Returns a list of parsed integer samples.
        Each sample is an integer where bits represent channel states.
        """
        self.buffer.extend(raw_data)
        samples = []
        
        if self.mode == 'binary':
            # 1 byte = 8 channels, 2 bytes = 16 channels...
            bytes_per_sample = (self.channels + 7) // 8
            
            if bytes_per_sample == 0:
                return []

            while len(self.buffer) >= bytes_per_sample:
                sample_bytes = self.buffer[:bytes_per_sample]
                self.buffer = self.buffer[bytes_per_sample:]
                value = int.from_bytes(sample_bytes, byteorder='little')
                samples.append(value)
                
        elif self.mode == 'text':
            # expecting comma separated values ending with newline. e.g. "1,0,1,1\n"
            while b'\n' in self.buffer:
                line_end = self.buffer.find(b'\n')
                line = self.buffer[:line_end].decode('utf-8', errors='ignore').strip()
                self.buffer = self.buffer[line_end + 1:]
                
                if line:
                    try:
                        parts = line.split(',')
                        val = 0
                        for i, p in enumerate(parts):
                            if i < self.channels and p.strip() == '1':
                                val |= (1 << i)
                        samples.append(val)
                    except Exception:
                        pass
        return samples

    def extract_channels_numpy(self, samples):
        """
        Given a list of integer samples, return a list (length = channels) 
        of numpy arrays containing 0 and 1.
        """
        if not samples:
            return [np.array([], dtype=np.int8) for _ in range(self.channels)]
            
        samples_arr = np.array(samples, dtype=np.uint32)
        ch_data = []
        for i in range(self.channels):
            bit_array = (samples_arr >> i) & 1
            ch_data.append(bit_array.astype(np.int8))
            
        return ch_data

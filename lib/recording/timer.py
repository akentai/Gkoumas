from .recorder import Recorder
import numpy as np
from time import time

class TimerRecorder(Recorder):

    def __init__(self,
                 fs: int = 48000,
                 channels: int = 1,
                 stop_interval: int = 10):
        Recorder.__init__(self, fs, channels)
        self.stop_interval = stop_interval

    def record(self) -> np.ndarray:
        # Flush read buffer
        self.rdbuffer = list()
        # Start stream
        self.input_stream.start()
        # Get recording start time
        start_time = time()

        print("Started recording.")

        while time() - start_time < self.stop_interval:
            data, overflow = self.input_stream.read(self.input_stream.read_available)
            self.rdbuffer.append(data)

        print("Recording stopped by timer.")

        return np.concatenate(self.rdbuffer, axis=0)

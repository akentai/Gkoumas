from abc import ABC, abstractmethod
from sounddevice import InputStream, play
import numpy as np
from scipy.io.wavfile import write


class Recorder(ABC):

    def __init__(self,
                 fs: int = 48000,
                 channels: int = 1,
                 playback: bool = False):
        self.fs = fs
        self.channels = channels
        self.input_stream = InputStream(samplerate=self.fs, channels=self.channels)
        self.rdbuffer: list[np.ndarray] = list()

    @abstractmethod
    def record(self) -> np.ndarray:
        pass

    def playback(self, data: np.ndarray):
        print("Playing recorded audio")
        play(data, self.fs, blocking=True)

    def to_file(self, name, data):
        write(name, self.fs, data)
    



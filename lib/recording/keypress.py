from .recorder import Recorder
import numpy as np
from pynput import keyboard

class KeyPressRecorder(Recorder):
    
    def __init__(self,
                 fs: int = 48000,
                 channels: int = 1):
        Recorder.__init__(self, fs, channels)

    def record(self) -> np.ndarray:
        # On key-press event
        def _on_keypress(key):
            if key.char == 'q':
                self.input_stream.stop()

        # Setup the event listener
        listener = keyboard.Listener(on_press=_on_keypress)
        listener.start()

        # Flush read buffer
        self.rdbuffer = list()
        # Start stream
        self.input_stream.start()

        print("Started recording.")

        try:
            while self.input_stream.active:
                data, overflow = self.input_stream.read(self.input_stream.read_available)
                self.rdbuffer.append(data)
        except:
            pass

        listener.stop()

        print("Recording stopped by user.")

        return np.concatenate(self.rdbuffer, axis=0)

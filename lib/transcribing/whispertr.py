from .transcriber import Transcriber
import whisper


class WhisperTranscriber(Transcriber):

    def __init__(self, model="base"):
        self.model = whisper.load_model(model)

    def transcribe(self, filename: str) -> str:
        audio = whisper.load_audio(filename)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        res = whisper.decode(self.model, mel)

        return res.text

from .transcriber import Transcriber
import os
from speechmatics.models import BatchTranscriptionConfig
from speechmatics.batch_client import BatchClient


class SpeechmaticsTranscriber(Transcriber):

    def __init__(self):
        self.language = "auto" # auto-detect language
        self.client = BatchClient(os.environ["SPM_API_KEY"])
        self.conf = {
                "type": "transcription",
                "transcription_config": {
                    "language": self.language
                },
                "language_identification_config": {
                    "low_confidence_action": "allow",
                    "default_language": "en"
                }
        }


    def transcribe(self, filename: str) -> str:
        with self.client:
            job_id = self.client.submit_job(filename, self.conf)
            transcript = self.client.wait_for_completion(job_id)
            print(transcript)
            return ""

from .transcriber import Transcriber
import os
import deepgram


class DeepgramTranscriber(Transcriber):

    def __init__(self):
        self.client = deepgram.DeepgramClient(api_key=os.environ["DGR_API_KEY"])
        self.options = deepgram.PrerecordedOptions(model="nova-2-general",
                                                   detect_language=True,
                                                   punctuate=True,
                                                   smart_format=True)


    def transcribe(self, filename: str) -> str:
        audio = open(filename, "rb")
        data = audio.read()
        audio.close()

        source = {"buffer": data}

        res = self.client.listen.prerecorded.v("1").transcribe_file(
                source, self.options
        )

        return res.to_json(indent=4)


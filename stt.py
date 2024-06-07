from lib.recording import *
from lib.transcribing import *
import argparse
from scipy.io.wavfile import read
from sounddevice import play, wait


if __name__ == "__main__":

    # Parsing audio data
    parser = argparse.ArgumentParser(prog="sst")

    # Input file
    parser.add_argument("-i", "--input",
                        default=None, help="Path to audio file")

    # Recording arguments
    parser.add_argument("-r", "--recorder",
                        default="keypress", help="Specify the recorder type",
                        choices=["keypress", "timer"])
    parser.add_argument("-s", "--stop-interval",
                        type=int, default=10, help="""If timer recording is
                        enabled then specify the seconds to stop since
                        recording""")
    parser.add_argument("--play", action="store_true",
                        help="Playback the recording")

    # Transcribing arguments
    parser.add_argument("-t", "--transcriber", default="whisper",
                        choices=["whisper", "deepgram", "speechmatics"], help="""Decide the
                        type of transcriber""")

    args = parser.parse_args()

    if args.input is not None:
        filename = args.input
    else:
        # Use microphone recording
        filename = "record.wav"

        if args.recorder == "keypress":
            recorder = KeyPressRecorder()
        else:
            recorder = TimerRecorder(stop_interval=args.stop_interval)

        data = recorder.record()

        recorder.to_file(filename, data)

    if args.play:
        fs, data = read(filename)
        play(data, fs)

    if args.transcriber == "whisper":
        transcriber = WhisperTranscriber(model="small")
    elif args.transcriber == "deepgram":
        transcriber = DeepgramTranscriber()
    elif args.transcriber == "speechmatics":
        transcriber = SpeechmaticsTranscriber()
    else:
        raise RuntimeError("Improper transcriber provided")

    print()
    print(transcriber.transcribe(filename))
    print()

    wait()

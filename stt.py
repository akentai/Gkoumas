from lib.recording import *
from lib.transcribing import *
import argparse


if __name__ == "__main__":

    # Parsing audio data
    parser = argparse.ArgumentParser(prog="sst")

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
                        choices=["whisper", "deepgram"], help="""Decide the
                        type of transcriber""")

    args = parser.parse_args()

    if args.recorder == "keypress":
        recorder = KeyPressRecorder()
    else:
        recorder = TimerRecorder(stop_interval=args.stop_interval)

    data = recorder.record()

    recorder.to_file("record.wav", data)

    if args.play:
        recorder.playback(data)

    if args.transcriber == "whisper":
        transcriber = WhisperTranscriber()
    else:
        transcriber = DeepgramTranscriber()

    print()
    print(transcriber.transcribe("record.wav"))
    print()

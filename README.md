# Gkoumas
This is the group project of Dimitris and Stratos for a Voice Assistant which can be used for Educational purpose in Dutch environment.


## Project Structure ##
* Part 1: Speech Recognition, Transcription, Speech to Text (STT), Automatic Speech Recognition (ASR), Wakeword
* Part 2: Large Language Model (LLM) prompting
* Part 3: Speech Generation, Text to Speech (TTS), Voice Cloning
* Metrics
* Future: Suggestions

### Part 1: STT ###
* [Whisper](https://github.com/openai/whisper): OpenAI's STT. [Here](https://colab.research.google.com/github/petewarden/openai-whisper-webapp/blob/main/OpenAI_Whisper_ASR_Demo.ipynb) is a Colab Demo for Whisper.
* Good Reddit [post](https://www.reddit.com/r/MachineLearning/comments/14xxg6i/d_what_is_the_most_efficient_version_of_openai/) with many Whisper variations
* Github [post](https://github.com/sindresorhus/awesome-whisper#readme) with many Whisper variations
* Honorabe variations: [Faster Whisper](https://github.com/SYSTRAN/faster-whisper), [Insanely Faster Whisper](https://github.com/Vaibhavs10/insanely-fast-whisper), [WhisperLive](https://github.com/collabora/WhisperLive), [WhisperX](https://github.com/m-bain/whisperX/tree/main), [whisper.cpp](https://github.com/ggerganov/whisper.cpp). Some of those are better suited for real-time/streaming transcription. Usually STT is done by recording voice and then running transcription. For real-time transcription, the recording and the transcription are done simultaneously or by breaking the recording in batches. There are many variations out there but I believe the basic Whisper can be sufficient for the first proof of concept phase.
* Custom solutions in Github that support real-time transcription: [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT), [whisper_real_time](https://github.com/davabase/whisper_real_time)
* [Colab Notebook](https://colab.research.google.com/drive/1Z6VIRZ_sX314hyev3Gm5gBqvm1wQVo-a#scrollTo=xuKJ4wBU6gxx) for ASR using online recording

__NOTE 1__: The STT should support at least English, Dutch, Turkish, Polish, Arabic, Ukranian. Probably more will be added. Thus, we are looking for flexible solutions that offer great variety in languages. <br />
__NOTE 2__: There are also commercial solutions. For example, Google Cloud, Amazon Web, Microsoft Azure, AssemblyAI, Deepgram etc.

### Part 2: LLM ###
Free Models: <br />
* [GPT4Free](https://github.com/xtekky/gpt4free)
* [EdgeGPT](https://github.com/acheong08/EdgeGPT)
* [GPT4Free-TS](https://github.com/xiangsx/gpt4free-ts)

Paid Model: <br />
* OpenAI's [ChatGPT](https://platform.openai.com/docs/quickstart)

__NOTE 1__: The LLM should support English, Dutch, Turkish, Polish, Arabic, Ukranian or at least Engilish/Dutch and translation to all those. <br />

### Part 3: TTS ###

_To be continued....._

### Part 4: Metrics ###
Thee folllowing should be noted for all parts
* Response time
* Resources required
* Pricing
* Accuracy

### Part 5: Suggestions ###
* Translation
* Real-time Transcription
* Tuned Transfer Learning Model



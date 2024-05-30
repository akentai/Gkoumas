from abc import ABC, abstractmethod


class Transcriber(ABC):

    @abstractmethod
    def transcribe(self, filename: str) -> str:
        pass


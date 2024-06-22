from abc import ABC, abstractmethod
class StreamingInterface(ABC):
    @abstractmethod
    def authenticate():
        pass
    @abstractmethod
    def buildPlaylists():
        pass
    @abstractmethod
    def searchMusic():
        pass
    @abstractmethod
    def createPlaylist():
        pass

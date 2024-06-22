from typing import Type

class Music:
    def __init__(self, name:str, author:dict)->None:
        self.__name=name
        self.__author=author
    def showInfo(self):
        print(f"{self.__name}   / Autor: {self.__author["name"]}")
    @property
    def name(self):
        return self.__name
    @property
    def author(self):
        return self.__author

class Playlist:
    def __init__(self, name:str, id:str)->None:
        self.__name=name
        self.__id=id
        self.__musics=list()
    
    @property
    def name(self):
        return self.__name
    
    @property
    def musics(self):
        return self.__musics
    
    def addMusic(self, music:Music):
        self.__musics.append(music)
    
    def showPlaylistName(self):
        print(f"{self.__name}")

    def showPlaylistSongs(self):
        music:Type[Music]
        for music in self.__musics:
            music.showInfo()
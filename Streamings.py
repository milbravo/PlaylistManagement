from typing import Type
from MusicLibrary import *
class Streaming:
    def __init__(self):
        self._user=dict()
        self._playlists=list()
        self._isLogged=False
        self._loginExpires=""

    @property
    def isLogged(self):
        return self._isLogged
    @property
    def loginExpires(self):
        return self._loginExpires
    
    def listPlaylists(self)->int:
        playlist:Type[Playlist]
        index=0
        for playlist in self._playlists:
            index+=1
            print( str(index) + " - ", end=" ")
            playlist.showPlaylistName()
        return index

    def playlistSongs(self, number:int):
        playlist:Type[Playlist]
        playlist=self._playlists[number-1]
        print("\n-----------------------------------------------------------")
        playlist.showPlaylistName()
        playlist.showPlaylistSongs()
        print("\n-----------------------------------------------------------")
    
    def importPlaylist(self)->Playlist:
        varName=str(input("Informe o nome da playlist: "))
        if not varName:
            raise ValueError
        varFileName=str(input("Informe o nome do arquivo txt com as músicas (sem a extensão): "))
        if not varFileName:
            raise ValueError
        playlist=Playlist(varName,"")
        with open(varFileName+".txt") as file:
            for line in file:
                music=Music(line, dict(name="null"))
                playlist.addMusic(music)
        return playlist

        

import urllib.parse
from Interface import StreamingInterface
import requests
import webbrowser
import urllib
from Streamings import *
from MusicLibrary import *
from datetime import *

class Deezer(Streaming,StreamingInterface):
    def __init__(self)->None:
        super().__init__()
        self.__secretKey="5cc30ab1ddffd3ead61dcff5d780eaa1"
        self.__appId="563442"
        self.__token=""
    
    def authenticate(self)->None:
        url="https://connect.deezer.com/oauth/auth.php?app_id="+self.__appId+"&redirect_uri=http://localhost:5500/index.html&perms=basic_access,email,manage_library,delete_library"
        #Abre o navegador para o usuário realizar o login
        webbrowser.open(url)
        code=input("Digite o codigo carregado na página: ")
        self.__getToken(code)
        self._isLogged=True
        
    def __getToken(self, code:str)->None:
        #Obtém token de acesso para realizar as outras chamadas de API
        url="https://connect.deezer.com/oauth/access_token.php?app_id="+self.__appId+"&secret="+self.__secretKey+"&code="+code+"&output=json"
        response=requests.get(url)
        content=response.json()
        self.__token=content['access_token']
        self.__getUser()

    def __getUser(self)->None:
        #Obtém o perfil do usuário
        url="https://api.deezer.com/user/me?access_token="+self.__token
        response=requests.get(url)
        self._user=response.json()
        self._loginExpires=datetime.now().strftime("%H:%M")


    def buildPlaylists(self)->None:
        #Obtém as playlists do usuário
        url="https://api.deezer.com/user/"+str(self._user["id"])+"/playlists?limit=100&access_token="+self.__token
        response=requests.get(url)
        content=response.json()
        for playlist in content["data"]:
            #Para cada playlist obtida é criada um objeto Playlist
            currentPlaylist=Playlist(playlist["title"],playlist["id"])
            #Obtém as musicas da playlist
            url="https://api.deezer.com/playlist/"+str(playlist["id"])+"?access_token="+self.__token
            response=requests.get(url)
            content=response.json()
            for music in content["tracks"]["data"]:
                #Para cada música, instancia um objeto Music e adiciona na playlist
                currentMusic=Music(music["title"],music["artist"])
                currentPlaylist.addMusic(currentMusic)
            #Adiciona a playlist na conta local    
            self._playlists.append(currentPlaylist)

    def searchMusic(self, name:str)->dict:
        #Recebe o nome da música a ser pesquisada
        queryCoded= urllib.parse.quote("\""+name+"\"")
        url= "https://api.deezer.com/search?q="+queryCoded
        response=requests.get(url)
        content=response.json()
        #retorna o resultado da busca
        return content
    
    
    def createPlaylist(self, playlist: Type[Playlist])->None:
        #playlist=recebe uma playlist local
        url="https://api.deezer.com/user/"+str(self._user["id"])+"/playlists?title="+ urllib.parse.quote(playlist.name) +"&access_token="+self.__token
        response=requests.post(url)
        content=response.json()
        notFound=0
        songsString=""
        music: Type[Music]
        for music in playlist.musics:

            foundMusic=self.searchMusic(music.name)
            
            if foundMusic["total"]==0:
                notFound+=1
            elif str(foundMusic["data"][0]["id"]) in songsString:
                pass
            else:
                songsString = songsString + "," +str(foundMusic["data"][0]["id"])

        if len(songsString)>0:
            self.__addToPlaylist(str(content["id"]), songsString)
        print(f"Playlist {playlist.name} criada com sucesso!\n"
              f"{notFound} musica(s) não foi/foram encontrada(s) para adicionar...")
                

    def __addToPlaylist(self, playlistId: str, songsString:str )->None:
        #Recebe o Id da playlist e a lista de musicas
        #Adiciona a lista de músicas na playlist com o Id informado
        url="https://api.deezer.com/playlist/" + playlistId + "/tracks?songs=" + songsString + "&access_token="+self.__token
        response=requests.post(url)
        content=response.json()
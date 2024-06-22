import urllib.parse
from Interface import StreamingInterface
import requests
import webbrowser
import urllib
import base64
from Streamings import *
from MusicLibrary import *
from datetime import *

class Spotify(Streaming,StreamingInterface):
    def __init__(self)->None:
        super().__init__()
        self.__secretKey="e86e9b70bfed4017a11de42597132b15"
        self.__appId="d62a888fd620443aac1cbe0ec4b83660"
        self.__token=""

    def authenticate(self)->None:
        url="https://accounts.spotify.com/authorize?client_id="+self.__appId+"&redirect_uri=http://localhost:5500/index.html&response_type=code&scope="+urllib.parse.quote("user-read-private user-read-email playlist-read-private playlist-modify-public playlist-modify-private")
        #Abre o navegador para o usuário realizar o login
        webbrowser.open(url)
        code=input("Digite o codigo carregado na página: ")
        self.__getToken(code)
        self._isLogged=True
        
    def __getToken(self, code:str)->None:
        #Obtém token de acesso para realizar as outras chamadas de API
        url="https://accounts.spotify.com/api/token"
        form={
            "code": code,
            "redirect_uri": "http://localhost:5500/index.html",
            "grant_type": "authorization_code"
        }
        headers={
        "content-type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + base64.b64encode((self.__appId + ":" + self.__secretKey).encode("ascii")).decode("ascii")
      }
        response=requests.post(url,data=form, headers=headers,json=True)
        content=response.json()
        self.__token=content["access_token"]
        self.__getUser()

    def __getUser(self)->None:
        #Obtém o perfil do usuário
        url="https://api.spotify.com/v1/me"
        headers={
        "Authorization": "Bearer " + self.__token
        }
        response=requests.get(url, headers=headers)
        self._user=response.json()
        self._loginExpires=datetime.now().strftime("%H:%M")
        

    def buildPlaylists(self)->None:
        #Obtém as playlists do usuário
        url="https://api.spotify.com/v1/users/"+str(self._user["id"])+"/playlists?limit=50"
        headers={
        "Authorization": "Bearer " + self.__token
        }
        response=requests.get(url, headers=headers)
        content=response.json()
        for playlist in content["items"]:
            #Para cada playlist obtida é criada um objeto Playlist
            currentPlaylist=Playlist(playlist["name"],playlist["id"])
            #Obtém as musicas da playlist
            url="https://api.spotify.com/v1/playlists/"+str(playlist["id"])+"/tracks?limit=50&market=BR"
            headers={
            "Authorization": "Bearer " + self.__token
            }
            response=requests.get(url, headers=headers)
            content=response.json()
            for music in content["items"]:
                #Para cada música, instancia um objeto Music e adiciona na playlist
                currentMusic=Music(music["track"]["name"],music["track"]["artists"][0])
                currentPlaylist.addMusic(currentMusic)
            #Adiciona a playlist na conta local  
            self._playlists.append(currentPlaylist)

    def searchMusic(self, name:str, author:str)->dict:
        #Recebe o nome e autor da música a ser pesquisada
        if author == "null":
            queryCoded= urllib.parse.quote("track:" + name)
        else:
            queryCoded= urllib.parse.quote("track:" + name) + urllib.parse.quote(" artist:" + author)
        
        url="https://api.spotify.com/v1/search?q=" + queryCoded + "&type=track&limit=1"
        headers={
            "Authorization": "Bearer " + self.__token
            }
        response=requests.get(url, headers=headers)
        content=response.json()
        #retorna o resultado da busca
        return content["tracks"]
    
    
    def createPlaylist(self, playlist: Type[Playlist])->None:
        #playlist=recebe uma playlist local
        url="https://api.spotify.com/v1/users/" + str(self._user["id"]) + "/playlists"
        data={
                "name": playlist.name,
                "public": False
            }
        headers={
            "Content-Type":"application/json",
            "Authorization": "Bearer " + self.__token
            }
        response=requests.post(url, headers=headers, json=data)
        content=response.json()
        notFound=0
        uris=list()
        music: Type[Music]
        for music in playlist.musics:
            foundMusic=self.searchMusic(music.name, music.author["name"])
            
            if foundMusic["total"]==0:
                notFound+=1
            elif foundMusic["items"][0]["uri"] in uris:
                pass
            else:
                uris.append(foundMusic["items"][0]["uri"])

        if len(uris)>0:
            self.__addToPlaylist(str(content["id"]), uris)
        print(f"Playlist {content["name"]} criada com sucesso!\n"
              f"{notFound} musica(s) não foi/foram encontrada(s) para adicionar...")
                

    def __addToPlaylist(self, playlistId: str, uris:list )->None:
        #Recebe o Id da playlist e a lista de musicas
        url="https://api.spotify.com/v1/playlists/" + playlistId + "/tracks"
        data={
                "uris": uris,
                "position": 0
            }
        headers={
            "Content-Type":"application/json",
            "Authorization": "Bearer " + self.__token
            }
        response=requests.post(url, headers=headers, json=data)
        content=response.json()
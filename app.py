from Deezer import *
from Spotify import *
from MusicLibrary import *

def appRun():
    varNavigation="login"
    print("Bem vindo ao Playlist Management Studio!\n")
    deezerAccount=Deezer()
    spotifyAccount=Spotify()
    while varNavigation != "exit":
        match varNavigation:
            case "login":
                #Menu inicial
                print("LOGIN------------------------------------------------------------------")
                print("Escolha o Stream em que deseja realizar o login e lembre-se que cada \n"
                      "login é válido por uma hora:\n"
                    "1 - Deezer\n"
                    "2 - Spotify\n")
                try:
                    varAction=int(input("Digite o número referente à escolha: "))
                    if not varAction:
                        raise ValueError
                    elif varAction<1 or varAction>2:
                        raise ValueError
                except Exception:
                    print("Valor inválido!")
                else:
                    if(varAction==1):
                        try:
                            deezerAccount.authenticate()
                            deezerAccount.buildPlaylists()
                        except Exception:
                            print("Ocorreu um erro ao logar no Deezer")
                    else:
                        try:
                            spotifyAccount.authenticate()
                            spotifyAccount.buildPlaylists()
                        except Exception:
                            print("Ocorreu um erro ao logar no Spotify")

                    if(varAction==1):
                        print("\nDeseja fazer o login no Spotify?\n"
                            "1 - Sim\n"
                            "2 - Não\n")
                        try:
                            varAction=int(input("Digite o número referente à escolha: "))
                            if not varAction:
                                raise ValueError
                            elif varAction<1 or varAction>2:
                                raise ValueError
                        except Exception:
                            print("Valor inválido!")
                        else:
                            if(varAction==1):
                                try:
                                    spotifyAccount.authenticate()
                                    spotifyAccount.buildPlaylists()
                                except Exception:
                                    print("Ocorreu um erro ao logar no Spotify!")
                    else:
                        print("\nDeseja fazer o login no Deezer?\n"
                            "1 - Sim\n"
                            "2 - Não\n")
                        try:
                            varAction=int(input("Digite o número referente à escolha: "))
                            if not varAction:
                                raise ValueError
                            elif varAction<1 or varAction>2:
                                raise ValueError
                        except Exception:
                            print("Valor inválido!")
                        else:
                            if(varAction==1):
                                try:
                                    deezerAccount.authenticate()
                                    deezerAccount.buildPlaylists()
                                except Exception:
                                    print("Ocorreu um erro ao logar no Deezer!")
                    varAction=0
                    if(deezerAccount.isLogged and spotifyAccount.isLogged):
                        varNavigation="mainMenu"
                    elif(deezerAccount.isLogged or spotifyAccount.isLogged):
                        if(deezerAccount.isLogged):
                            varNavigation="mainMenuDeezer"
                        else:
                            varNavigation="mainMenuSpotify"
                    else:
                        print("Você precisa logar em pelo menos um plataforma para continuar!")
            case "mainMenu":
                #Menu principal
                print("\nMENU PRINCIPAL------------------------------------------------------")
                print(f"                                                Login Deezer: {deezerAccount.loginExpires}")
                print(f"                                                Login Spotify: {spotifyAccount.loginExpires}\n")
                print("Operações disponíveis:")
                print("Deezer\n"
                      "  1 - Ver playlists\n"
                      "  2 - Criar playlist\n")
                print("Spotify\n"
                      "  3 - Ver playlists\n"
                      "  4 - Criar playlist\n")
                print("5 - Tela de login\n"
                      "0 - Sair")
                try:
                    varAction=int(input("Digite o número referente à escolha: "))
                    if varAction<0 or varAction>5:
                        raise ValueError
                except Exception:
                    print("Valor inválido!")
                else:
                    match varAction:
                        case 1:
                            varNavigation="deezerListPlaylist"
                        case 2:
                            varNavigation="deezerCreatePlaylist"
                        case 3:
                            varNavigation="spotifyListPlaylist"
                        case 4:
                            varNavigation="spotifyCreatePlaylist"
                        case 5:
                            varNavigation="login"
                        case 0:
                            varNavigation="exitConfirmation"
                        case _:
                            print("Escolha uma opção válida!")
                            varNavigation="mainMenuDeezer"                
            case "mainMenuDeezer":
                #Menu principal
                print("\nMENU PRINCIPAL DEEZER---------------------------------------------")
                print(f"                                                Login Deezer: {deezerAccount.loginExpires}")
                print(f"                                                Login Spotify: {spotifyAccount.loginExpires}\n")
                print("Operações disponíveis:")
                print("Deezer\n"
                      "  1 - Ver playlists\n"
                      "  2 - Criar playlist")
                print("5 - Tela de login\n"
                      "0 - Sair")
                try:
                    varAction=int(input("Digite o número referente à escolha: "))
                    if varAction<0 or varAction>5:
                        raise ValueError
                except Exception:
                    print("Valor inválido!")
                else:
                    match varAction:
                        case 1:
                            varNavigation="deezerListPlaylist"
                        case 2:
                            varNavigation="deezerCreatePlaylist"
                        case 5:
                            varNavigation="login"
                        case 0:
                            varNavigation="exitConfirmation"
                        case _:
                            print("Escolha uma opção válida!")
                            varNavigation="mainMenu"
            case "mainMenuSpotify":
                #Menu principal
                print("\nMENU PRINCIPAL SPOTIFY---------------------------------------------")
                print(f"                                                Login Deezer: {deezerAccount.loginExpires}")
                print(f"                                                Login Spotify: {spotifyAccount.loginExpires}\n")
                print("Operações disponíveis:")
                print("Spotify\n"
                      "  1 - Ver playlists\n"
                      "  2 - Criar playlist")
                print("5 - Tela de login\n"
                      "0 - Sair")
                try:
                    varAction=int(input("Digite o número referente à escolha: "))
                    if varAction<0 or varAction>5:
                        raise ValueError
                except Exception:
                    print("Valor inválido!")
                else:
                    match varAction:
                        case 1:
                            varNavigation="spotifyListPlaylist"
                        case 2:
                            varNavigation="spotifyCreatePlaylist"
                        case 5:
                            varNavigation="login"
                        case 0:
                            varNavigation="exitConfirmation"
                        case _:
                            print("Escolha uma opção válida!")
                            varNavigation="mainMenu"           
            case "deezerListPlaylist":
                print("\nPLAYLISTS DEEZER------------------------------------------------------")
                print(f"                                                Login Deezer: {deezerAccount.loginExpires}")
                print(f"                                                Login Spotify: {spotifyAccount.loginExpires}\n")
                nrPlaylists=deezerAccount.listPlaylists()
                print("\nPara cada uma das playlists é possível realizar as seguintes operações:\n"
                      "1 - Ver musicas")
                if(spotifyAccount.isLogged):
                    print("2 - Tranferir para spotify")
                print( "0 - Voltar ao menu anterior")
                try:
                    varAction=int(input("Digite o número referente à escolha: "))
                    if varAction<0 or varAction>2:
                        raise ValueError
                    if varAction!=0:
                        varChoice=int(input("Digite o número da playlist: "))
                        if not varChoice:
                            raise AttributeError
                        elif varChoice<1 or varChoice>nrPlaylists:
                            raise AttributeError
                except ValueError:
                    print("Valor inválido!")
                except AttributeError:
                    print("Playlist inválida!")
                except Exception:
                    print("Ocorreu um erro nos valores informados!")
                else:
                    match varAction:
                        case 1:
                            deezerAccount.playlistSongs(varChoice)
                        case 2:
                            if spotifyAccount.isLogged:
                                index=(varChoice-1)
                                spotifyAccount.createPlaylist(deezerAccount._playlists[index])
                        case 0:
                            if(deezerAccount.isLogged and spotifyAccount.isLogged):
                                varNavigation="mainMenu"
                            elif(deezerAccount.isLogged or spotifyAccount.isLogged):
                                if(deezerAccount.isLogged):
                                    varNavigation="mainMenuDeezer"
                                else:
                                    varNavigation="mainMenuSpotify"
                            else:
                                varNavigation="login"
            case "deezerCreatePlaylist":
                try:
                    playlist=deezerAccount.importPlaylist()
                    deezerAccount.createPlaylist(playlist)
                except:
                    print("Ocorreu um erro ao importar a playlist!")
                else:
                    if(deezerAccount.isLogged and spotifyAccount.isLogged):
                        varNavigation="mainMenu"
                    elif(deezerAccount.isLogged or spotifyAccount.isLogged):
                        if(deezerAccount.isLogged):
                            varNavigation="mainMenuDeezer"
                        else:
                            varNavigation="mainMenuSpotify"
                    else:
                        varNavigation="login"
            case "spotifyListPlaylist":
                print("\nPLAYLISTS SPOTIFY------------------------------------------------------")
                print(f"                                                Login Deezer: {deezerAccount.loginExpires}")
                print(f"                                                Login Spotify: {spotifyAccount.loginExpires}\n")
                nrPlaylists=spotifyAccount.listPlaylists()
                print("\nPara cada uma das playlists é possível realizar as seguintes operações:\n"
                      "1 - Ver musicas")
                if(deezerAccount.isLogged):
                    print("2 - Tranferir para deezer")
                print( "0 - Voltar ao menu anterior")
                try:
                    varAction=int(input("Digite o número referente à escolha: "))
                    if varAction<0 or varAction>2:
                        raise ValueError
                    if varAction!=0:
                        varChoice=int(input("Digite o número da playlist: "))
                        if not varChoice:
                            raise AttributeError
                        elif varChoice<1 or varChoice>nrPlaylists:
                            raise AttributeError
                except ValueError:
                    print("Valor inválido!")
                except AttributeError:
                    print("Playlist inválida!")
                except Exception:
                    print("Ocorreu um erro nos valores informados!")
                else:
                    match varAction:
                        case 1:
                            spotifyAccount.playlistSongs(varChoice)
                        case 2:
                            if deezerAccount.isLogged:
                                index=(varChoice-1)
                                deezerAccount.createPlaylist(spotifyAccount._playlists[index])
                        case 0:
                            if(deezerAccount.isLogged and spotifyAccount.isLogged):
                                varNavigation="mainMenu"
                            elif(deezerAccount.isLogged or spotifyAccount.isLogged):
                                if(deezerAccount.isLogged):
                                    varNavigation="mainMenuDeezer"
                                else:
                                    varNavigation="mainMenuSpotify"
                            else:
                                varNavigation="login"
            case "spotifyCreatePlaylist":
                try:
                    playlist=spotifyAccount.importPlaylist()
                    spotifyAccount.createPlaylist(playlist)
                except:
                    print("Ocorreu um erro ao importar a playlist!")
                else:
                    if(deezerAccount.isLogged and spotifyAccount.isLogged):
                        varNavigation="mainMenu"
                    elif(deezerAccount.isLogged or spotifyAccount.isLogged):
                        if(deezerAccount.isLogged):
                            varNavigation="mainMenuDeezer"
                        else:
                            varNavigation="mainMenuSpotify"
                    else:
                        varNavigation="login"
            case "exitConfirmation":
                print("AVISO!!!------------------------------------------------------\n\n")
                print("Tem certeza que deseja sair da aplicação???\n"
                      "1 - Sim\n"
                      "2 - Não")
                try:
                    varAction=int(input("Digite o número referente à escolha: "))
                    if not varAction:
                        raise ValueError
                    elif varAction<1 or varAction>2:
                        raise ValueError
                except Exception:
                    print("Valor inválido!")
                else:
                    if(varAction==2):
                        if(deezerAccount.isLogged and spotifyAccount.isLogged):
                            varNavigation="mainMenu"
                        elif(deezerAccount.isLogged or spotifyAccount.isLogged):
                            if(deezerAccount.isLogged):
                                varNavigation="mainMenuDeezer"
                            else:
                                varNavigation="mainMenuSpotify"
                    else:
                        varNavigation="exit"
            case _:
                print("Escolha uma opção válida!")


appRun()    
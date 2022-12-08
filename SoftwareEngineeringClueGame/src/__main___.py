#!/usr/bin/env python3


#Imports
import socket
import re
import random
import sys
import time
import itertools


#imports for classes
from Game_Server import Game_Server
from Player import players
from Game_Board import gameBoard



#Game art for right now still working on board

game_art1 = '''
==================================================================================
Welcome to the classic detective game: 
==================================================================================
'''
game_art2 = '''
 .d8888b.     888                             888              
d88P  Y88b    888                             888              
888    888    888                             888             
888           888    888  888     .d88b.      888     .d88b.     .D88b.  .D88b.
888           888    888  888    d8P  Y8b     888    d8P  Y8b   d8P     d8P
888    888    888    888  888    88888888     888    88888888      88P     88P
Y88b  d88P    888    Y88b 888    Y8b.         888    Y8b.      888PP   888PP
 "Y8888P"     888     "Y88888     "Y8888      888     "Y8888 
 '''
game_art3 = '''
===============================================================================
Let the investigation begin...
===============================================================================
 
'''
option_table = """  
================================================
||........Suspects.......||......Weapons......||
||  1.) Colonel Mustard  ||  1.) Dagger       ||
||  2.) Professor Plum   ||  2.) Candlestick  ||
||  3.) Reverend Green   ||  3.) Revolver     ||
||  4.) Mrs. Peacock     ||  4.) Rope         ||
||  5.) Miss Scarlett    ||  5.) Lead piping  ||
||  6.) Mrs. White       ||  6.) Spanner      ||
================================================
"""
room_table = """  
=========================
||........Rooms........||
||  1.) Hall           ||
||  2.) Lounge         ||
||  3.) Library        ||
||  4.) Kitchen        ||
||  5.) Billiard Room  ||
||  6.) Study          ||
=========================
"""
suggestion = '''
--------------
| Killer: {} |
| Weapon: {} |
| Place : {} |
-------------- 
'''
cards = [["Colonel Mustard", "Professor Plum", "Reverend Green", "Mrs. Peacock", "Mrs. White", "Miss Scarlett"],
         ["Dagger", "Candlestick", "Revolver", "Rope", "Lead piping", "Spanner"], ["Hall", "Study",
                                                                                   "Billiard Room", "Lounge", "Library",
                                                                                   "Kitchen"]]
suspects = {1: "Colonel Mustard", 2: "Professor Plum", 3: "Reverend Green", 4: "Mrs. Peacock", 5: "Miss Scarlett",
            6: "Mrs. White"}
weapon = {1: "Dagger", 2: "Candlestick", 3: "Revolver", 4: "Rope", 5: "Lead piping", 6: "Spanner"}
rooms = {1: "Hall", 2: "Lounge", 3: "Library", 4: "Kitchen", 5: "Billiard Room", 6: "Study"}




def main():
    
    #Global game variables
    playersList = []
    nicknamesList = []
    membersIdList = {}
    playersDeck = {}
    playerPoints = {}
    secretDeck = {}
    masterGameBoard = []
    
    #Game starts here
    print("________________Setting up the Game Server__________________")
    serverType = input("Choose the type of server...\n1.)Offline Server\n2.)Online Server\n")

    numPlayers = int(input("Enter the number of players (2-6)\n(Least 3 players are recommended)\n"))

    newBoardObject = gameBoard.Gameboard(masterGameBoard)

    ###Add new number of players to the starting room
    masterGameBoard = newBoardObject.returnGameBoard()
    newBoardObject.setMasterGameBoard(masterGameBoard)

    newGameObject = Game_Server.Game_Server(numPlayers, serverType, nicknamesList, membersIdList, playerPoints)

    playersList = newGameObject.connectPlayers(serverType, numPlayers, playersList, playersDeck, secretDeck)

    print(playersList)

    nicknamesList = newGameObject.returnNickNames()
    membersIdList = newGameObject.returnMembers()
    playerPoints = newGameObject.returnPlayerPoints()

    ##Make sure to update global lists from objects

    playersDeck, secretDeck = newGameObject.shuffleCards(cards, numPlayers, nicknamesList, secretDeck)
    nicknamesList = newGameObject.returnNickNames()

    ###Added players to the "Start" room
    masterGameBoard = newBoardObject.addPlayersToGameBoard(masterGameBoard, playersList)


    time.sleep(2)
    newGameObject.broadcastUpdates(playersList, "\nShuffling Cards...")
    time.sleep(2)
    newGameObject.broadcastUpdates(playersList, "...")
    time.sleep(2)
    newGameObject.broadcastUpdates(playersList, "...")
    time.sleep(2)
    newGameObject.broadcastUpdates(playersList, game_art1)
    time.sleep(2)
    newGameObject.broadcastUpdates(playersList, game_art2)
    time.sleep(2)
    newGameObject.broadcastUpdates(playersList, game_art3)
    time.sleep(2)
    nicknamesList.sort()
    
    
    masterPlayersListObject = players.Players(playersList, nicknamesList, membersIdList, playersDeck, playerPoints)


    """Passes player name to 'player_turn' function turn-by-turn until one player wins."""
    iter_nickname = itertools.cycle(nicknamesList)
    nickname = next(iter_nickname)
    win = False
    while not win:
        time.sleep(1)
        masterPlayersListObject.playerDetails(nicknamesList, membersIdList, playerPoints, playersDeck)
        time.sleep(1)
        ##pass in newGameObject to do broadcasting
        turnBoard = None
        win, turnBoard = masterPlayersListObject.playerTurn(nickname, playersList, secretDeck, membersIdList, nicknamesList, suggestion, playerPoints, playersDeck, option_table, suspects, weapon, room_table, rooms, newGameObject, masterGameBoard)
        masterGameBoard = turnBoard
        ###Make sure to update the GUI with the newly returned game board
        
        nickname = next(iter_nickname)
    newGameObject.broadcastUpdates(playersList, "\nThanks for playing.")
    newGameObject.closeConnect
    try:
        membersIdList.get(nickname).recv(1024).decode("utf-8")
    except Exception as e:
        print(e)
    newGameObject.closeConnect


    return None

    ##This object is the listmanager, holds all the players
    #masterPlayersListObject = players.Players(playersList)







if __name__ == "__main__":
    main()
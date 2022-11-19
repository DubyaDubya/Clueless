#!/usr/bin/env python3

#Imports
import socket
import re
import random
import sys
import time
import itertools

class Game_Server:
    def __init__(self, numPlayers, serverType, nickNames, members, points):
        self.numPlayers = numPlayers
        self.serverType = serverType
        self.nickNames = nickNames
        self.members = members
        self.playerPoints = points


    def runGame(self):
        print()


    def returnNumPlayers(self):
        return self.numPlayers


    def closeConnect(self):
        print("Its over")
        sys.exit(1)

    
    def returnNickNames(self):
        return self.nickNames


    def returnMembers(self):
        return self.members


    def returnPlayerPoints(self):
        return self.playerPoints



    def broadcastUpdates(self, players, message, ex_id=""):
        #Sends message to all players in the game.
        for player in players:
            if player == ex_id:
                continue
            player.send(message.encode("utf-8"))


    def player_nickname(self, player):
        """ Ask newly joined players to choose a nickname does a check for wrong entries"""

        valid_name_pattern = r'[A-Za-z0-9-_]*'
        
        player.send("Please choose a nickname: ".encode("utf-8"))
        nickname = player.recv(1024).decode("utf-8")
        while True:
            if re.fullmatch(valid_name_pattern, nickname):
             break
            else:
                player.send('Invalid character used !'.encode("utf-8"))
                player.send("Choose a valid nickname: ".encode("utf-8"))
                nickname = player.recv(1024).decode("utf-8")
        while nickname in self.nickNames:
            player.send("This name is not available!\nPlease choose another nickname: ".encode("utf-8"))
            nickname = player.recv(1024).decode("utf-8")
        self.nickNames.append(nickname)
        self.members.update({nickname: player})
        self.playerPoints.update({nickname: 0})
        return nickname



    def shuffleCards(self, allCards, numPlayers, nickNamesList, secretDeck):

        """ Shuffle cards and distribute among players.
    Returns two dictionaries: 1.) nickname-their cards 2.) Murder Envelope cards. """
        x = 0
        y = int(15 / numPlayers)
        count = y
        excess_cards = 15 % numPlayers
        temp_decs = []
        p_cards = []
        params = ["Killer", "Weapon", "Place"]  # .................................... Keys to access Murder Envelope cards.
        for i in range(0, 3):
            random.shuffle(allCards[i])
            secretDeck.update({params[i]: allCards[i][i]})
        for i in range(0, 3):
            allCards[i].remove(secretDeck[params[i]])
            p_cards.extend(allCards[i])
        random.shuffle(p_cards)
        for i in range(0, numPlayers):
            dec = p_cards[x:count]
            temp_decs.append(dec)
            x = count
            count += y
        count = 15 - excess_cards
        if excess_cards != 0:
            for i in range(1, excess_cards + 1):
                temp_decs[i].append(p_cards[count + i - 1])
        decks = {}
        for i in range(0, numPlayers):
            temp1 = nickNamesList[i]
            temp2 = temp_decs[i]
            tempDict = {temp1: temp2}
            decks.update(tempDict)
        print(decks, "\n", secretDeck)
        return decks, secretDeck


    def connectPlayers(self, serverType, numPlayers, playersList, playersDeck, secretDeck):
        if serverType == "1":
            serverType = "127.0.0.1"  # .................................................................Local host IP address.
        elif serverType == "2":
            try:
                server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                server.connect(("8.8.8.8", 80))  # ..................................Using Google DNS -To get your IPV4 Address.
                serverType = server.getsockname()[0]
                print(f"Players can connect using: {serverType} address.")
                server.close()
            except Exception as online_error:
                print(f"{online_error}: Check your internet connection.")
                sys.exit(1)
        else:
            print("Invalid option !")
            sys.exit(1)


        if type(numPlayers) == int and 6 >= numPlayers >= 2:
            print("Waiting for players to join....")
        else:
            print("Invalid character entered.")
            sys.exit(1)

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((serverType, 55555))
        server.listen(numPlayers)

        ##Logical continuation

        """Accepts new connection until selected number of people join."""
        while len(playersList) < self.numPlayers:
            self.broadcastUpdates(playersList, "Waiting for other players to join...")
            player, address = server.accept()
            playersList.append(player)
            player.send("Hey there!\n".encode("utf-8"))
            nickname = self.player_nickname(player)
            self.broadcastUpdates(playersList, f"{nickname} has joined the Game.\n")

        return playersList
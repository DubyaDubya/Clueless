#!/usr/bin/env python3

#Imports
import socket
import re
import random
import sys
import time
import itertools

class Players:
    def __init__(self, playersList, nicknamesList, membersIdList, playersDeck, playerPoints):
        self.players = playersList
        self.nicknamesList = nicknamesList
        self. membersIdLst = membersIdList
        self.playersDeck = playersDeck
        self.playerPoints = playerPoints

    
    def returnListOfPlayers(self):
        return self.players

    def playerPosition():
        print()


    def dice_s(self):
        return random.randint(1, 6)


    def playerTurn(self, playerNickName, playersList, secretDeck, membersList, nickNamesList, suggestionList, playerPointList, playersDeck, optionsTable, suspectList, weaponsList, roomTable, roomList, newGameObject, masterGameBoard):
        """Ask the given player to roll dice and enter in room to make suggestion if applicable.
        returns True only when player wins."""
        player_id = membersList[playerNickName]
        temp_win = True
        player_id.send("---------------------------------------------------\n".encode("utf-8"))
        player_id.send(f"\nWelcome {playerNickName} it is now your turn!".encode("utf-8"))
        player_id.recv(1024).decode("utf-8")
        """dice_count = self.dice_s()"""
        dice_count = 0
        player_id.send("\n=============================================".encode("utf-8"))
        """player_id.send(f"You have rolled: {dice_count}.".encode("utf-8"))"""
        """newGameObject.broadcastUpdates(playersList, f"{playerNickName} rolled: {dice_count}", ex_id=player_id)"""
        playerPointList[playerNickName] += dice_count
        if playerPointList[playerNickName] >= 0:
            player_id.send("\nWant to enter in a room ?(y)  Want to enter a hallway?(n)".encode("utf-8"))
            choice = player_id.recv(1024).decode("utf-8")
            if choice == 'y':
                roomPos = None
                tempCount = 0
                foundPlayer = False
                movingPlayer = None
                for player in playersList:
                    if player_id == player:
                        movingPlayer = player

                while foundPlayer == False:
                    if movingPlayer in masterGameBoard[tempCount]:
                        roomPos = tempCount
                        foundPlayer = True
                    else:
                        tempCount +=1

                playerPointList[playerNickName] = 0
                player_id.send(roomTable.encode("utf-8"))
                player_id.send("\nChoose a room to enter: ".encode("utf-8"))
                room_no = 0
                while room_no > 6 or room_no < 1 or type(room_no) != int:  # .......... To check if entered option is valid.
                    try:
                        room_no = int(player_id.recv(1024).decode("utf-8"))
                    except Exception as e:
                        player_id.send("Invalid room selected!\n".encode("utf-8"))
                        print(f"Invalid Character Entered by user: {e}")
                        room_no = 0

                roomName = roomList[room_no]
                roomPos2 = None
                tempCount2 = 0
                foundRoom = False

                while foundRoom == False:
                    if roomName in masterGameBoard[tempCount2]:
                        roomPos2 = tempCount2
                        foundRoom = True
                    else:
                        tempCount2 +=1

                masterGameBoard[roomPos2].append(movingPlayer)
                masterGameBoard[roomPos].remove(movingPlayer)
                newGameObject.broadcastUpdates(playersList, f"{playerNickName} has moved to room {roomName}.")

                player_id.send("\nChoose Suspect and Weapon. (separated by space)".encode("utf-8"))
                time.sleep(0.5)
                player_id.send(optionsTable.encode("utf-8"))
                sus_wea = [0, 0]
                while sus_wea[0] > 6 or sus_wea[0] < 1 or type(sus_wea[0]) != int or len(sus_wea) != 2:
                    # ..................................................................To check if entered option is valid.
                    try:
                        sus_wea = list(map(int, player_id.recv(1024).decode("utf-8").split(" ")))
                    except Exception as er:
                        print(f"Invalid Character Entered: {er}")
                        player_id.send("Invalid Character selected!".encode("utf-8"))
                        sus_wea = [0, 0]
                while sus_wea[1] > 6 or sus_wea[1] < 1 or type(sus_wea[1]) != int or len(sus_wea) != 2:
                    # ..................................................................To check if entered option is valid.
                    try:
                        sus_wea = list(map(int, player_id.recv(1024).decode("utf-8").split(" ")))
                    except Exception as er:
                        print(f"Invalid Weapon Entered: {er}")
                        player_id.send("Invalid Character selected!".encode("utf-8"))
                        sus_wea = [0, 0]
                newGameObject.broadcastUpdates(playersList, f"\n{playerNickName}'s suggestion:")
                newGameObject.broadcastUpdates(playersList, suggestionList.format((suspectList[sus_wea[0]]), weaponsList[sus_wea[1]], roomList[room_no]))
                accused = [suspectList[sus_wea[0]], weaponsList[sus_wea[1]], roomList[room_no]]
                time.sleep(2)
                for name in nickNamesList:
                    for accuse in accused:
                        if accuse in playersDeck[name] and name != playerNickName:
                            newGameObject.broadcastUpdates(playersList, f"{name} has disapproved {playerNickName}'s suggestion.", player_id)
                            player_id.send(f"{name} has {accuse}.".encode("utf-8"))
                            temp_win = False
                            break
                    if not temp_win:
                        break
                if temp_win:
                    newGameObject.broadcastUpdates(playersList, f"No proof against {playerNickName}'s suggestion.")
                player_id.send("Do you want to reveal cards ?(y/n)".encode("utf-8"))
                choice_r = player_id.recv(1024).decode("utf-8")
                if choice_r == 'y':
                    if secretDeck["Killer"] == suspectList[sus_wea[0]] and secretDeck["Weapon"] == weaponsList[sus_wea[1]] and \
                            secretDeck["Place"] == roomList[room_no]:
                        newGameObject.broadcastUpdates(playersList, f"{playerNickName} WON !")
                        player_id.send(f"\nCongrats {playerNickName} you have solved the case !".encode("utf-8"))
                        return True
                    else:
                        newGameObject.broadcastUpdates(playersList, f"Wrong accusation !\n{playerNickName} will no longer make accusations.")
                        nickNamesList.remove(playerNickName)
                else:
                    pass
            else:
                ###They enter a hallway here
                roomPos = None
                tempCount = 0
                foundPlayer = False
                movingPlayer = None
                for player in playersList:
                    if player_id == player:
                        movingPlayer = player

                while foundPlayer == False:
                    if movingPlayer in masterGameBoard[tempCount]:
                        roomPos = tempCount
                        foundPlayer = True
                    else:
                        tempCount +=1

                if (roomPos-1 >= 0 and roomPos-1 <= 24):
                    if "H" in masterGameBoard[roomPos-1]:
                        ###if so append the player inside and take them out of old room
                        masterGameBoard[roomPos-1].append(movingPlayer)
                        masterGameBoard[roomPos].remove(movingPlayer)
                        newGameObject.broadcastUpdates(playersList, f"{playerNickName} has entered the hallway!")
                elif (roomPos+1 >= 0 and roomPos+1 <= 24):
                    if "H" in masterGameBoard[roomPos+1]:
                        ###if so append the player inside and take them out of old room
                        masterGameBoard[roomPos+1].append(movingPlayer)
                        masterGameBoard[roomPos].remove(movingPlayer)
                        newGameObject.broadcastUpdates(playersList, f"{playerNickName} has entered the hallway!")
                elif (roomPos-5 >= 0 and roomPos-5 <= 24):
                    if "H" in masterGameBoard[roomPos-5]:
                        ###if so append the player inside and take them out of old room
                        masterGameBoard[roomPos-5].append(movingPlayer)
                        masterGameBoard[roomPos].remove(movingPlayer)
                        newGameObject.broadcastUpdates(playersList, f"{playerNickName} has entered the hallway!")
                elif (roomPos+5 >= 0 and roomPos+5 <= 24):
                    if "H" in masterGameBoard[roomPos+5]:
                        ###if so append the player inside and take them out of old room
                        masterGameBoard[roomPos+5].append(movingPlayer)
                        masterGameBoard[roomPos].remove(movingPlayer)
                        newGameObject.broadcastUpdates(playersList, f"{playerNickName} has entered the hallway!")
                else:
                    newGameObject.broadcastUpdates(playersList, f"{playerNickName} couldn't enter the hallway!")

                
        return False, masterGameBoard



    


    def playerDetails(self, nickNameList, membersList, playerPoints, playerDeck):
        """Display each player their cards"""
        for name in nickNameList:
            player_id = membersList[name]
            point = playerPoints[name]
            deck = playerDeck[name]
            player_id.send("\n=============================================\n".encode("utf-8"))
            player_id.send(f"Your Cards: {deck}\n\n".encode("utf-8"))
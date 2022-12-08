#!/usr/bin/env python3

#Imports


class Gameboard:
    def __init__(self, masterBoard):
        self.masterBoard = masterBoard



    def initializeBoard(self):
        masterBoard = []

        ##create a list that holds the map (A1-9, B1-9 etc, etc..)
        newBoard = [["Study"],   ["H"],   ["Hall"],       ["H"],       ["Lounge"],
                       ["H"],       ["*"],     ["H"],        ["*"],           ["H"],
                       ["Library"], ["H"], ["Billard Room"], ["H"],  ["Dining Room"], 
                       ["H"],     ["*"],            ["H"],  ["*"],            ["H"], 
                       ["Secret Room 1"], ["H"], ["Secret Room 2"], ["H"], ["Secret Room 3"],]

        masterBoard = newBoard
        return masterBoard


    def returnGameBoard(self):
        return self.masterBoard

    
    def setMasterGameBoard(self, gameBoard):
        self.masterBoard = gameBoard


    def addPlayersToGameBoard(self, masterBoard, playersList):
        ###Loop thru and add the player objects to the first room "Start"
        tempBoard = masterBoard
        tempSpots = [0, 2, 4, 10, 12, 14]
        tempNum = 0
        for player in playersList:
            tempPos = tempSpots[tempNum]
            tempBoard[tempPos].append(player)
            tempNum += 1

        return tempBoard

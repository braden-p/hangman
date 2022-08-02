#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hangman
Created by Braden Piper, bradenpiper.com
Created on Tue Jul 19, 2022
Version = 1.1
------------------------------------------
A basic hangman game. The program will select a word from a word list at
random, and the user has an allotted number of guesses to guess the correct
letters in the word. If the user guesses all the letters, they win. If the user
runs out of guesses, they lose.
------------------------------------------
"""

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordSet = set(list(secretWord))
    lettersGuessedSet = set(lettersGuessed)
    return secretWordSet.issubset(lettersGuessedSet)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWordList = list('_'*(len(secretWord)))
    index = -1
    for l in secretWord:
        index += 1
        if l in lettersGuessed:
            guessedWordList[index] = l
        else:
            guessedWordList[index] = '_ '
    return ''.join(guessedWordList)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetList = list(alphabet)
    for l in lettersGuessed:
        if l in alphabetList:
            alphabetList.remove(l)
    return ''.join(alphabetList)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, lets the user know how many 
      letters the secretWord contains.

    * Asks the user to supply one guess (i.e. letter) per round.

    * The user receives feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, displays to the user the partially guessed word
      so far, as well as letters that the user has not yet guessed.
    '''
    lettersGuessed = []
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    guessesLeft = 8
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',(len(secretWord)), 'letters long.')
    
    while guessesLeft > 0: 
        print('-------------')
        print('Guesses left:',guessesLeft)
        print('Available letters:',availableLetters)
        guess = (input('Please guess a letter: ')).lower()   # get guess
        lettersGuessed.append(guess)   # add the guess to lettersGuessed
        if len(guess) > 1:
            print('You may only guess one letter at a time')
        elif guess not in availableLetters:
            print("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            print('Good guess! ',getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Sorry! That letter is not in my word: ',getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        availableLetters = getAvailableLetters(lettersGuessed)
        if guessesLeft == 0:
            print('-----------')
            print('Sorry, you ran out of guesses. The word was',secretWord)
        if isWordGuessed(secretWord, lettersGuessed):
            print('------------')
            print('Congratulations, you won!')
            guessesLeft = 0
            

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

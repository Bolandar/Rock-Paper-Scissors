#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""
import random

class Player:
    def __init__(self):
        self.their_last_move = random.choice(moves)
        self.my_last_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_last_move = their_move
        self.my_last_move = my_move

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player):
    def move(self):
        return self.their_last_move

class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("What is your move (rock, paper, or scissors? ")
            if choice in moves:
                return choice
            else:
                print (f"{choice} is not a valid choice, try again.")

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        p1_score = 0
        p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.show_winner(move1, move2)

    def show_winner(self, p1_move, p2_move):
        if beats(p1_move, p2_move) == True:
            print(f"{p1_move} beats {p2_move}, Player 1 wins!")
        elif beats(p2_move, p1_move) == True:
            print(f"{p2_move} beats {p1_move}, Player 2 wins!")
        else:
            if p1_move == p2_move:
                print(f"Both players picked {p1_move}, game is a tie!")
            else:
                print("Wow, I'm not sure what happened")


    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(ReflectPlayer(), HumanPlayer())
    game.play_game()

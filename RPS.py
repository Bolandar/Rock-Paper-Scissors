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
        self.name = "PC"

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_last_move = their_move
        self.my_last_move = my_move

class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Random(PC)"

    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Reflect(PC)"

    def move(self):
        return self.their_last_move

class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Cycle(PC)"

    def move(self):
        pos = moves.index(self.my_last_move)
        return moves[(pos +1)%3]

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Human"

    def move(self):
        while True:
            choice = input("  What is your move (rock, paper, or scissors)? ")
            if (choice.lower()) in moves:
                return (choice.lower())
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
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\n  {self.p1.name} picks: {move1}  {self.p2.name} picks: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.show_winner(move1, move2)

    def show_winner(self, p1_move, p2_move):
        if beats(p1_move, p2_move) == True:
            print(f"\n  {p1_move} beats {p2_move}, {self.p1.name} wins!\n")
            self.p1_score += 1
        elif beats(p2_move, p1_move) == True:
            print(f"\n  {p2_move} beats {p1_move}, {self.p2.name} wins!\n")
            self.p2_score += 1
        else:
            if p1_move == p2_move:
                print(f"\n  Both players picked {p1_move}, game is a tie!\n")
            else:
                print("  Wow, I'm not sure what happened")


    def play_game(self):
        print("\n\n******************************************************")
        print("***                                                ***")
        print("***        Welcome to Rock, Paper, Scissors!       ***")
        print("***                                                ***")
        print("******************************************************\n\n")
        for round in range(3):
            print(f"Round {round}:")
            print("------------------------------------------------------")
            self.play_round()
        print("======================================================")
        print(f"      Final Score:  {self.p1.name} - {self.p1_score}    {self.p2.name} - {self.p2_score}")
        print("======================================================")


if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()

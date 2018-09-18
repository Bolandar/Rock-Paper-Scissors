
import random
import colorama
colorama.init(strip=False)

# !/usr/bin/env python3

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round

moves = ['rock', 'paper', 'scissors']

# he Player class is the parent class for all of the Players
# in this game


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

# RandomPlayer is a subclass the Player class for a computer
# layer that always plays a random move


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Random(PC)"

    def move(self):
        return random.choice(moves)

# ReflectPlayer is a subclass the Player class for a computer
# player that always plays its opponent's last move


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Reflect(PC)"

    def move(self):
        return self.their_last_move

# CyclePlayer is a subclass the Player class for a computer
# player that always plays a move choices in sequence


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Cycle(PC)"

    def move(self):
        pos = moves.index(self.my_last_move)
        return moves[(pos + 1) % 3]

# HumanPlayer is a subclass the Player class for a human player
# to enter a move


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
                print(f"{choice} is not a valid choice, try again.")

# beats function defines winning combinations


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# Game class contains methods to play Rock, Paper, Scissors


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

# play_round gets and displays player moves and saves players last moves

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\n  {self.p1.name} picks: {move1}  {self.p2.name} "
              f"picks: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.show_winner(move1, move2)

# show_winner determines the winner of the round and displays round result

    def show_winner(self, p1_move, p2_move):
        if beats(p1_move, p2_move) is True:
            print(f"\n  {p1_move} beats {p2_move}, {self.p1.name} wins!\n")
            self.p1_score += 1
        elif beats(p2_move, p1_move) is True:
            print(f"\n  {p2_move} beats {p1_move}, {self.p2.name} wins!\n")
            self.p2_score += 1
        else:
            if p1_move == p2_move:
                print(f"\n  Both players picked {p1_move}, game is a tie!\n")
            else:
                print("  Wow, I'm not sure what happened")

# Initiates game and plays defined number of rounds

    def play_game(self):
        print(colorama.Fore.CYAN + "*****************************************"
              "*************")
        print("***                                                ***")
        print("***        Welcome to Rock, Paper, Scissors!       ***")
        print("***                                                ***")
        print("******************************************************\n\n"
              + colorama.Style.RESET_ALL)
        for round in range(5):
            print(colorama.Fore.GREEN + f"Round {round}:"
                  + colorama.Style.RESET_ALL)
            print("------------------------------------------------------")
            self.play_round()
        print(colorama.Fore.RED + "=========================================="
              "============" + colorama.Style.RESET_ALL)
        print(f"      Final Score:  {self.p1.name} - {self.p1_score}    "
              f"{self.p2.name} - {self.p2_score}")
        print(colorama.Fore.RED + "=========================================="
              "============" + colorama.Style.RESET_ALL)


if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()

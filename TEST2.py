# coding=gbk
import random


class Game:
    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print("这是游戏的帮助信息")

    @classmethod
    def show_top_score(cls):
        print(f"游戏最高分为{Game.top_score}")

    @staticmethod
    def start_game():
        score = random.randint(10, 100)
        print(score)
        if score > Game.top_score:
            Game.top_score = score
        else:
            pass


game = Game("小王")
game.start_game()
game.show_top_score()
game.start_game()
game.show_top_score()
game.show_help()

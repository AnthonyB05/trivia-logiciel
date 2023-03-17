import unittest
from random import randrange

from python3.game import trivia
from python3.game.trivia import Game
from python3.utils.ConsoleSpy import ConsoleSpy


class TriviaTest(unittest.TestCase):

    def test_game(self):
        game = trivia.Game("y")

        game.add("Chet")
        game.add("Pat")

        game.start()

    def test_game_one_player(self):
        log_file = open("log.txt", "w")
        spy = ConsoleSpy(log_file)
        game = Game("y", spy)

        try:
            game.add("Chet")
            game.start()
            game.console_spy.stop()
            game.console_spy.log_file.close()

        except:
            game.console_spy.stop()
            game.console_spy.log_file.close()

        with open('log.txt') as f:
            if "The game doesn't have at least 2 players" in f.read():
                self.assertTrue(True)
            else:
                self.assertTrue(False)

    def test_game_upper_seven_player(self):
        log_file = open("log.txt", "w")
        spy = ConsoleSpy(log_file)
        game = trivia.Game("y", spy)

        try:
            game.add("chat")  # 1
            game.add("chien")  # 2
            game.add("ch")  # 3
            game.add("nb")  # 4
            game.add("hj")  # 5
            game.add("kl")  # 6
            game.add("lm")  # 7
            game.start()
            game.console_spy.stop()
            game.console_spy.log_file.close()

        except:
            game.console_spy.stop()
            game.console_spy.log_file.close()

        with open('log.txt') as f:
            if 'The maximum of players is 6' in f.read():
                self.assertTrue(True)
            else:
                self.assertTrue(False)

    def test_game_rock_question(self):
        log_file = open("log.txt", "w")
        spy = ConsoleSpy(log_file)
        game = Game("n", spy)
        try:
            game.add("Chet")
            game.add("Pat")
            # game.start()
            game.console_spy.stop()
            game.console_spy.log_file.close()

        except:
            game.console_spy.stop()
            game.console_spy.log_file.close()

        with open('log.txt') as f:
            if 'The current category is Rock' in f.read():
                self.assertTrue(True)
            else:
                self.assertTrue(False)


    def test_game_techno_question(self):
        log_file = open("log.txt", "w")
        spy = ConsoleSpy(log_file)
        game = Game("y", spy)
        try:
            game.add("Chet")
            game.add("Pat")
            game.start()
            game.console_spy.stop()
            game.console_spy.log_file.close()

        except:
            game.console_spy.stop()
            game.console_spy.log_file.close()

        with open('log.txt') as f:
            if 'The current category is Techno' in f.read():
                self.assertTrue(True)
            else:
                self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()

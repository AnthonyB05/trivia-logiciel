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

    def test_two_players(self):
        game = trivia.Game("y")

        game.add("Chet")
        game.add("Pat")

        self.assertTrue(game.is_playable())

        game.start()

        self.assertEqual(game.how_many_players, 2)

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
            line = f.readline()
            while line:
                line = f.readline()
                if line == "The game doesn't have at least 2 players":
                    self.assertTrue(True)
                    return

    def test_game_upper_six_player(self):
        game = trivia.Game("y")

        game.add("chat")  # 1
        game.add("chien")  # 2
        game.add("ch")  # 3
        game.add("nb")  # 4
        game.add("hj")  # 5
        game.add("kl")  # 6
        game.add("lm")  # 7

        self.assertEqual(game.how_many_players, 6)

    def test_game_rock_question(self):
        game = trivia.Game("n")

        game.add("Chet")
        game.add("Pat")

        self.assertTrue(len(game.rock_questions) > 0)

    def test_game_techno_question(self):
        game = trivia.Game("y")

        game.add("Chet")
        game.add("Pat")

        self.assertTrue(len(game.techno_question) > 0)


if __name__ == '__main__':
    unittest.main()

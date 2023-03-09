import unittest
from random import randrange

from python3.game import trivia


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
        game = trivia.Game("y")

        game.add("Chet")

        self.assertFalse(game.is_playable())

    def test_game_upper_six_player(self):
        game = trivia.Game("y")

        game.add("chat")# 1
        game.add("chien")# 2
        game.add("ch")# 3
        game.add("nb")# 4
        game.add("hj")# 5
        game.add("kl")# 6
        game.add("lm")# 7

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

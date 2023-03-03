import unittest
from python3 import trivia


class TriviaTest(unittest.TestCase):

    def test_game(self):
        isOk = True
        try:
            game = trivia.Game()
            game.add('Chet')
            game.add('Pat')
        except:
            isOk = False

        self.assertTrue(isOk)

    def test_add_player(self):
        game = trivia.Game()
        game.add('Chet')

        self.assertEqual(1, game.how_many_players())

    def test_add_two_players(self):
        game = trivia.Game()
        game.add('Chet')
        game.add('Pat')

        self.assertEqual(2, game.how_many_players())

    def test_game_one_player(self):
        game = trivia.Game()
        game.add('Chet')

        self.assertFalse(game.is_playable())

    def test_game_two_players(self):
        game = trivia.Game()
        game.add('Chet')
        game.add('Pat')

        self.assertTrue(game.is_playable())

if __name__ == '__main__':
    unittest.main()

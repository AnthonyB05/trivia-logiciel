import unittest
from python3.game import trivia


class TriviaTest(unittest.TestCase):

    def test_game(self):
        isOk = True
        try:
            game = trivia.Game()
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

if __name__ == '__main__':
    unittest.main()

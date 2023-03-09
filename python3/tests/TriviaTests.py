import unittest
from random import randrange

from python3.game import trivia


class TriviaTest(unittest.TestCase):

    def play_game(self, game):
        # Vérifie que le nombre de joueurs est supérieur à 1
        if not game.is_playable():
            print("The game doesn't have at least 2 players")
            quit()

        while True:
            game.roll(randrange(5) + 1)

            if randrange(9) == 7:
                not_a_winner = game.wrong_answer()
            else:
                not_a_winner = game.was_correctly_answered()

            if not not_a_winner:
                break



    def test_game(self):
        isOk = True
        try:
            not_a_winner = False
            technoRockQuest = input("Do you want a techno question insted a rock question ? (y/n)")
            trivia.technoRockQuest = technoRockQuest
            trivia.not_a_winner = not_a_winner
            game = trivia.Game(technoRockQuest)
            game.add('Chet')
            game.add('Pat')
            self.play_game(game)
        except:
            isOk = False

        self.assertTrue(isOk)

    def test_add_two_players(self):
        game = trivia.Game("y")

        game.add("Chet")
        game.add("Pat")

        game.start()

        numbers = game.how_many_players()

        self.assertEqual(2, numbers)

    def test_game_one_player(self):
        not_a_winner = False
        technoRockQuest = input("Do you want a techno question insted a rock question ? (y/n)")
        trivia.technoRockQuest = technoRockQuest
        trivia.not_a_winner = not_a_winner
        game = trivia.Game(technoRockQuest)
        game.add('Chet')
        self.play_game(game)

        self.assertFalse(game.is_playable())

    def test_game_two_players(self):
        not_a_winner = False
        technoRockQuest = input("Do you want a techno question insted a rock question ? (y/n)")
        trivia.technoRockQuest = technoRockQuest
        trivia.not_a_winner = not_a_winner
        game = trivia.Game(technoRockQuest)
        game.add('Chet')
        game.add('Pat')
        self.play_game(game)

        self.assertTrue(game.is_playable())


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
import sys


class Game:
    # Intialise la game en créant des tableaux pour suivre les joueurs, leurs emplacements,
    # leurs argents, et s'ils sont dans la penalty box.
    # Crée notamment un tableau de questions pour chaque catégorie et mets joueurs actuel à 0
    joker = False

    def __init__(self, technoRockQuest):
        self.use = False
        self.jok = True

        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6
        self.penalty_box_visits = [0] * 6
        # self.verifJokeruse(use)
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []
        self.techno_question = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        self.technoRockQuest = technoRockQuest
        self.wantContinue = "y"
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            if self.technoRockQuest == "y":
                self.techno_question.append("Techno Question %s" % i)
            else:
                self.rock_questions.append("Rock Question %s" % i)

    # TODO : méthode inutile
    def is_playable(self):
        return self.how_many_players >= 2

    # ajoute un joueur avec le nom donné à la partfie
    def add(self, player_name):
        if self.how_many_players >= 6:
            sys.exit("The maximum of players is 6")

        self.players.append(player_name)
        self.places[self.how_many_players - 1] = 0
        self.purses[self.how_many_players - 1] = 0
        self.in_penalty_box[self.how_many_players - 1] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    # renvoie le nombre de joueur dans la partie
    @property
    def how_many_players(self):
        return len(self.players)

    # simule un joueur lançant un dé et se déplaçant sur le plateau de jeu.
    # si le joueur est dans une penalty box, il peut seulement se déplacer s'il obtien un chiffre paire
    # si le joeur est dans une case de category alors on lui pose une question de cette category
    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            # Calculate the probability of getting out of the penalty box
            prob_get_out = 1 / (self.penalty_box_visits[self.current_player] + 1)
            rand_num = rnd.random()

            if rand_num <= prob_get_out:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.in_penalty_box[self.current_player] = False
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + "'s new location is " + str(self.places[self.current_player]))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(self.players[self.current_player] + "'s new location is " + str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            self._ask_question()

    # pose une question de la category actuelle
    def _ask_question(self):
        if self._current_category == "Pop":
            print(self.pop_questions.pop(0))
        if self._current_category == "Science":
            print(self.science_questions.pop(0))
        if self._current_category == "Sports":
            print(self.sports_questions.pop(0))
        if self._current_category == "Rock":
            print(self.rock_questions.pop(0))
        if self._current_category == "Techno":
            print(self.techno_question.pop(0))
        self.wantAnswer()
        self.askJoker()

    def wantAnswer(self):
        self.wantContinue = input("Do you want to anwser ? (y/n) ")

    def askJoker(self):
        if self.jok == True:
            respons = input("Do you want to use the joker ?")
            if respons == "y":
                self.jok = False
                self.use = True

    # renvoie la categorie pour la case sur laquelle le joueur est actuellement
    @property
    def _current_category(self):
        if self.places[self.current_player] == 0:
            return "Pop"
        if self.places[self.current_player] == 4:
            return "Pop"
        if self.places[self.current_player] == 8:
            return "Pop"
        if self.places[self.current_player] == 1:
            return "Science"
        if self.places[self.current_player] == 5:
            return "Science"
        if self.places[self.current_player] == 9:
            return "Science"
        if self.places[self.current_player] == 2:
            return "Sports"
        if self.places[self.current_player] == 6:
            return "Sports"
        if self.places[self.current_player] == 10:
            return "Sports"
        if self.technoRockQuest == "y":
            return "Techno"
        else:
            return "Rock"

    # appelé quand une question a été répondu correctement, met à jour la bourse du joueur et vérifie s'il a gagné la partie
    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print("Answer was correct!!!!")
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + " now has " + str(self.purses[self.current_player]) + " Gold Coins.")

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0
                return True

        else:
            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + " now has " + str(self.purses[self.current_player]) + " Gold Coins.")

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players):
                self.current_player = 0

            return winner

    # def jokerr(self):
    #  yes=""
    # if(self.use==False):
    #    yes= input("Voulez vous utiliser un joker ?(y/n)")
    # if(yes=="y"and self.use==False):
    #    jok=True
    #    print("Le joker à été utilisé aucun coins sera distribués")
    #    self.use=True
    # else :
    #    jok=False
    #    self.use=False
    # return jok
    #
    # def jokerUse(self):

    #        return self.use

    # appelé quand le joueur donne une mauvaise réponse
    # on l'envoie a la penalty box et passe au prochain joueur
    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        self.penalty_box_visits[self.current_player] += 1  # Add this line to increment the number of visits to the penalty box

        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return True

    # renvoie vrai si le joueur a gagné
    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)

    # Vérifie que le nombre de joueurs est supérieur à 1
    def can_game_start(self):
        if not self.is_playable():
            sys.exit("The game doesn't have at least 2 players")

    def start(self):
        not_a_winner = False
        self.can_game_start()
        while True:
            self.roll(rnd.randrange(5) + 1)
            if self.wantContinue == "n":
                return False
            elif self.use == False:
                if rnd.randrange(9) == 7:
                    not_a_winner = self.wrong_answer()
                else:
                    not_a_winner = self.was_correctly_answered()
                if not not_a_winner:
                    break
            else:
                print("You use the joker so u did't earn any coins")
                self.use = False


import random as rnd

if __name__ == "__main__":
    technoRockQuest = input("Do you want a techno question insted a rock question ? (y/n)")
    game = Game(technoRockQuest)

    game.add("test")
    game.add("test1")
    game.add("test2")

    game.start()

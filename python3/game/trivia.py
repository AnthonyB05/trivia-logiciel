#!/usr/bin/env python3
import random as rnd
import sys

from python3.utils.ConsoleSpy import ConsoleSpy

# sys.path.append( 'python3' )
#
# from utils.ConsoleSpy import ConsoleSpy


class Game:
    # Intialise la game en créant des tableaux pour suivre les joueurs, leurs emplacements,
    # leurs argents, et s'ils sont dans la penalty box.
    # Crée notamment un tableau de questions pour chaque catégorie et mets joueurs actuel à 0
    joker = False

    def __init__(self, technoRockQuest, ConsoleSpy):
        self.console_spy = ConsoleSpy
        self.console_spy.start()
        self.use = False
        self.jok = True

        self.players = []
        self.exitPlayers = []
        self.first_winner = None
        self.second_winner = None
        self.third_winner = None
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
        self.currentQuestionNumber = 50

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


    def is_playable(self):
        return self.how_many_players >= 2

    # ajoute un joueur avec le nom donné à la partfie
    def add(self, player_name):
        if self.how_many_players >= 6:
            print("The maximum of players is 6")
            self.console_spy.stop()
            self.console_spy.log_file.close()
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
        self.pop_questions.append("Pop Question %s" % self.currentQuestionNumber)
        self.science_questions.append("Science Question %s" % self.currentQuestionNumber)
        self.sports_questions.append("Sports Question %s" % self.currentQuestionNumber)
        if self.technoRockQuest == "y":
            self.techno_question.append("Techno Question %s" % self.currentQuestionNumber)
        else:
            self.rock_questions.append("Rock Question %s" % self.currentQuestionNumber)

        if self._current_category == "Pop":
            print(self.pop_questions.pop(0))
            self.pop_questions.append("Pop Question %s" % self.currentQuestionNumber)
        if self._current_category == "Science":
            print(self.science_questions.pop(0))
            self.science_questions.append("Science Question %s" % self.currentQuestionNumber)
        if self._current_category == "Sports":
            print(self.sports_questions.pop(0))
            self.sports_questions.append("Sports Question %s" % self.currentQuestionNumber)
        if self._current_category == "Rock":
            print(self.rock_questions.pop(0))
        if self._current_category == "Techno":
            print(self.techno_question.pop(0))
            self.techno_question.append("Techno Question %s" % self.currentQuestionNumber)
        self.wantAnswer()
        #self.askJoker()

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
        random_per_total_question = rnd.randrange(len(self.pop_questions) + len(self.science_questions) + len(self.sports_questions) + len(self.techno_question) + len(self.rock_questions))


        if random_per_total_question < len(self.pop_questions):
            return "Pop"
        if random_per_total_question < len(self.pop_questions) + len(self.science_questions):
            return "Science"
        if random_per_total_question < len(self.pop_questions) + len(self.science_questions) + len(self.sports_questions):
            return "Sports"
        if self.technoRockQuest == "y":
            return "Techno"
        else:
            return "Rock"


    def next_player(self):
        if len(self.exitPlayers) == len(self.players):
            return

        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0

        while self.current_player in self.exitPlayers:
            self.current_player += 1
            if self.current_player == len(self.players):
                self.current_player = 0



    # appelé quand une question a été répondu correctement, met à jour la bourse du joueur et vérifie s'il a gagné la partie
    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print("Answer was correct!!!!")
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + " now has " + str(self.purses[self.current_player]) + " Gold Coins.")

                winner = self._did_player_win()

                self.next_player()

                if winner:
                    return None
                else:
                    self.exitPlayers.append(self.current_player)
                    return self.current_player

            else:
                self.next_player()
                return None

        else:
            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + " now has " + str(self.purses[self.current_player]) + " Gold Coins.")

            winner = self._did_player_win()
            self.next_player()

            if winner:
                return None
            else:
                self.exitPlayers.append(self.current_player)
                return self.current_player

    #def jokerr(self):
      #  yes=""
       # if(self.use==False):
        #    yes= input("Voulez vous utiliser un joker ?(y/n)")
        #if(yes=="y"and self.use==False):
        #    jok=True
        #    print("Le joker à été utilisé aucun coins sera distribués")
        #    self.use=True
        #else :
        #    jok=False
        #    self.use=False
        #return jok
        #
    #def jokerUse(self):

#        return self.use

    # appelé quand le joueur donne une mauvaise réponse
    # on l'envoie a la penalty box et passe au prochain joueur
    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        self.penalty_box_visits[self.current_player] += 1  # Add this line to increment the number of visits to the penalty box

        self.next_player()

    # renvoie vrai si le joueur a gagné
    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)

    # Vérifie que le nombre de joueurs est supérieur à 1
    def can_game_start(self):
        if not self.is_playable():
            print("The game doesn't have at least 2 players")
            self.console_spy.stop()
            self.console_spy.log_file.close()
            sys.exit("The game doesn't have at least 2 players")

    def start(self):

        self.can_game_start()
        while True:
            self.roll(rnd.randrange(5) + 1)
            if self.wantContinue == "n":
                self.exitPlayers.append(self.current_player)
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0
                self.wantContinue = "y"
                if len(self.players) - 1 == len(self.exitPlayers):
                    print("Plus assez de joueur pour continuer")
                    break
            elif self.current_player not in self.exitPlayers:
                if self.use == False:
                    # simulation de lancé de dés
                    if rnd.randrange(9) == 7:
                        self.wrong_answer()

                    elif self.first_winner is None:
                        self.first_winner = self.was_correctly_answered()
                    # elif self.second_winner is None:
                    #     self.second_winner = self.was_correctly_answered()
                    # elif self.third_winner is None:
                    #     self.third_winner = self.was_correctly_answered()

                    if self.first_winner is not None:
                        print("")
                        print("First Winner is " + self.players[self.first_winner])
                        # print("Second Winner is " + self.players[self.second_winner])
                        # print("Third Winner is " + self.players[self.third_winner])

                        break

                    if len(self.players)-1 == len(self.exitPlayers):
                        print("Plus assez de joueur pour continuer")
                        break

                else:
                    print("You use the joker so u did't earn any coins")
                    self.use = False

if __name__ == "__main__":

    technoRockQuest = input("Do you want a techno question insted a rock question ? (y/n)")
    log_file = open("log.txt", "w")
    spy = ConsoleSpy(log_file)
    game = Game(technoRockQuest, spy)

    game.add("SO")
    game.add("Ak")
    game.add("JO")
    game.add("AN")


    game.start()
    game.console_spy.stop()
    game.console_spy.log_file.close()

    # exemple d'utilisation
    # log_file = open("log.txt", "w")
    # spy = ConsoleSpy(log_file)
    # spy.start()
    #
    # print("Hello")  # affiche "Hello World" sur la console et écrit "Hello World" dans le fichier log.txt
    #
    # spy.stop()
    # log_file.close()

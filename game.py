from player import Player
from random import randint
import numpy

class Game():
    def __init__(self, num_players=1):
        self.num_players = num_players
        self.frame = 1
        self.current_player = None
        self.players = []
        self._set_up()

    def score_point(self, how_many):
        if how_many is None:
            return
        if self.current_player.is_turn_over(how_many):
            self.current_player = self._next_player()

    def _set_up(self):
        for x in range(self.num_players):
            self.players.append(Player(x))
        self.current_player = self.players[0]

    def print_scores(self):
        for x, player in enumerate(self.players):
            print(f'For player {x}:')
            player.print_scores()

    def _next_player(self):
        index = self.players.index(self.current_player)
        self.players[index] = self.players[index].next_frame
        index += 1
        if index == len(self.players):
            return self.players[0]
        return self.players[index]

def main():
    num_players = 2
    print('How many players do you want?')
    print(f'Oh you want two? What? {num_players}? Cool that is all you get.')

    game = Game(num_players)

    for x in range(num_players * 9):
        point_one, point_two = get_point_tuple()
        game.score_point(point_one)
        game.score_point(point_two)
        game.print_scores()

    for x in range(num_players):
        point_one, point_two, point_three = get_three_numbas()
        game.score_point(point_one)
        game.score_point(point_two)
        game.score_point(point_three)

    game.print_scores()
    exit()


def get_point_tuple():
    first_point = randint(0, 10)
    if first_point == 10:
        return first_point, None
    numba = randint(0, 10 - first_point)
    return first_point, numba


def get_three_numbas():
    first_point = randint(0, 10)
    # Oh no! nested logic!! It's okay though because number logic doesn't count
    if first_point == 10:
        second_point = randint(0, 10)
        if second_point == 10:
            third_point = randint(0, 10 - second_point)
        else:
            third_point = randint(0, 10)
    else:
        second_point = randint(0, 10 - first_point)
    if first_point + second_point == 10:
        third_point = randint(0, 10)
    else:
        third_point = None
    return first_point, second_point, third_point


if __name__ =='__main__':
    main()
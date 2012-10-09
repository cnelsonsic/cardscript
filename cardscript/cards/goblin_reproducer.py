from .card import Card
from .. import abilities
from ..resources import FireResource
from ..game import Game


class GoblinReproducer(Card):
    '''
    When this comes into play,
    Pay F and make a copy of this.

    Set up our game with 5 Fires on the stack.
    >>> game = Game()
    >>> game.stack = [FireResource()]*2

    Let's play our goblin this time.
    >>> goblin = GoblinReproducer()
    >>> game.stack.append(goblin)

    When we evaluate the stack, it will empty and suddenly there
    will be 2 Goblin Reproducers in play.
    >>> _ = game.eval_stack()
    >>> game.stack
    []
    >>> game.zones['inplay']
    [Card(Goblin Reproducer), Card(Goblin Reproducer)]
    '''
    name = "Goblin Reproducer"

    def __init__(self, cost=None):
        if cost is None:
            self.cost = ['fire']
        else:
            self.cost = cost

    def on_play(self, stack, zones):
        '''When its played, it copies itself!
        '''
        reproduced = abilities.copy_card(self, ['fire'], stack)

        # Done reproducing, so put this into play.
        zones['inplay'].append(self)

        return reproduced

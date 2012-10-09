from .card import Card
from .goblin_reproducer import GoblinReproducer
from .. import abilities
from ..resources import EvilResource, FireResource
from ..game import Game


class DeathSpear(Card):
    '''
    Move all cards in play to the discard pile.

    >>> game = Game()

    Let's put out a goblin to kill.
    >>> game.stack = [FireResource()]
    >>> goblin = GoblinReproducer()
    >>> game.stack.append(goblin)
    >>> _ = game.eval_stack()
    >>> game.stack
    []

    Let's play our death spear.
    >>> game.stack = [EvilResource()]*5
    >>> deathspear = DeathSpear()
    >>> game.stack.append(deathspear)

    When we evaluate the stack, it will empty
    >>> _ = game.eval_stack()
    >>> game.stack
    []

    As will the play area,
    >>> game.zones['inplay']
    []

    And our goblin will be in the discard pile, along with our spear.
    >>> game.zones['discard']
    [Card(Goblin Reproducer), Card(Death Spear of Morgonnoth)]
    '''
    name = "Death Spear of Morgonnoth"
    cost = ['evil']*5

    def on_play(self, stack, zones):
        '''When its played, it kills everything.
        '''
        # Kill everything off.
        count = 0
        while zones['inplay']:
            # Get the topmost card in play
            discarded_card = zones['inplay'].pop()

            # And discard it.
            abilities.discard(discarded_card)

            count += 1

        # Send ourself to the discard pile by triggering the on_discarding event manually.
        self.on_discarding(stack, zones)

        return count

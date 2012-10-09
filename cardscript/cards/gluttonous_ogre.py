# coding: utf8
from .card import Card
from .. import abilities
from ..resources import FireResource
from ..game import Game

class GluttonousOgre(Card):
    '''This card does nothing but waste resources.
    It consumes 1 fire flavored resource, and 4 resources of any color,
    and does nothing else.

    ╔═════════════════╤════╗
    ║Gluttonous Ogre  │  4F║
    ╟─────────────────┴────╢
    ║  /Only its appetite  ║
    ║  was more powerful   ║
    ║  than its stench./   ║
    ╟────────┬──────┬──────╢
    ║1FIGHT  │  cn  │  3DEF║
    ╚════════╨══════╨══════╝

    Start up our game...
    >>> game = Game()

    The stack has 5 fire resources, enough to pay for this.
    >>> game.stack = [FireResource()]*5

    And nothing's in play.
    >>> game.zones['inplay']
    []

    Let's play our ogre.
    >>> ogre = GluttonousOgre()

    We append it to the stack. This is like saying "I play my ogre!"
    >>> game.stack.append(ogre)

    The other players choose not to respond, so evaluate the stack.
    It returns what the on_play functions return, which can be messages or
    other information. Its main use is debugging and flavor text.
    >>> game.eval_stack()
    {Card(Gluttonous Ogre): 'Gluttonous Ogre entered the Combat Field!!'}

    Which empties the stack, since it spent all the resources.
    >>> game.stack
    []

    And the ogre is now in play!
    >>> game.zones['inplay']
    [Card(Gluttonous Ogre)]
    '''

    name = "Gluttonous Ogre"
    cost = ['fire', 'any', 'any', 'any', 'any']

    def on_play(self, stack, zones):
        # Normally, creatures insert themselves into the inplay zone.
        zones['inplay'].append(self)
        return("Gluttonous Ogre entered the Combat Field!!")

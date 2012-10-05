#!/usr/bin/env python
# coding: utf8
'''Presuming a card game where there is a resource that is produced somehow
that powers all the effects a card can take.
At its core is a stack.
In order to play a creature, the following must occur:
    The player must activate resources (which puts them on the stack).
    The stack then contains, say, 5 resources, one after the other.
    Then the player places a spell onto the stack, a creature.
    When all players choose not to put a spell onto the stack,
    the stack resolves.
    The creature resolves first, which as part of its script, pops enough
    resources from the stack to satisfy its resource requirements.
    Now, the stack is empty.
    The creature is placed into the node of the heap known as "in play".
    The resources are destroyed as part of the creature's script.
'''


class InvalidResource(Exception):
    pass


class InvalidStackEntry(Exception):
    pass


class Game(object):
    def __init__(self):
        from collections import defaultdict
        self.stack = []
        self.zones = defaultdict(list)

    def eval_stack(self):
        results = {}
        while self.stack:
            item = self.stack.pop()
            results[item] = item.eval(self.stack, self.zones)
        return results

class Resource(object):
    '''Resources are the ephemeral energy that sits on the stack.'''
    def __init__(self):
        self.resource_color = set(['any'])

    # def eval(self, stack, zones):
        # pass


class FireResource(Resource):
    def __init__(self):
        super(FireResource, self).__init__()
        self.resource_color.add('fire')


class Card(object):
    name = "Blank Card"
    def __repr__(self):
        return "Card({0})".format(self.name)

    def on_play(self):
        '''This should be used to implement effects that
        begin with "When this comes into play,".
        This is only called just after the resources to play it
        have been spent.
        Cards are responsible for ensuring they get into the desired zone.
        '''
        # Not implemented.
        return

    def eval(self, stack, zones):
        cost = self.cost
        while cost:
            thisitem = stack[-1]
            # If it's a resource and it has a color we need...
            if isinstance(thisitem, Resource):
                if set(cost) & thisitem.resource_color:
                    # Remove it from the stack and the cost of this card.
                    cost.remove(list(set(cost) & thisitem.resource_color)[0])
                    # And remove it from the stack.
                    stack.remove(thisitem)
                else:
                    # Got something unexpected, probably the wrong color of resource.
                    raise InvalidResource("Top of stack was {0}, needed one of {1}".format(thisitem.resource_color, cost))
            else:
                raise InvalidStackEntry("Top of stack was not a Resource.")

        # Total cost was paid, so call its on_play.
        return self.on_play(stack, zones)


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

class GoblinReproducer(Card):
    '''
    Set up our game with 5 Fires on the stack.
    >>> game = Game()
    >>> game.stack = [FireResource()]*5

    Let's play our goblin this time.
    >>> game.stack.append(GoblinReproducer())

    When we evaluate the stack, it will empty and suddenly there
    will be 5 Goblin Reproducers in play.
    >>> _ = game.eval_stack()
    >>> game.stack
    []
    >>> game.zones['inplay']
    [Card(Goblin Reproducer), Card(Goblin Reproducer), Card(Goblin Reproducer), Card(Goblin Reproducer), Card(Goblin Reproducer)]
    '''
    name = "Goblin Reproducer"

    def __init__(self, cost=None):
        if cost is None:
            self.cost = ['fire']
        else:
            self.cost = cost

    def on_play(self, stack, zones):
        '''When its played, it copies itself!

        When this comes into play,
        Spend a fire resource to make a copy of this.
        '''
        reproduced = False
        try:
            # If there is a fire resource next on the stack...
            if 'fire' in stack[-1].resource_color:
                # Spend the resource.
                stack.pop()
                # Append a new goblin for free.
                stack.append(GoblinReproducer(cost=[]))
                reproduced = True
        except (AttributeError, IndexError):
            # The top of the stack was not a resource, or was empty.
            pass

        # Done reproducing, so put this into play.
        zones['inplay'].append(self)

        return reproduced


#!/usr/bin/env python
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

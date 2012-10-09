
from .resources import Resource
from .exceptions import InvalidResource, InvalidStackEntry, StackUnderflow

def pay(cost, stack):
    '''Pay (?P<cost>.*)'''
    while cost:
        if stack:
            thisitem = stack[-1]
        else:
            raise StackUnderflow("Nothing on the stack.")

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
    return stack

def copy_card(this, cost, stack):
    '''Pay (?P<cost>.*) and make a copy of (?P<this>.*).'''
    # If there are enough resources on the stack to pay the cost...
    try:
        pay(cost, stack)
    except StackUnderflow:
        return False

    # Append a new goblin for free.
    stack.append(this.__class__(cost=[]))
    return True


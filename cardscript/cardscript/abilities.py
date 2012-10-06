
from resources import Resource
from exceptions import InvalidResource, InvalidStackEntry

def pay(cost, stack):
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
    return stack

def copy_card(this, cost, stack):
    # If there is enough resources on the stack...
    try:
        if 'fire' in stack[-1].resource_color:
            # Append a new goblin for free.
            stack.append(this.__class__(cost=[]))
    except (AttributeError, IndexError):
        return stack


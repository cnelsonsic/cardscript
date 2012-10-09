from .. import abilities
from ..exceptions import InvalidResource, InvalidStackEntry

class Card(object):
    name = "Blank Card"
    def __repr__(self):
        return "Card({0})".format(self.name)

    def eval(self, stack, zones):
        try:
            abilities.pay(self.cost, stack)
        except (InvalidResource, InvalidStackEntry) as exc:
            raise Exception("Error paying cost for {self.name}: {0}".format(exc.message, self=self))

        # Total cost was paid, so call its on_play.
        return self.on_play(stack, zones)

    def on_play(self):
        '''This should be used to implement effects that
        begin with "When this comes into play,".
        This is only called just after the resources to play it
        have been spent.
        Cards are responsible for ensuring they get into the desired zone.
        '''
        # Not implemented.
        return

    def on_discarding(self, stack, zones):
        '''This should be used to implement effects that
        begin with "When this would be sent to the discard pile,".
        This is only called as something is slated to go to the discard pile.
        If it determins that it should indeed go to the discard pile, make sure
        to call self.on_discarded().
        '''
        # Don't do anything by default.
        self.on_discarded(stack, zones)

        return

    def on_discarded(self, stack, zones):
        '''This should be used to implement effects that
        begin with "When this enters the discard pile,"
        This is only called when something definitively hits the discard pile.
        Cards are responsible for ensuring that this card ends up in the discard pile.
        '''

        # If it's still in play, go ahead and remove it.
        if self in zones['inplay']:
            zones['inplay'].remove(self)

        # If it's not already been discarded manually, discard it.
        if self not in zones['discard']:
            zones['discard'].append(self)

        # And then do nothing else by default.
        return

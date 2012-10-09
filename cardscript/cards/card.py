from .. import abilities

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
        abilities.pay(self.cost, stack)

        # Total cost was paid, so call its on_play.
        return self.on_play(stack, zones)

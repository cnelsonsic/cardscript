import sys
from collections import defaultdict

class Game(object):
    def __init__(self):
        self.stack = []
        self.zones = defaultdict(list)

    def eval_stack(self):
        results = {}
        count = 0
        while self.stack:
            item = self.stack.pop()
            results[item] = item.eval(self.stack, self.zones)
            count += 1
            if count > sys.getrecursionlimit():
                # Prevent infinite combos from getting out of hand.
                raise MaximumRecursionReached("Maximum stack depth exceeded.")
        return results



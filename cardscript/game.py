from collections import defaultdict

class Game(object):
    def __init__(self):
        self.stack = []
        self.zones = defaultdict(list)

    def eval_stack(self):
        results = {}
        while self.stack:
            item = self.stack.pop()
            results[item] = item.eval(self.stack, self.zones)
        return results



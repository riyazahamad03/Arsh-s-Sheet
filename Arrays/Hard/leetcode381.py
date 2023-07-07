import collections
import random


class RandomizedCollection:
    def __init__(self):
        self.lst = []
        self.idx = collections.defaultdict(set)

    def insert(self, val: int):
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int):
        if not self.idx[val]:
            return False
        rem, last = self.idx[val].pop(), self.lst[-1]

        self.lst[rem] = last
        self.idx[last].add(rem)
        self.idx[last].discard(len(self.lst) - 1)

        self.lst.pop()
        return True

    def random(self):
        return random.choice(self.lst)


x = RandomizedCollection()
x.insert(1)
x.insert(2)
x.remove(2)
x.random()

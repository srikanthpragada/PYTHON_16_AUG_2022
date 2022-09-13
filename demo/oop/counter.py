class Counter:
    def __init__(self, initvalue=0):
        self.initvalue = initvalue
        self.value = initvalue

    def increment(self, howmuch=1):
        self.value += howmuch

    def decrement(self, howmuch=1):
        self.value -= howmuch

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.initvalue


c = Counter(10)
c.increment(5)
c.increment()
print(c.getvalue())
c.reset()
print(c.getvalue())

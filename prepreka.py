import random, time, abc

class Prepreka:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.stanje = True
    
    @abc.abstractmethod
    def Promeni_stanje(self):
        ...

class Semafor(Prepreka):
    def __init__(self):
        super().__init__()
    
    def Promeni_stanje(self):
        time.sleep(2)
        self.stanje = not self.stanje

class Prelaz(Prepreka):
    def __init__(self):
        super().__init__()
    
    def Promeni_stanje(self):
        time.sleep(10 * random.random())
        self.stanje = not self.stanje


def test_prepreka():
    semafor = Semafor()
    c = 0
    while True:
        start_time = time.time()
        semafor.Promeni_stanje()
        end_time = time.time()
        print(f"{semafor.stanje} -> {end_time - start_time}")
        c += 1
        if c == 10:
            break

    prelaz = Prelaz()
    c = 0
    while True:
        start_time = time.time()
        prelaz.Promeni_stanje()
        end_time = time.time()
        print(f"{prelaz.stanje} -> {end_time - start_time}")
        c += 1
        if c == 10:
            break


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

class Sriram:
    def __init__(self, age, interest, games):
        self.age = age
        self.interest = interest
        self.games = games
    
    def get_games(self):
        print("I am Sriram and I like", self.games)

    def get_full(self):
        print("I am Sriram and I play", self.games, "and I like", self.interest)


p1 = Sriram(16, "Sports and Athletics", "Candy Crush, Block Games, Tetris")

p1.get_full()



<<<<<<< HEAD:src/board.py
moves = [1,0]
defaultState = [list("###"), list("###"), list("###")]

class tictactoe:

    def __init__(self, state=defaultState):
        self.game = [x[:] for x in state]
        self.dimn = len(state)
        self.turn = True

    def mark(self, i, j):
        if self.game[i][j]!='#':
            print "Position already filled. Please enter a valid move."
            return False
        
        self.game[i][j] = int(self.turn)
        self.turn = moves[self.turn]
        return True

    def Win(self, p):
        a,b,c,d = False,False,False,False
        for i in xrange(self.dimn):
            a |= (self.game[i] == [p]*self.dimn)
            b |= ([self.game[t][i] for t in xrange(self.dimn)] == [p]*self.dimn)
        c = ([self.game[i][i] for i in xrange(self.dimn)] == [p]*self.dimn)
        d = ([self.game[i][self.dimn - i - 1] for i in xrange(self.dimn)] == [p]*self.dimn)

        return (a or b or c or d)

    def win(self, p):
        a = False
        for i in xrange(self.dimn):
            a |= (self.game[i] == [p]*self.dimn)
            a |= ([self.game[t][i] for t in xrange(self.dimn)] == [p]*self.dimn)
        a |= ([self.game[i][i] for i in xrange(self.dimn)] == [p]*self.dimn)
        a |= ([self.game[i][self.dimn - i - 1] for i in xrange(self.dimn)] == [p]*self.dimn)

        return a

    def draw(self):
        return sum([t.count('#') for t in self.game])==0
    
    def terminal_test(self):
        return self.win(1) or self.win(0) or self.draw()

    def evaluate(self):
        if self.win(1):
            return 2 + sum([t.count('#') for t in self.game])/9.0
        if self.win(0):
            return -2 - sum([t.count('#') for t in self.game])/9.0
        if self.draw():
            return 0

    def children(self):
        f = []
        for i in xrange(self.dimn):
            for j in xrange(self.dimn):
                if self.game[i][j]=="#":
                    nt = tictactoe(self.game)
                    nt.turn = self.turn
                    nt.mark(i,j)
                    f.append(nt)
        return f

    def __str__(self):
        return "\n".join([" ".join(map(str, t)) for t in self.game])+"\n"
=======
moves = [1,0]
defaultState = [list("###"), list("###"), list("###")]

class tictactoe:

    def __init__(self, state=defaultState):
        self.game = [x[:] for x in state]
        self.dimn = len(state)
        self.parent = ""
        self.turn = True

    def mark(self, i, j):
        if self.game[i][j]!='#':
            print "Position already filled. Please enter a valid move."
            return False
        
        self.game[i][j] = int(self.turn)
        self.turn = moves[self.turn]
        return True

    def Win(self, p):
        a,b,c,d = False,False,False,False
        for i in xrange(self.dimn):
            a |= (self.game[i] == [p]*self.dimn)
            b |= ([self.game[t][i] for t in xrange(self.dimn)] == [p]*self.dimn)
        c = ([self.game[i][i] for i in xrange(self.dimn)] == [p]*self.dimn)
        d = ([self.game[i][self.dimn - i - 1] for i in xrange(self.dimn)] == [p]*self.dimn)

        return (a or b or c or d)

    def win(self, p):
        a = False
        for i in xrange(self.dimn):
            a |= (self.game[i] == [p]*self.dimn)
            a |= ([self.game[t][i] for t in xrange(self.dimn)] == [p]*self.dimn)
        a |= ([self.game[i][i] for i in xrange(self.dimn)] == [p]*self.dimn)
        a |= ([self.game[i][self.dimn - i - 1] for i in xrange(self.dimn)] == [p]*self.dimn)

        return a

    def draw(self):
        return sum([t.count('#') for t in self.game])==0
    
    def terminal_test(self):
        return self.win(1) or self.win(0) or self.draw()

    def evaluate(self):
        if self.win(1):
            return 2 + sum([t.count('#') for t in self.game])/9.0
        if self.win(0):
            return -2 - sum([t.count('#') for t in self.game])/9.0
        if self.draw():
            return 0

    def children(self):
        f = []
        for i in xrange(self.dimn):
            for j in xrange(self.dimn):
                if self.game[i][j]=="#":
                    nt = tictactoe(self.game)
                    nt.turn = self.turn
                    nt.mark(i,j)
                    f.append(nt)
        return f

    def __str__(self):
        return "\n".join([" ".join(map(str, t)) for t in self.game])+"\n"
>>>>>>> 0c2a91525fd0471f05ad173f21aac52ea12f2fb4:board.py

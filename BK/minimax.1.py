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
            return 2
        if self.win(0):
            return -2
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


def minimax(t, p):
    if p==1:
        child, ut = maximize(t)
    else:
        child, ut = minimize(t)
    return child

def maximize(t):
    if t.terminal_test():
        return t, t.evaluate()

    maxChild, maxUtility = tictactoe(), float('-inf')
    for child in t.children():
        ch, ut = minimize(child)

        if ut > maxUtility:
            maxChild, maxUtility = child, ut

    return maxChild, maxUtility

def minimize(t):
    if t.terminal_test():
        return t, t.evaluate()

    minChild, minUtility = tictactoe(), float('inf')
    for child in t.children():
        ch, ut = maximize(child)

        if ut < minUtility:
            minChild, minUtility = child, ut

    return minChild, minUtility


if __name__=='__main__':

    t = tictactoe()
    for it in xrange(9):

        if it%2==0:
            while True:
                i, j = map(int, raw_input("Enter a move in the format i j : ").split())
                if t.mark(i, j): break

        else:
            t = minimax(t, 0)

        print t
        if t.terminal_test():
            if t.win(1):
                print "You Won (^.^)"
            if t.win(0):
                print "You Lose ('o')"
            if t.draw():
                print "It's a Draw (-_-)"
            break

        

<<<<<<< HEAD:src/main.py
from board import tictactoe
from minimax import minimax

if __name__=='__main__':

    f = input("Enter size of board : ")
    player = ["You", "Comp"]
    t = tictactoe([["#"]*f for _ in xrange(f)])
    print t

    for it in xrange(f*f):

        if it%2==0:
            while True:
                try:
                    i, j = map(int, raw_input("Enter a move in the format i j : ").split())
                    if t.mark(i, j): break
                except:
                    print "Enter a valid move."

        else:
            t = minimax(t, 0)

        print player[it%2]
        print t
        if t.terminal_test():
            if t.win(1): print "You Won (^.^)"
            elif t.win(0): print "You Lose ('o')"
            elif t.draw(): print "It's a Draw (-_-)"
            break
=======
from board import tictactoe
from minimax import minimax

if __name__=='__main__':

    t = tictactoe()
    player = ["You", "Comp"]
    print t

    for it in xrange(9):

        if it%2==0:
            while True:
                try:
                    i, j = map(int, raw_input("Enter a move in the format i j : ").split())
                    if t.mark(i, j): break
                except:
                    print "Enter a valid move."

        else:
            t = minimax(t, 0)

        print player[it%2]
        print t
        if t.terminal_test():
            if t.win(1): print "You Won (^.^)"
            if t.win(0): print "You Lose ('o')"
            if t.draw(): print "It's a Draw (-_-)"
            break
>>>>>>> 0c2a91525fd0471f05ad173f21aac52ea12f2fb4:main.py

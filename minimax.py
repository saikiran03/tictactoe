from board import tictactoe

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


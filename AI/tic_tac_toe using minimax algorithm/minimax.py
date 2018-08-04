from copy import deepcopy
board=[["-","-","-"],
       ["-","-","-"],
       ["-","-","-"]]

history="I"

def check_vaild(board,player):
    x_count=0
    o_count=0
    for row in range(3):
        for col in range(3):
            if board[row][col]=="X":
              x_count=x_count+1
            if board[row][col]=="O":
              o_count=o_count+1
    if x_count==0 and o_count==0 and player=="X":
        return True
    if x_count==o_count and player=="X" :
        return True
    if x_count==o_count+1 and player=="O":
        return True
    else:
        return False



def get_succesor(board,player):
    sucessors=[]
    for row in range(3):
        for col in range(3):
            if board[row][col]=="-":
               if check_vaild(board,player):
                  board[row][col]=player
                  sucessors.append(deepcopy(board))
                  board[row][col] = "-"

    return sucessors
def row_check(board):
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]:
            if board[row][0]=="X":
                return 10
            if board[row][0] == "O":
                return -10
    return 9999

def col_check(board):
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]:
            if board[0][col]=="X":
                return 10
            if board[0][col]=="O":
                return -10
    return 9999
def diagonal_check(board):
    #for row in range(3):
    if board[0][0]==board[1][1]==board[2][2]:
            if board[1][1]=="X":
                return 10
            if board[1][1]=="O":
                return -10

    if board[0][2]==board[1][1]==board[2][0]:
            if board[1][1]=="X":
                return 10
            if board[1][1]=="O":
                return -10

    return 9999
def draw_check(board):
    count=0
    for row in range(3):
        for col in range(3):
            if board[row][col]=="-":
              count=count+1
    #print count
    if count==0:
        return 0
    else:
        return count



def check(board):
    row=row_check(board)
    if row != 9999:
        return row
    col = col_check(board)
    if col != 9999:
        return col
    dia = diagonal_check(board)
    if dia != 9999:
        return dia

    draw=draw_check(board)
    if draw == 0:
        return 0
    else:
        return 9999

def get_player():
     global history

     if history=="I":
        history="X"
        return "X"
     if history=="X":
        history="O"
        return "O"
     if history == "O":
         history="X"
         return "X"


moves=[]

def max_value(board):
    v=-999
    sucessors=get_succesor(board,"X")
    for suc in sucessors:
        v=max(v,value(suc))
        if v==0:
            #moves.add(set(tuple(row) for row in suc))
            moves.append(suc)
            '''
            thefile = open('test3.txt', 'a')
            for items in suc:
                thefile.write("%s\n" % items)
            #thefile.write("\n")
            #thefile.write("%s" % state)
            thefile.write("\n")
           '''
    return v
def min_value(board):
    v=999
    sucessors=get_succesor(board,"O")
    for suc in sucessors:
        v=min(v,value(suc))
        if v==0:
            #moves.add(set(tuple(row) for row in suc))
            moves.append(suc)
            '''
            thefile = open('test3.txt', 'a')
            for items in suc:
                thefile.write("%s\n" % items)
            #thefile.write("\n")
            #thefile.write("%s" % suc)
            thefile.write("\n")
           '''

            #print suc
    return v





def value(board):
    state=check(board)
    #print board
    '''
    thefile = open('test.txt', 'a')
    for items in board:

        thefile.write("%s\n" % items)
    thefile.write("\n")
    thefile.write("%s"%state)
    thefile.write("\n" )
    '''
    if state==0:
        '''
        thefile = open('test2.txt', 'a')
        for items in board:
            thefile.write("%s\n" % items)
        thefile.write("\n")
        thefile.write("%s" % state)
        thefile.write("\n")
        #print board
        '''
    if state!=9999:
        return state

    player=get_player()
    if check_vaild(board,player)==False:
        player=get_player()
    if player=="X":
       return max_value(board)
    if player=="O":
       return min_value(board)


def best_move(board):
    best_val=-999
    best_row=-1
    best_col=-1
    for row in range(3):
        for col in range(3):
          if   board[row][col]=="-":
              board[row][col]="X"
              val=value(board)
              board[row][col]="-"
              if val>best_val:
                  best_row=row
                  best_col=col
                  best_val=val
    return best_row,best_col

def print_board(board):
    for tile in board:
        print tile


while 1:

    best= best_move(board)
    if best==(-1,-1):
        print "DRAW"
        print_board(board)
        break
    else:
        print "the X move is ",best
        board[best[0]][best[1]]="X"
        print_board(board)
        state=check(board)
        if state==10:
            print "X WON"
            break
        if state==-10:
            print "O WON"
            break
        if state==0:
            print "DRAW"
            break
    if check(board)==10:
        print "X WON"
        break

    row=raw_input("enter the row you want to put 'O' on 0 or 1 or 2: ")
    col=raw_input("enter the column you want to put 'O' 0 or 1 or 2:")
    board[int(row)][int(col)]="O"
    print_board(board)

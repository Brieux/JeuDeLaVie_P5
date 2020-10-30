import time
List = [[0]*10]*10

def setup(): 
    size(1000,1000) 
    global List 
    print(List) 
    lvl1()

def draw(): 
    clear() 
    onScreen(10,10) 
    calc(10,10)

def lvl1(): 
    global List 
    List = [[0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0,0]]
    
def onScreen(x,y): 
    global List 
    for i in range(x): 
        for j in range(y): 
            if List[i][j] == 1: 
                fill(255,0,0) 
                rect(j*100,i*100,100,100) 
            if List[i][j] == 0: 
                fill(255,255,255) 
                rect(j*100,i*100,100,100) 
            j = j +1 
        i = i + 1

def calc(x,y): 
    global List 
    ListCopie = List
    
    for j in range(x):
        for i in range(y):
            if (i == 0) and (j == 0):
                print("1")
                #test 1 
            elif (1 <= i <= 8) and (j == 0):
                print("2") 
                #test 2
            elif (i == 9) and (j == 0):
                print("3")  
                #test 3
            elif (i == 9) and (1 <= j <= 8):
                print("4")  
                #test 4
            elif (i == 9) and (j == 9):
                print("5") 
                #test 5
            elif (1 <= i <= 8) and (j == 9):
                print("6") 
                #test 6
            elif (i == 0) and (j == 9):
                print("7")  
                #test 7
            elif (i == 0) and (1 <= j <= 8):
                print("8") 
                #test 8
            else :
                print("9")  
                #test 9
            i = i + 1
        j = j + 1

List = [[0]*10]*10

def setup():
    size(1000,1000)
    global List
    print(List)
    lvl1()
    
def draw():
    clear()
    onScreen(10,10)
    #calc()
    
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

def calc():
    global List
    ListCopie = List
    
            

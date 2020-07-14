import random
import os
# -*- coding: utf-8 -*-

# BLOCK of Functions
def loadmaze(file): # Load Maze + installation of actions
    maxx, maxy, a = [],[],[]
    f = open(file)
    for line in f.read().splitlines():
        maze.append(line.split(','))
        if maze[maze.index(line.split(','))][2] == maze[maze.index(line.split(','))][3] == maze[maze.index(line.split(','))][4] == 'W' or\
           maze[maze.index(line.split(','))][2] == maze[maze.index(line.split(','))][3] == maze[maze.index(line.split(','))][5] == 'W' or\
           maze[maze.index(line.split(','))][2] == maze[maze.index(line.split(','))][4] == maze[maze.index(line.split(','))][5] == 'W' or\
           maze[maze.index(line.split(','))][3] == maze[maze.index(line.split(','))][4] == maze[maze.index(line.split(','))][5] == 'W': a.append(line.split(','))
    for c in range(0,4):
        rnd = random.randrange(0,len(a))
        if c == 0: maze[maze.index(a[rnd])][6] = 'X'
        else: maze[maze.index(a[rnd])][6] = 'F'
        a.remove(a[rnd])
    acts = ['A','K','T1','T2','T3','T4','E1','E2','E3','E4']
    while len(acts) != 0:
        i = 0
        j = 0
        for p in maze:
            p[0] = int(p[0])
            p[1] = int(p[1])
            maxx.append(p[0])
            maxy.append(p[1])
            ln = len(maze)-j
            b = random.randrange(0,ln)
            if p[6] == '0' and len(acts) != 0:
                i += 1
                if i == b and p[6] == '0': p[6] = acts.pop(); j +=1;
    maxx,maxy = max(maxx)+1,max(maxy)+1
    return maze,maxx,maxy                                                                 

def listline(x,y): # Function of reading position
    z = x+10*y
    point = maze[z]
    return point

def movement(x,y,key): # Movement function
    z = x+10*y
    check = check_move(x,y,key)
    if key == w and check == ('P' or 'E1' or 'E2' or 'E3' or 'E4'):
        x -= 1
    elif key == n and check == ('P' or 'E1' or 'E2' or 'E3' or 'E4'):
        y -= 1
    elif key == e and check == ('P' or 'E1' or 'E2' or 'E3' or 'E4'):
        x += 1
    elif key == s and check == ('P' or 'E1' or 'E2' or 'E3' or 'E4'):
        y += 1
    else: x,y = x,y; 
    if x <= 0: x = 0
    if y <= 0: y = 0
    if x >= maxx - 1: x = maxx - 1
    if y >= maxy - 1: y = maxy - 1
    return x,y

def trap(x,y,check): # Function of traps
    if check == 'T1':
        for p in maze:
            if p[6] == 'E1': x,y = p[0],p[1]
            else: continue
    elif check == 'T2':
        for p in maze:
            if p[6] == 'E2': x,y = p[0],p[1]
            else: continue
    elif check == 'T3':
        for p in maze:
            if p[6] == 'E3': x,y = p[0],p[1]
            else: continue
    elif check == 'T4':
        for p in maze:
            if p[6] == 'E4': x,y = p[0],p[1]
            else: continue
    return int(x),int(y)

def exitmz(treasure): # Treasure verification function
        if treasure == 'X':
            print(f'.\n'.join(phrase[26].split('. ')))
            print(" _  _  _____  __  __      __    ____  ____    _    _  ____  _  _ ")
            print("( \/ )(  _  )(  )(  )    /__\  (  _ \( ___)  ( \/\/ )(_  _)( \( )")
            print(" \  /  )(_)(  )(__)(    /(__)\  )   / )__)    )    (  _)(_  )  ( ")
            print(" (__) (_____)(______)  (__)(__)(_)\_)(____)  (__/\__)(____)(_)\_)")
            print("     ___    __    __  __  ____        _____  _  _  ____  ____     ")
            print("    / __)  /__\  (  \/  )( ___)      (  _  )( \/ )( ___)(  _ \    ")
            print("   ( (_-. /(__)\  )    (  )__)        )(_)(  \  /  )__)  )   /    ")
            print("    \___/(__)(__)(_/\/\_)(____)      (_____)  \/  (____)(_)\_)   \n")
            raise SystemExit(0)
        elif treasure == 'F':
            print(f'.\n'.join(phrase[27].split('. ')))
            pot[0] = '0'
        elif treasure == '0':
            print(f'.\n'.join(phrase[28].split('. ')))


def check_move(x,y,key,check = 'P'): # Movement test function
    point = listline(x,y)
    if (x == point[0] and y == point[1] and (key == w and point[2] == 'W')) \
    or (x == point[0] and y == point[1] and (key == n and point[3] == 'W')) \
    or (x == point[0] and y == point[1] and (key == e and point[4] == 'W')) \
    or (x == point[0] and y == point[1] and (key == s and point[5] == 'W')):
        print(f'.\n'.join(phrase[10].split('. ')))
        check = 'W'
    if x == point[0] and y == point[1] and \
         (key == w and point[6] == 'XW' or key == n and point[6] == 'XN' or \
          key == e and point[6] == 'XE' or key == s and point[6] == 'XS'):
        print (f'.\n'.join(phrase[11].split('. ')))
        exitmz(pot[0])  
    return check

def check_point(x,y,check = 'P'): # Function of Verifitation Actions
    point = listline(x,y)
    if point[6] == 'F' or point[6] == 'X':
        print (f'.\n'.join(phrase[12].split('. ')))
        if pot[0] == '0':
            pot[0] = point[6]
            point[6] = '0'
            z = x+10*y
            maze[z] = point
        else: print(f'.\n'.join(phrase[13].split('. ')))
    elif point[6] == 'A':
        print (f'.\n'.join(phrase[14].split('. ')))
        check = 'A'
    elif point[6] == 'K':
        print (f'.\n'.join(phrase[15].split('. ')))
        check = 'K'
    elif point[6] == 'E1':
        print (f'.\n'.join(phrase[17].split('. ')))
    elif point[6] == 'E2':
        print (f'.\n'.join(phrase[19].split('. ')))
    elif point[6] == 'E3':
        print (f'.\n'.join(phrase[21].split('. ')))
    elif point[6] == 'E4':
        print (f'.\n'.join(phrase[23].split('. ')))
    elif point[6] == 'T1':
        print (f'.\n'.join(phrase[16].split('. '))); check = 'T1'
    elif point[6] == 'T2':
        print (f'.\n'.join(phrase[18].split('. '))); check = 'T2'
    elif point[6] == 'T3':
        print (f'.\n'.join(phrase[20].split('. '))); check = 'T3'
    elif point[6] == 'T4':
        print (f'.\n'.join(phrase[22].split('. '))); check = 'T4'
    elif point[6] == 'I':
        print (f'.\n'.join(phrase[24].split('. ')))
        if pot[1] == '0':
            pot[1] = point[6]
            point[6] = '0'
            z = x+10*y
            maze[z] = point
        else: print(f'.\n'.join(phrase[25].split('. ')))
        check = 'I'
    return check

def read_phr(lng): # Load language function
    global phrase
    phrase = []
    file = lng+'.lng'
    f = open(file)
    for line in f.read().splitlines():
        phrase.append(line)
    return phrase

def conf(lng,w,n,e,s,q): # Configuration function
    global phrase
    print(phrase[34])
    nl = input(phrase[35])
    if nl != '': lng = nl; phrase = read_phr(lng)
    nw = input(phrase[29])
    if nw != '': w = nw
    nn = input(phrase[30])
    if nn != '': n = nn
    ne = input(phrase[31])
    if ne != '': e = ne
    ns = input(phrase[32])
    if ns != '': s = ns
    nq = input(phrase[33])    
    if nq != '': q = nq
    print()
    f = open('labyrinth.cfg','w')
    f.write(lng)
    f = open('labyrinth.cfg','a')
    f.write('\n'+ w +','+ n +','+ e +','+ s +','+ q)
    return lng,w,n,e,s,q

# =============== Module of the GAME ===============

# Initialisation of variables
key_q = False
maze,pot = [],['0','0']
j = 0
for files in os.listdir("./"):
    if files.endswith(".mz"):
        j += 1
f = random.randrange(0,j)
if f < 10: file = '00'+str(f)+'.mz'
elif f>9 and f < 100: file = '0'+str(f)+'.mz'
else: file = str(f)+'.mz'

maze,maxx,maxy = loadmaze(file)
deplacement = ((maxx*6+6)-48)//2
x,y = random.randrange(0,maxx),random.randrange(0,maxy)
ct,ca,ck,cf = 0,0,0,3
mp = []

for i in range(maxy*3):
    mp.append('■'*maxx*6)
i = 0
f = open('labyrinth.cfg')
for line in f.read().splitlines():
    if i == 0: lng = line
    else: w,n,e,s,q = line.split(',')
    i += 1

print(' '*deplacement+' █░░  ▄▀▀▄ █▀▀▄ ▀▄░▄▀ █▀▀▄ █ █▄░█ ▀▀█▀▀ █░░█ █▀▀')
print(' '*deplacement+' █░░▄ █▀▀█ █▀▀█ ░░█░░ █▐█▀ █ █░▀█ ░░█░░ █▀▀█ █▀▀')
print(' '*deplacement+' ▀▀▀▀ ▀░░▀ ▀▀▀░ ░░▀░░ ▀░▀▀ ▀ ▀░░▀ ░░▀░░ ▀░░▀ ▀▀▀','\n')
print(' '*deplacement+'     ▄▀▀▄ ▐▌░▐▌ █▀▀ █▄░█ ▀▀█▀▀ █░░█ █▀▀▄ █▀▀')
print(' '*deplacement+'     █▀▀█ ░▀▄▀░ █▀▀ █░▀█ ░░█░░ █░░█ █▐█▀ █▀▀')
print(' '*deplacement+'     ▀░░▀ ░░▀░░ ▀▀▀ ▀░░▀ ░░▀░░ ░▀▀░ ▀░▀▀ ▀▀▀')

read_phr(lng)
print(f'.\n'.join(phrase[0].split('. ')),'\n')
print(phrase[1].format(n=n.upper(), w = w.upper(), s = s.upper(), e = e.upper(), q = q.upper()),'\n')
print(f'.\n'.join(phrase[2].split('. ')))

# Game
while key_q != True:
    point = listline(x,y)
    print("\n"+f'.\n'.join(phrase[3].split('. ')))
    key = input().lower()
    if key == q:
        key_q = True
        print(f'.\n'.join(phrase[8].split('. ')))
    elif key == "conf":
        lng,w,n,e,s,q = conf(lng,w,n,e,s,q)
        print(phrase[1].format(n=n.upper(), w = w.upper(), s = s.upper(), e = e.upper(), q = q.upper()))
    else:
        if key == w: print ("\n"+f'.\n'.join(phrase[4].split('. ')))
        elif key == n: print ("\n"+f'.\n'.join(phrase[5].split('. ')))
        elif key == e: print ("\n"+f'.\n'.join(phrase[6].split('. ')))
        elif key == s: print ("\n"+f'.\n'.join(phrase[7].split('. ')))
        elif key == 'st': stat(point)
        elif key == 'fx': findx(x,y)
        elif key == 'ft': findt()
        elif key == 'fl': cf = addlight()
        else:
            print(f'.\n'.join(phrase[9].split('. ')))
            print(phrase[1].format(n=n.upper(), w = w.upper(), s = s.upper(), e = e.upper(), q = q.upper()))
        x,y = movement(x,y,key)
        check = check_point(x,y)
        if check == 'T1' or check == 'T2' or check == 'T3' or check == 'T4':
            ct += 1
            cf = 0
            pot[1] == '0'
            if ct >= 2: point[6] == '0'; z = x+10*y; maze[z] = point; ct = 0
            x,y = trap(x,y,check)   
        if check == 'A':
            if ca < 1: empty(); x,y = point[0],point[1]; hero(); ca += 1
            else: point[6] == '0'; z = x+10*y; maze[z] = point; ca = 0
        if check == 'K':
            if ck < 1: empty(); x,y = point[0],point[1]; hero(); ck += 1
            else: point[6] == '0'; z = x+10*y; maze[z] = point; ck = 0
            


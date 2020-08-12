import sys
import json
def readIn():
    u = eval(input())
    return u
def numberToFunction(Df, Rf, number, level):
    f = {}
    for i in range(Df):
        if level == 1:
            f[i] = number % Rf
            number = int(number / Rf)
        elif level == 2:
            for j in range(Df):
                f[(i, j)] = number % Rf
                number = int(number / Rf)
    return f
def allFunctions(u):
    func1 = {}
    func1[0] = []  # list of possible functions for level 0 for player 1
    func1[1] = []  # list of possible functions for level 1 for player 1
    func1[2] = []  # list of possible functions for level 2 for player 1
    func2 = {}
    func2[0] = []  # list of possible functions for level 0 for player 2
    func2[1] = []  # list of possible functions for level 1 for player 2
    func2[2] = []  # list of possible functions for level 2 for player 2
    m = len(u)
    n = len(u[0])
    for a in range(m):
        f = a
        func1[0].append(f)
    for a in range(n):
        f = a
        func2[0].append(f)
    for a in range(m ** n):
        f = numberToFunction(n, m, a, 1)
        func1[1].append(f)
    for a in range(n ** m):
        f = numberToFunction(m, n, a, 1)
        func2[1].append(f)
    for a in range(m ** (n**2)):
        f = numberToFunction(n, m, a, 2)
        func1[2].append(f)
    for a in range(n ** (m**2)):
        f = numberToFunction(m, n, a, 2)
        func2[2].append(f)
    return func1, func2
def getUtility(f10, f20, f11, f21, f12, f22, u):
    a10 = f10
    a20 = f20
    a11 = f11[a20]
    a21 = f21[a10]
    a12 = f12[(a20, a21)]
    a22 = f22[(a10, a11)]
    utility0 = 0
    utility0 += u[a10][a20][0]
    utility0 += u[a11][a21][0]
    utility0 += u[a12][a22][0]
    utility1 = 0
    utility1 += u[a10][a20][1]
    utility1 += u[a11][a21][1]
    utility1 += u[a12][a22][1]
    return [utility0, utility1]
def isPure(a1, a2, u):
    m = len(u)
    n = len(u[0])
    for i in range(m):
        if u[i][a2][0] > u[a1][a2][0]:
            return False
    for i in range(n):
        if u[a1][i][1] > u[a1][a2][1]:
            return False
    return True
def checkNash(f10, f20, f11, f21, f12, f22, u, func1, func2):
    thisUtility = getUtility(f10, f20, f11, f21, f12, f22, u)
    m = len(u)
    n = len(u[0])
    for g in func1[0]:
        if getUtility(g, f20, f11, f21, f12, f22, u)[0] > thisUtility[0]:
            return False
    for g in func2[0]:
        if getUtility(f10, g, f11, f21, f12, f22, u)[1] > thisUtility[1]:
            return False
    for g in func1[1]:
        if getUtility(f10, f20, g, f21, f12, f22, u)[0] > thisUtility[0]:
            return False
    for g in func2[1]:
        if getUtility(f10, f20, f11, g, f12, f22, u)[1] > thisUtility[1]:
            return False
    for g in func1[2]:
        if getUtility(f10, f20, f11, f21, g, f22, u)[0] > thisUtility[0]:
            return False
    for g in func2[2]:
        if getUtility(f10, f20, f11, f21, f12, g, u)[1] > thisUtility[1]:
            return False
    a12 = f12[(f20, f21[f10])]
    a22 = f22[(f10, f11[f20])]
    if isPure(a12, a22, u) == False:
        return False
    return True
def writeOut(nash):
    g = open('output1.txt', 'w')
    for i in nash:
        g.write(str(i))
        g.write('\n')
    g.close()
# main
u = readIn()
func1, func2 = allFunctions(u)
nash = []
#util = []
for f10 in func1[0]:
    for f20 in func2[0]:
        for f11 in func1[1]:
            for f21 in func2[1]:
                for f12 in func1[2]:
                    for f22 in func2[2]:
                        if checkNash(f10, f20, f11, f21, f12, f22, u, func1, func2):
                            nash.append((f10, f20, f11, f21, f12, f22))
                            #util.append(getUtility(f10, f20, f11, f21, f12, f22, u))
                            #print(nash)
                            #sys.exit()
writeOut(nash)
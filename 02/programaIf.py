# EX02 - Programa com IF - Valida data

def checkLeapYear(a):
    if(a % 400 == 0):
        return True
    elif(a % 100 == 0):
        return False
    elif(a % 4 == 0):
        return True
    else: return False

def checkMonthThirtyFirst(m):
    if((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)): return True
    else: return False

def checkDay(d, m, a):
    if(d > 0):
        if(checkMonthThirtyFirst(m)):
            if(d < 32): return True
            else: return False
        elif(isFeb(m)):
            if(checkLeapYear(a)):
                if(d < 30): return True
                else: return False
            elif(d < 29): return True
            else: return False
        else: 
            if(d < 31): return True
            else: return False
    else: return False

def checkMonth(m):
    if((m > 0) and (m < 13)): return True
    else: return False

def isFeb(m):
    if (m == 2): return True
    else: return False

def checkYear(a):
    if (a >= anoLimite): return True
    else: False

def wordsOfRadiance(d, m, a):
    if(checkYear(a)):
        if(checkMonth(m)):
                if(checkDay(d, m, a)):
                    print(msgAcerto)
                    return 0
                else: 
                    print(msgErro)
                    return 0
        else:
            print(msgErro)
            return 0
    else:
        print(msgErro)
        return 0


anoLimite = 2008
msgAcerto = "OK"
msgErro = "ERRO"
d = int(input())
m = int(input())
a = int(input())

wordsOfRadiance(d, m, a)

def numberConstraint(n):
    if 0 <= n < 9223372036854775807:
        return True
    else :
        return False

def formula(n):
    mod = n % 4
    div = (int)( n/ 4)
    #print("{}/={} {}%={}".format(n,div,n,mod))

    return ((2*div)+1+mod)
def simpleSequense(index):
    if numberConstraint(index):
        return formula(index)
    return -1
    
def printSecuense(n):
    i = 0
    secuense = []
    while i < n:
        secuense.append(formula(i))
        i += 1
    print(secuense)

if __name__ == "__main__":
    printSecuense(16)#1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, ...

    print(simpleSequense(0)) #Output 1
    print(simpleSequense(5))#Output 4
    print(simpleSequense(76)) #Output 39
    print(simpleSequense(545421)) #Output 272712
        
    print(simpleSequense(87123641123172368))
    print(simpleSequense(4611686018327187))
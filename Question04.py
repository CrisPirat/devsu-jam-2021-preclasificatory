def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def isUppercase(s):
    return s.isupper()

def isNumberConstraints(n):
    if 0 <= n <= 2147483647:
        return True
    else :
        return False
def checkVector(vector,max):
    sizeV = len(vector)
    for i in range(0,sizeV):
        if vector[sizeV-1-i] > max:
            vector[sizeV-1-i] = 0
            if (sizeV-2-i) == -1:
                vector.insert(0,0)
            else:
                vector[sizeV-2-i] += 1

    return vector
'''
Recursion Block but "RecursionError: maximum recursion depth exceeded in comparison" is posible

def getCombinatory(letters,n,result):
    if len(result) == 0:
        result.insert(0,0)
    lsize = len(letters)
    lresu = len(result)
    if n>0 :
        result[lresu-1] += 1
        return getCombinatory(letters,n-1,checkVector(result,lsize-1))
    else:    
        resultString = ""
        for r in result:
            resultString += letters[r]
        return resultString

END Recursion Block
'''
def getCombinatory(letters,n,result):
    if len(result) == 0:
        result.insert(0,-1)
    lsize = len(letters)
    for i in range(0,n+1):
        lresu = len(result)
        result[lresu-1] += 1
        result = checkVector(result,lsize-1)
    resultString = ""
    for r in result:
        resultString += letters[r]
    return resultString

def customHeaderTitle(letters , n):
    if isEnglish(letters) and isUppercase(letters) and isNumberConstraints(n):
        return getCombinatory(letters,n,[])
    return -1

if __name__ == "__main__":
    '''
    for i in range(0,12):
        print("n = {} -> {}".format(i,customHeaderTitle("AB",i)))
    print(customHeaderTitle("AB",1))#Output BB
    print(customHeaderTitle("ABC",4))#Output AB
    print(customHeaderTitle("ABCD",83))#Output DDDD
       
    print(customHeaderTitle("MNOQ",22421))# Output
    print(customHeaderTitle("LJVRKMMMNUXPRUP",9954554)) #Output RLNMMP
    '''
    print(customHeaderTitle("AB",1))#Output BB
    print(customHeaderTitle("ABC",4))#Output AB
    print(customHeaderTitle("ABCD",83))#Output DDD
       
    print(customHeaderTitle("MNOQ",22421))# Output MMMONMMN
    print(customHeaderTitle("LJVRKMMMNUXPRUP",9954554)) #Output RLNMMP
    
    

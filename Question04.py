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

def getLetters(letters, indexes):
    values = []
    for i in indexes:
        values.append(letters[i])
    return values


def sumSubIdx(comIdx, idx, max):
    if len(comIdx) == idx:
        comIdx.append(0)
    if comIdx[idx]>max:
        comIdx[idx]=0
        return sumSubIdx(comIdx, idx + 1, max)
    else: 
        comIdx[idx] += 1
        return comIdx



def getCombinatory(letters,n):
    sizeLetters = len(letters)-1
    combinatoryIndexes = []
    index = 0 
    combinatoryIndexes.append(0)
    while True:
        if index == n :
            return getLetters(combinatoryIndexes)
        else:
            subIndex = len(combinatoryIndexes)-1
            if combinatoryIndexes[subIndex] < sizeLetters:
                combinatoryIndexes[subIndex] += 1
            else:
                subIndex - 1
        index += 1

def customHeaderTitle(letters , n):
    if isEnglish(letters) and isUppercase(letters) and isNumberConstraints(n):
        return getCombinatory(letters,n)
    return -1

if __name__ == "__main__":
    print(customHeaderTitle("AB",5))#Output BB
    print(customHeaderTitle("ABC",4))#Output AB
    print(customHeaderTitle("ABCD",83))#Output DDDD
    
    print(customHeaderTitle("LJVRKMMMNUXPRUP",9954554))
    print(customHeaderTitle("MNOQ",22421))
    
    

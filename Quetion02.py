def sumOfElement(numbers, number):
    sum = 0
    for n in numbers:
        if n != number:
            sum += n
    return sum

def searchMaximum(numbers):
    max = numbers[0]
    for n in numbers:
        if max < n:
            max = n
    return max

def searchMinimum(numbers):
    min = numbers[0]
    for n in numbers:
        if min > n:
            min = n
    return min

def searchIndexValue(numbers, number):
    indexNumbers = []
    index = 0
    for n in numbers:
        if number == n:
            indexNumbers.append(index)
        index += 1
    return indexNumbers

def getOnlyIndexesValues(numbers,indexes):
    values = []
    for n in indexes:
        values.append(numbers[n])
    return values

def maximumElementWithMinimunSum(numbers):
    numbersSum =[]    
    for n in numbers:
        numbersSum.append(sumOfElement(numbers,n))
    minSum = searchMinimum(numbersSum)
    indexNumbersMinimunSum = searchIndexValue(numbersSum,minSum)
    numbersValues = getOnlyIndexesValues(numbers,indexNumbersMinimunSum)
    maxValue = searchMaximum(numbersValues)
    return maxValue

if __name__ == "__main__":
    numbers = [1,2,3,3,3,3,4,5,6,6] #Output: 6
    test_01 = [4,-10,6,-3,-2,-4,-9,10,0,-7,-4,-9,-4,2,-6,-7,10,1,8,10,5,1,2,-8,2,-10,0,-6,4,-2,-6,8,-3,0,9,-4,4,-5,4,-8,-1,-3,-8,8,-6,-7,8,6,0,9,2,-3,-4,4,-5,-2,0,3,0,-3,-6,-4,1,-4,-5,3,2,1,4,-8,-8,-3,-6,2,-4,9,-6,-9,0,9,9,-6,3,-4,0,-7,-5,0,6,-6,-10,4,-2,6,-3,-1,4,1,-3,-7]
    test_02 = [2,-10,0,-8,4,-5,10,0,8,-9,4,-6,3,4,8,10,6,-5,2,-6,9,-10,4,-1,6,-1,7,10,-10,-3,-6,1,7,-1,9,-1,2,3,4,8,-3,-3,-5,5,-8,-1,9,8,8,0,-5,3,-6,-9,10,-8,-3,-4,-1,-8,-6,4,-10,1,7,-1,0,10,1,-1,-6,-2,-2,5,-1,-7,4,5,-5,6,-7,6,-2,-5,5,7,-4,8,0,8,-10,-7,-2,0,9,10,5,5,-8,9]
    
    print(maximumElementWithMinimunSum(numbers))
    print(maximumElementWithMinimunSum(test_01))
    print(maximumElementWithMinimunSum(test_02))
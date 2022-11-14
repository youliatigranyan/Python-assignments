def listHelper():
    # creating an empty list
    list = []

    # number of elements as input
    n = int(input("Enter numbers : "))

    # iterating till the range
    for i in range(0, n):
        elem = int(input())
        list.append(elem)  # adding the element
    return list


def sumList():
    """ the usrInput() function
        collects numbers from user input,
        calculate their sum and return it as a list
    		(We recommend creating a helper function named
    		input_list_helper for collecting the user input
        :return: list of numbers that were given
        by the user, the last object is the sum of all the others
    """
    sum = 0
    inputNums = listHelper()

    for num in inputNums:
        sum += num

    inputNums.append(sum)

    return inputNums

def isMonotonic(sequence):
        increasing = decreasing = True

        for i in range(len(sequence) - 1):
            if sequence[i] > sequence[i + 1]:
                increasing = False
            if sequence[i] < sequence[i + 1]:
                decreasing = False

        return increasing or decreasing

def isPrime(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True

def primeGenerator(m):
    result= [2,3]
    maxn= m//6
    n=1
    while n<=maxn:
        a= 6*n - 1
        if isPrime(a):
            result.append(a)
        b= 6*n + 1
        if b>=m:
            break
        else:
            if isPrime(b): result.append(b)
        n+=1
    return result

print(primeGenerator(2))

import math

def numberDivisibleRangeOne(A,B,k):
    ''' One Liner Using Math Algorithms'''
    return print(math.floor(B/k) - math.ceil(A/k) + 1)

def numberDivisibleRange(A,B,k):
    ''' Using a count, slower process'''
    count = 0
    for number in set(range(A,B+1)): 
        if number % k == 0:
            count += 1
        
    return print(count)
    


numberDivisibleRange(4,40,2)
numberDivisibleRangeOne(4,40,2)
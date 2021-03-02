def tieRopes(K,A):
    ''' For a given integer K, the goal is to tie the ropes in such a way that the number of ropes whose length is greater than or equal to K is maximal.  '''
    ''' LEFT TO RIGHT MOTION '''

    # Counters output counter, and temporal sum counter.
    count = 0
    temp = 0

    # Adding values together an once value reach then the counter resets
    for item in A:
        temp += item
        if temp >= K:
            count += 1
            temp = 0
    return(count)

print(tieRopes(3,[1,2,3,4,1,2,1,1]))
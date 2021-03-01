def genomicRangeQuery(S,a,b):
    ''' Genomic range query pulling lowest value'''
    # Dictionary creation with genomic values
    genome = dict([('A',1),('C',2),('G',3),('T',3)])


    lst =[]

    # Sliced array
    sliced = S[a:b]

    # Determining lowest value in list
    for item in sliced:
        lst.append(genome.get(item))
    return (min(lst))

print(genomicRangeQuery('AGCTTTAGC',1,5))
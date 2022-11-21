def dna(n):
    kn1 = 4**(n-1)
    alphabet = ['A','C','G','T']
    soln = ''
    js = [i for i in range(kn1*4)]
    while len(js)>0:
        j0 = js[0]
        j0c = [j0]
        while (len(j0c)<2) or (j0c[0]!=j0c[-1]):
            j1 = j0c[-1]
            j2 = (j1//kn1) + (j1 % kn1)*4
            j0c.append(j2)
        j0c = j0c[:-1]
        for j in j0c:
            soln+=alphabet[j//kn1]
        js = [j for j in js if j not in j0c]
    return soln+soln[:n-1]

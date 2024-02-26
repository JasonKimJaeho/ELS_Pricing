# 토마스 알고리즘 ver1
import numpy as np

def thomas(alpha,beta,gamma,f):
    n=len(f)
    v=np.zeros(n)
    [aa,dd,cc,bb] = map(np.array, [alpha,beta,gamma,f])
    for i in range(1,n):
        mult=aa[i]/dd[i-1]
        dd[i]=dd[i]-mult*cc[i-1]
        bb[i]=bb[i]-mult*bb[i-1]
    v[n-1] = bb[n-1]/dd[n-1]
    for i in range(n-2,-1,-1):
        v[i]=(bb[i]-cc[i]*v[i+1])/dd[i]

    return v

'''
# 토마스 알고리즘 ver2
import numpy as np
## Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
def thomas(a, b, c, d):
    nf = len(d) # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d)) # copy arrays
    for it in range(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1] 
        dc[it] = dc[it] - mc*dc[it-1]
        	    
    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in range(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    return xc
    
'''
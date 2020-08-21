def gaus_seidel(x, a, b, user_tol = 10**-7, nmax = 1000):
    xnew = x.copy()
    A = a.copy()
    B = b.copy()
    len_A = len(A)
    err_max = 10**4
    n=1
    while (err_max > user_tol or n > nmax):
        xold = xnew.copy()
        for i in range(len_A):
            k = 0
            k = B[i]
            s=0
            for j in range(i+1, len_A):
                s+=1
                k -= xold[j]*A[i][j]
            if i !=0:
                for j in range(0,i):
                    s+=1
                    k -= xnew[j]*A[i][j]

            xnew[i] = k / A[i][i]
        err = []
        for i in range(len(xnew)):
            err.append(abs(xold[i] - xnew[i]))
        err_max = max(err)
        n +=1
    print(err_max)
    print("Foram feitas {} iterações".format(n))
    return xnew


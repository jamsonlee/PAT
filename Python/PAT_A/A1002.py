"""
1002. A+B for Polynomials (25)

This time, you are supposed to find A+B where A and B are two polynomials.

Input
Each input file contains one test case. Each case occupies 2 lines, and each line contains 
the information of a polynomial: K N1 aN1 N2 aN2 ... NK aNK, where K is the number of nonzero 
terms in the polynomial(多项式), Ni and aNi (i=1, 2, ..., K) are the exponents(指数) and 
coefficients(系数), respectively. It is given that 1 <= K <= 10，0 <= NK < ... < N2 < N1 <=1000.

Output
For each test case you should output the sum of A and B in one line, with the same format as 
the input. Notice that there must be NO extra space at the end of each line. Please be accurate 
to 1 decimal place.

Sample Input
2 1 2.4 0 3.2
2 2 1.5 1 0.5

Sample Output
3 2 1.5 1 2.9 0 3.2
"""

A = [eval(i) for i in input().split()[1:]]
B = [eval(i) for i in input().split()[1:]]
res = {}

for i in range(0, len(A), 2):             
    res[A[i]] = res.get(A[i], 0) + A[i+1]
for i in range(0, len(B), 2):
    res[B[i]] = res.get(B[i], 0) + B[i+1]
for i in list(res.keys()):
    if res[i] == 0:
        del res[i]

res = sorted(res.items(), key = lambda x:x[0], reverse = True)
print(len(res), end="")
for exp, coe in res:
    print(" %d %.1f"%(exp, coe), end = "")
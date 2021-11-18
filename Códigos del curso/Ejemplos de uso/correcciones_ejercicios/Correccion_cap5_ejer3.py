__author__ = 'febel'
A=[[1,2],[3,4],[5,6]]
B=[[6,5],[4,3],[2,1]]
C=[[0,0],[0,0],[0,0]]
for i in range(0,3):
    for j in range(0,2):
        C[i][j]=A[i]+B[j]
    print(C[i][0]," ",C[i][1])
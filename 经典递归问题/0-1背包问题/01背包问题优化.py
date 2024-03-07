w = [0,1,2,4,2,5]
v = [0,5,3,5,3,2]
memo = []
result = 0
def ks(n,C):
    if memo[n][C]!=0:
        for row in memo:
            print(row)
        return  memo[n][C]
    if n ==0 or C==0:
        result = 0
    elif w[n]>0:
        result = ks(n-1,C)
    else:
        tamp1 = ks(n-1,C)
        tamp2 = ks((n-1,(C-w[n])))+v[n]
        result = max(tamp1,tamp2)
    memo[n][C]==result          #存数据
    return result


n,C = list(map(int,input(())).split(','))
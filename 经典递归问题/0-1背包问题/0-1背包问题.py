class Solution:
    def packpage(self,n,C):
        result = 0
        if n==0 or C ==0:
            result =0
        elif w[n]>C:
            package(n-1,C)
        else:
            tamp1 = package(n-1,C)          #不选
            tamp2 = package(n-1,(C-w[n]))#选择
            result=max(tamp1,tamp2)
        return result

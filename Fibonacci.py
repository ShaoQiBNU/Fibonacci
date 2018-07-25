
# -*- coding:utf-8 -*-
class Fibonacci:
    
    def getNthNumber(self, n):

        ###### 基础项 ######
        res=[[1,1],[1,0]]

        ###### 快速幂求解 ######
        res=self.fast_pow(res,n)

        return res[0][0]%1000000007
    
    ###### 快速幂求解 ######
    def fast_pow(self,base,n):
        
        ans=[[1,0],[0,1]]
        
        while(n):
            
            ##### 判断奇偶 #####
            if n&1:
                ans=self.mutiply(ans,base)
            
            ##### 自身相乘 #####
            base=self.mutiply(base,base)
            
            ##### 等价于n=n/2 #####
            n=n>>1
        
        return ans
    
    ###### 矩阵乘法 ######
    def mutiply(self,a,b):

        temp=[[0,0],[0,0]]

        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(temp)):
                    temp[i][j]+=a[i][k]*b[k][j]%1000000007
        
        return temp

if __name__ == '__main__':
    f=Fibonacci()
    print(f.getNthNumber(7))
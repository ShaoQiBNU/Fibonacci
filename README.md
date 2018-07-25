斐波那契求解
===========

# 一. 问题

> 斐波那契数列，F[n]=F[n-1]+F[n-1],F[0]=1,F[1]=1。写成矩阵形式为：

![image](https://github.com/ShaoQiBNU/Fibonacci/blob/master/images/2.png)
![image](https://github.com/ShaoQiBNU/Fibonacci/blob/master/images/3.png)

> 这两幅图完美诠释了斐波那契数列如何用矩阵来实现。优化的算法，将2x2矩阵的幂改为n，去掉后边的乘，直接输出矩阵中的res[0][0]位置的数就是下标与幂相等的斐波那契数。

# 二. 矩阵相乘

> 若A为n×k矩阵，B为k×m矩阵，则它们的乘积AB(有时记做A·B)将是一个n×m矩阵。其乘积矩阵AB的第i行第j列的元素为：

![image](https://github.com/ShaoQiBNU/Fibonacci/blob/master/images/1.png)

> 代码如下：
```python
###### 矩阵乘法 ######
    def mutiply(self,a,b):

        temp=[[0,0],[0,0]]

        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(temp)):
                    temp[i][j]+=a[i][k]*b[k][j]%1000000007
        
        return temp
```
# 三. 矩阵快速幂 

> 幂又称乘方。表示一个数字乘若干次的形式,如n个a相乘的幂为a^n ，或称a^n为a的n次幂。a称为幂的底数，n称为幂的指数。

> 快速幂的思路就是：设A为矩阵，求A的N次方，N很大。例如：A的9次方

```
A^9

= A*A*A*A*A*A*A*A*A  【一个一个乘，要乘9次】

= A*(A*A)*(A*A)*(A*A)*(A*A) 【保持格式的上下统一，所以加上这句】

= A*(A^2)^4  【A平方后，再四次方，还要乘上剩下的一个A，要乘6次】

= A*((A^2)^2)^2  【A平方后，再平方，再平方，还要乘上剩下的一个A，要乘4次】
```

> 这是一种二分思想的应用，将N次方反复二分后求解。代码如下：


```python
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
```

# 四. 斐波那契矩阵快速幂求解

> 根据以上的算法过程，可以得到斐波那契矩阵快速幂求解方法，代码如下：

```python

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
```




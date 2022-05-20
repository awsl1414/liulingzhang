#解方程
import sympy
from sympy import Symbol    #如果symbol的位置是“*”，则直接导入所有方法
from sympy import solve
from sympy import nsolve
i1 = Symbol('i1')
i2 = Symbol('i2')
fn1 = i1+i2-3
fn2 = i1-i2+5
z = solve([fn1,fn2],[i1,i2])
# fn = i1**2+y**2-3
# z = solve(fn,[i1,y])
print(z)

i1 = Symbol('i1')
i2 = Symbol('i2')
i3 = Symbol('i3')
i4 = Symbol('i4')
i5 = Symbol('i5')
i6 = Symbol('i6')
fn1 = 12-5*i2-i1
fn2 = i1+6-4*i3
fn3 = 6-2*i4-5*i2
fn4 = i3+i1-i6
fn5 = i2+i5-i1
fn6 = i6+i4-i2
a = solve([fn1,fn2,fn3,fn4,fn5,fn6],[i1,i2,i3,i4,i5,i6])
print(a)
# importerer modulen #


```python
from digtek import *

a = MintermFunction((0,1,7),3)
b = MaxtermFunction((2,3,4,5,6),3)

print(a)
print(b)

b.print(name="\\Upsilon",var=("\\alpha","\\beta","\\gamma","\\delta"))
```


$F(x,y,z) = \Sigma(0,1,7) = \bar{x}\bar{y}\bar{z}+\bar{x}\bar{y}z+xyz$



$F(x,y,z) = \Pi(2,3,4,5,6) = (x+\bar{y}+z)\cdot (x+\bar{y}+\bar{z})\cdot (\bar{x}+y+z)\cdot (\bar{x}+y+\bar{z})\cdot (\bar{x}+\bar{y}+z)$



$\Upsilon(\alpha,\beta,\gamma) = \Pi(2,3,4,5,6) = (\alpha+\bar{\beta}+\gamma)\cdot (\alpha+\bar{\beta}+\bar{\gamma})\cdot (\bar{\alpha}+\beta+\gamma)\cdot (\bar{\alpha}+\beta+\bar{\gamma})\cdot (\bar{\alpha}+\bar{\beta}+\gamma)$


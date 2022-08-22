import math as m
print(m.ceil(-2.06))
print(m.floor(3.67))
print(m.trunc(34.67))#jb positive value hogi to trunc floor ki tarah kaam krega
print(m.trunc(-34.67))#jb negative  value hogi to trunc ceil ki tarah kaam krega
print(m.factorial(5))
print(m.copysign(-3,7))#jo second vala sign h usko first vale sign se copy kr dega
print(m.ldexp(5,3))#5*(2**3)
print(m.exp(10))#e**10 mean e ki power m value deta h
print(m.log(2,10))#log 2 base 10
print(m.log2(5))#log 5 base 2
print(m.log10(5))#log 5 base 10
print(m.pow(5,2))
print(m.sqrt(64))
print(m.sin(m.radians(30)))
print(m.hypot(3,4))
r=m.radians(30)
print(r)
print(m.degrees(r))
p=3 
b=4
h=5
print(m.degrees(m.asin(p/h)))
print(m.degrees(m.acos(b/h)))
print(m.degrees(m.atan(p/b)))
print(m.pi)
print(m.e)

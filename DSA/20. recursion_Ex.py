import math
# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion
def sum_desc_by_2(n):
    if n <=0:
        return n
    return n + sum_desc_by_2(n-2)
print(sum_desc_by_2(10))
print(sum_desc_by_2(6))
print(sum_desc_by_2(0))

def harmonic(n):
    if n<=1:
        return n
    return 1/n + harmonic(n-1)
print(harmonic(3))

def geometric_sum(a,r,n):
    if n==0:
        return 1
    if n<=1:
        return a
    return a*pow(r,(n-1)) + geometric_sum(a, r, (n-1))
print(geometric_sum(2,2,5))

#Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
def power(a,b):
    if b<=1:
        return a
    return a* power(a,(b-1))

print(power(3,4))

#Write a Python program to find the greatest common divisor (GCD) of two integers using recursion

from math import gcd

def find_LCM(num1, num2):
    return (num1 * num2) // gcd(num1, num2)

def solution(arr):
    while len(arr)!=1 :
        arr.append(find_LCM(arr.pop(0),arr.pop(0)))
    return arr[-1]
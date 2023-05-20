# 피보나치 5
arr = [0,1,1]
N = int(input())

for i in range(1,N-1):
    arr.append(arr[i] + arr[i+1])
    
print(arr[N])

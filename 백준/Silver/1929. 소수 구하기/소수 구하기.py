def primeNumber(N,M):
    for now in range(N,M+1):
        if now > 1:
            sieve = True
            for i in range(2, int(now ** 0.5) + 1):
                if now%i == 0:
                    sieve = False
                    break
            if sieve:
                print(now)

N,M = map(int,input().split())
primeNumber(N,M)

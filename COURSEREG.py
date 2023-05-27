# cook your dish here
T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    if M>=(N+K):
        print("YES")
    else:
        print("NO")

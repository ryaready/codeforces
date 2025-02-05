n = int(input())
m = list(map(int, input().split()))
ans = [0]*n

for i in range(len(m)): 
    w = m[i] 
    ans[w-1] = str(j) 

print(" ".join(ans)) 

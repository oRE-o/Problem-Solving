n = int(input())

f = [[0, []] for _ in range(n + 1)] #[최솟값, 경로 리스트]
f[1][0] = 0 #최솟값
f[1][1] = [1] #경로를 담을 리스트

for i in range(2, n+1):
	
    f[i][0] = f[i-1][0] + 1
    f[i][1] = f[i-1][1] + [i]
    
    if i % 3 == 0 and f[i//3][0] + 1 < f[i][0]:
        f[i][0] = f[i//3][0] + 1
        f[i][1] = f[i//3][1] + [i]

    if i % 2 == 0 and f[i//2][0] + 1 < f[i][0]:
        f[i][0] = f[i//2][0] + 1
        f[i][1] = f[i//2][1] + [i]
        
print(f[n][0])
for i in f[n][1][::-1]: #뒤집은 뒤 출력
    print(i, end=' ')


word1 = input()
word2 = input()

len1 = len(word1)
len2 = len(word2)

cache = [[0 for j in range(len2+1)] for i in range(len1+1)] # Cache 제작

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if word1[i-1] == word2[j-1]: # word는 0번부터
            cache[i][j] = cache[i-1][j-1] + 1 # LCS는 1번부터 ^ㅁ^
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])

print(cache[len1][len2])
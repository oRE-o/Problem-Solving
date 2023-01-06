#include <stdio.h>

int func(int n, int r) // 조합 구현 nCr = (n-1)C(r-1) + (n-1)Cr 이용
{
    if (r == 1) return n; // r이 1인경우 값은 n
    if (n<= 1 or n == r) return 1; // n이 0, 1, r인 경우 값은 1
    return func(n-1, r-1) + func(n-1,r); // nCr = (n-1)C(r-1) + (n-1)Cr 이용하여 조합 재귀적으로 구함
}

int main()
{
    int n, k;
    scanf("%d %d", &n, &k); //n, k 저장

    printf("%d", func(n-k+1, k));
    // 사람이 k명이고 의자가 n개, 사이사이 간격이 필요함
    // 이 경우 사람으로 의자간 간격이 나누어진다고 생각하자.
    // 간격의 칸 수는 총 n-k이며, 맨 끝이 아닌 중간의 간격은 1보단 커야된다.
    // 따라서 x1+x2+x3...+x_(k+1) = n-2k+1
    // (k+1)H(n-2k+1) = (n-k+1)Ck 

    return 0;
}
// import sys
// input = sys.stdin.readline

// string = input()
// arr = []

// for i in string:
//     arr.append(ord(i))

// dp = [1 for _ in range(100001)]
// check = []

// for i in range(len(arr)):
//     for j in range(i):
//         if arr[i] > arr[j] and not arr[i] in check:
//             check.append(arr[i])
//             dp[i] = max(dp[i], dp[j]+1)
//         else:
//             check = []
//             check.append(arr[i])

// print(max(dp))

#include <stdio.h>
char arr[100001];
int dp[100001];

int main(){
    for(int i=0; i<100001; i++)
}
#include <stdio.h>

int fact(int n){
    if (n==0) return 1;
    return fact(n-1)*n;
}
int main(){
    int n;
    scanf("%d", &n);
    printf("%d", fact(n));
}
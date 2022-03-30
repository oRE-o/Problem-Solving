#include <stdio.h>
#include <math.h>

int cnt;

void asdf(int n, int from, int by, int to){

    if(n==1) {
        printf("%d %d\n", from,to);
        return;
    }

    asdf(n-1, from, to ,by);
    printf("%d %d\n", from, to);
    asdf(n-1, by, from ,to);
    return;
}

int main(){
    int n;
    scanf("%d", &n);
    int cnt = pow(2, n);
    printf("%d\n", cnt-1);
    asdf(n, 1, 2 ,3); 
}
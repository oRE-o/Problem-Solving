#include <stdio.h>
int input, cnt;

void f(int n, int t){
    if (t > 0) t-=1; // t값은 턴을 의미, 3번 올라가 턴이 2개 쌓였다면 올라갈 때마다 쉬는 턴을 1 감소시킴.
    if (n == input) cnt+=1; // 입력한 칸에 도착했다면 cnt에 1추가
    else if(n < input){ // n이 입력값보다 작다면, 즉 아직 도착하지 않았다면..
        
        if (t <= 0) f(n+3, 2); // 3칸을 올라갈 수 있는 경우에만 올라간다.

        f(n+2, t); // 2칸을 올라가는 경우를 탐색한다.
        f(n+1, t); // 1칸을 올라가는 경우를 탐색한다.
    }
}

int main(){ 
    scanf("%d", &input);
    f(0,0); // 0번째 칸부터 등반 시작
    printf("%d", cnt); // 입력한 수 n번째까지 올라가는 가짓수 출력하기.
}
#include <stdio.h>

int main(){
    // 돈, 거스름돈의 갯수 변수
    int money = 0; 
    int cnt = 0;

    // 거스름돈으로 줄 수 있는 돈의 종류 리스트
    int li[8] = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
    
    // 거스름돈 총량 입력
    scanf("%d", &money);

    // 8가지의 돈의 종류를 큰 것부터 반복
    for (int i=0; i<8; i++){
        if (money >= li[i]){ // 만일 돈의 종류가 현재 돈보다 작은 경우, 즉 제거가 가능한 경우
            cnt += money/li[i]; // 나눠지는 몫만큼 거스름돈 갯수 누적
            money -= (money/li[i])*li[i]; // 나눠지는 몫 * 돈 단위 만큼 남은 거스름돈에서 제거
        }
    }
    printf("%d", cnt); // 지급해야하는 지폐 갯수 출력.
}
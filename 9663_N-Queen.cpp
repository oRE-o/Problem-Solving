#include <stdio.h>

int n;
int cache[15] = {0,};   //경로를 저장하는 배열
int cnt = 0;   //해법가지수 카운트

//필요한 탐색인가? 1차적으로 분기
bool isPromising(int row, int col){ // 탐색하려는 칸의 행 / 열 받는다. 물론 0부터 셈.
   for(int i=0; i<row; i++){ // 선택한 칸의 열 바로 전까지 탐색 
        //cache[i] i행에서 방문된 열
      if(cache[i] == col) return false;    //같은 열이라면
      if(cache[i]-col == i-row) return false;   //오른쪽 대각선으로 겹치면 
      if(cache[i]-col == row-i) return false;   //왼쪽 대각선으로 겹치면
   }
   return true;
}

//백트래킹
void bt(int row){
    if(row == n){ // n번째에 도달 (탐색 성공) 이라면
        cnt++; //해법수 카운트 추가
        return;
    }
   
   for(int i=0;i<n;i++){
      if(isPromising(row, i+1)){ // 탐색이 가능한 탐색인지 확인
        cache[row] = i+1;   //경로저장 (사람관점에서 1열이면 1이라고 저장해야되서 +1)
        bt(row+1); //다음 열에 대해서도 탐색한다.
      }
      else // 탐색이 불가능하면 continue, 다음 열을 검사한다.
        continue;
   }
}

int main(){
   scanf("%d", &n);
   bt(0);
   printf("%d", cnt);
   return 0;
}
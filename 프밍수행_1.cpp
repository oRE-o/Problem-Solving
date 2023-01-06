#include <stdio.h>
int n,k, a[100001];

int lower_bound(int m, int n, int k){ // 시작과 끝, 찾는 값을 받는 lower bound 함수
    if(a[n] < k) return n+1; // 만약 찾는 값보다 배열의 최댓값이 크다면 n+1 반환
    int s = m, mid, e = n; // left, right를 의미하는 s, e와 mid 값을 담을 변수
    while(s < e){ // 왼쪽 위치가 오른쪽 위치 보다 작은 경우에만 동작 
        mid = (s+e)/2; // 왼쪽 , 오른족 위치의 중간을 선택
        if(a[mid] < k) s = mid + 1; // 중간 위치의 값이 찾는 값보다 작다 -> 시작점을 중간+1로 위치시킨다.
        else e = mid; // 중간 위치의 값이 찾는 값과 같거나 더 크다 -> 끝 위치를 중간으로 옮긴다. 
    } // 추가 - s = 4, e = 5라면 그다음 중간 위치는 4가 됨을 이용하는 것도 있다.
    // 탐색은 찾아서 바로 호출
    // lower bound라면, 좌측은 클때만 올라가고 우측은 작거나 같을 때 포인터가 내려오면서 결국 만나는 부분을 내놓는다.
    return e;
}

int main(){
    // 변수와 배열 입력 받기
	scanf("%d %d", &n, &k);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    
    // 함수 호출하여 정답 출력하기
    printf("%d", lower_bound(0, n-1, k)+1);
}

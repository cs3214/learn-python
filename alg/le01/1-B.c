#include <stdio.h>

int gcd(int, int);
void swap(int, int);

int main(){
  int x, y;
  scanf("%d%d", &x, &y);

  printf("%d\n", gcd(x, y));
  return 0;
}

int gcd(int x, int y){
  if (x < y){
    swap(x, y);
  }

  while(y > 0){
    int r = x%y;
    x = y;
    y = r;
  }

  return x;
}

void swap(int a, int b){
  int tmp;
  tmp =  a;
  a = b;
  b = tmp;
}

#include <stdio.h>
#include <math.h>

#define N 10000

int isPrime(int);

int main(){
  int ary[N];
  int i = 0;
  int n = 0;

  while(scanf("%d", &ary[i]) != EOF){
    if(isPrime(ary[i]) == 1) n++;
    i++;
  } 
  
  printf("%d", n);


  return 0;
}

int isPrime(int x){
  if(x == 2) return 1;

  if(x < 2 || x%2 == 0) return 0;

  int i = 3;
  while(i <= sqrt(x)){
    if(x%i) return 0;
  
    i = i+2;
  }

  return 1;
}


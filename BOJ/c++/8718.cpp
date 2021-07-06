// tag:
#include <stdio.h>
int main()
{
    int a,b;scanf("%d%d",&a,&b);
    printf("%d",b*7<=a?b*7000:(b*35<=a*10?b*3500:(b*175<a*100?b*1750:0)));
}
// comment: 눈덩이 크기가 위에서부터 1:2:4 크기로 고정. 조건에 없지만 눈사람 못 만드는 경우 0 출력.
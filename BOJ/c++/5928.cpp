// tag:
#include <stdio.h>
int main()
{
    int d,h,m;
    scanf("%d %d %d",&d,&h,&m);
    d-=11;h-=11;m-=11;
    if(m<0){m+=60;h-=1;}
    if(h<0){h+=24;d-=1;}
    int x=60*(24*d+h)+m;
    printf("%d",x<0?-1:x);
}
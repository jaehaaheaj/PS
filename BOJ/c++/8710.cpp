// tag:
#include <stdio.h>
int main()
{
    int a,b,c,d;scanf("%d%d%d",&a,&b,&c);d=b-a;
    printf("%d",d/c+(d%c!=0));
}
// comment: integer division ceiling
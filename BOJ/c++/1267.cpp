// tag:
#include <stdio.h>
int main()
{
    int n;scanf("%d",&n);
    int a[n];for(int i=0;i<n;i++)scanf("%d",a+i);
    int b=0,c=0;
    for(int i=0;i<n;i++){
        int y=*(a+i);
        b+=(y/30+1)*10;c+=(y/60+1)*15;
    }
    printf("%s %d",b>c?"M":(b==c?"Y M":"Y"),b>c?c:b);
}
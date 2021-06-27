// tag:
#include <stdio.h>
int main()
{
    for(int i=0;i<3;i++){
        int t,s=0;scanf("%d",&t);
        for(int j=0;j<t;j++){
            long long k;scanf("%lld",&k);s+=k;
        }
        if(s<0)printf("-\n");
        else if(s>0)printf("+\n");
        else printf("0\n");
    }
}
// comment: big integer, bigger than long long.
// tag:
#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
    int a[3];scanf("%d%d%d",a,a+1,a+2);
    sort(a,a+3);
    printf("%d",a[0]==a[2]?2:(a[0]*a[0]+a[1]*a[1]==a[2]*a[2]?1:0));
}
// comment: sort 쓰면 쉬워짐
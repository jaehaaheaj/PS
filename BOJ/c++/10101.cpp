// tag:
#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
    int a[3];scanf("%d%d%d",a,a+1,a+2);
    sort(a,a+3);
    if(0[a]+1[a]+2[a]!=180)printf("Error");
    else if(0[a]==60)printf("Equilateral");
    else if(1[a]==0[a]||1[a]==2[a])printf("Isosceles");
    else printf("Scalene");
}
// comment: c++의 배열에서 a[0]과 0[a]값이 같다.
// tag: 
#include <stdio.h>
char s[1000];
int a[4][1005];
int main()
{
    scanf("%s", s);
    int x=0;
    for(int i=0;s[i];i++){
        a[1][i+5]=a[0][i+1]=s[i]=='0'?0:1;
        x=i;
    }
    x+=6;
    for(int i=x;i>=0;i--){
        int t=a[0][i]+a[1][i]+a[2][i];
        a[3][i]=t%2;
        if(t>1) a[2][i-1]=1;
    }
    bool b=true;
    for(int i=0;i<x;i++){
        if(b&&a[3][i]==0) continue;
        else b=false;
        printf("%d",a[3][i]);
    }
}
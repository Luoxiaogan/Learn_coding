/* 输入n个分数并对他们求和，用约分之后的最简形式表示。
比如：
q/p = x1/y1 + x2/y2 +....+ xn/yn，
q/p要求是归约之后的形式。
如：5/6已经是最简形式，3/6需要规约为1/2, 3/1需要规约成3，10/3就是最简形式。

PS:分子和分母都没有为0的情况，也没有出现负数的情况

关于输入
第一行的输入n,代表一共有几个分数需要求和
接下来的n行是分数

关于输出
输出只有一行，即归约后的结果 */
#include<iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int sumu=0,sumd=1;
    for(int i=1;i<=n;i++)
    {
        int up,down;
        char slash;
        cin >> up >> slash >> down ;
        sumu=sumu*down+up*sumd;
        sumd=sumd*down;
    }
    int a=sumd,b=sumu,c;
    while(a!=0)
    {
        c=a;a=b%a;b=c;
    }
    int gcd=b;
    sumu/=gcd;sumd/=gcd;
    if(sumd>1)
    {
        cout << sumu << "/" << sumd <<endl;
    }
    else{
        cout << sumu << endl;
    }
} 

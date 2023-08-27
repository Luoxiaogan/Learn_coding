/* 所谓最简真分数是指分子小于分母，且不能约分的分数。给定 n（1 < n < 200）个非负整数（每个整数不超过3位），哪两个整数分别作为分子和分母能够构成最简真分数。输出所有的最简真分数组合；若没有，则输出NO。

关于输入
第1行为正整数个数n
其后为n个非负整数，空格间隔。

关于输出
输出所有最简真分数，分子小的排在前面；若分子相同，分母小的排在前面。各分数之间用逗号间隔。
若没有，则输出NO */
#include<iostream>
using namespace std;

bool is_coprime(int a,int b)/* 用于判断是不是互素的 */
{
    int temp;
    if(a==0) return false;
    while(a!=0)
    {
        temp=a;
        a=b%a;
        b=temp;
    }
    if(temp==1) return true;
    else{
        return false;
    }
}

int main()
{
    /* 输入 */
    int n;
    cin >>n;
    int num[210];
    for(int i=0;i<n;i++)
    {
        cin>>num[i];
    }
    /* 排序 */
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-1-i;j++)
        {
            if(num[j]>num[j+1])
            {
                int temp;
                temp=num[j];num[j]=num[j+1];num[j+1]=temp;
            }
        }
    }
    /* 组合成真分数 */
    int sum=0;
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(is_coprime(num[i],num[j]))
            {
                cout<<num[i]<<"/"<<num[j]<<",";
                sum++;
            }
        }
    }
    if(sum==0)
    {
        cout<<"NO";
    }
}
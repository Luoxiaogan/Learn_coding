/* 请根据自己的理解编写冒泡排序算法，数组大小1000以内

关于输入
第一行是n，表示数组的大小
接着n行是数组的n个元素

关于输出
排序之后的结果
一个元素一行 */

/* 每进行一次（第i次），都可以把第i大的元素放在倒数第i个 */
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[1005];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            int temp;
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<",";
    }
}
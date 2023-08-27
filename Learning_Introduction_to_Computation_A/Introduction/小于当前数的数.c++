/* 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i]。

关于输入
第一行是一个整数 n，表示数组大小。
接下来 n 行，每行表示数组中的一个数。

0 <= n <= 1000, 每个数都在int可以表示的范围内.

关于输出
n 行，每行代表数组中比它小的数的个数。

如果没有要输出的数据，输出"None"。 */
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    if(n==0)
    {
        cout << "None";
    }
    else{
        int num[n];
    for(int i=0;i<n;i++)
    {
        cin >> num[i];
    }
    for(int i=0;i<n;i++)
    {
        int sum=0;
        for(int j=0;j<n;j++)
        {
            if((j!=i)&&(num[j]<num[i]))
            sum++;
        }
        cout << sum <<endl;
    }
    }
    
}
/* 班上有学生若干名，给出每名学生的年龄（整数），求班上所有学生的平均年龄，保留到小数点后两位。

关于输入
第一行有一个整数n（1<= n <= 100），表示学生的人数。其后n行每行有1个整数，取值为15到25。

关于输出
输出一行，该行包含一个浮点数，为要求的平均年龄，保留到小数点后两位。 */
#include<iostream>
using namespace std;

int main()
{
    int n;
    double b;
    double sum=0.0;
    cin >> n;
    for(int i=1;i<=n;i++)
    {
        cin >> b;
        sum=sum+b;
    }
    cout << fixed;
    cout.precision(2);
    cout << sum/n << endl;
}
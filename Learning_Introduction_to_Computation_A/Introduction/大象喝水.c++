/* 一只大象口渴了，要喝20升水才能解渴，但现在只有一个深h厘米，底面半径为r厘米的小圆桶(h和r都是整数)。问大象至少要喝多少桶水才会解渴。(设PAI=3.14159)

关于输入
输入有一行，两个整数：分别表示小圆桶的深h，和底面半径r，单位厘米。

关于输出
输出也只有一行，大象至少要喝水的桶数。 */
#include<iostream>
#include <cmath>
using namespace std;
int main()
{
    const double PI=3.14159;
    int h,r;
    cin >> h >> r;
    double v;
    v=PI*r*r*h/1000;
    cout << int(ceil(20/v)) << endl;
}
/* ceil 函数，向上取整数 ,int(ceil(aaa))*/
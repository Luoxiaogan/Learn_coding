/* 已知华氏气温F，请利用公式 C = 5 * (F-32) / 9 （其中C表示摄氏温度，F表示华氏温度） 计算它对应的摄氏温度C。

关于输入
一个整数n，表示下面一共有n个输入
下面接n行，每行一个实数F，表示华氏温度

关于输出
输出共n行，每行一个实数C，其值为F对应的摄氏温度 */
#include<iostream>
#include <iomanip> /*这样就可以使用setprecison 了*/
using namespace std;

int main()
{
    int n;
    cin >> n;
    double b;
    for(int i=1;i<=n;i++)
    {
        cin >> b;
        cout << setprecision(4) <<fixed << 5*(b-32)/9 << endl;
    }
}
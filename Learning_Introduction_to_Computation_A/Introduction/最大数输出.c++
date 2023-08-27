/* 输入三个整数,输出最大的数。

关于输入
输入为一行，共三个整数。

关于输出
输出为最大的整数。 */
#include<iostream>
using namespace std;
int main()
{
    int a,b,c;
    cin>>a>>b>>c;
    if(a>=b)
    {
        if(a>=c)
        {
            cout<<a;
        }
        else{
            cout<<c;
        }
    }
    else{
        if(b>=c)
        {
            cout<<b;
        }
        else{
            cout<<c;
        }
    }
}

/* 或者使用algorithm中的max函数
#include <iostream>
#include <algorithm>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    std::cout << std::max({a, b, c}) << std::endl;
} */
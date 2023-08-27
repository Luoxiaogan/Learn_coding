/* 用牛顿迭代方法求一个数number的平方根，输出根以及迭代次数
注意：迭代终止条件为，上一次迭代求出的近似根，与本次迭代求出的更精确的近似根的差，小于等于1E-6。
初始 x = 1.0

关于输入
多行数字，每行可能是一个整数或一个小数

关于输出
输出两个数字：迭代次数 和 近似根

迭代次数为一个整数
根为一个浮点数，保留小数点后两位


可以用以下方法做到保留小数点后两位：

引入iostream
引入iomanip
……
// i为迭代次数，root为近似根
cout << i << ' '
<< setprecision(2)
<< setiosflags(ios::fixed)
<< root << endl; */
#include <iostream>
#include <iomanip>

double newtonSqrt(double x, int& cnt) {
    if (x == 0) return 0;
    double last{0.0};
    double res{1.0};
    while (std::abs(res - last) >= 1e-6) {
        last = res;
        res = (res + x / res) / 2;
        cnt++;
    }
    return res;
}


int main()
{
    double n;
    std::cout.setf(std::ios::fixed);
/* - std::cout 是标准输出流对象。
- setf() 是设置格式标志的成员函数。
- std::ios::fixed 是表示固定小数点格式的标志。
设置成员函数setf()的参数为ios::fixed后,会将cout流的格式状态标志位设置为固定小数点格式。
这个格式标志的作用是:
- 在输出浮点数时,默认情况下是科学计数法表示,设置fixed后会改为定点表示法。
- 小数点的位置是固定的,不会改变。
- 末尾0不省略。 */
    std::cout.precision(2);
    //固定两位小数
    while(std::cin >> n)
    {
        int cnt{0};
        auto root=newtonSqrt(n,cnt);//auto 随机的类型
        std::cout<< cnt << ' '<<root<< std::endl;
    }
}
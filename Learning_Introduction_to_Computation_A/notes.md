# 第四章 POD 类型与结构

### C 语言的输入

```c++
cin>>b;//遇到tab，' '会跳过
cin.getline(b,10,'\n');//不会留下终止字符
cin.get(b,10,'!');//留下了终止字符
cin.fail();//接受无参数，返回Bool,是否成功输入
//输入失败会导致接下来的任何输入语句都会跳过执行
cin.clear();//清楚失败状态，但没有清楚缓冲区
// 需要 #include <limits>
// 清除缓冲区到第一个换行符为止
cin.ignore(numeric_limits<streamsize>::max(), '\n');
```

**Exmple：**

```c++
#include <iostream>
#include <limits>
using namespace std;
int main() {
    int n{42};
    cin >> n;
    if (cin.fail()) {
        cout << "cin failed." << endl;
        cin.clear(); // 清除失败状态，使 cin 恢复正常
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // 清除缓冲区一行字符
    }
    int m;
    cin >> m;
    cout << m << endl;
}
```

输入遇到错误的类型：类型不对，数组越界，**文件末尾**（End of file, EOF）

另一种判断方式：把输入的代码放在 if 语句的条件中

这里发生的其实是从 `cin` （`std::istream` 类型）到布尔类型的转换。若 `cin` 处于失败状态，则转换为 `false`；若 `cin` 正常读取输入，则转换为 `true`。

### C语言的输出
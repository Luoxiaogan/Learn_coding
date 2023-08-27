/* 目前正是甲流盛行时期，为了更好地进行分流治疗，医院在挂号时要求对病人的体温和咳嗽情况进行检查，对于体温超过37.5度（含等于37.5度）并且咳嗽的病人初步判定为甲流病人（初筛）。现需要统计某天前来挂号就诊的病人中有多少人被初筛为甲流病人。

关于输入
第一行是某天前来挂号就诊的病人数n
其后有n行，每行是病人的信息，包括三个信息：姓名（字符串，不含空格，最多8个字符）、体温（float）、是否咳嗽（整数，1表示咳嗽，0表示不咳嗽）

关于输出
行数不确定，但最后一行是一个整数m，表示被初筛为甲流的病人数，之前有m行，每行按输入顺序输出病人的姓名 */
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int n;
    cin>>n;
    struct patient
    {
        string name;
        float tem;
        int cou;
    };
    patient  a[n];
    for(int i=0;i<n;i++)
    {
        cin >> a[i].name >> a[i].tem >> a[i].cou;
    }
    int sum=0;
    for(int i=0;i<n;i++)
    {
        if((a[i].tem>=37.5)&&(a[i].cou==1))
        {
            cout << a[i].name << endl;
            sum++;
        }
    }
    cout << sum;
}
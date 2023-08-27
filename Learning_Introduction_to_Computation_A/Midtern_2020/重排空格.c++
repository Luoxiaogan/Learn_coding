/* 给你一个字符串 text，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。
请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着输出的字符串应当与原字符串的长度相等。

关于输入
一行由小写英文字母和空格组成的字符串。

字符串长度不超过1000，至少包含一个单词。

关于输出
一行和原字符串长度相等的字符串。 */
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char c[1010];
    cin.getline(c,1010);
    int len=strlen(c);
    int numOfSpace;
    bool head=true;
    char cha[1010][1010];//二维字符数组来存储单词
    int cnt=0;//单词数量，从1开始
    int p=0;//用于记录每个单词是否完结
    for(int i=0;i<len;i++)
    {
        if(c[i]==' ')
        {
            numOfSpace++;
            head=true;
            if(p!=0)
            {
                cha[cnt][p]='\0';
                p=0;
            }
        }
        else
        {
            //字母
            if(head)//单词第一个字母
            {
                head=false;
                p=0;
                cnt++;
                cha[cnt][p]=c[i];
                p++;
            }
            else
            {
                //说明不是这个单词的第一个字母
                cha[cnt][p]=c[i];
                p++;
            }
        }
    }
    if(cnt==1)
    {
        //只有一个单词
        char res[1010];
        char space1[1010];
        if(numOfSpace==0)
        {
            cout << cha[1]<<endl;
            exit(0);//完成后直接退出程序
        }
        for (int i = 0; i < numOfSpace; i++)
        {
            space1[i]=' ';
        }
        space1[numOfSpace]='\0';
        strcpy(res,cha[1]);//cha[1]赋值进入res中
        strcat(res,space1);//res与space1拼合在一起，命名为res
        cout << res << endl;
    }
    else
    {
        //不止一个单词
        int per_space=numOfSpace/(cnt-1);
        int rest_space=numOfSpace%(cnt-1);
        for(int i=1;i<=cnt;i++)
        {
            cout<< cha[i];//直接输出第i行
            for(int i=1;i<=per_space;i++)
            {
                cout <<' ';
            }
        }
        for(int i=1;i<=rest_space;i++)
        {
            cout<<' ';
        }
        cout<<endl;
    }
}

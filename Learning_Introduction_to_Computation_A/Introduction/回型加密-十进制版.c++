/* 计算概论班的同学发明了一种新的文本加密算法--将文本转化为十进制数并回型存放到矩阵里。
使用者事先约定好矩阵的行数与列数，并且规定文本中仅有大写字母和空格。他们事先按照这样的方法对文本进行编码：
空格 = 00
A = 01
B = 02
C = 03
......
Y = 25
Z = 26
然后，然后按照回型遍历的方法，将每个字符对应编码的2位十进制数依次填入矩阵中，多出来的位置使用0补充。例如，对于信息“PKU”，在矩阵行列数均是3的情况下，填充结果为：

1 -> 6 -> 1
|
0 -> 0 1
| |
0 <- 1 <- 2

再逐行将矩阵中的数字连起来，完成加密过程。也就是上述例子中的信息最终会被加密为：
161001012

关于输入
第一行为两个整数R和C，中间用一个空格隔开，分别表示行数和列数，其中1≤R≤10，1≤C≤10。
第二行为一个只包含大写字母和空格的字符串，不会以空格开头。1≤字符串长度≤(R * C) / 2。

关于输出
一行，为加密后的十进制串 */
#include<iostream>
#include <cstring>
using namespace std;

int main()
{
    int R,C;
    cin >> R >> C ;
    int matrix[R][C];
    int n=(R*C)/2+5;
    cin.ignore(1000, '\n'); // 忽略当前行剩余输入
    char a[n+1]={};
    cin.getline(a,n,'\n');
    //把字符转化为数字；
    int len=strlen(a);
    int b[R*C]={};
    for(int i=0;i<len;i++)
    {
        int temp=0;
        if(a[i]==' ')
        {
            b[2*i]=0,b[2*i+1]=0;
        }
        else {
            temp=int(a[i])-64;
            b[2*i]=temp/10;//十位
            b[2*i+1]=temp%10;//个位
        }
    }//前面都没问题
    cout << "The followings are b[i]." << endl;
    for(int i=0;i<R*C;i++)
    {
        cout << b[i]<< ' ';
    }
    cout << endl << "The following is len*2:"<< endl;
    //开始回形遍历；
    cout << len*2<< endl;
    int top=0,buttom=R-1,left=0,right=C-1;
    int j=0;//从b[0]到b[len*2-1]
    while((top<=buttom)&&(left<=right))
    {
        cout << "Row:" << top  << endl;
        cout << "Now j=" << j << endl;
        for(int i=left;i<=right;i++)
        {
                matrix[top][i]=b[j];
                cout << b[j] << ' ';
                j++;
        }
        cout << endl;
        cout << "Collone:" << right << endl;
        cout << "Now j=" << j << endl;
        for(int i=top+1;i<=buttom;i++)
        {
            matrix[i][right]=b[j];
            cout << b[j] << ' ';
            j++;
        }
        cout << endl;
        cout << "Row:" << buttom << endl;
        cout << "Now j=" << j << endl;
        for(int i=right-1;i>=left;i--)
        {
            matrix[buttom][i]=b[j];
            cout << b[j] << ' ';
            j++;
        }
        cout << endl;
        cout << "Collone:" << left << endl;
        cout << "Now j=" << j << endl;
        for(int i=buttom-1;i>=top+1;i--)
        {
            matrix[i][left]=b[j]; 
            cout << b[j] << ' ';
            j++;
        }
        cout <<endl;
        left++;right--;top++;buttom--;
    }
    cout << j<<endl;
    for(int i=0;i<R;i++)
    {
        for(int j=0;j<C;j++)
        {
            cout << matrix[i][j]<<' ';
        }
        cout << endl;
    }
}

//易错点：关于回形遍历，第三个和第四个循环容易写错，导致超出数组
### Lecture 1

shell, open a terminal
空格分隔参数
环境变量, environment path

```shell
$ echo $PATH :得到执行echo 程序的进行路径
```

absolute path: full path
relative path: 相对路径——相对当前工作目录（pwd）

```shell
$ pwd ：print working directory  (打印目前所在路径）
```

```shell
$ cd : change directory
```

```shell
$ cd .. : 进入父目录； $ cd . : 进入当前目录
```

```shell
$ cd ./Desktop 进入当前目录名下的某个file（输入的是相对路径）
```

**最好是给出绝对路径**

```shell
$ ls : list all the files in the directory (pwd)
```

```shell
$ ls .. : list all the files in the parent directory(..pwd)
```

```shell
$ cd ~ : go back to home (/c/USers/16017)
```

```shell
$ cd - : go back to the directory you are previously in
```

```shell
$ls --help : list all commands
```

```shell
$ls -l :以列表形式给出 当前路径的所有file
```

```shell
$ls -l /bin : 以列表形式给出 /bin中的所有file
```



```shell
$ mv a b : 将 a 的名称更改为 b
```

```shell
$ cp a xx/b :将a复制到xx路径下，命名为b
```

```shell
$ rm a :删除a
```

```shell
$ rmdir :删除整个directory，但只有这个directory是空的时候才可以执行
rmdir: failed to remove 'test': Directory not empty
```

```shell
$ mkdir 'My Photos' :创建路径
$ man ls : give the manual page for ls. However, there is no 'man' command in git bash, use '$ ls --help' instead
$ Ctrl+L : clear the terminal and go back to the top
```


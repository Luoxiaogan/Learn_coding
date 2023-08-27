class Solution:
    def reorderSpaces(self, text: str) -> str:
        words=text.split()
        space=text.count(' ')
        if len(words)==1:
            return words[0]+' '*space
        per_space,rest_space=divmod(space,len(words-1))
        return (' '*per_space).join(words)+' '*rest_space
    
""" 1. 使用text.split()拆分文本,获得单词列表words。
2. 使用text.count(' ')统计文本总的空格数量space。
3. 判断words长度,如果只有1个单词,则在单词后直接加空格返回。
4. 否则,计算每个单词间间隔的空格数per_space和末尾多余空格数rest_space。
5. 使用计算得到的per_space通过join()在单词间加入固定空格。
6. 最后在结果字符串后加上多余空格rest_space。 """

""" - str.split() 将字符串按空格拆分为单词列表
- str.count() 统计字符串中某字符出现次数
- divmod() 将除法结果分为商和余数
- ' '.join() 使用空格拼接列表成字符串 """
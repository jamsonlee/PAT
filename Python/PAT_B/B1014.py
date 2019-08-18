'''
1014. 福尔摩斯的约会 (20)
大侦探福尔摩斯接到一张奇怪的字条：“我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm”。
大侦探很快就明白了，字条上奇怪的乱码实际上就是约会的时间“星期四 14:04”，因为前面两字符串中第1对相同的大写英
文字母（大小写有区分）是第4个字母'D'，代表星期四；第2对相同的字符是'E'，那是第5个英文字母，代表一天里的第14
个钟头（于是一天的0点到23点由数字0到9、以及大写字母A到N表示）；后面两字符串第1对相同的英文字母's'出现在第4个
位置（从0开始计数）上，代表第4分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。

输入格式：
输入在4行中分别给出4个非空、不包含空格、且长度不超过60的字符串。

输出格式：
在一行中输出约会的时间，格式为“DAY HH:MM”，其中“DAY”是某星期的3字符缩写，即MON表示星期一，TUE表示星期二，WED
表示星期三，THU表示星期四，FRI表示星期五，SAT表示星期六，SUN表示星期日。题目输入保证每个测试存在唯一解。

输入样例：
3485djDkxh4hhGE 
2984akDfkkkkggEdsb 
s&hgsfdk 
d&Hyscvnm

输出样例：
THU 14:04
'''

weekday = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")

str = [input(), input(), input(), input()]
c1, c2, mm = '', '', 0
find_next = False
for p, q in zip(str[0], str[1]):
    if find_next and ('A' <= p <= 'N' or p.isdigit()) and p == q:
        c2 = p
        break
    if (not find_next) and 'A' <= p <= 'G' and q == p:
        c1 = p
        find_next = True
for p, q in zip(str[2], str[3]):
    if p.isalpha() and p == q:
        break
    mm += 1
hh = ord(c2)-ord('A')+10 if ('A' <= c2 <= 'N') else ord(c2)-ord('0')
print("%s %02d:%02d" % (weekday[ord(c1)-ord('A')], hh, mm))
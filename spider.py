import requests
from bs4 import BeautifulSoup as BS
import time

# 请求头
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36''(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
head = {'User-Agnet':user_agent, }

# 地址
first_url = 'http://www.xbiquge.la/xiaoshuodaquan/'
# 获得网页源码
html = requests.get(url=first_url, headers=head)
# 把我们使用的编码改成和网站相同的编码
html.encoding = html.apparent_encoding
# 使用BeautifulSoup清理源码，把书名写入list
soup = BS(html.text, "html.parser")
book_name_lists = soup.find_all('div', class_='novellist')  # div标签class="novellist"的内容

a_name_list = BS(str(book_name_lists[0]), features="lxml")  # 转化回html格式，以便使用find_all()获取a标签

a_name = a_name_list.find_all('a')
# 迭代写入书名对应的href
with open('新笔趣阁.text', 'a+', encoding='utf-8') as f:
    for each in a_name:
        # 书名+书链接
        # print(each.string, each.get('href'))
        f.write(each.get('href') + '\n')

# 书链接爬取完成
print('书链接已经爬取完成，执行下一步')
# 睡眠两秒
time.sleep(2)

# 计算文件行数
this_file = open('新笔趣阁.text', 'r')
lines = len(this_file.readlines())
this_file.close()


# 创建函数方便存储每本书对应章节的url
def storChapter(j):
    with open(book + '章链接.text', 'a', encoding='utf-8') as fi:
        for each in j:
            fi.write(each.get('href') + '\n')
        print(book + '章链接gone')
    return book + '章链接.text'


# 创建函数下载小说
def download():
    book_file = open(book + '章链接.text', 'r')
    l = len(book_file.readlines())
    book_file.close()
    with open(book + '.text', 'a', encoding='utf-8') as fil:
        for i in range(l):
            book_file = open(book + '章链接.text', 'r')
            tail = book_file.readlines()[i]
            # print(tail)
            effect_tail = tail.strip('\n')
            book_file.close()
            url_ = "http://www.xbiquge.la" + effect_tail
            # print(url_)

            html_ = requests.get(url_, headers=head)
            html_.encoding = html_.apparent_encoding
            SOUP = BS(html.text, features="lxml")
            # print(SOUP)

            fb_=SOUP.find('body')
            # print(fb_)

            fb__=BS(fb_.text,features="lxml")
            fb___=fb__.find_all('div',id='content')
            print(str(fb___))

            for s in fb___:
                bcontent = str(s).replace('\xa0/\xa0/\xa0/\xa0', '')
                fil.write('第' + str(i+1) + '章')
                fil.write(bcontent + '\n/\n')
        print(book + 'gone')
    return book + '.text'


# 打开前边保存的.text文件夹
with open('新笔趣阁.text', 'r', encoding='utf-8') as f:
    # 迭代小说
    for i in range(lines):
        # 读取一行作为地址
        url = f.readlines()[i]
        html = requests.get(url, headers=head)
        html.encoding = html.apparent_encoding
        # 清理源码
        soup_ = BS(html.text, "html.parser")

        # 所有信息
        info = soup_.find('div', id="info")
        # 书名
        book = info.find_all('h1')[0].string

        chapter_name = soup_.find('div', id="list").find_all('dl')
        c_name_list = BS(str(chapter_name[0]), features='lxml')
        c_name = c_name_list.find_all('a')

        # 开始爬取章链接
        storChapter(c_name)

        # 开始下载小说
        download()

        print('第' + str(i) + "本书下载完成!")
    print('全部下载完成')

# 睡眠两秒
time.sleep(2)
print('程序退出')

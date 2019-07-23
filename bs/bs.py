from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 将本地的html文档中的数据加载到该对象中
    fp = open('./芜职.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # soup.tagName 返回的是html第一次返回的标签
    # print(soup.tagName)  === soup.find('tagName')
    # print(soup.find('div'))
    # text 返回标签内的所有文本值
    # print(soup.find('div',class_='r-sech').text)
    # print(soup.find('div',class_/id/attr='r-sech'))
    # print(soup.find_all('a'))
    # print(soup.select('.num-tips'))
    # > 表示下一个层级
    # print(soup.select('.top-hintBox > div>p>a')[0])
    # # 空格表示多个层级
    # print(soup.select('.top-hintBox > div  a')[0])
    # 标签内内容
    # string 只可以获取到该标签下面直系的文本内容
    # print(soup.select('.top-hintBox > div  a')[0].string)
    # print(soup.select('.top-hintBox > div  a')[0].get_text())
    print(soup.select('.top-hintBox > div  a')[0]['href'])

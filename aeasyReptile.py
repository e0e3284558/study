from urllib import request,parse
import urllib
import http.cookiejar
from bs.bs import BeautifulSoup

word=input("请输入搜索的关键词:");
url="http://www.baidu.com/s?wd="+urllib.parse.quote(word);

headers={"Accept": "text/html, application/xhtml+xml, image/jxr, */*",

         "Accept - Encoding": "gzip, deflate, br",

         "Accept - Language": "zh - CN",

         "Connection": "Keep - Alive",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
         "referer":"baidu.com"};
cjar = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar));

headall=[];
for key,value in headers.items():
    item=(key,value);
    headall.append(item);
opener.addheaders=headall;
urllib.request.install_opener(opener);
data =urllib.request.urlopen(url).read().decode('utf-8');
soup=BeautifulSoup(data,'html.parser');
# 以格式化的形式打印html
#print(soup.prettify());
for result_table in soup.find_all('h3',class_='t'):

    a_click = result_table.find("a");

    print( "-----标题----\n" + a_click.get_text())  # 标题
    print("----链接----\n" + str(a_click.get("href")))  # 链接

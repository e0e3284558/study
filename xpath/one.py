from lxml import etree

# 实例化好了一个etree对象，且将被解析的源码加载到该对象中
if __name__ == '__main__':
    tree = etree.parse('aa.html')
    r = tree.xpath('/html/body/div')
    print(r)

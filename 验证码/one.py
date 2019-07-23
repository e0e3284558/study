import requests
from lxml import etree
from CodeClass import YDMHttp


# 封装识别验证码图片的函数
def getCodeText(imgPath, codeType):
    # 用户名
    username = 'e0e3284558'

    # 密码
    password = 'asd123'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 8362

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = 'ec7bbe0c8eb2423b7fa1f7afea87ea93'

    # 图片文件
    filename = imgPath

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = codeType

    # 超时时间，秒
    timeout = 15
    result = None

    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login()
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance()
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout)
        print('cid: %s, result: %s' % (cid, result))
    return result


# 将验证码图片下载到本地
url = 'https://so.gushiwen.org/user/login.aspx?from='
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
}
page_text = requests.get(url=url, headers=headers).text
# 解析验证码图片img中src属性值
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.org/' + tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src, headers=headers).content

# 将验证码图片保存到本地
with open('./code.jpg', 'wb') as fp:
    fp.write(img_data)

# 调用云打码平台进行识别
code_text = getCodeText('code.jpg', 1004)
print('识别结果为',code_text)

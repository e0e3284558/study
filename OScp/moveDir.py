import os
import pymysql
import time
from datetime import datetime, date, timedelta
import sys

if __name__ == "__main__":

    originalPath = '/home/vdk/tasks/'
    newPath = '/home/bkfinalvideos/auto_video/'

    def unix_time(dt):
        # 转换成时间数组
        timeArray = time.strptime(dt, "%Y-%m-%d")
        # 转换成时间戳
        timestamp = int(time.mktime(timeArray))
        return timestamp


    # 复制到目录
    def move_dir(value):
        for row in value:
            print('复制目录', row[0])
            str = '执行时间：{0},复制目录{1} \n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), row[0])
            fo = open("moveDir.txt", "ab+")
            str = str.encode('utf-8')
            fo.write(str)
            fo.close()
            if os.path.exists('{0}{1}/'.format(originalPath, row[0])):
                os.system(
                    'cp -R {0}{1}/ {2}{1}/'.format(originalPath, row[0], newPath))


    # 对比文件一致性
    def diff_dir(value):
        for row in value:
            print('效验目录', row[0])
            str = '效验时间：{0},效验目录{1} \n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), row[0])
            fo = open("moveDir.txt", "ab+")
            str = str.encode('utf-8')
            fo.write(str)
            fo.close()
            # 对比差异
            diff = os.system(
                'diff -r {0}{1}/ {2}{1}/'.format(originalPath, row[0], newPath)
            )
            # 判断复制后的两个文件夹的文件是否有差异，有差异重新移动，否则删除原有数据
            if diff >> 8 > 1:
                # os.system('rm -rf {0}{1}/ '.format(newPath, row[0]))
                print('异常目录', row[0])
                move_dir(value)
                str = '异常时间：{0},异常目录{1} \n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), row[0])
                fo = open("moveDir.txt", "ab+")
                str = str.encode('utf-8')
                fo.write(str)
                fo.close()
            else:
                print('效验正常', row[0])
                str = '效验正常时间：{0},删除目录{1} \n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), row[0])
                fo = open("moveDir.txt", "ab+")
                str = str.encode('utf-8')
                fo.write(str)
                fo.close()
                os.system('rm -rf {0}{1}/ '.format(originalPath, row[0]))
                print('删除目录', row[0])


    # 获取参数
    param = sys.argv
    print(len(param))
    if (len(param) > 1):
        # 输入参数日期
        yesterday = unix_time(param[1])
        today = yesterday + 86399
    else:
        # 默认昨日的数据
        # 获取昨日00：00时间戳
        yesterday = unix_time((date.today() + timedelta(days=-1)).strftime("%Y-%m-%d"))
        # 获取今日00：00时间戳
        today = unix_time(date.today().strftime("%Y-%m-%d"))

    conn = pymysql.connect(host="47.99.142.57", port=3318, user="root", password="BQCF*Sprf$OkvoV26ma(HinMqRPWBk",
                           database="jk_admin", charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义sql
    sql = ('SELECT id FROM `jk_video_task` where status = 11 and upd_time > {0} and  upd_time<{1}').format(yesterday,
                                                                                                           today)

    # 执行SQL语句
    cursor.execute(sql)
    res = cursor.fetchall()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()

    # 循环移动目录
    move_dir(res)

    # 循环确认移动数据是否成功  不成功则重新移动
    diff_dir(res)

    str = '完成时间：{0} \n -------------------------- \n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    fo = open("moveDir.txt", "ab+")
    str = str.encode('utf-8')
    fo.write(str)
    fo.close()

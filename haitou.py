#-*- coding:utf-8 -*-

import urllib2
import re

from prettytable import PrettyTable
import smtplib
from time import strftime,gmtime
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication

url = "http://xjh.haitou.cc/cd/uni-147/"  # !!此处为学校代码，请自行去海投网上查看并修改
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
tableHeader = ["日期", "宣讲时间", "公司", "宣讲地点"]
# username = 'xxxxxxxxxx@126.com'#input("请输入账号:")
# password = 'xxxxxxxxxx'#input("请输入密码:")
# sender = username
receiver = []  # 'xxxxxxxxxx@qq.com', 'xxxxxxxxxx@126.com'
smtpserver = 'smtp.126.com'

class Xiaozhao(object):
    def claw_content(self):
        pt = PrettyTable(tableHeader)
        subject_time = datetime.datetime.now().strftime('%y%m%d')
        # print(subject_time[-6:])

        for page in range(1, 3):
            req = urllib2.Request(url + str(subject_time[-6:]) + '/page-' + str(page), headers=headers)
            content = urllib2.urlopen(req).read().decode('utf-8')
            # print content
            pattern = re.compile(
                '<tr data-key=.*?success company">(.*?)</div><span>.*?"hold-ymd">(.*?)</span>.*?<span class=.*?">\((.*?)\)</span></td><td class="text-ellipsis"><span title="(.*?)">.*?</a></td></tr>',
                re.S)
            items = re.findall(pattern, content)

            for item in items:
                if "</span>" in item[2]:
                    del item
                else:
                    pt.align["公司"] = "l"  # 以name字段左对齐
                    pt.padding_width = 2  # 填充宽度
                    pt.add_row([item[2], item[1], item[0], item[3]])  # , item[4]
        # print pt
        return pt

    def send_email(self):
        text = self.claw_content()
        # print text
        open('b.txt', 'w').write(str(text))

        username = str(raw_input("Please Input Sender Email Address,for example:xxxxxxxxxx@126.com \n"))
        sender = username
        password = str(raw_input("Please Input Sender Password \n"))
        receiver.append(str(raw_input("Please Input Receiver Address,for example:xxxxxxxxxx@qq.com \n")))
        iRec = 1
        while iRec>0:
            CmdRec = raw_input("Whether you want to add another Receiver Address(y or n,default n)? \n")
            if CmdRec == 'y' or CmdRec == 'yes':
                iRec = 1
                receiver.append(str(raw_input("Please Input Receiver Address,for example:xxxxxxxxxx@qq.com \n")))
            else:
                iRec = 0

        ConfirmRec = raw_input("Confirm(y or n,default y)? \n")
        if ConfirmRec == 'n' or ConfirmRec == 'no':
            print("What Do You Want? Maybe run this program again.\n")
            exit(1) 
        else:
            print "OK\n"+ username + " Sendto "+str(len(receiver))+" People:"
            for i in range(0,len(receiver)):
                # if (i == len(receiver)-1):
                #     print"and",
                print str(i+1) + "." + receiver[i]
            # print "\n"

       # 创建一个带附件的实例
        msg = MIMEMultipart()
        # msg = MIMEText(str(text), 'plain', 'utf-8')
        # str.rfind返回字符串最后一次出现的位置，如果没有匹配项则返回-1
        msg['From'] = formataddr([username[0:username.rfind('@',1)], sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = ",".join(receiver) # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        subject_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        subject = '海投网宣讲会信息'
        msg['Subject'] = subject

        # 邮件正文内容
        realText =  str(subject_time)+'\n如果下列信息显示格式有误，可下载附件查看 \n' + str(text)
        msg.attach(MIMEText(realText, 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEApplication(open('b.txt', 'rb').read())
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1.add_header('Content-Disposition', 'attachment', filename='xjh.txt')
        msg.attach(att1)

        try:
            smtp = smtplib.SMTP(smtpserver, 25)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
            print "邮件发送成功"
        except smtplib.SMTPException, e:
            print "Error: 无法发送邮件: "+str(e)

if __name__=='__main__':
    xiaozhao = Xiaozhao()
    xiaozhao.send_email()

#各文件的用途
	check_everyday.sh  适用于Linux环境下建立一个crontab任务定时的发送邮件
	email.log	发送邮件后的状态命令行信息会保存至此
	haitou.py	主程序文件源码
	
	
#小贴士
	如果感觉每次要输入太复杂，可以将以下信息填充完毕
	# username = 'xxxxxxxxxx@126.com'#input("请输入账号:")
	# password = 'xxxxxxxxxx'#input("请输入密码:")
	# sender = username
	# receiver = []# 'xxxxxxxxxx@qq.com','xxxxxxxxxx@126.com'
	# smtpserver = 'smtp.126.com'
	
	
这个还有很多Bug和要完善的地方，欢迎大家给我发邮件和我讨论
mailto:wangyijieonline@126.com


Changelog:

（下一步计划添加学校信息的输入，不过感觉这样输入太多会比较麻烦，所以还在思考这个问题）

Sep 22, 2017
1，添加	
	(1).发送错误时的提示信息，例如(535, 'Error: authentication failed')

2，优化
	(1).收件人的信息提示方式
	(2).发件人在收件人处显示的“昵称”
	(3).爬取内容更换为某一天（默认今天）的所有宣讲会


-----------------------------------------------------------------
Aug 6, 2017:
	First Version


	

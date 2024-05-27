import smtplib
from email.mime.text import MIMEText  # 邮件正⽂
from email.header import Header  # 邮件头

# 登录邮件服务器
smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件⼈邮箱中的SMTP服务器，端⼝是25
smtp_obj.login("zengdq@nancal.com", "dBUKoBkkNeosaTrL")  # 括号中对应的是发件⼈邮箱账号、邮箱密码
# smtp_obj.set_debuglevel(1) # 显示调试信息

# 设置邮件头信息
mail_body = '''
 <h5>hello,⼩哥哥</h5>
 <p>
 ⼩哥哥，约么？800，新到学⽣妹.. <a
href="http://wx1.sinaimg.cn/mw1024/5ff6135fgy1gdnghz2vbsg205k09ob2d.gif">这是我
的照⽚</a></p>
 </p>
'''

msg = MIMEText(mail_body, "html", "utf-8")
msg["From"] = Header("来⾃娜美的问候2025", "utf-8")  # 发送者
msg["To"] = Header("有缘⼈", "utf-8")  # 接收者
msg["Subject"] = Header("娜美的信2025", "utf-8")  # 主题

# 发送邮件
smtp_obj.sendmail("zengdq@nancal.com", ["zengdq@nancal.com", "675445664@qq.com"], msg.as_string())

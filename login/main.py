from flask import Flask
from flask import request,render_template
from mysqldb.mysqls import Mysqlpython
sqlh = Mysqlpython("chatroom")
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        account = request.form['account']
        password = request.form['password']
        emailid = request.form['emailid']

        sql = "select * from user where name= %s"
        result = sqlh.all(sql,[name])
        # print('********',result)

        sql = "select * from user where account= %s"
        result2 = sqlh.all(sql,[account])
        # print('********', result2)


        if result:
            # message = '该用户昵称已存在'
            return render_template('register.html',message = '该用户昵称已存在')


        elif result2:
            # error = '该用户帐号已存在'
            return render_template('register.html',error = '该用户帐号已存在')


        else:
            sql = "insert into user(name,account,password,emailid) value(%s,%s,%s,%s)"
            sqlh.zhixing(sql,[name,account,password,emailid])
            # message = '恭喜您，注册成功'
            return render_template('success.html')

    else:
        return render_template('register.html')


@app.route('/find',methods=['POST','GET'])
def find():
    if request.method == 'POST':
        account = request.form['account']
        emailid = request.form['emailid']

        act = "select * from user where account= %s"
        act2 = sqlh.all(act,[account])
        # print('******',act2)
        if len(act2)>0:
            act2 = sqlh.all(act, [account])[0][2]
            email = sqlh.all(act,[account])[0][5]

            if act2==account and email==emailid:
				
				# 邮箱服务器地址
                mailserver = "smtp.qq.com"  
                username_send = '88888888@qq.com'
                password = '自己邮箱的密码口令'
                username_recv = email

                pwd = sqlh.all(act, [account])[0][3]
                mail = MIMEText('您的密码为：%s' % pwd)

                mail['Subject'] = '系统邮件'
                mail['From'] = username_send
                mail['To'] = username_recv

                try:
                    # 连接邮箱服务器端口号是25
                    smtp = smtplib.SMTP(mailserver, port=25)
                    smtp.login(username_send, password)
                    smtp.sendmail(username_send, username_recv, mail.as_string())
                    print('send success')
                except:
                    print('send fail')
                finally:
                    smtp.quit()

                    message = '提交成功,请登录邮箱查看密码'
                    return render_template('success2.html',message2 = message)

            else:
                # error = '您输入的帐号或邮箱有误'
                return render_template('find.html',error = '您输入的帐号或邮箱有误')

        else:
            # error = '您输入的帐号或邮箱有误'
            return render_template('find.html',error = '您输入的帐号或邮箱有误')

    else:
        return render_template('find.html')


@app.errorhandler(404)
def failmessage(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1')

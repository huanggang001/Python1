import os
from datetime import date
import yagmail

# Email参数
email_account = '340214909@qq.com'
email_pwd = 'atwesnlgaedybigf'
email_host = 'smtp.qq.com'
email_port ='465'
email_to_accunt = 'humanmike@163.com'
email_to_accunt_list = ['hello18820855535@163.com','340214914@qq.com']
time2 = date.today()
# -------------------------------------------------------------------------------
# 函数/过程名称：GetNewReport
# 函数/过程的目的：获取最新报告文件
# 假设：无
# 影响：无
# 输入：无
# 返回值：文件全路径
# 创建者：老道
# 创建时间：2019/05/25
# 修改者：谁敢
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------
# 报告路径
reportPath = "D:/Python-Pycharm/set4/reports"
def get_new_report():
    l = os.listdir(reportPath)
    l.sort(key = lambda fn :os.path.getmtime(reportPath + '\\' + fn))
    f = os.path.join(reportPath,l[-1])
    return f
# -------------------------------------------------------------------------------
# 类名称：SendEmail
# 类的目的：发送文本邮件或发送带附件邮件
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：老道
# 创建时间：2019/05/25
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------
def sendEmail(s_user,s_pwd,host,port,to_user,body,subject,report_flie):
    '''
    :param s_user:    发送者账号
    :param s_pwd:     发送者授权码
    :param host:       邮箱范围器
    :param port:       非SSL端口25，SSL端口465 或 994
    :param to_user:    接收者邮箱
    :param body:       邮箱内容
    :param subject:    邮箱主题
    :param report_flie:  测试报告
    :return:
    '''
    send = yagmail.SMTP(user=s_user,password =s_pwd,host=host,port=port)

    if type(to_user) is list:
        # 邮件群发，如果报错或失败提示（554），尝试把双方都加为发送联系人，cc为抄送自己
        send.send(to =to_user,cc=s_user,subject=subject,contents=[body,report_flie])
        flag = True

    elif type(to_user) is str:
        # 发送给单个用户
        send.send(to = to_user ,subject =subject ,contents = [body , report_flie])
        flag = True

    else:
        flag = False

    return flag

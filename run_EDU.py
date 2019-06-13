import time , os  , unittest
from HTMLTestReportCN import HTMLTestRunner
from tool.send_email import (sendEmail,
    get_new_report,
    email_account,
    email_host,
    email_port,
    email_pwd,
    email_to_accunt,
    email_to_accunt_list,
    time2)


def run_edu():
    edu_dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "./scripts"))
    edu_testfile = unittest.defaultTestLoader.discover(edu_dirpath,pattern='*_tc.py')
    time1 = time.strftime('%y%m%d %H%M%S')
    reportflie = ('./reports/'+'EDU_'+time1+'.html')
    tmpdir = os.path.abspath(os.path.join(os.path.dirname(__file__), reportflie))
    with open(tmpdir,'w',encoding='utf-8') as edu:
        runnet = HTMLTestRunner(stream=edu,
                                title= 'EDU测试报告',
                                description='EDU系统UI界面自动化测试，更新到五月版本',
                                tester='老道',
                                verbosity= 2)
        runnet.run(edu_testfile)
    report = get_new_report()
    sendEmail(s_user=email_account,s_pwd=email_pwd,port=email_port,host=email_host,report_flie=report,
              to_user=email_to_accunt_list,subject='EDU自动化测试报告',body='各位领导，今天{}的报告已生成，请查阅'.format(time2))
    print('邮件已发送')

if __name__=="__main__":
    run_edu()
    # run_test()
import xlrd,itchat,datetime
from itchat.content import *
workbook=xlrd.open_workbook('供电所用户信息统计表（2019）.xlsx')
sheet=workbook.sheet_by_index(0)
rows=sheet.get_rows()
roadList=sheet.col_values(3)
def main():
    road=input('请输入路名：')
    if road=='q':
        return 1
    while roadConfirm(road):
        road=input('未查到该线路，请重新输入:')
    roadData=get(road)
    #print(roadData)
    msg=decorate(roadData)
    if input('是否确认发送（y/n）：')=='y':
        wechat(msg,'filehelper')
        print('发送成功')
    else:
        print('取消发送')
def get(road):
    n = roadList.index(road)
    roadData = sheet.row_values(n)
    roadData[16]
    return roadData
def decorate(roadData):
    #text='影响高户%d户，影响低户%d户，影响居民%d户'%(int(roadData[9]),int(roadData[10]),int(roadData[11]))
    stime=datetime.datetime.now()
    etime=datetime.datetime.now()+datetime.timedelta(hours=6)
    user=roadData[16]+roadData[17]+roadData[18]+roadData[19]+roadData[20]
    stime,road,etime=stime.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}").format(y='年', m='月', d='日',h="时",m1="分",),roadData[3],etime.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}").format(y='年', m='月', d='日',h="时",m1="分",)
    text='北中心各位同事：1.停电地点：北京市大兴区%s；2.停电时间：%s；3.停电原因：%s故障；4.预计恢复时间：%s。如有以上地点客户反映停电报修或投诉，请客服人员代为解释，谢谢！'%(user,stime,road,etime)
    print(text)
    return text
def wechat(text,contact):
    itchat.auto_login(hotReload=True)
    #itchat.auto_login()
    itchat.send(text, toUserName='filehelper')
def roadConfirm(road):
    #road=input('请输入路名：>>>')
    if road in roadList:
       return 0
    else:
       return 1
while True:
    if main():
        break

'''
@itchat.msg_register(TEXT)
def get_msg(msg):
    print(msg['Text'])
    print(msg)
    if msg['Text']=='故障':
        print('输入故障路名')
#itchat.auto_login(enableCmdQR=True)
itchat.auto_login(hotReload=True)
#itchat.send('1',toUserName='filehelper')
#itchat.run()
'''
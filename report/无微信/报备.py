import xlrd,itchat,datetime,pyperclip
from itchat.content import *
workbook=xlrd.open_workbook('大兴10kV线路停电报备信息汇总.xlsx')
sheet=workbook.sheet_by_index(0)
rows=sheet.get_rows()
roadList=sheet.col_values(2)
def main():
    road=input('请输入路名：液压路'
               '')
    if road=='q':
        return 1
    while roadConfirm(road):
        road=input('未查到该线路，请重新输入:')
        if road=='q':
            return 1
    roadData=get(road)
    #print(roadData)
    msg=decorate(roadData)
    pyperclip.copy(msg)
    print("已复制粘贴板，请发送")
def get(road):
    n = roadList.index(road)
    roadData = sheet.row_values(n)
    return roadData
def decorate(roadData):
    stime=datetime.datetime.now()
    etime=datetime.datetime.now()+datetime.timedelta(hours=6)
    user=roadData[3]
    stime,road,etime=stime.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}").format(y='年', m='月', d='日',h="时",m1="分",),roadData[3],etime.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}").format(y='年', m='月', d='日',h="时",m1="分",)
    #text='北中心各位同事：1.停电地点：北京市大兴区%s；2.停电时间：%s；3.停电原因：%s故障；4.预计恢复时间：%s。如有以上地点客户反映停电报修或投诉，请客服人员代为解释，谢谢！'%(user,stime,road,etime)
    text=user.replace('time',stime,1)
    print('报备信息'.center(40,'-'))
    print(text)
    print('-'.center(44,'-'))
    return text
def wechat(text,contact):
    itchat.auto_login(hotReload=True)
    #itchat.auto_login()
    #itchat.send(text, toUserName='filehelper')
    SentChatRoomsMsg(contact,text)
def roadConfirm(road):
    #road=input('请输入路名：>>>')
    if road in roadList:
       return 0
    else:
       return 1
def SentChatRoomsMsg(name, context):
    #itchat.auto_login(hotReload=True)
    #if not (itchat.auto_login()):
    #    print("登录失败")
    #    return 0
    itchat.auto_login()
    itchat.get_chatrooms(update=True)
    iRoom = itchat.search_chatrooms(name)
    #print(iRoom)
    userName=''
    for room in iRoom:
        if room['NickName'] == name:
            userName = room['UserName']
            break
    if not userName:
        print('未找到该联系人')
        return 0
    itchat.send_msg(context, userName)
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

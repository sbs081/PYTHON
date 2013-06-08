# -*- coding: cp936 -*-
import urllib, urllib2, cookielib
import time
import json


############################################################
#Create by Jack 2009.5.25 
#xiaonei:http://http://xiaonei.com/profile.do?id=228857313
#csdn:http://hi.csdn.net/blessyou312
#baidu:http://hi.baidu.com/blessyou312/blog
#
#现在荣光医院还没有助手，最近比较忙，没时间来完善代码
#希望我的代码能够起到抛砖引玉的作用
#大家可以写出功能更全的助手软件
#
#如果要使用，请修改Login的参数和mainuid spyid1 spyid2
############################################################

##################################################
#全局变量
cookiejar = cookielib.CookieJar()
hpcookiejar=cookielib.CookieJar()
friendscookiejar=cookielib.CookieJar()#好友操作时要用这个

sessionkey=''
mainuid='自己的ID'#自己的ID
spyid1='xxxx'#派监视员1的ID
spyid2='xxxx'#派监视员2的ID

opurl='http://xn.rongame.com/ac.php?t='

callbacktime=60*60  #招回自己监察员时间（秒），应在30以上，为了保证能够成功建议设置在35分钟以上

##################################################
#登录校内方法
def login(email,pwd):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    params = {'email':email, 'password':pwd}
    data = urllib.urlencode(params)
    fobj = opener.open('http://login.xiaonei.com/Login.do', data)

#获得指定URL的内容
def GetHtml(visturl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    fobj=opener.open(visturl)
    data=fobj.read()
    return data

#登录医院
def loginhp():
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(hpcookiejar))
    #http://xn.rongame.com/xn_index.php?origin=103&xn_sig_in_iframe=1&xn_sig_method=get&xn_sig_time=1242962110548&xn_sig_added=1&xn_sig_user=228857313
    #&xn_sig_session_key=2.b02c67c5388d1727d1696046873942d2.3600.1242968400-228857313
    #&xn_sig_expires=0&xn_sig_api_key=b3563e6eba0349b898ed0810cc3a9de4&xn_sig_app_id=29507
    hpurl='http://xn.rongame.com/xn_index.php?origin=103&xn_sig_in_iframe=1&xn_sig_method=get&xn_sig_time='+GetTime()+'&xn_sig_added=1&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&xn_sig_expires=0&xn_sig_api_key=b3563e6eba0349b898ed0810cc3a9de4&xn_sig_app_id=29507'
    fobj = opener.open(hpurl)
    res=fobj.read()
    return res

#得到医院数据
def hpGetHtml(visiturl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(hpcookiejar))
    fobj=opener.open(visiturl)
    data=fobj.read()
    return data

#得到好友信息
def GetFriends():
    frurl=opurl+GetTime()+'&ac=friends&pid=2&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=9'
    content=hpGetHtml(frurl)
    return content

#得到sessionkey
def GetSessionkey():
    sessionkeycontent=GetHtml('http://apps.xiaonei.com/ronhospital/?origin=103')
    begin=sessionkeycontent.index("xn_sig_session_key=")
    if begin==-1:
        return -1
    end=sessionkeycontent.index("&",begin,begin+100)
    if end>begin:
        global sessionkey
        sessionkey=sessionkeycontent[begin+19:end]
    return 0

#生成操作的URL
def InitUrl(act):
    mainurl=opurl+GetTime()+'&ac='+act+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=9'
    return mainurl

#生成时间
def GetTime():
    s=time.time()
    ss=str(s*100)[0:12]+'0'
    return ss


############################################################################
#检查自己的医院有没有人在监视,返回ID和名字
def Checkhp():
    opstr=InitUrl('userdata')
    content=hpGetHtml(opstr)
    begin=content.index('v={')
    newc=content[begin+2:]
    locations=json.loads(newc)
    fuid1=locations["friendadminid1"]
    funame1=locations['friendadminname1']
    fuid2=locations["friendadminid2"]
    funame2=locations['friendadminname2']
    return fuid1+':'+funame1+':'+fuid2+':'+funame2

#查看自己的监察员情况
def CheckMyhp():
    opstr=InitUrl('prexy')
    content=hpGetHtml(opstr)
    begin=content.index('v={')
    newc=content[begin+2:]
    locations=json.loads(newc)

    fuid1=locations['ownadminid1']
    funame1=locations['ownadminname1']
    futime1=locations['ownadminpasstime1']
    fumoney1=locations['ownadmingivemoney1']

    fuid2=locations['ownadminid2']
    funame2=locations['ownadminname2']
    futime2=locations['ownadminpasstime2']
    fumoney2=locations['ownadmingivemoney2']

    return fuid1+':'+funame1+':'+futime1+':'+fumoney1+':'+fuid2+':'+funame2+':'+futime2+':'+fumoney2

#派自己的监察员
def SendMySpy(fuid):
    purl=opurl+GetTime()+'&ac=action&key=k2&fuid='+fuid+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=2'
    strres=hpGetHtml(purl)
    return CheckRes(strres)
#叫回自己的监察员
def CallBackSpy(pid,fuid):
    purl=opurl+GetTime()+'&ac=action&key=a3&pid='+pid+'&fuid='+fuid+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=2'
    strres=hpGetHtml(purl)
    return CheckRes(strres)

#驱逐好友的监察员
def DriveSpy(fuid):
    purl=opurl+GetTime()+'&ac=action&key=a1&fuid='+fuid+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=2'
    strres=hpGetHtml(purl)
    return CheckRes(strres)
#检查返回的语句
def CheckRes(content):
    begin=content.index('v={')
    newc=content[begin+2:]
    locations=json.loads(newc)
    state=locations['stat']
    return state



def mainfun():
    print '尝试登录校内网'
    login('email','password');
    print '登录成功，登录查找Sessionkey'
    loghpres=GetSessionkey()
    print '登录医院'
    loginhp()
    if loghpres==-1:
        print '登录医院失败'
    
    print '登录医院成功，检查自己的侦探状态'


    #检查自己的医院有没人监视
    myhpdata=Checkhp()
    #如果有，尝试驱逐
    spylist=myhpdata.split(':')
    if spylist[0]!='0':
        print DriveSpy(str(spylist[0]))
    if spylist[2]!='0':
        print DriveSpy(str(spylist[2]))

    #检查自己的监视员，如果闲着就放到指定的ID上
    myspydata=CheckMyhp()
    myspylist=myspydata.split(':')
    if myspylist[0]=='0':
        print '1号监察员空闲，尝试派到好友处'
        print SendMySpy(spyid1)
    elif int(myspylist[2])>=callbacktime:
        print u'1号监察员在['+myspylist[1]+u']处，赚得金钱：'+myspylist[3]+u' 超过指定时间，尝试招回'
        print CallBackSpy('1',myspylist[0])
        print SendMySpy(spyid1)
    else:
        print u'1号监察员在['+myspylist[1]+u']处，赚得金钱：'+myspylist[3]+u' 不到指定时间，不招回'
    if myspylist[4]=='0':
        print '2号监察员空闲，尝试派到好友处'
        print SendMySpy(spyid2)
    elif int(myspylist[6])>=callbacktime:
        print u'2号监察员在['+myspylist[5]+u']处，赚得金钱：'+myspylist[7]+u' 超过指定时间，尝试招回'
        print CallBackSpy('2',myspylist[4])
        print SendMySpy(spyid2)
    else:
        print u'2号监察员在['+myspylist[5]+u']处，赚得金钱：'+myspylist[7]+u' 不到指定时间，不招回'
    print '一次执行完毕！'


#********************************************************
#以下为调用过程
#********************************************************
mainfun()


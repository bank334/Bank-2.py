# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ✞[B̲̲̅̅a̲̲̅̅n̲̲̅̅k̲̲̅ ̲̲̅ʙ̲̲̅̅ᴏ̲̲̅̅ᴛ̲̲̅̅ ̲̲̅̅&̲̲̅̅ ̲̲̅̅L̲̲̅̅i̲̲̅n̲̲̅̅e̲̲̲̅̅̅]✞


✞[Mid]
✞[Gid]
✞[Ginfo]
✞[Gn 〘Namagroup〙 ]
✞[Qr]
✞[Oqr]
✞[Invite ❰Mid❱ ]
✞[Cqr]
✞[แท็ค]
✞[Sayonara]
✞[Cancel all]
✞[Me]
✞[Time]
✞[Gift]
✞[Tag@]
✞[Group Bc]
✞[Creator]

"""

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

wait2 = {    
    'message':"Thanks for add me,[By.B̲̲̅̅a̲̲̅̅n̲̲̅̅k̲̲̅ ̲̲̅ʙ̲̲̅̅ᴏ̲̲̅̅ᴛ̲̲̅̅ ̲̲̅̅&̲̲̅̅ ̲̲̅̅L̲̲̅̅i̲̲̅n̲̲̅̅e̲̲̲̅̅̅]"    
    }

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()                        
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)                 
                          
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass  
                            
def NOTIFIED_ADD_CONTACT(op):
    try:        
        client.findAndAddContactsByMid(op.param1)
        sendMessage(op.param1,"Thanks for add me,[By.B̲̲̅̅a̲̲̅̅n̲̲̅̅k̲̲̅ ̲̲̅ʙ̲̲̅̅ᴏ̲̲̅̅ᴛ̲̲̅̅ ̲̲̅̅&̲̲̅̅ ̲̲̅̅L̲̲̅̅i̲̲̅n̲̲̅̅e̲̲̲̅̅̅]")
        if (wait2["message"] ):
                    pass
        else:
            sendMessage(op.param1,"Thanks for add me,[By.B̲̲̅̅a̲̲̅̅n̲̲̅̅k̲̲̅ ̲̲̅ʙ̲̲̅̅ᴏ̲̲̅̅ᴛ̲̲̅̅ ̲̲̅̅&̲̲̅̅ ̲̲̅̅L̲̲̅̅i̲̲̅n̲̲̅̅e̲̲̲̅̅̅]")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    try:
        sendMessage(op.param1, "Welcome สวัสดีครับ\n[ยินดีต้อนรับคุณ] " + client.getContact(op.param2).displayName)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

tracer.addOpInterrupt(17,NOTIFIED_ACCEPT_GROUP_INVITATION)

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        sendMessage(op.param1, " ถูกลบออกจากกลุ่ม😁\n" + client.getContact(op.param3).displayName)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)

def NOTIFIED_LEAVE_GROUP(op):
    try:
        sendMessage(op.param1, " ออกอีกแล้ว😁\n " + client.getContact(op.param2).displayName)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return

tracer.addOpInterrupt(15,NOTIFIED_LEAVE_GROUP)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25, RECEIVE_MESSAGE)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 0:
            if msg.contentType == 0:
                if msg.text == "mid":
                    sendMessage(msg.to, msg.to)
                if msg.text == "me":
                    sendMessage(msg.to, text=None, contentMetadata={'mid': msg.from_}, contentType=13)
                if msg.text == "gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
                else:
                    pass
            else:
                pass
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "Mid":
                    sendMessage(msg.to, msg.from_)
                if msg.text == "Gid":
                    sendMessage(msg.to, msg.to)
                if msg.text == "#Ginfo":
                    group = client.getGroup(msg.to)
                    md = "[Group Name]\n" + group.name + "\n\n[gid]\n" + group.id + "\n\n[Group Picture]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nInvitationURL: Permitted\n"
                    else: md += "\n\nInvitationURL: Refusing\n"
                    if group.invitee is None: md += "\nMembers: " + str(len(group.members)) + "人\n\nInviting: 0People"
                    else: md += "\nMembers: " + str(len(group.members)) + "People\nInvited: " + str(len(group.invitee)) + "People"
                    sendMessage(msg.to,md)    
                if "Gn " in msg.text:
                    if msg.toType == 2:
                        X = client.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        client.updateGroup(X)                
                if msg.text == "Qr":
                    sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to))
                if msg.text == "Oqr":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == False:
                        sendMessage(msg.to, "Qr Sudah Terbuka")
                    else:
                        group.preventJoinByTicket = False
                        client.updateGroup(group)
                        sendMessage(msg.to, "Qr Terbuka")
                if msg.text == "Cqr":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == True:
                        sendMessage(msg.to, "Qr Sudah Tertutup")
                    else:
                        group.preventJoinByTicket = True
                        client.updateGroup(group)
                        sendMessage(msg.to, "Qr Tertutup")
		if msg.text in ["แท็ค"]:
    			group = client.getGroup(msg.to)
    			nama = [contact.mid for contact in group.members]
    			cb = ""
    			cb2 = ""
    			strt = int(0)
    			akh = int(0)
    			for md in nama:
        			akh = akh + int(5)
        			cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
        			strt = strt + int(6)
        			akh = akh + 1
        			cb2 += "@nrik\n"
    			cb = (cb[:int(len(cb)-1)])
    			msg.contentType = 0
    			msg.text = cb2
    			msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
    			try:
        			client.sendMessage(msg)
    			except Exception as error:
        			print error
                if "kick:" in msg.text:
                    key = msg.text[5:]
                    client.kickoutFromGroup(msg.to, [key])
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"sorry")

                if msg.text == "#Ratakan":
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = client.getGroup(msg.to)
                    sendMessage(msg.to,"Fuck You All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"error")
                    else:
                        for target in targets:
                            try:
                                klist=[client]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendMessage(msg.to,"error")                                       	
                if "#Sp" in msg.text:
                    start = time.time()
                    sendMessage(msg.to, "Progress...")
                    elapsed_time = time.time() - start
                    sendMessage(msg.to, "%sseconds" % (elapsed_time))
                if msg.text in ["Sayonara"]:                
                    if msg.toType == 2:
                        ginfo = client.getGroup(msg.to)
                        try:
                            client.leaveGroup(msg.to)
                        except:
                            pass
         #-------------Fungsi BC-------------------#
                    
                if "Group bc " in msg.text:                
                 bctxt = msg.text.replace("Group bc ", "")
                 n = client.getGroupIdsJoined()
                 for manusia in n:
                      sendMessage(manusia, (bctxt))

                if "Contact bc " in msg.text:               
                 bctxt = msg.text.replace("Contact bc ", "")
                 t = client.getAllContactIds()
                 for manusia in t:
                      sendMessage(manusia, (bctxt))                                         
                    
         #-------------Fungsi BC Finish-------------------#
#-----------------------------------------------------------            
                elif msg.text.lower() == 'ใครแอบ':
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
                elif msg.text.lower() == 'ออกมา':
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik [Check] dulu dudul Baru bilang [Recheck]")
#-----------------------------------------------------------
         #-------------Fungsi List group Start---------------------#                      

                if msg.text in ["Gclist","List gc","List groupGc list"]:              
                 gid = client.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                     h += "[✞]%s\n" % (client.getGroup(i).name   + " : " + str (len (client.getGroup(i).members)))
                 sendMessage(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))
         #-------------Fungsi List Group Done---------------------#
                if msg.text in ["Creator"]:              
                 msg.contentType = 13
                 msg.contentMetadata = {'mid': 'u00f827ce6641038d7c9b6704a9777dfa'}
                 sendMessage(msg)
                 sendMessage(msg.to,"[B̲̲̅̅a̲̲̅̅n̲̲̅̅k̲̲̅ ̲̲̅ʙ̲̲̅̅ᴏ̲̲̅̅ᴛ̲̲̅̅ ̲̲̅̅&̲̲̅̅ ̲̲̅̅L̲̲̅̅i̲̲̅n̲̲̅̅e̲̲̲̅̅̅]")                 

                if msg.text in ["#คำสั่ง"]:              
                    sendMessage(msg.to,helpMessage)
                else:
                    sendMessage(msg.to,helpt)                        
                if "Info" in msg.text:
                    nk0 = msg.text.replace("Info ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = client.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"Tidak Ada Akun")
                        pass
                    else:
                        for target in targets:
                            try:
                                print (msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu)) 
                            except:
                                sendMessage(msg.to,"Semoga Diterima disisinya")        
                if "Bunuh" in msg.text:
                    nk0 = msg.text.replace("Bunuh ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = client.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"Tidak Ada Akun")
                        pass
                    else:
                        for target in targets:
                            try:
                                klist=[client]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendMessage(msg.to,"Semoga Diterima disisinya")
                                sendMessage(msg.to,"Amin")                    
                if msg.text == "#ยกเลิก":
                    group = client.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "Tidak Ada Yang Bisa Dicancel")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + " Beres Bosq")
                if "#Invite " in msg.text:
                    midd = msg.text.replace("#Invite ","")
                    client.findAndAddContactsByMid(midd)
                    client.inviteIntoGroup(msg.to,[midd])
                    sendMessage(msg.to, ""+contact.displayName+"Saya Mengundangmu")
                if "Bc " in msg.text:                
				bctxt = msg.text.replace("Bc ","")
				client.sendMessage(msg.to,(bctxt))    
                if msg.text == "#Me":
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': msg.from_}
                    client.sendMessage(M)
                if "show:" in msg.text:
                    key = msg.text[-33:]
                    sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"'s contact")
                if msg.text == "Time":
                    sendMessage(msg.to, "Waktu Sekarang " + datetime.datetime.today().strftime('Tahun %Y Bulan %m Tanggal %d Jam %H:%M:%S'))
                if msg.text == "#Gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata= {'PRDID': '749ecd23-e038-4cd5-acac-23d46f4277c8','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)
                if msg.text == "#Set":
                    sendMessage(msg.to, "Setpoint")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.datetime.today().strftime('Tahun %Y Bulan %m Tanggal %d Jam %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    print wait
                if msg.text == "Cek":
                    if msg.to in wait['readPoint']:
                        if wait["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        sendMessage(msg.to, "Tercyduck %s\n\nRead Tapi Ga Chatt\n%sSepoint Pada:\n[%s]"  % (wait['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        sendMessage(msg.to, "Setpoint Dulu Coeg")
                else:
                    pass
        else:
            pass

    except Exception as e:
        print e
        print ("\n\nSEND_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    tracer.execute()

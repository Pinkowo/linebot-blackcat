from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage,  PostbackEvent
from module import func
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

levelNum = [0,0] #提示用[0]，關卡選單用[1]
 
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == "查看成績":
                        func.sendErrorNum(event)
                    elif mtext == "小黑再見～":
                        func.clearErrorNum(event)                             
                    elif mtext == "貓貓靈光一閃":
                        if levelNum[0] == 1:
                            func.sendHint1(event) #給予第一關提示
                        elif levelNum[0] == 2:
                            func.sendHint2(event) #給予第二關提示
                        elif levelNum[0] == 3:
                            func.sendHint3(event) #給予第三關提示
                        elif levelNum[0] == 4:
                            func.sendHint4(event) #給予第四關提示
                        elif levelNum[0] == 5:
                            func.sendHint5(event) #給予第五關提示
                        elif levelNum[0] == 6:
                            func.sendHint6(event) #給予第六關提示
                        else:
                            func.sendLevel0(event) #回覆開始玩                   
                    elif mtext == "開啟關卡選單":
                        if levelNum[1] == 1:
                            func.sendLevel1(event) #關卡轉盤1
                        elif levelNum[1] == 2:
                            func.sendLevel2(event) #關卡轉盤1~2
                        elif levelNum[1] == 3:
                            func.sendLevel3(event) #關卡轉盤1~3
                        elif levelNum[1] == 4:
                            func.sendLevel4(event) #關卡轉盤1~4
                        elif levelNum[1] == 5:
                            func.sendLevel5(event) #關卡轉盤1~5
                        elif levelNum[1] == 6:
                            func.sendLevel5(event) #關卡轉盤1~5  
                        else:
                            func.sendLevel0(event) #回覆開始玩  
                    elif mtext == "第一關":
                        levelNum[0] = 1
                        levelNum[1] = 1
                        func.sendPuzzle1(event) #測試用關卡轉盤1
                    elif mtext == "第二關":
                        levelNum[0] = 2
                        levelNum[1] = 2
                        func.sendPuzzle2(event) #測試用關卡轉盤2
                    elif mtext == "第三關":
                        levelNum[0] = 3
                        levelNum[1] = 3
                        func.sendPuzzle3(event) #測試用關卡轉盤3
                    elif mtext == "第四關":
                        levelNum[0] = 4
                        levelNum[1] = 4
                        func.sendPuzzle4(event) #測試用關卡轉盤4
                    elif mtext == "第五關":
                        levelNum[0] = 5
                        levelNum[1] = 5
                        func.sendPuzzle5(event) #測試用關卡轉盤5   
                    elif mtext == "第六關":
                        levelNum[0] = 6
                        levelNum[1] = 6
                        func.sendPuzzle6(event) #測試用關卡轉盤6        
                    elif mtext == "前往第一關" and levelNum[1] >= 1:
                        levelNum[0] = 1
                        func.sendPuzzle1(event) #關卡轉盤1
                    elif mtext == "前往第二關" and levelNum[2] >= 2:
                        levelNum[0] = 2
                        func.sendPuzzle2(event) #關卡轉盤1~2
                    elif mtext == "前往第三關" and levelNum[3] >= 3:
                        levelNum[0] = 3
                        func.sendPuzzle3(event) #關卡轉盤1~3
                    elif mtext == "前往第四關" and levelNum[4] >= 4:
                        levelNum[0] = 4
                        func.sendPuzzle4(event) #關卡轉盤1~4
                    elif mtext == "前往第五關" and levelNum[5] >= 5:
                        levelNum[0] = 5
                        func.sendPuzzle5(event) #關卡轉盤1~5
                    else:
                        if mtext == "出發":
                            levelNum[0] = 1
                            levelNum[1] = 1
                            func.sendPuzzle1(event) #前往第一題
                        elif mtext =="6月16日": #第一題答案
                            levelNum[0] = 2
                            levelNum[1] = 2
                            func.sendPuzzle2(event) #前往第二題
                        elif mtext =="密碼鎖的顏色順序是":
                            func.sendPuzzle2_2(event) #前往第二題之2
                        elif mtext =="紅綠藍黃": #第二題答案
                            levelNum[0] = 3
                            levelNum[1] = 3
                            func.sendPuzzle3(event) #前往第三題
                        elif mtext =="藍紅綠黃":
                            func.sendP2_fault(event) #第二題錯誤
                        elif mtext =="黃綠紅藍":
                            func.sendP2_fault(event) #第二題錯誤
                        elif mtext =="綠藍黃紅":
                            func.sendP2_fault(event) #第二題錯誤
                        elif mtext =="再試試看":
                            func.sendPuzzle2_2(event) #第二題錯誤2
                        elif mtext =="TUNA": #第三題答案
                            levelNum[0] = 4
                            levelNum[1] = 4
                            func.sendPuzzle4(event) #前往第四題
                        elif mtext =="Tuna":
                            func.sendP3_fault(event) #第三題要大寫
                        elif mtext =="tuna":
                            func.sendP3_fault(event) #第三題要大寫
                        elif (mtext != "TUNA" or mtext != "Tuna" or mtext != "tuna") and levelNum[0] == 3:
                            func.sendP3_faultNumPlus(event) #第三題答錯且不等於上述字
                        elif mtext == "黃":
                            func.sendP4_yellow(event) #第四題黃
                        elif mtext == "藍":
                            func.sendP4_blue(event)  #第四題藍
                        elif mtext == "紫":
                            func.sendP4_purple(event)  #第四題紫
                        elif mtext == "紅":
                            func.sendP4_red(event)  #第四題紅
                        elif mtext == "藍黃紫紅":  #第四題答案
                            levelNum[0] = 5
                            levelNum[1] = 5
                            func.sendPuzzle5(event)  #前往第五題
                        elif mtext == "再重按吧":
                            func.sendP4_reset(event)  #第四題錯誤
                        elif (mtext != "藍黃紫紅") and levelNum[0] == 4:
                            func.sendP4_fault(event)
                        elif mtext == "我知道鑰匙在哪了":
                            func.sendPuzzle5_2(event)  #前往第五題之2
                        elif mtext == "三角形洞": #第五題答案
                            func.sendBranch(event)  #前往分支
                        elif mtext == "圓形洞":
                            func.sendP5_fault(event)  #第五題錯誤
                        elif mtext == "星形洞":
                            func.sendP5_fault(event)  #第五題錯誤
                        elif mtext == "方形洞":
                            func.sendP5_fault(event)  #第五題錯誤
                        elif mtext == "再找找":
                            func.sendPuzzle5_2(event)  #前往第五題之2
                        elif mtext == "走吧GoGo":
                            func.goGate(event)  #前往結局一:大門
                        elif mtext == "先等一下喔":
                            levelNum[0] = 6
                            levelNum[1] = 6
                            func.sendPuzzle6(event)  #前往第六題
                        elif mtext == "讓我看看":
                            func.sendHome(event)  #前往轉盤
                        elif mtext == "櫃子旁有一道門":
                            func.sendPuzzle6_1(event)  #傳送門
                        elif mtext == "地上有一張紙條":
                            func.sendPuzzle6_2(event)  #傳送紙條
                        elif mtext == "查看其他地方":
                            func.sendHome(event)  #前往轉盤
                        elif mtext == "BALCONY":
                            func.goBalcony(event)  #前往結局二:陽台
                        elif mtext =="balcony":
                            func.sendP6_fault(event) #第六題要大寫
                        elif mtext =="Balcony":
                            func.sendP6_fault(event) #第六題要大寫
                        elif (mtext != "BALCONY" or mtext != "balcony" or mtext != "Balcony") and levelNum[0] == 6:
                            func.sendP6_faultNumPlus(event) #第三題答錯且不等於上述字
                        elif mtext == "我想看其他結局":
                            func.sendBranch(event)  #前往分支
                        else:
                            func.sendQ(event)           
                    

            if isinstance(event, PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data))
                if backdata.get('action') == 'go':
                    func.sendData_date(event, backdata) 

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

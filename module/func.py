from django.conf import settings
from linebot import LineBotApi
from linebot.models import (
    Sender,TextSendMessage,ImageSendMessage,StickerSendMessage,
    LocationSendMessage,QuickReply,QuickReplyButton,MessageAction, 
    TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, 
    URITemplateAction, PostbackTemplateAction,DatetimePickerTemplateAction,
    ImageCarouselTemplate,ImageCarouselColumn,ImagemapSendMessage,
    MessageImagemapAction, BaseSize, URIImagemapAction,  ImagemapArea,
    CarouselTemplate,CarouselColumn,ConfirmTemplate
)
import datetime

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

errorNum = []
triggerSix = False
P4_color = []
hintNum = []

def sendMenu(event): #同樣錯誤超過3次，提示可以開啟選單
    try:
        message = TextSendMessage(text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～")
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendErrorNum(event): #傳送最後結算錯誤次數
    try:
        one = errorNum.count("一")
        two = errorNum.count("二")
        three = errorNum.count("三")
        four = errorNum.count("四")
        five = errorNum.count("五")
        six = errorNum.count("六")
        errSum = one+two+three+four+five+six
        if errSum>5:
            replyText3 = "請加油QQ"
            packageID = 8525
            stickerID = 16581313
        else:
            replyText3 = "很棒喔！！"
            packageID = 8525
            stickerID = 16581302

        if triggerSix == True:
            replyText4 = "\n第六關答錯{}次".format(six)
        else:
            replyText4 = ""
            
        replyText = "第一關答錯{}次\n第二關答錯{}次\n第三關答錯{}次\n第四關答錯{}次\n第五關答錯{}次{}".format(one,two,three,four,five,replyText4)
        replyText2 = "總共答錯{}次，{}".format(errSum,replyText3)
        message = [
            TextSendMessage(text = "最後來看看總共錯了幾次喵！"),
            TextSendMessage(text = replyText),
            TextSendMessage(text = replyText2),
            StickerSendMessage(
                package_id = packageID,
                sticker_id = stickerID
            ),
            TextSendMessage(
                text='要嘗試其他結局嗎？',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="好啊",
                                text="我想看其他結局")),
                        QuickReplyButton(
                            action=MessageAction(label="不要",
                                text="小黑再見～"))
                    ]))]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def clearErrorNum(event): #清空錯誤次數
    try:
        errorNum.clear()
        hintNum.clear()
        message = TextSendMessage(text = "拜拜(=^･ω･^=)ฅ")
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendPuzzle1(event): #傳送第一題
    try:
        message = [
            TextSendMessage(text = "鏟屎的會在日曆上把特別的日子圈起來，其中一天要帶我去結紮，不知道是哪一天喵？"),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/UUyCgg1.jpg",
                preview_image_url = "https://i.imgur.com/UUyCgg1.jpg"
            ),
            TemplateSendMessage(
            alt_text = '日期',
            template = ButtonsTemplate(
                text = '鏟屎的二五要上課，假日不出門。然後獸醫院開門時間是早上9:00-11:30還有下午14:00-18:00。',
                actions = [
                    DatetimePickerTemplateAction(
                        label = "選取日期",
                        data = "action=go&mode=date",
                        mode = "date",
                        initial = "2022-06-01",
                        min = "2022-06-01",
                        max = "2022-06-30"
                    )
                ]
            )
        )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendData_date(event, backdata): #第一題回答
    try:
        if backdata.get('mode') == 'date':
            if(event.postback.params.get('date')=='2022-06-16'):
                message =TextSendMessage(
                        text='喵？你知道是哪一天了嗎？',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=MessageAction(label="我覺得是......",
                                        text="6月16日")
                    )]))
            else:
                errorNum.append("一")
                if errorNum.count("一")==3:
                    message = [
                        TextSendMessage(
                            text = '喵嗚？是這一天嗎？\n好像有哪裡不對喵，再想一下。'),
                        TextSendMessage(
                            text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～") 
                    ]
                else:
                    message = TextSendMessage(
                    text = '喵嗚？是這一天嗎？\n好像有哪裡不對喵，再想一下。')              
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text="錯誤喵啦"))


def sendPuzzle2(event): #傳送第二題
    try:       
        message = [
            TextSendMessage(
                text = "對對，好像就是6月16號！那要趕快收拾行李了喵！"
            ),
            TextSendMessage(
                text = "逃家怎麼可以沒有罐罐呢～\n不過放罐頭的房間有上鎖......"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/PjklAN5.jpg",
                preview_image_url = "https://i.imgur.com/PjklAN5.jpg"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/4kHadeF.jpg",
                preview_image_url = "https://i.imgur.com/4kHadeF.jpg"
            ),
            TextSendMessage(
                        text='咦？地上居然有個空罐頭喵。',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=MessageAction(label="我知道了",
                                        text="密碼鎖的顏色順序是")
            )]))
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendPuzzle2_2(event): #傳送第二題-2
    try:
        message = TemplateSendMessage(
                alt_text="圖片轉盤",
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/JMXQUgJ.png',
                            action=MessageAction(
                                label='我覺得是這個',
                                text='藍紅綠黃'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/FjphfzO.png',
                            action=MessageAction(
                                label='我才是正解',
                                text='黃綠紅藍'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/7TkZhPa.png',
                            action=MessageAction(
                                label='這個才對啦',
                                text='紅綠藍黃'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://i.imgur.com/tBeEHTp.png',
                            action=MessageAction(
                                label='是我啦哈哈',
                                text='綠藍黃紅'
                            )
                        )
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP2_fault(event): #傳送第二題錯誤訊息
    try:
        errorNum.append("二")
        if errorNum.count("二")==3:
            message = [
                        TextSendMessage(
                            text = '打不開......好像不對喵'),
                        TextSendMessage(
                            text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～",
                            quick_reply=QuickReply(
                                items=[
                                    QuickReplyButton(
                                        action=MessageAction(label="再試試看",
                                            text="再試試看")
                            )]))]
        else:
            message = TextSendMessage(
                text='打不開......好像不對喵',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="再試試看",
                                text="再試試看")
                )]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendPuzzle3(event): #傳送第三題
    try:
        message = [
            TextSendMessage(
                text = "終於進來了～\n哪尼？連放罐頭的櫃子都有鎖？！\n密碼長得好像火星文......"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/jGGok1S.jpg",
                preview_image_url = "https://i.imgur.com/jGGok1S.jpg"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/3XRTgZR.jpg",
                preview_image_url = "https://i.imgur.com/3XRTgZR.jpg"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/ti8xqCq.jpg",
                preview_image_url = "https://i.imgur.com/ti8xqCq.jpg"
            ),
            TextSendMessage(
                text = "如果你知道答案可以直接告訴我嗎？霸脫霸脫～"
            )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP3_fault(event): #傳送第三題錯誤訊息(要大寫)
    try:
        errorNum.append("三")
        if errorNum.count("三")==3:
            message = [
                        TextSendMessage(
                            text = "密碼鎖上的字好像全都是比較大的喵！"),
                        TextSendMessage(
                            text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～") 
                    ]
        else:
            message = TextSendMessage(
                    text = "密碼鎖上的字好像全都是比較大的喵！"
                )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP3_faultNumPlus(event): #增加3錯誤次數
    try:
        errorNum.append("三")
        if errorNum.count("三")==3:
            message = [
                        TextSendMessage(
                            text = "好像不是這個密碼喵。"),
                        TextSendMessage(
                            text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～") 
                    ]
        else:
            message = TextSendMessage(
                    text = "好像不是這個密碼喵。"
                )
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendPuzzle4(event): #傳送第四題
    try:
        P4_color.clear()
        image_url = 'https://i.imgur.com/YvdZEoP.jpg'
        imgwidth = 1040
        imgheight = 1040
        message = [
            TextSendMessage(
                text = "偷吃了一個罐頭，有點口渴惹，可是飲水機被鏟屎的關掉了，要怎麼打開喵？"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/0r6nLPj.jpg",
                preview_image_url = "https://i.imgur.com/0r6nLPj.jpg"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/WjfFQJP.jpg",
                preview_image_url = "https://i.imgur.com/WjfFQJP.jpg"
            ),
            TextSendMessage(
                text = "這些是飲水機的按鍵，我看鏟屎的每次都會按四個鍵，順序我忘了。"
            ),
            ImagemapSendMessage(
                base_url = image_url,
                alt_text="飲水機",
                base_size = BaseSize(height=imgheight,width=imgwidth),
                actions = [
                    MessageImagemapAction(
                        text = '黃',
                        area = ImagemapArea(
                            x=0,
                            y=0,
                            width=imgwidth*0.5,
                            height=imgheight*0.5
                        )
                    ),
                    MessageImagemapAction(
                        text = '藍',
                        area = ImagemapArea(
                            x=imgwidth*0.5,
                            y=0,
                            width=imgwidth*0.5,
                            height=imgwidth*0.5
                        )
                    ),
                    MessageImagemapAction(
                        text = '紫',
                        area = ImagemapArea(
                            x=0,
                            y=imgwidth*0.5,
                            width=imgwidth*0.5,
                            height=imgwidth*0.5
                        )
                    ),
                    MessageImagemapAction(
                        text = '紅',
                        area = ImagemapArea(
                            x=imgwidth*0.5,
                            y=imgwidth*0.5,
                            width=imgwidth*0.5,
                            height=imgwidth*0.5
                        )
                )])
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP4_yellow(event): #傳送第四題訊息:黃
    try:
        P4_color.append("黃")
        if len(P4_color) == 4:
            sendP4_check(event)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP4_blue(event): #傳送第四題訊息:藍
    try:
        P4_color.append("藍")
        if len(P4_color) == 4:
            sendP4_check(event)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP4_purple(event): #傳送第四題訊息:紫
    try:
        P4_color.append("紫")
        if len(P4_color) == 4:
            sendP4_check(event)
  
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP4_red(event): #傳送第四題訊息:紅
    try:
        P4_color.append("紅")
        if len(P4_color) == 4:
            sendP4_check(event)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP4_check(event):
    try:
        text_color = "開啟飲水機的按鈕順序是{}{}{}{}對喵？".format(P4_color[0],P4_color[1],P4_color[2],P4_color[3])
        reply_color = "{}{}{}{}".format(P4_color[0],P4_color[1],P4_color[2],P4_color[3])
        message = TemplateSendMessage(
            alt_text = '顏色順序',
            template = ConfirmTemplate(
                text = text_color,
                actions=[
                    MessageTemplateAction(
                        label="沒錯",
                        text=reply_color
                    ),
                    MessageAction(
                        label="不對",
                        text="再重按吧"
                    )
                ]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP4_reset(event): #傳送第四題重按訊息
    try:
        P4_color.clear()
        image_url = 'https://i.imgur.com/YvdZEoP.jpg'
        imgwidth = 1040
        imgheight = 1040
        message = ImagemapSendMessage(
                base_url = image_url,
                alt_text="飲水機",
                base_size = BaseSize(height=imgheight,width=imgwidth),
                actions = [
                    MessageImagemapAction(
                        text = '黃',
                        area = ImagemapArea(
                            x=0,
                            y=0,
                            width=imgwidth*0.5,
                            height=imgheight*0.5
                        )
                    ),
                    MessageImagemapAction(
                        text = '藍',
                        area = ImagemapArea(
                            x=imgwidth*0.5,
                            y=0,
                            width=imgwidth*0.5,
                            height=imgwidth*0.5
                        )
                    ),
                    MessageImagemapAction(
                        text = '紫',
                        area = ImagemapArea(
                            x=0,
                            y=imgwidth*0.5,
                            width=imgwidth*0.5,
                            height=imgwidth*0.5
                        )
                    ),
                    MessageImagemapAction(
                        text = '紅',
                        area = ImagemapArea(
                            x=imgwidth*0.5,
                            y=imgwidth*0.5,
                            width=imgwidth*0.5,
                            height=imgwidth*0.5
                        )
                )])
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP4_fault(event): #傳送第四題錯誤訊息
    try:
        errorNum.append("四")
        if errorNum.count("四")==3:
            message = [
                TextSendMessage(
                    text = '飲水機沒有反應喵。'),
                TextSendMessage(
                    text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="再重按吧",
                                    text="再重按吧")
                    )]))]
        else: 
            message = TextSendMessage(
                text='飲水機沒有反應喵。',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="再重按吧",
                                text="再重按吧")
                )]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendPuzzle5(event): #傳送第五題
    try:
        message = [
            TextSendMessage(
                text = "咕嚕咕嚕，水水好喝<3"
            ),
            TextSendMessage(
                text = "鏟屎的把貓跳台上我會跳到的地板都鋪上了綠色地墊，踩起來很舒服～\n我把出去的鑰匙偷偷藏在某個洞裡了喵，我想想路線喔......"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/XxkBsVD.jpg",
                preview_image_url = "https://i.imgur.com/XxkBsVD.jpg"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/K0XCtpW.jpg",
                preview_image_url = "https://i.imgur.com/K0XCtpW.jpg"
            ),
            TextSendMessage(
                text='從藏鑰匙的地方接著往下跳，爬樓梯下來，再往左跳，就又回到原來的地方喵！',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="我知道鑰匙在哪了",
                                text="我知道鑰匙在哪了")
            )]))
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendPuzzle5_2(event): #傳送第五題-2
    try:
        message = TextSendMessage(
            text='在貓跳台的哪個洞裡呢？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="圓形洞",
                            text="圓形洞")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="星形洞",
                            text="星形洞")
                    ),
                                        QuickReplyButton(
                        action=MessageAction(label="方形洞",
                            text="方形洞")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="三角形洞",
                            text="三角形洞")
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP5_fault(event): #傳送第五題錯誤訊息
    try:
        errorNum.append("五")
        if errorNum.count("五")==3:
            message = [
                TextSendMessage(
                    text = '咦？裡面沒東西喵？'),
                TextSendMessage(
                    text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="再找找",
                                    text="再找找")
                    )]))]
        else: 
            message = TextSendMessage(
                text='咦？裡面沒東西喵？',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="再找找",
                                text="再找找")
                )]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendBranch(event): #傳送分支
    try:
        message = [
            TextSendMessage(
                text = "費盡千辛萬苦終於拿到大門鑰匙了喵！"
            ),
            TextSendMessage(
                text='那麼要開門出去了嗎～？',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="走吧",
                                text="走吧GoGo")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="先等等",
                                text="先等一下喔")
                        )
                    ]))]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def goGate(event): #傳送結局一
    try:
        message = [
            TextSendMessage(
                text = "耶！門打開了，自由了喵～"
            ),
            TextSendMessage(
                text = "咦？小黑你在這啊～\n醫生說結紮可以改到明天，今晚要先禁食喔！",
                sender=Sender(
                    name="主人",
                    icon_url="https://i.imgur.com/OAa3G4a.jpg")
            ),
            TextSendMessage(
                text = "Noooooooooooooo!!!"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/f2yH4Jc.jpg",
                preview_image_url = "https://i.imgur.com/f2yH4Jc.jpg"
            ),
            TextSendMessage(
                text='恭喜破關喵！',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="查看成績",
                                text="查看成績")
                        )
                ]))]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def goBalcony(event): #傳送結局二
    try:
        triggerSix = True
        message = [
            TextSendMessage(
                text = "這扇門後面居然是通到陽台！？太好了，窗戶是開的！"
            ),
            TextSendMessage(
                text = "咦？小黑又亂跑去哪裡了？\n算了，把他抓去結紮之後應該會乖一點吧～",
                sender=Sender(
                    name="主人遙遠的聲音",
                    icon_url="https://i.imgur.com/OAa3G4a.jpg")
            ),
            TextSendMessage(
                text = "喵哈哈哈哈－－！\n鏟屎的想都別想，我才不要結紮！\n謝謝你的幫忙，我們再也不見，本小黑要去廣大的世界闖蕩了喵～～～"
            ),
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/5buVG3m.jpg",
                preview_image_url = "https://i.imgur.com/5buVG3m.jpg"
            ),
            TextSendMessage(
                text='恭喜破關喵！',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="查看成績",
                                text="查看成績")
                        )
                    ]))]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendPuzzle6(event): #傳送第六關
    try:
        message = TextSendMessage(
            text='感覺有哪裡不對勁，再找找看還有沒有其他出口吧喵！',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="環顧四周",
                            text="讓我看看")
            )]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendHome(event): #第六關家具轉盤
    try:
        message = TemplateSendMessage(
            alt_text="第六關家具轉盤",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/lIo2Pop.jpg',
                        text='櫃子',
                        actions=[
                            MessageTemplateAction(
                                label='查看櫃子旁邊',
                                text='櫃子旁有一道門'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/WdHDLeq.jpg',
                        text='書桌',
                        actions=[
                            MessageTemplateAction(
                                label='查看書桌附近',
                                text='只有一堆書，跟著月亮走......\n嗯，還是放回去好了。'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/s7lKDPP.jpg',
                        text='床',
                        actions=[
                            MessageTemplateAction(
                                label='查看床邊',
                                text='地上有一張紙條'
                            )
            ])]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendPuzzle6_1(event): #傳送第六題之門
    try:
        message = [
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/80Gh04l.jpg",
                preview_image_url = "https://i.imgur.com/80Gh04l.jpg"
            ),
            TextSendMessage(
                text='這裡居然藏著一道門！不知道是通往哪裡的喵。\n如果你知道答案的話能直接幫我輸入嗎？',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="查看其他地方",
                                text="查看其他地方")
            )]))
            
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendPuzzle6_2(event): #傳送第六題之紙條
    try:
        message = [
            ImageSendMessage(
                original_content_url = "https://i.imgur.com/KfcnfFw.jpg",
                preview_image_url = "https://i.imgur.com/KfcnfFw.jpgg"
            ),
            TextSendMessage(
                text='上面寫了好奇怪的火星文',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="查看其他地方",
                                text="查看其他地方")
            )]))
            
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP6_fault(event): #傳送第六題錯誤訊息(要大寫)
    try:
        errorNum.append("六")
        if errorNum.count("六")==3:
            message = [
                        TextSendMessage(
                            text = "好像是要大寫的火星文喵！"),
                        TextSendMessage(
                            text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～") 
                    ]
        else:
            message = TextSendMessage(
                text = "好像是要大寫的火星文喵！")
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendP6_faultNumPlus(event): #增加6錯誤次數
    try:
        errorNum.append("六")
        if errorNum.count("六")==3:
            message = [
                        TextSendMessage(
                            text = "好像不是這個密碼喵。"),
                        TextSendMessage(
                            text = "點左下角三條線切換成選單模式，開啟選單後，左邊的按鈕可以【獲得提示】～") 
                    ]
        else:
            message = TextSendMessage(
                    text = "好像不是這個密碼喵。"
                )
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendQ(event): #傳送窩聽不懂你在說什麼喵
    try:
        message = TextSendMessage(
                text = "窩聽不懂你在說什麼喵"
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendHint1(event): #傳送第一關提示
    try:
        hintNum.append("一")
        if hintNum.count("一")==1:
            message = TextSendMessage(
                text = "圈起來的日期中，其中一天鏟屎的要把我抓去獸醫院哼。"
            )
        elif hintNum.count("一")==2:
            message = TextSendMessage(
                text = "看來鏟屎的只有星期一、三、四會出門做事。"
            )
        else:
            message = TextSendMessage(
                text = "1號、16號、20號好像都符合，不過獸醫院的開門時間是啥時來著？"
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendHint2(event): #傳送第二關提示
    try:
        hintNum.append("二")
        if hintNum.count("二")==1:
            message = [
                TextSendMessage(
                    text = "從中心點到出口，再走一遍試試看！"
                ),
                TextSendMessage(
                            text='你想到了嗎？',
                            quick_reply=QuickReply(
                                items=[
                                    QuickReplyButton(
                                        action=MessageAction(label="我知道了",
                                            text="密碼鎖的顏色順序是")
                )]))]
        elif hintNum.count("二")==2:
            message = [
                TextSendMessage(
                    text = "先後順序好像很重要喵？"
                ),
                TextSendMessage(
                            text='你想到了嗎？',
                            quick_reply=QuickReply(
                                items=[
                                    QuickReplyButton(
                                        action=MessageAction(label="我知道了",
                                            text="密碼鎖的顏色順序是")
                )]))]
        else:
            message = [
                TextSendMessage(
                    text = "過程中先後會經過四種不同的顏色唷～"
                ),
                TextSendMessage(
                            text='你想到了嗎？',
                            quick_reply=QuickReply(
                                items=[
                                    QuickReplyButton(
                                        action=MessageAction(label="我知道了",
                                            text="密碼鎖的顏色順序是")
                )]))]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendHint3(event): #傳送第三關提示
    try:
        hintNum.append("三")
        if hintNum.count("三")==1:
            message = TextSendMessage(
                    text = "角的數量不太一樣呢喵。"
                )
        elif hintNum.count("三")==2:
            message = TextSendMessage(
                    text = "將數字轉換成英文會變成什麼呢？"
                )
        else:
            message = TextSendMessage(
                    text = "圓形的角的數量是多少呢喵？記得是先乘除後加減。"
                )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendHint4(event): #傳送第四關提示
    try:
        hintNum.append("四")
        if hintNum.count("四")==1:
            message = TextSendMessage(
                    text = "地上的圖案似乎與數字有什麼關聯？"
                )
        elif hintNum.count("四")==2:
            message = TextSendMessage(
                    text = "貓咪數量與按鍵上的Z箭頭互相對應。"
                )
        else:
            message = TextSendMessage(
                    text = "按照箭頭的順序點擊飲水機的四個按鈕喵。"
                )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendHint5(event): #傳送第五關提示
    try:
        hintNum.append("五")
        if hintNum.count("五")==1:
            message = [
                TextSendMessage(
                    text = "我總共爬了兩次梯子喵！"
                ),
                TextSendMessage(
                    text='你知道了喵？',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="我知道鑰匙在哪了",
                                    text="我知道鑰匙在哪了")
                )]))]
        elif hintNum.count("五")==2:
            message = [
                TextSendMessage(
                    text = "四個洞中只有方形我沒有經過喵。"
                ),
                TextSendMessage(
                    text='你知道了喵？',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="我知道鑰匙在哪了",
                                    text="我知道鑰匙在哪了")
                )]))]
        else:
            message = [
                TextSendMessage(
                    text = "往下跳一次，爬樓梯，再往下跳一層就又回來了～"
                ),
                TextSendMessage(
                    text='你知道了喵？',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="我知道鑰匙在哪了",
                                    text="我知道鑰匙在哪了")
                )]))]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendHint6(event): #傳送第六關提示
    try:
        hintNum.append("六")
        if hintNum.count("六")==1:
            message = [
                TextSendMessage(
                    text = "數數看顏色吧喵～"
                ),
                TextSendMessage(
                    text='你有想法嗎？',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="查看其他地方",
                                    text="查看其他地方")
                )]))]
        elif hintNum.count("六")==2:
            message = [
                TextSendMessage(
                    text = "先將門牌上掛的顏色都轉換成數字吧！"
                ),
                TextSendMessage(
                    text='你有想法嗎？',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="查看其他地方",
                                    text="查看其他地方")
                )]))]
        else:
            message = [
                TextSendMessage(
                    text = "顏色的數量代表的是紙條上由左至右第幾個英文字母。"
                ),
                TextSendMessage(
                    text='你有想法嗎？',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="查看其他地方",
                                    text="查看其他地方")
                )]))]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendLevel0(event): #請玩家回覆出發
    try:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text = "請在對話框輸入【出發】開始遊戲"))
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendLevel1(event): #關卡轉盤1
    try:
        message = TemplateSendMessage(
            alt_text="第一關轉盤",
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/yB1U3sc.jpg',
                text='第一關',
                actions=[
                    MessageTemplateAction(
                        label='前往第一關',
                        text='前往第一關'
                    )
                ]
            ))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendLevel2(event): #關卡轉盤1~2
    try:
        message = TemplateSendMessage(
            alt_text="第一到第二關轉盤",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/yB1U3sc.jpg',
                        text='第一關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第一關',
                                text='前往第一關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/PjklAN5.jpg',
                        text='第二關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第二關',
                                text='前往第二關'
                            )
                        ]
                    )]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))


def sendLevel3(event): #關卡轉盤1~3
    try:
        message = TemplateSendMessage(
            alt_text="第一到第三關轉盤",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/yB1U3sc.jpg',
                        text='第一關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第一關',
                                text='前往第一關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/PjklAN5.jpg',
                        text='第二關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第二關',
                                text='前往第二關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/06rgQ4G.jpg',
                        text='第三關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第三關',
                                text='前往第三關'
                            )
            ])]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendLevel4(event): #關卡轉盤1~4
    try:
        message = TemplateSendMessage(
            alt_text="第一到第四關轉盤",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/yB1U3sc.jpg',
                        text='第一關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第一關',
                                text='前往第一關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/PjklAN5.jpg',
                        text='第二關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第二關',
                                text='前往第二關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/06rgQ4G.jpg',
                        text='第三關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第三關',
                                text='前往第三關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/y4c2sJV.jpg',
                        text='第四關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第四關',
                                text='前往第四關'
                            )
            ])]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

def sendLevel5(event): #關卡轉盤1~5
    try:
        message = TemplateSendMessage(
            alt_text="第一到第五關轉盤",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/yB1U3sc.jpg',
                        text='第一關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第一關',
                                text='前往第一關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/PjklAN5.jpg',
                        text='第二關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第二關',
                                text='前往第二關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/06rgQ4G.jpg',
                        text='第三關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第三關',
                                text='前往第三關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/y4c2sJV.jpg',
                        text='第四關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第四關',
                                text='前往第四關'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/XxkBsVD.jpg',
                        text='第五關',
                        actions=[
                            MessageTemplateAction(
                                label='前往第五關',
                                text='前往第五關'
                            )
            ])]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='錯誤喵'))

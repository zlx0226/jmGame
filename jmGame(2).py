#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#玩家请运行并只运行这一个，并删除下面变量前的#
print('please wait for a moment')
import tkinter as tk
from tkinter import PhotoImage
print('注：本作内容纯属虚构，与任何真实个人、组织无关')
print('欢迎一切抄袭、篡改')
print('本作纯属搞笑，无任何不良引导！')
print()
name=input('请输入你的名字：')
print(name,',欢迎来到jm')
print('今天也要努力学习哦!')
input('press enter to continue')
import random
fight=0
war=0
fakedie=0
bravery=0
week=1
classjm=1
stress=0
luyi=0
chao=0
huang=0
nigger=0
life=random.randint(60,80)
chinese=random.randint(80,90)
maths=random.randint(80,90)
english=random.randint(80,90)
physics=random.randint(50,70)
chemistry=random.randint(60,75)
biology=random.randint(70,90)
politics=random.randint(50,70)
history=random.randint(60,75)
geography=random.randint(70,90)
computer=100
warning=0
story1=0
story2=0
continue1=0
continue2=0
continue3=0
continue4=0
continue5=0
continueend=0
def write(i):
    input()
    print(i)
while week<=8:
    print()
    print('你的成绩： 语文',chinese,'数学',maths,'英语',english,'物理',physics,'化学',chemistry,'生物',biology,'政治',politics,'历史',
         history,'地理',geography,'信息',computer)
    print('生命值:',life,'压力:',stress)
    input()
    print('今天距离期中考还有',8-week,'周,请确保每科成绩都在及格线以上，','你成功存活了',week-1,'周')
    input('press enter to continue')
    for i in range(1,11):
        print()
        print('现在是第',classjm,'节课,','请选择你想好好上的课（填数字）：')
        print('1语文,2数学,3英语,4物理,5化学,6生物,7政治,8历史,9地理,10信息,11睡觉')
        classchoose=input('number:')
        if classchoose=='1':
            joke=random.randint(1,5)
            if joke==1:
                print('作业可以晚交，但不可以交')
            else:
                print('作业可以晚交，但不可以不交')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','语文+0，生命值-2')
                life-=2
            else:
                print('好累啊。','语文+5，生命值-5')
                chinese+=5
                life-=5
        elif classchoose=='2':
            joke=random.randint(1,5)
            if joke<=3:
                print('昨天的作业不多吧？隔壁班一天要做6页呢！')
            else:
                print('这道题很简单的啊？')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','数学+0，生命值-2')
                life-=2
            else:
                print('好累啊。','数学+5，生命值-5')
                maths+=5
                life-=5
        elif classchoose=='3':
            joke=random.randint(1,5)
            if joke<=3:
                print(name,'，你承认吧？')
            else:
                print(name,'，你出去吧！')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','英语+0，生命值-2')
                life-=2
            else:
                print('好累啊。','英语+5，生命值-5')
                english+=5
                life-=5
        elif classchoose=='4':
            joke=random.randint(1,5)
            if joke<=4:
                print('傻孩子们，不会了吧？')
            else:
                print('我打死我自己！')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','物理+0，生命值-2')
                life-=2
            else:
                print('好累啊。','物理+5，生命值-5')
                physics+=5
                life-=5
        elif classchoose=='5':
            joke=random.randint(1,4)
            if joke==1:
                print('在我的老家——河南……')
            elif joke==2:
                print('OK不OK？')
            else:
                print('抠手的抠手，不知道干什么的不知道干什么！')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','化学+0，生命值-2')
                life-=2
            else:
                print('好累啊。','化学+5，生命值-5')
                chemistry+=5
                life-=5
        elif classchoose=='6':
            joke=random.randint(1,5)
            if joke<=3:
                print('')
            else:
                print('')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','生物+0，生命值-2')
                life-=2
            else:
                print('好累啊。','生物+5，生命值-5')
                biology+=5
                life-=5
        elif classchoose=='7':
            joke=random.randint(1,5)
            if joke<=3:
                print('习的思想……')
            else:
                print('我斗胆再拖两分钟啊。')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','政治+0，生命值-2')
                life-=2
            else:
                print('好累啊。','政治+5，生命值-5')
                politics+=5
                life-=5
        elif classchoose=='8':
            joke=random.randint(1,5)
            print('老师：有的同学在默写里瞎写，下课到办公室来。')
            print('你往旁边一看，你的同桌的默写纸上赫然写着“汉朝重男轻女”（重农抑商）')
            print('你又回头看教父的杰作：汉武帝习近平，任用拳击手打击地方豪强……')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','历史+0，生命值-2')
                life-=2
            else:
                print('好累啊。','历史+5，生命值-5')
                history+=5
                life-=5
        elif classchoose=='9':
            joke=random.randint(1,5)
            if joke<=3:
                print('')
            else:
                print('')
            classquality=random.randint(1,5)
            if classquality==1:
                print('一不小心睡着了……','地理+0，生命值-2')
                life-=2
            else:
                print('好累啊。','地理+5，生命值-5')
                geography+=5
                life-=5
        elif classchoose=='10':
            joke=random.randint(1,5)
            if joke<=3:
                print('一个ASCII码几个bit!')
            else:
                print('一节课只有40分钟！这节课不听以后就只能听天书了！！！')
            classquality=random.randint(1,5)
            if classquality<=2:
                print('美美地睡了一觉','生命值+2')
                life+=2
            else:
                print('计算机课写作业太爽了！','信息-5，语数英+3，生命值-5')
                chinese+=3
                maths+=3
                english+=3
                computer-=5
                life-=5
        elif classchoose=='11':
            classquality=random.randint(1,5)
            if classquality<=4:
                print('美美地睡了一觉','生命值+15')
                life+=15
            else:
                print('老师送了你一根粉笔头','压力+5，生命值-5')
                stress+=5
                life-=5
        else:
            print('你企图旷课，但被年级组长抓了个正着。 压力+20 处分+1（集齐三份处分，即可召唤退学）')
            stress+=20
            warning+=1
        classjm+=1
    print()
    print('10：00了，你终于回到了寝室')
    input('press enter to continue')
    print('你今晚要：（填数字）')
    print('1谁也不能阻止我睡觉  2卷作业  3与舍友聊天')
    choicenight=input('数字：')
    if choicenight=='2':
        print('朋友！你见过jm凌晨4点的太阳吗？！')
        print('生命-30 语数英物化生政史地+3')
        chinese+=3
        maths+=3
        english+=3
        physics+=3
        chemistry+=3
        biology+=3
        politics+=3
        history+=3
        geography+=3
        life-=30
    elif choicenight=='3':
        chat=random.randint(1,5)
        if chat<=2:
            if story1==0:
                print('同学甲：你听说了吗？隔壁寝的耶稣在垃圾桶里发现了整整5瓶贝纳颂的空瓶！')
                input('press enter to continue')
                print('你吓得赶紧收起了刚买的一瓶贝纳颂。')
                input()
                print('压力-6  生命值+10')
                stress-=6
                life+=10
                story1+=1
            elif story1==1:
                print('同学甲：你听说了吗？隔壁寝在吃最后的晚餐时，武大犹打翻了杯子。满满一杯都是咖啡！')
                input()
                print('同学乙：我知道！上次卷到凌晨4：00，喝了5瓶贝纳颂的就是他！')
                input()
                print('同学甲：听说他被发现时，还自爆了自己是著名的jm小丑，食堂二楼双料高级特工，代号：西格玛！')
                input()
                print('同学乙：他被抓时，还在背及时雨，背了整整5遍abandon，吓得大哥一枪毙了他。')
                input()
                print('同学丙：这就是卷狗的下场！')
                input()
                print('你吓得赶紧收起了作业。')
                input()
                print('压力-10  生命值+10')
                stress-=10
                life+=10
                story1+=1
            else:
                print('你们聊了一晚上的天。 压力-7  生命值+10')
                stress-=7
                life+=10
        else:
            if story2==0:
                print('同学甲：你听说了吗？在jm的操场边有一片垃圾堆，那里有人似乎在鬼鬼祟祟地研究着一桶不明液体。')
                input()
                print('压力-7  生命值+10')
                stress-=7
                life+=10
                story2+=1
            else:
                print('你们聊了一晚上的天。 压力-7  生命值+10')
                stress-=7
                life+=10
    else:
        print('美美地睡了一觉。 生命值+20')
        life+=20
    input()
    if life<=0:
        print('第二天早晨6：15，你的舍友发现你猝死在了土耳其进行曲中……  （生命值小于等于0）')
        root = tk.Tk()
        root.wm_attributes('-topmost', True)
        img = PhotoImage(file="die.gif")
        panal = tk.Label(root, image=img)
        panal.pack(side='bottom', fill='both', expand=True)
        root.geometry('500x520')
        root.mainloop()
        break
    if stress>=60:
        print('3号楼五楼的风真凉爽……')
        input()
        print('你从教学楼顶一跃而下，终于得到了解脱。 （压力大于等于60）')
        root = tk.Tk()
        root.wm_attributes('-topmost', True)
        img = PhotoImage(file="exemple.gif")
        panal = tk.Label(root, image=img)
        panal.pack(side='bottom', fill='both', expand=True)
        root.geometry('500x520')
        root.mainloop()
        write('温馨提示：真实情况下，如果压力太大，建议去心理看老师，切勿做出上述图片中的行为！')
        write('本作纯属搞笑，无任何不良引导！')
        break
    if warning>=3:
        print('你被退学了。')
        break
    print('一夜过去，许多知识似乎再次离你而去了…… 语数英物化生政史地-3')
    if choicenight!='2':
        write('没写完作业，被老师骂了一顿。  压力+5')
        stress+=5
    chinese-=3
    maths-=3
    english-=3
    physics-=3
    chemistry-=3
    biology-=3
    politics-=3
    history-=3
    geography-=3
    classjm=1
    week+=1
if week==9:
    input()
    print('期中考时间到')
    input()
    if chinese>=90 and maths>=90 and english>=90 and physics>=60 and chemistry>=60 and biology>=60 and politics>=60 and history>=60 and geography>=60 and computer>=60:
        print('你安全地度过了期中考')
        continue1+=1
    else:
        print('你考砸了，被老爸老妈臭骂了一顿，压力骤增。 压力+50')
        stress+=50
        if stress>=60:
            input()
            print('3号楼五楼的风真凉爽……')
            input()
            print('你从教学楼顶一跃而下，终于得到了解脱。 （压力大于等于60）')
            root = tk.Tk()
            root.wm_attributes('-topmost', True)
            img = PhotoImage(file="exemple.gif")
            panal = tk.Label(root, image=img)
            panal.pack(side='bottom', fill='both', expand=True)
            root.geometry('500x520')
            root.mainloop()
            write('温馨提示：真实情况下，如果压力太大，建议去心理看老师，切勿做出上述图片中的行为！')
            write('本作纯属搞笑，无任何不良引导！')
        else:
            continue1+=1
    if continue1==1:
        input()
        print('终于考完了，你决定要在这个愉快的下午好好享受。')
        if story2>=1:
            input()
            print('就在这时，校霸和体委（男）来邀请一起打篮球。')
            while 1==1:
                write('请选择：1答应  2不答应')
                answer=input('填数字：')
                if answer=='1':
                    write('你欣然答应了。')
                    write('你们向操场走去，但走着走着，体委忽地停了下来。')
                    write('体委：不好，我好像闹肚子了！校霸！你帮我拿着球！就在这站着。等我！')
                    write('说着，他就跑了。校霸一脸不情愿接过球。')
                    input()
                    print('校霸：好烦呐！',name,'，我们就在旁边垃圾站那里等他吧，别挡着人。')
                    write('你们走过走过垃圾站的水龙头处。校霸突然手一松，球滚进了废墟深处。')
                    write('校霸十分不屑地打算离开，转头就撞见了体委。')
                    write('体委骂道：那是我的球！你居然不给我捡回来！你什么实力啊？！')
                    write('你们只好一起进去捡球')
                    write('校霸开心地走了进去。')
                    write('突然，破椅子堆中走出了一个包连长，但她看起来不太正常。')
                    write('她叫着石头哥模仿领导人，一前一后地走了出来。')
                    write('等等，他们模仿的真的是人吗？')
                    write('体委吓了一大跳，大叫：我靠！校霸你有病吧？为了吓我给我整这出！')
                    write('还有小石！你配这样看我吗？！你直接给我坐下！')
                    write('话音刚落，石头哥本来失焦的双眼突然转向了他的方向,然后露出了一个诡异的微笑。')
                    write('石头哥忽地冲上前，张开嘴，好像要吃掉体委。')
                    while 1==1:
                        write('体委大惊失色，你决定：1踹一脚石头哥   2尖叫')
                        answer1=input('填数字：')
                        if answer1=='1':
                            print('你惊恐地踹了一脚石头哥。')
                            bravery=1
                            break
                        elif answer1=='2':
                            print('校霸惊恐地踹了一脚石头哥。')
                            break
                        else:
                            print('请务必选一个！')
                    write('石头哥倒地不起。')
                    write('体委见状恢复了自信，笑道：就凭你？！你有没有实力？！')
                    write('没想到石头哥突然跳了起来咬了体委一口，体委在你和校霸惊恐的目光下变成了石头哥的样子。')
                    write('校霸和你发出尖锐爆鸣声，两个石头哥又冲向了校霸。')
                    write('说时迟那时快，教父从你的身后飞奔而来，书包一甩，砸得两个石头哥昏倒在地。')
                    write('包连长正要上前，教父拉起你们就跑。')
                    write('跑着跑着，跑进了一个小道，和开放日留念的明信片上的照片一样。')
                    write('但校园里好像其实并没有这个地方。')
                    write('后面，哦不，前面，“石头哥”又出现了，还有导师。')
                    write('导师：你有没有实力啊？')
                    write('导师：你有没有实力啊？')
                    write('导师：你有没有实力啊？')
                    write('校霸无奈地摸了下脸：我服了，这都是什么生物啊？')
                    write('校霸：我生物59看不懂啊！')
                    write('教父笑了一下，从口袋里掏出两个拳击手套。')
                    write('教父：你生物再好也研究不出这是什么。不过你物理好啊。')
                    write('教父：物竞不能自学，给导师展示一下你的实力！')
                    write('校霸颤抖着接过手套。')
                    write('校霸：可是我不是拳击手，打不了地方豪强啊？')
                    write('教父踹了校霸一脚，让他上前。')
                    write('导师以为他要来决斗，掏出萝卜刀！')
                    write('导师：今天，我是导数大神！')
                    write('然后导师一刀刺向校霸。')
                    write('导师：回家种田吧你！')
                    write('校霸根据正交分解算出最佳时机，然后——')
                    write('把手套一扔，逃跑了。')
                    write('教父无奈白眼，追上校霸。')
                    while 1==1:
                        write('你决定：1跟上他们   2捡起手套')
                        answer2=input('填数字：')
                        if answer2=='2':
                            print('你赶紧捡起手套，导师已在你的面前。')
                            bravery+=1
                            write('你用力一记左勾拳，导师跌倒在地。')
                            write('石头哥向你冲了过来。')
                            write('就在你觉得“吾命休矣”之时，一道靓影飞闪而过，将石头哥击倒在地。')
                            write('是清奇姐！')
                            write('抄抄紧随其后，熟练地给石头哥和导师戴上头套，绑了起来。')
                            write('抄抄：我是路易一世殿下临时危机处理部第一执行官。')
                            if bravery==2:
                                input()
                                print('抄抄：',name,'，我看你骨骼清奇，有没有兴趣加入我们战事部？')
                                while 1==1:
                                    write('你决定：1愿意  2不愿意')
                                    answer3=input('填数字：')
                                    if answer3=='1':
                                        print('你：好啊。')
                                        war=1
                                        write('抄抄满意地笑了笑，示意你拖走石头哥和导师。')
                                        write('清奇姐：以后，你就是姐的同事了。可别拖我后腿哦！')
                                        write('抄抄低头看了一眼诺基亚：现在可不是嘘寒问暖的时候，有紧急事件要处理！')
                                        write('清奇姐：又是哪里？')
                                        write('抄抄：有个有趣的人……不……我得先回去一趟！头……头套不够了，先撤！')
                                        write('抄抄：有她在，应该不会出事的……')
                                        break
                                    elif answer3=='2':
                                        print('你：啊，这也太危险了吧。我还是算了。')
                                        write('抄抄：那可真是太遗憾了。')
                                        continue2+=1
                                        break
                                    else:
                                        print('请务必选一个！')
                            else:
                                continue2+=1
                            if continue2==1:
                                write('抄抄低头看了一眼诺基亚：有紧急事件要处理……不……我得先回去一趟！头……头套不够了，先撤！')
                                write('抄抄：有她在，应该不会出事的……')
                            write('你们跟着抄抄跑校门口，翻过门，没有来到校外的破马路，却来到了南校区。')
                            write('抄抄飞快地离开了。')
                            write('你：她怎么了？')
                            write('清奇姐：谁知道呢？多半是路易一世叫她吧。管她呢！我先去放松一下，你在这儿瞎逛逛吧。')
                            while 1==1:
                                write('你决定去：1大礼堂  2实验室  3教学楼后  4玻璃房  5体育馆')
                                answer4=input('填数字：')
                                if answer4=='1':
                                    print('你向大礼堂走去。')
                                    write('大礼堂里，清奇姐正插着耳机，听着MP3跳着蒙古舞。')
                                    write('你欣赏了一会儿。  压力-3')
                                    stress-=3
                                    break
                                elif answer4=='2':
                                    print('你向实验室走去。')
                                    write('有一个身影在其中摇动。')
                                    write('你凑近一看，发现是黄老板在跳科目三。')
                                    write('你：你在干嘛呢？')
                                    write('黄老板停了下来：哦，你是新来的吧！我是研究部的，正在研究丧尸的生前行为。')
                                    write('黄老板：不过目前来看，不是没有生前行为，就是没人生前会跳科目三。')
                                    write('你看了一会儿黄老板做实验，感觉收获了一点无用的知识。  生物+2')
                                    biology+=2
                                    huang=1
                                    break
                                elif answer4=='3':
                                    print('你向教学楼后走去。')
                                    write('那里的花坛变成了一大片棉花种植园。')
                                    write('你：这里也发生了异化吗……')
                                    write('就在这时，你看到了一个熟悉的身影——抄抄！')
                                    write('她竟然在这儿！')
                                    write('你远远地看到她似乎在与一个带着面罩的人在交流。')
                                    write('等等……不好！她快步地向着你的方向走了过来，你赶紧转身快速离开了。')
                                    nigger=1
                                    break
                                elif answer4=='4':
                                    print('你向玻璃房走去。')
                                    write('一个硕大的身躯在其中忙碌着。')
                                    write('你：嘿！路易一世！怎么是你？')
                                    write('路易一世：我可是临时危机处理部部长,怎么不能在这儿？')
                                    write('虽然你感觉这个这个什么部听起来十分野鸡，但不得不说还挺有用的。')
                                    write('至少他们救了你。')
                                    write('你：嘿！正是人不可貌相！')
                                    write('路易一世：你说谁呢？')
                                    write('你和他聊了一会儿目前的状况。')
                                    write('话说抄抄其实没来这儿吗？')
                                    luyi=1
                                    fight+=1
                                    break
                                elif answer4=='5':
                                    print('你到体育馆进行了锻炼。')
                                    fight+=1
                                    break
                                else:
                                    print('请务必选一个！')
                            write('你游荡到了南校区边缘，忽然看到了抄抄和路易一世。')
                            write('你走进一看，教父居然也来了。')
                            write('抄抄：你就是教父吧。现在进展如何了？')
                            write('教父：你在说什么？')
                            write('抄抄拿出一本本子，翻到某页。')
                            write('抄抄：执行记录上第二页写了“丧尸出现分化”,纵使我记忆不好，应该也是没有错误了。')
                            write('教父：你怎么知道？你是什么人？！')
                            write('抄抄露出得意一笑：路易一世殿下临时危机处理部第一执行官——抄抄！')
                            write('抄抄：这里是南校区。丧尸智商不高，短时间内应该找不到这儿。')
                            write('抄抄：对了，有个人想见你，跟我走吧！')
                            write('教父：谁？')
                            write('抄抄：你会想见她的。')
                            write('体育生跟着抄抄走了。')
                            while 1==1:
                                write('你决定：1跟上去看看  2留在原地')
                                answer5=input('填数字：')
                                if answer5=='1':
                                    print('你跟上抄抄和教父。')
                                    write('抄抄快步走进大礼堂，然后转身走了。')
                                    while 1==1:
                                        write('你决定：1跟上抄抄  2跟上教父')
                                        answer6=input('填数字：')
                                        if answer6=='1':
                                            chao-=1
                                            print('你跟上了抄抄。')
                                            write('抄抄发现你跟着她，赶紧停下来，转身。')
                                            write('抄抄：你跟着我做什么？可以麻烦你离开吗？这是我的隐私问题。')
                                            while 1==1:
                                                write('你决定：1偷偷跟着她  2算了')
                                                answer7=input('填数字：')
                                                if answer7=='1':
                                                    print('你：好好好，我不跟着你了。')
                                                    write('话虽这么说，你还是偷偷跟上了她。')
                                                    write('你尾随着她跑到了教学楼后面。')
                                                    if nigger==0:
                                                        write('那里的花坛变成了一大片棉花种植园。')
                                                        write('你：这里也发生了异化吗……')
                                                        write('你远远地看到她似乎在与一个带着面罩的人在交流。')
                                                        write('等等……不好！她快步地向着你的方向走了过来，你赶紧转身快速离开了。')
                                                        nigger+=1
                                                    else:
                                                        write('你远远地看到她似乎在与一个带着面罩的人在交流。')
                                                        write('这次可以猜测了，那个戴面罩的家伙不太对劲……')
                                                        write('不好！她快步地向着你的方向走了过来，你赶紧转身快速离开了。')
                                                        nigger+=1
                                                    break
                                                elif answer7=='2':
                                                    print('你：好好好，我不跟着你了。')
                                                    write('你还是回到了大礼堂。')
                                                    write('清奇姐正听着MP3，跳着蒙古舞。')
                                                    write('教父惊奇地叫道：清奇姐！！')
                                                    write('清奇姐惊喜地跳下舞台。')
                                                    write('清奇姐：教父！！')
                                                    write('你看着她们嘘寒问暖了一阵。')
                                                    write('就在这时，黄老板突然冲了进来。')
                                                    write('黄老板：快！快！出事了！')
                                                    if war==1:
                                                        input()
                                                        print('黄老板：',name,'，清奇姐！还有教父！出动！南校门口！')
                                                        write('清奇姐：跟姐来！')
                                                        write('你们一起跑了出去。')
                                                    else:
                                                        write('黄老板：清奇姐！还有教父！出动！南校门口！')
                                                        write('你跟着他们一起跑了出去。')
                                                    break
                                                else:
                                                    print('请务必选一个！')
                                            break
                                        elif answer6=='2':
                                            write('你跟着到了大礼堂。')
                                            write('清奇姐正听着MP3，跳着蒙古舞。')
                                            write('教父惊奇地叫道：清奇姐！！')
                                            write('清奇姐惊喜地跳下舞台。')
                                            write('清奇姐：教父！！')
                                            write('你看着她们嘘寒问暖了一阵。')
                                            write('就在这时，黄老板突然冲了进来。')
                                            write('黄老板：快！快！出事了！')
                                            if war==1:
                                                input()
                                                print('黄老板：',name,'，清奇姐！还有教父！出动！南校门口！')
                                                write('清奇姐：跟姐来！')
                                                write('你们一起跑了出去。')
                                            else:
                                                write('黄老板：清奇姐！还有教父！出动！南校门口！')
                                                write('你跟着他们一起跑了出去。')
                                            break
                                        else:
                                            print('请务必选一个！')
                                    write('你，清奇姐，教父跑到校门口，只见老祖狼狈地摔在地上，校霸坐在地上。')
                                    write('三个石头哥乱作一团，导师骑着马哥威风凛凛。')
                                    break
                                elif answer5=='2':
                                    print('你留在了原地。')
                                    if luyi==0:
                                        write('你：路易一世，你也在这儿？')
                                        write('路易一世：我可是临时危机处理部部长,怎么不能在这儿？')
                                    write('你：路易一世，你不跟她们一起吗？')
                                    write('路易一世刚想说话，一个熟悉的身影从墙上摔了下来。')
                                    write('是校霸！')
                                    write('在校门口，只见老祖和校霸狼狈地摔在地上。')
                                    write('三个石头哥也跳过围墙，降落到了南校区。')
                                    write('校霸鼓起勇气，投出一个拳击手套：我可是一场球进30分的男人！')
                                    write('拳击手套遮盖住了一个石头哥的脸，两个石头哥围攻上来。')
                                    write('校霸以投篮的姿势左右闪避，转身一个扫腿，两个石头哥直接坐下')
                                    write('校霸本来试图喊出‘你直接给我坐下’，突然意识到这不是他的台词，于是没说出来。')
                                    write('此时本应‘无声胜有声’，但他听到有人娴熟地说：‘你直接给我坐下！’')
                                    write('他吓了一跳，转身一看，导师骑着马哥跑来了。')
                                    write('敌人实力大大增强，校霸吓得腿一软，直接坐下了。')
                                    break
                                else:
                                    print('请务必选一个！')
                            break
                        elif answer2=='1':
                            print('你赶紧追上他们。')
                            write('导师：你什么实力啊？')
                            write('导师：你什么实力啊？')
                            write('导师：你什么实力啊？')
                            write('导师看见校霸跑走，想要追上，无奈体育不好，变成了抓人游戏。')
                            write('这时，他看向身后的操场，从上面拎出了正在踢球的马哥，血脉压制逼迫他变身。')
                            write('马哥大叫：我就是jm最大的小丑啊！')
                            write('他化身为马的形态，导师跃上马背，骑马奔向你们的方向，并叫石头哥大军尽快跟上。')
                            write('七个石头哥追在后面，五个包连长也跟了上来。')
                            write('你们眼看就要被追上了。')
                            write('老祖在操场上散步，看见丧尸大军惊得下巴都快掉了。')
                            write('教父看到老祖，把吓呆了的校霸扔向了老祖。')
                            write('教父：你跑得快，背着他跑，他吓得动弹不得了！')
                            write('草哥无奈背起校霸。')
                            write('就在这时，教父又发现了二年级小学生骑着滑板车路过。')
                            write('她一把抢过滑板车，背起小学生，拉着你就跑。')
                            write('小学生怒骂："Oh!Sh*t!"，并吐出一口口水。')
                            write('教父：哎哟，干嘛~大妈！现在的小学生怎么这么抽象！')
                            write('老祖背着校霸单脚跳了2.2米。')
                            write('一堆断手的石头哥和包连长跟上。')
                            write('你们开始想，他们是怎么被感染的？那片区域、明信片……究竟还有什么秘密？')
                            write('你们再一次绕到了垃圾场。')
                            write('一个高二学长正坐在那儿把玩着一个废轮胎，见你们来了，歪头扯出一个笑。')
                            write('他缓缓坐在轮胎旁的椅子上，手中仍把玩着轮胎。')
                            write('你们几人面面相觑，小学生不懂事，直接对他扔出玩偶，问道：你谁啊？')
                            write('高二学长终于开了口：第四次鬼打墙了，你们有没有发现？')
                            write('就在这时，石头哥大军和包连长们围了上来，你们陷入了进退两难的境地。')
                            write('校霸灵光一现，再次拿出拳击手套，让小学生往上面吐口水。')
                            write('然后，他再次扔出拳击手套，顺利击溃一排丧尸。')
                            write('校霸：疯狂星期四，肯得击，馋到你流口水！！')
                            write('校霸对自己的成果十分满意。')
                            write('小学生抢回滑板车，高兴得跳了起来，叫道：傻B大哥哥！')
                            write('高二学长歪头笑道：现在的小学生都那么抽象了吗？马哥，给她点教训！')
                            write('马哥不愿上前，恢复了人的形态，吼道：安静！！！')
                            write('教父十分不安，要拉着你们离开，可校霸还在大笑，小学生还在拍手跳。')
                            write("一个石头哥叫道：OK不OK？Let's go boys!Let's go!")
                            write('这两句话一下子激活了马哥的DNA，马哥再次化身为马，冲上前。')
                            write('教父赶紧拉走老祖、校霸和你，还没来得及抓走小学生，马哥就咬到了她的手臂。')
                            write('小学生立刻变成了马。')
                            write('教父嫌弃地看了一眼残局，一跃跳上了椅子堆，逾墙走。')
                            while 1==1:
                                write('你决定：1跟上教父  2留在原地')
                                answer8=input('填数字：')
                                if answer8=='1':
                                    print('你赶紧跟上教父。')
                                    write('你们摔到了一个不知名处，等你们站起来，只看到路易一世和抄抄在雾中若隐若现。')
                                    input()
                                    print("抄抄：你就是教父吧。","你是",name,"。现在进展如何了？")
                                    write('教父：你在说什么？')
                                    write('抄抄拿出一本本子，翻到某页。')
                                    write('抄抄：执行记录上第二页写了“丧尸出现分化”,纵使我记忆不好，应该也是没有错误了。')
                                    write('教父：你怎么知道？你是什么人？！')
                                    write('抄抄露出得意一笑：路易一世殿下临时危机处理部第一执行官——抄抄！')
                                    write('抄抄：这里是南校区。丧尸智商不高，短时间内应该找不到这儿。')
                                    if bravery==1:
                                        input()
                                        print('抄抄：',name,'，我看你骨骼清奇，有没有兴趣加入我们战事部？')
                                        while 1==1:
                                            write('你决定：1愿意  2不愿意')
                                            answer3=input('填数字：')
                                            if answer3=='1':
                                                print('你：好啊。')
                                                war=1
                                                write('抄抄满意地笑了笑。') 
                                                break
                                            elif answer3=='2':
                                                print('你：啊，这也太危险了吧。我还是算了。')
                                                write('抄抄：那可真是太遗憾了。')
                                                break
                                            else:
                                                print('请务必选一个！')
                                    write('抄抄：对了，有个人想见你，跟我走吧！')
                                    write('教父：谁？')
                                    write('抄抄：你会想见她的。')
                                    write('体育生跟着抄抄走了。')
                                    while 1==1:
                                        write('你决定：1跟上去看看  2留在原地')
                                        answer5=input('填数字：')
                                        if answer5=='1':
                                            print('你跟上抄抄和教父。')
                                            write('抄抄快步走进大礼堂，然后转身走了。')
                                            while 1==1:
                                                write('你决定：1跟上抄抄  2跟上教父')
                                                answer6=input('填数字：')
                                                if answer6=='1':
                                                    chao-=1
                                                    print('你跟上了抄抄。')
                                                    write('抄抄发现你跟着她，赶紧停下来，转身。')
                                                    write('抄抄：你跟着我做什么？可以麻烦你离开吗？这是我的隐私问题。')
                                                    while 1==1:
                                                        write('你决定：1偷偷跟着她  2算了')
                                                        answer7=input('填数字：')
                                                        if answer7=='1':
                                                            print('你：好好好，我不跟着你了。')
                                                            write('话虽这么说，你还是偷偷跟上了她。')
                                                            write('你尾随着她跑到了教学楼后面。')
                                                            write('那里的花坛变成了一大片棉花种植园。')
                                                            write('你：这里也发生了异化吗……')
                                                            write('你远远地看到她似乎在与一个带着面罩的人在交流。')
                                                            write('等等……不好！她快步地向着你的方向走了过来，你赶紧转身快速离开了。')
                                                            nigger+=1
                                                            break
                                                        elif answer7=='2':
                                                            print('你：好好好，我不跟着你了。')
                                                            write('你还是回到了大礼堂。')
                                                            write('清奇姐正听着MP3，跳着蒙古舞。')
                                                            write('教父惊奇地叫道：清奇姐！！')
                                                            write('清奇姐惊喜地跳下舞台。')
                                                            write('清奇姐：教父！！')
                                                            write('你看着她们嘘寒问暖了一阵。')
                                                            write('就在这时，黄老板突然冲了进来。')
                                                            write('黄老板：快！快！出事了！')
                                                            if war==1:
                                                                input()
                                                                print('黄老板：',name,'，清奇姐！还有教父！出动！南校门口！')
                                                                write('清奇姐：跟姐来！')
                                                                write('你们一起跑了出去。')
                                                            else:
                                                                write('黄老板：清奇姐！还有教父！出动！南校门口！')
                                                                write('你跟着他们一起跑了出去。')
                                                            break
                                                        else:
                                                            print('请务必选一个！')
                                                    break
                                                elif answer6=='2':
                                                    write('你跟着到了大礼堂。')
                                                    write('清奇姐正听着MP3，跳着蒙古舞。')
                                                    write('教父惊奇地叫道：清奇姐！！')
                                                    write('清奇姐惊喜地跳下舞台。')
                                                    write('清奇姐：教父！！')
                                                    write('你看着她们嘘寒问暖了一阵。')
                                                    write('就在这时，黄老板突然冲了进来。')
                                                    write('黄老板：快！快！出事了！')
                                                    if war==1:
                                                        input()
                                                        print('黄老板：',name,'，清奇姐！还有教父！出动！南校门口！')
                                                        write('清奇姐：跟姐来！')
                                                        write('你们一起跑了出去。')
                                                    else:
                                                        write('黄老板：清奇姐！还有教父！出动！南校门口！')
                                                        write('你跟着他们一起跑了出去。')
                                                    break
                                                else:
                                                    print('请务必选一个！')
                                            write('你，清奇姐，教父跑到校门口，只见老祖狼狈地摔在地上，校霸坐在地上。')
                                            write('三个石头哥乱作一团，导师骑着马哥威风凛凛。')
                                            break
                                        elif answer5=='2':
                                            print('你留在了原地。')
                                            write('你：路易一世，你也在这儿？')
                                            write('路易一世：我可是临时危机处理部部长,怎么不能在这儿？')
                                            write('你：路易一世，你不跟她们一起吗？')
                                            write('路易一世刚想说话，一个熟悉的身影从墙上摔了下来。')
                                            write('是校霸！')
                                            write('在校门口，只见老祖和校霸狼狈地摔在地上。')
                                            write('三个石头哥也跳过围墙，降落到了南校区。')
                                            write('校霸鼓起勇气，投出一个拳击手套：我可是一场球进30分的男人！')
                                            write('拳击手套遮盖住了一个石头哥的脸，两个石头哥围攻上来。')
                                            write('校霸以投篮的姿势左右闪避，转身一个扫腿，两个石头哥直接坐下')
                                            write('校霸本来试图喊出‘你直接给我坐下’，突然意识到这不是他的台词，于是没说出来。')
                                            write('此时本应‘无声胜有声’，但他听到有人娴熟地说：‘你直接给我坐下！’')
                                            write('他吓了一跳，转身一看，导师骑着马哥跑来了。')
                                            write('敌人实力大大增强，校霸吓得腿一软，直接坐下了。')
                                            break
                                        else:
                                            print('请务必选一个！')
                                    break
                                elif answer8=='2':
                                    print('你留在了原地，和校霸、老祖一起瑟瑟发抖。')
                                    write('你们看着石头哥和包连长们不断后退，僵持了好一会儿。')
                                    write('终于，你们回过神来，沿教父的路线逃跑了。')
                                    write('但离谱的是，三个石头哥也跟了过来。')
                                    write('校霸鼓起勇气，投出一个拳击手套：我可是一场球进30分的男人！')
                                    write('拳击手套遮盖住了一个石头哥的脸，两个石头哥围攻上来。')
                                    write('校霸以投篮的姿势左右闪避，转身一个扫腿，两个石头哥直接坐下')
                                    write('校霸本来试图喊出‘你直接给我坐下’，突然意识到这不是他的台词，于是没说出来。')
                                    write('此时本应‘无声胜有声’，但他听到有人娴熟地说：‘你直接给我坐下！’')
                                    write('他吓了一跳，转身一看，导师骑着马哥跑来了。')
                                    write('敌人实力大大增强，校霸吓得腿一软，直接坐下了。')
                                    break
                                else:
                                    print('请务必选一个！')
                            break
                        else:
                            print('请务必选一个！')
                    write('导师：你什么实力啊？')
                    write('导师：你什么实力啊？')
                    write('导师：你什么实力啊？')
                    write('导师命令石头哥进攻。')
                    write('石头哥们好不容易站起来，正乱作一团。')
                    write('这个简短的混乱改变了整个局面。')
                    write('说时迟，那时快，一个书包飞了过来，砸到了马哥。')
                    write('马哥惊叫一声，把导师摔下马背，一溜烟跑了。')
                    write('石头哥还没来得及反应，又一个书包就砸了过来。')
                    write('清奇姐闪亮登场，迅速打翻一个石头哥。')
                    write('清奇姐：姐赏你的！')
                    write('说着，她给打倒的石头哥戴上了头套。')
                    write('教父也赶来了，一个巨舌鞭挞（本人要加的），又打倒了一个石头哥。')
                    if war==1:
                        write('路易一世对你说：你也是战事部的吧！最后一个交给你了！')
                        if fight>=1:
                            write('你：好啊！')
                            write('说罢，你逼向了最后一个石头哥。')
                        else:
                            write('你：啊？我不会啊？')
                            write('清奇姐：哼，还是姐来吧！')
                            write('说罢，她逼向了最后一个石头哥。')
                    else:
                        write('清奇姐：哼，最后一个了。')
                        write('说罢，她逼向了最后一个石头哥。')
                    write('没想到，最后一个石头哥突然开始向你们鞠躬道歉。')
                    write('石头哥：对不起大哥！')
                    write('石头哥：对不起大哥！')
                    write('石头哥：对不起大哥……啊！')
                    write('那个石头哥还没说完，教父就给他戴上了头套。')
                    write('黄老板徐徐走了出来。')
                    write('黄老板：哈哈！看起来丧尸真的会有生前行为呢！我想我已经知道这是谁了。')
                    if huang==0:
                        write('你：这谁啊？')
                        write('路易一世：这是研究部部长。')
                    write('黄老板拖走了已被控制住的石头哥们和导师。')
                    write('黄老板：它们我带走研究了啊！')
                    write('抄抄姗姗来迟。')
                    write('抄抄：哦！已经解决好了啊！可以暂时放心一下了。战事部的，去训练一下吧！')
                    write('路易一世：抄抄，你干嘛去了？')
                    write('抄抄：没什么，这不重要。')
                    write('路易一世：你不会看到他了吧？')
                    write('抄抄已经转身走了，没有回答，似乎并没有听见。')
                    if war==1:
                        while 1==1:
                            write('你决定：1跟上抄抄去训练  2与校霸交流')
                            answer9=input('填数字：')
                            if answer9=='1':
                                print('你们一起进行了训练。')
                                fight+=1
                                break
                            elif answer9=='2':
                                print('你和校霸、老祖感叹了一会儿如今的境况。')
                                break
                            else:
                                print('请务必选一个！')
                    else:
                        write('你和校霸、老祖感叹了一会儿如今的境况。')
                    write('似乎过了十几分钟，抄抄急匆匆地跑了过来。')
                    write('抄抄：快！快！战事部集合！')
                    write('教父：咋了？')
                    write('抄抄：监控显示津辰小姐和香凝姐姐也误闯了丧尸空间，被包连长们包围了！')
                    write('清奇姐：那我们快出动吧！')
                    if war==1:
                        write('你们正准备出发，校霸突然拉住了你们。')
                        write('校霸：让我也跟你们走吧！')
                        write('抄抄：这不好吧？')
                        write('校霸：我保证不拖后腿！')
                        write('抄抄：哎哟！你们投票决定吧。')
                        write('清奇姐：姐才不带他！')
                        write('教父：他还是有点用的啦！')
                        write('抄抄问你：那你呢？')
                        while 1==1:
                            write('你决定：1让他去  2不让')
                            answer10=input('填数字：')
                            if answer10=='2':
                                print('你：不行！太危险了！')
                                write('抄抄：校霸，你还是安心呆在这儿吧！')
                                write('校霸：真让人失望！')
                                xiaoba=0
                                break
                            elif answer=='1':
                                print('你：他的确有点实力。')
                                write('校霸：太好了！')
                                write('抄抄：算了，你们随便吧。')
                                xiaoba=1
                                break
                            else:
                                print('请务必选一个！')
                        write('你们翻过墙到了主校区，抄抄留在了创新楼。')
                        continue3+=1
                    else:
                        write('他们很快走了，只有抄抄留在了创新楼，马上也走远了。')
                        input()
                        print('校霸：',name,'，你想不想跟过去？帮帮忙？')
                        while 1==1:
                            write('你决定：1想  2不想')
                            answer11=input('填数字：')
                            if answer11=='1':
                                print('你：好主意！窝在这里我们也毫无用处。')
                                write('校霸高兴地拍拍你的肩：知音啊！')
                                write('你们翻过墙到了主校区。')
                                continue3+=1
                                xiaoba=1
                                break
                            elif answer11=='2':
                                print('你：好了伤疤忘了疼！不记得咱被丧尸追得有多惨了吗？')
                                write('校霸：也是，算了算了！')
                                write('你们最后留在了创新楼。')
                                while 1==1:
                                    write('你决定去：1大礼堂  2实验室  3教学楼后  4玻璃房  5体育馆')
                                    answer4=input('填数字：')
                                    if answer4=='1':
                                        print('你向大礼堂走去。')
                                        write('大礼堂里空空荡荡，你休息了一会儿。 生命值+5')
                                        life+=5
                                        break
                                    elif answer4=='2':
                                        print('你向实验室走去。')
                                        write('有一个身影在其中摇动。')
                                        write('你凑近一看，发现是黄老板在跳科目三。')
                                        if huang==0:
                                            write('你：你在干嘛呢？')
                                            write('黄老板停了下来：哦，你是新来的那个吧！我正在研究丧尸的生前行为。')
                                            write('黄老板：不过目前来看，不是没有生前行为，就是没人生前会跳科目三。')
                                        else:
                                            write('你：你咋还在跳？其实是你自己想跳吧！')
                                        write('你看了一会儿黄老板做实验，感觉收获了一点无用的知识。  生物+2')
                                        biology+=2
                                        huang+=1
                                        break
                                    elif answer4=='3':
                                        print('你向教学楼后走去。')
                                        write('那里的花坛变成了一大片棉花种植园。')
                                        if nigger==0:
                                            write('你：这里也发生了异化吗……')
                                            write('就在这时，你看到了一个熟悉的身影——抄抄！')
                                            write('她竟然在这儿！')
                                            write('你远远地看到她似乎在与一个带着面罩的人在交流。')
                                        else:
                                            write('你：抄抄果然又在这儿，总觉得她在干什么危险的事。')
                                        nigger+=1
                                        break
                                    elif answer4=='4':
                                        print('你向玻璃房走去。')
                                        write('一个硕大的身躯在其中忙碌着。')
                                        write('你：嘿！路易一世！')
                                        write('他的这个什么部听起来十分野鸡，但不得不说还挺有用的。')
                                        write('至少他们救了你。')
                                        write('你：嘿！正是人不可貌相！')
                                        write('路易一世：你说谁呢？')
                                        write('你和他聊了一会儿目前的状况。')
                                        fight+=1
                                        break
                                    elif answer4=='5':
                                        print('你到体育馆进行了锻炼。')
                                        fight+=1
                                        break
                                    else:
                                        print('请务必选一个！')
                                write('你听到外面吵吵嚷嚷的，多半是战事部的家伙回来了。')
                                write('你顺着声音又来到了校门口。')
                                write('清奇姐：那几个包连长战力太强了！连姐都要差点打不过了。')
                                write('教父：津辰、香凝姐姐，你们怎么也闯过来了？')
                                write('津辰：害，我们就是散散步，看到垃圾堆有些诡异，就来拍照留念。')
                                write('香凝姐姐：是啊，结果莫名奇妙被一堆包连长追杀了。')
                                write('教父拍拍她的肩：难姐难妹。')
                                continue4=1
                                break
                            else:
                                print('请务必选一个！')
                    if continue3==1:
                        write('你们很快找到了被五个包连长围攻的津辰和香凝姐姐。')
                        write('清奇姐：姐来帮你们！')
                        write('说着她扑向一个包连长。')
                        write('没想到，包连长比石头哥强多了，清奇姐没能立刻压制住包连长，只能跟她缠打在一起。')
                        write('教父很快也和一个包连长纠缠在了一起。')
                        if xiaoba==1:
                            write('一个包连长向你和校霸冲了过来。')
                            while 1==1:
                                write('你决定：1保护校霸  2自卫')
                                answer13=input('填数字：')
                                if answer13=='1':
                                    print('你：校霸！小心！！')
                                    if fight>=1:
                                        write('你一拳打倒了包连长，训练果然有用。')
                                        write('你们废了好大的劲终于救走了津辰和香凝姐姐，回到了创新楼。')
                                        write('清奇姐：那几个包连长战力太强了！连姐都要差点打不过了。')
                                        write('教父：津辰、香凝姐姐，你们怎么也闯过来了？')
                                        write('津辰：害，我们就是散散步，看到垃圾堆有些诡异，就来拍照留念。')
                                        write('香凝姐姐：是啊，结果莫名奇妙被一堆包连长追杀了。')
                                        write('教父拍拍她的肩：难姐难妹。')
                                        continue4=1
                                    else:
                                        write('你：啊！！！')
                                        write('你在校霸惊恐的目光下被包连长狠狠地咬了一口。')
                                        write('你变成了包连长。')
                                        fakedie=1
                                    break
                                elif answer13=='2':
                                    print('你抛弃了校霸，选择了自卫。')
                                    if fight>=1:
                                        write('你一拳打倒了包连长，训练果然有用。')
                                        write('校霸也逃过了一劫。')
                                        write('你们废了好大的劲终于救走了津辰和香凝姐姐，回到了创新楼。')
                                        write('清奇姐：那几个包连长战力太强了！连姐都要差点打不过了。')
                                        write('教父：津辰、香凝姐姐，你们怎么也闯过来了？')
                                        write('津辰：害，我们就是散散步，看到垃圾堆有些诡异，就来拍照留念。')
                                        write('香凝姐姐：是啊，结果莫名奇妙被一堆包连长追杀了。')
                                        write('教父拍拍她的肩：难姐难妹。')
                                        continue4=1
                                    else:
                                        write('校霸：啊！！！')
                                        write('包连长咬完校霸再次冲向了你。')
                                        write('你：啊！！！')
                                        write('你也被包连长狠狠地咬了一口。')
                                        write('你变成了包连长。')
                                        write('你没机会知道，在一天过后，整个jm的人都变成了丧尸。')
                                    break
                                else:
                                    print('请务必选一个！')
                        else:
                            if fight>=1:
                                write('你一拳打倒了包连长，训练果然有用。')
                                write('你们废了好大的劲终于救走了津辰和香凝姐姐，回到了创新楼。')
                                write('清奇姐：那几个包连长战力太强了！连姐都要差点打不过了。')
                                write('教父：津辰、香凝姐姐，你们怎么也闯过来了？')
                                write('津辰：害，我们就是散散步，看到垃圾堆有些诡异，就来拍照留念。')
                                write('香凝姐姐：是啊，结果莫名奇妙被一堆包连长追杀了。')
                                write('教父拍拍她的肩：难姐难妹。')
                                continue4=1
                            else:
                                write('你：啊！！！')
                                write('你被包连长狠狠地咬了一口。')
                                write('你变成了包连长。')
                                fakedie=1
                    if continue4==1:
                        write('突然，你看到路易一世急匆匆地跑了过来。')
                        write('路易一世：你们看到抄抄了吗？黄老板找她有事！')
                        write('清奇姐：没欸！')
                        write('教父：没有。')
                        write('津辰、香凝姐姐：抄抄也在？')
                        write('你：没有看到。')
                        write('校霸：抄抄不见了？')
                        write('老祖：我跑得快，要不我去找找？')
                        write('路易一世：害，你们一起帮忙找找她吧！')
                        write('你们兵分几路，四散开来。')
                        if nigger>=1:
                            write('你：我想我大概知道她在哪儿……')
                            write('你直奔教学楼后。')
                            write('在一片棉花地里，你果然又看到了抄抄和一个笼子。')
                            write('你走了过去：抄抄！黄老板找你！')
                            write('抄抄看见你，猛地一惊，快速地企图用旁边的布遮住笼子。')
                            write('但她明白你已经看到了她的秘密，很快放弃了徒劳地尝试。')
                            write('那个巨大的笼子里赫然关着一个没戴头套的石头哥！')
                            write('你：抄抄！你……你在干什么？！')
                            write('抄抄一改平日的样子，恶狠狠地盯着你。')
                            write('抄抄：你什么都没看见！滚！不许告诉任何人！')
                            write('你：创新楼出现不明丧尸，最好还是要汇报的吧？')
                            write('你：还是说……你，是故意的？！')
                            write('抄抄：你不懂！给我滚！')
                            write('但你决定要好好处理这个事件。')
                            while 1==1:
                                write('你决定：1逼出内幕  2安抚冷静')
                                answer14=input('填数字：')
                                if answer14=='1':
                                    print('你：你最好说出内幕！否则我就对你不客气了！')
                                    write('抄抄死死地盯着你，眼睛泛红。')
                                    write('抄抄：你小心我开门放泥哥！')
                                    write('你：哦！这是泥哥啊！不会是你做出的新品丧尸吧？')
                                    write('抄抄：你！我要杀了你！')
                                    write('抄抄变得歇斯底里，但你感觉你很快就能问出真相，说不定就能结束这荒诞的一切。')
                                    write('你：我知道你不是这种人，告诉我，这一切是你造就的吗？')
                                    write('抄抄：我可以是！！！')
                                    write('说着，她打开了笼子门，饥饿难耐的石头哥一下子向你冲了过来。')
                                    if chao<=0:
                                        write('抄抄冷冷地看着你被咬，变成了石头哥。')
                                        write('在你最后一丝意识还未失去时，你看到那个被称作泥哥的石头哥咬中了抄抄。')
                                        write('你没机会知道，在一天过后，整个jm的人都变成了丧尸。')
                                    else:
                                        write('抄抄似乎被石头哥的反应吓了一跳，下意识地拦住他。')
                                        write('你也终于反应过来，打了石头哥一拳，拉着抄抄赶紧躲开，俯身躲进棉花丛中。')
                                        write('石头哥智商不高，绕了一圈拿走了地上的一瓶绿茶就离开了。')
                                        write('抄抄：泥哥原来是最忠心于我的nigger。')
                                        write('抄抄：但我们来调查丧尸事件时，他不幸被咬了。')
                                        write('抄抄：黄老板说，他要研究泥哥，要解剖他的。')
                                        write('抄抄：我不会让他伤害泥哥。')
                                        write('你：哦呀！黄老板这是在口嗨呢！')
                                        if huang>=1:
                                            write('你：你去看看他！他就一直让丧尸们看他跳科目三，解剖啥啊！')
                                        else:
                                            write('你：你自己去看看好了！')
                                        write('抄抄：呀！也是！我一遇到泥哥的事就失了理智！')
                                        write('抄抄：对了！泥哥刚刚跑掉了！我得去追他！')
                                        write('你：好的！我会帮你找回你最忠心的nigger的！')
                                        write('你：也请你多信任我们一些！')
                                        write('你们一起走出了棉花地。')
                                        continue5=1
                                    break
                                elif answer14=='2':
                                    print('你：抄抄，你冷静！')
                                    write('抄抄：你要交出我的泥哥！我就跟你拼了！！！')
                                    write('你：抄抄，你冷静！我不交泥哥！')
                                    write('抄抄：你，你……我要，我要……')
                                    write('抄抄：我……我又失去理智了……')
                                    write('抄抄：你也别误会了。我给你讲讲我们吧！')
                                    write('抄抄：泥哥原来是最忠心于我的nigger。')
                                    write('抄抄：但我们来调查丧尸事件时，他不幸被咬了。')
                                    write('抄抄：黄老板说，他要研究泥哥，要解剖他的。')
                                    write('抄抄：我不会让他伤害泥哥。')
                                    write('你：哦呀！黄老板这是在口嗨呢！')
                                    if huang>=1:
                                        write('你：你去看看他！他就一直让丧尸们看他跳科目三，解剖啥啊！')
                                    else:
                                        write('你：你自己去看看好了！')
                                    write('抄抄：呀！也是！我一遇到泥哥的事就失了理智！')
                                    write('就在这时，笼子发出了一声噪音。')
                                    write('笼子门松了，石头哥拿起旁边的绿茶逃跑了！')
                                    write('抄抄：糟了！快去追他！')
                                    write('你：好的！我会帮你找回你最忠心的nigger的！')
                                    write('你：也请你多信任我们一些！')
                                    write('你们一起走出了棉花地。')
                                    continue5=1
                                    break
                                else:
                                    print('请务必选一个！')
                        else:
                            write('你开始在教学楼内疯狂搜索。')
                            write('就在这时，清奇姐跑了过来。')
                            write('清奇姐尖叫道：石头哥跑了！抄抄发飙了！完蛋了！她变成石头哥！完了！')
                            write('清奇姐：啊！我被咬了！')
                            write('就这样，你们所有人全军覆没。')
                            write('你没机会知道，在一天过后，整个jm的人都变成了丧尸。')
                    if continue5==1:
                        write('你们一群人一起来到了主校区。')
                        write('你们分为了三组：你、校霸和抄抄一组，老祖、教父和路易一世一组，清奇姐、津辰和香凝姐姐一组。')
                        write('黄老板并不在场，所以没叫他。')
                        write('你们抄抄组率先发现了拿着绿茶的石头哥。')
                        write('抄抄：泥哥！！！')
                        write('你：快追！')
                        write('但是马哥拦住了你们的去路。')
                        write('马哥：安静！')
                        write('清奇姐飞奔过来：这里交给我们！你们快追！')
                        write('你们追着泥哥跑到了教学楼里，但和拦路的一个包连长纠缠了一番后，你们跟丢了。')
                        write('抄抄：教学楼也发生了异化，并没有学生，丧尸应该也不多，我们挨间教室搜吧！')
                        write('但当你们追到了高一2班的教室时，一个石头哥正拿着扫帚盘踞在教室里。')
                        write('石头哥：落榜美术生万岁！')
                        write('石头哥：落榜美术生万岁！')
                        write('石头哥：落榜美术生万岁！')
                        write('校霸：小心！他会耍太刀！')
                        write('石头哥发现了你们，向你们冲了过来！')
                        write('石头哥：落榜美术生万岁！')
                        write('石头哥：落榜美术生万岁！')
                        write('校霸：糟了！糟了！他要来咬我！')
                        write('校霸害怕地躲在桌子底下，石头哥耍着扫帚、跨过椅子向他逼近。')
                        write('校霸吓得跳起来继续逃窜，撞翻了桌子。')
                        write('桌子上的‘上海堡垒’哗的一下倾泻在了石头哥的头上。')
                        write('石头哥从一片狼藉中费力地爬出来，脑袋上还顶着一本石头哥生前爱看的《少女终末旅行》漫画书。')
                        write('校霸：啊！！！他要吃我！')
                        write('但是石头哥并没有追上去。')
                        write('他茫然地盯着你们：为什么我在教室里？其他同学呢？')
                        write('抄抄小心地问他：你还记得期中考语文作文是什么吗？')
                        write('石头哥：当然！是有人说青春是什么……是什么……是什么……')
                        write('石头哥：具体的游戏策划都不记得了。太难了！我差点就写不完了！')
                        write('校霸高兴地扑向石头哥。')
                        write('校霸：太好了！你恢复了！')
                        write('石头哥：你不要过来啊！！')
                        write('抄抄嫌弃地看了一眼。')
                        write('你：被jm南通吓哭了。')
                        write('你们简略地向他说明了现在的情况，石头哥认为大概是《少女终末旅行》让他恢复了。')
                        write('他拿着《少女终末旅行》走到班门口。')
                        write('石头哥：啊！！！！！')
                        write('一个石头哥赫然站在门口，手里还拿着一瓶绿茶。')
                        write('石头哥：啊！！！怎么还有一个我！！！')
                        write('他尖叫着把《少女终末旅行》扔到‘石头哥’的脸上，逃回了教室里。')
                        write('抄抄：泥哥！！！')
                        write('抄抄冲上了前，要抓住她的nigger。')
                        write('校霸：抄抄小心！泥哥没有恢复！《少女终末旅行》对他没用！')
                        write('校霸拉着吓坏了的石头哥和失去理智的抄抄从另一扇门冲出了教室。')
                        if fight>=2:
                            write('你小心地靠近泥哥，迅速举起一个书包，狠狠地砸向泥哥。（危险动作，请勿模仿）')
                            write('泥哥被你砸晕了。')
                            write('你赶紧跑出教室，拖走了泥哥。')
                            write('你看到清奇姐拉着路易一世跑了过来，教父和津辰追在后面。')
                        else:
                            write('你赶紧跟上校霸。')
                            write('泥哥发现了你们，快乐地追了上来。')
                            write('就在千钧一发之时，清奇姐跑了过来，一个书包砸晕泥哥。')
                            write('清奇姐：终于抓住了！')
                            write('你看到路易一世气喘吁吁地跑了过来，教父和津辰追在后面。')
                        write('路易一世：大事不妙啦！老祖被一匹吐着口水的小马咬了，变成了马！香凝姐姐也变成了包连长！')
                        write('清奇姐：情况变得糟透了！马哥进化了！')
                        write('教父：马哥进化成飞马了！！！')
                        write('抄抄：撤！我们先赶紧撤吧！')
                        write('马哥盘旋在你们的头上，你们一行人费劲心思终于回到了创新楼。')
                        write('路易一世：现在我们复盘一下此次行动的伤亡情况……啊！！！')
                        write('他看向了清醒的石头哥。')
                        write('清奇姐：石头哥！吃姐一书包！！！')
                        write('清奇姐正要砸真石头哥，校霸赶紧拦住她。')
                        write('校霸：别，别！他是真的石头哥，他恢复了！')
                        write('石头哥：干嘛~诶哟！我真的不是丧尸了！')
                        write('清奇姐：谁信你！吃我一书包！！！')
                        write('就在这时，黄老板徐徐走出。')
                        write('黄老板：我信他！')
                        write('大家齐刷刷地看向他。')
                        write('黄老板：我叫抄抄就是为了这事。就在刚刚，周子恢复了！')
                        write('黄老板：我正在跳科目三，一个一直叫着‘卷我！卷我！’的石头哥也跟着跳了起来。')
                        write('黄老板：结果他跳着跳着，就恢复了周子的样子，理智也恢复了。')
                        if huang>=1:
                            write('你：还真给你跳出名堂经了！')
                        write('路易一世：大喜讯啊！')
                        write('周子也走了出来,他看向了石头哥。')
                        write('周子：呀啊啊啊！就是这个东西咬了我！')
                        write('黄老板：周子，他也已经恢复了，是真的石头哥。')
                        write('抄抄：对了，石头哥，你就是最早那批变丧尸的吧！请说说你是怎么变的吧？')
                        write('石头哥想了想，说道：害，我想多半是在期中考结束的中午吧！')
                        write('他开始了遥远的回忆……')
                        write('（以下是回忆场景）')
                        write('包连长：石头哥、大哥，我发现了一个有趣的地方，你要不要跟我来看看？')
                        write('石头哥：好啊好啊！')
                        write('大哥：你告诉我在哪儿，我和兄弟们一会儿再去！')
                        write('他们一起来到了垃圾堆，导师也在那儿。')
                        write('导师：你们也来了？你们看！这儿有一株奇怪的植物。')
                        write('石头哥：居然长在一桶黑色药水里！')
                        write('包连长：还结了几个野果！')
                        write('导师：你们说这果子味道如何？')
                        write('就在这时，一个足球飞了过来，砸中了那桶黑色药水。')
                        write('导师还没时间研究果子好不好吃，掉下来的植物果子就落到了他的嘴里。')
                        write('导师：好吃！咦？身体怎么变得怪怪的了。')
                        write('黑色药水打翻在了石头哥与包连长的身上。')
                        write('马哥冲过来捡球，却被椅子绊倒，吃了一嘴的叶子。')
                        write('导师：你什么实力啊？')
                        write('马哥：我就是jm最大的小丑！')
                        write('导师：你什么实力啊？')
                        write('高二学长：WuNooooooo!我的上课不睡觉药！！！')
                        write('石头哥：落榜美术生万岁！')
                        write('（回忆结束）')
                        write('石头哥：大概就是这样了。')
                        write('周子：我就是被大哥拉过来的！')
                        write('路易一世：我对这个故事感到无语。')
                        write('黄老板：我觉得恢复的关键在于进行生前对丧尸来说重要的行为。')
                        write('路易一世：而离开异化空间的关键大概就是高二学长，或者是那个垃圾堆！')
                        write('抄抄：是的，监控显示，高二学长从未离开过垃圾堆上的那个椅子，也从未停止过把玩轮胎。')
                        write('校霸：但他的目的是什么？')
                        write('抄抄：不知道。')
                        write('路易一世：现在主要问题是，即使我们理清了思路，以我们现在的战力，也很难实行。')
                        write('你：我和抄抄先去把泥哥恢复一下吧！先增加一下战力。')
                        write('黄老板：我也先去试着恢复一下目前抓到的三个石头哥。')
                        write('路易一世：那好，其他人先来规划一下接下来的行动吧！')
                        write('你跟着抄抄来到了种植园。')
                        write('泥哥的恢复并不困难，抄抄让他摘了几朵棉花就恢复了。')
                        write('泥哥：以前在太平洋种植园时，我一天可以摘好几亩的棉花呢！')
                        write('突然，不远处传来了清奇姐的尖叫。')
                        write('清奇姐：啊！！！飞马马哥入侵创新楼了！！！')
                        write('你们三人赶紧跑回创新楼。')
                        write('津辰：啊！！！')
                        write('校霸：啊！！！')
                        write('马哥：安静！')
                        write('他盘旋在创新楼中。')
                        write('清奇姐和教父根本攻击不到他，其他人都在尖叫着逃窜。')
                        write('飞马马哥太强了！')
                        write('路易一世：完蛋了，临时危机处理部完蛋了。')
                        write('就在这时，一个羽毛球拍飞过，击中了飞马马哥。飞马马哥倒下了！')
                        write('一群人涌入创新楼。大师：高一2班救援小队来也！')
                        write('大师：虽然不知道什么时候成立了个野鸡临时危机处理部，但坚持到现在还是要表扬你们一下。')
                        write('大师：你们流下的每一滴汗水都是你们流下的！')
                        write('黄老板：你废什么话呀！')
                        write('唐：队长，注意时间！')
                        write('大师：哦哟，别急嘛！我们浪费的每一秒时间的时间都是我们浪费的！')
                        write('路易一世：你们怎么来了？来送人头？')
                        write('大师：才不是！我们的到来是为了我们的到来！')
                        write('唐：队长，你快别说了！事实上是小缪发现2班晚自习时，教室空了一半，就去找Erica。')
                        write('唐：然后Erica就叫我们来找你们，结果一起跑到这儿来了。')
                        write('路易一世：那不就是来送人头的吗？')
                        write('大师：那不是，我们送的每一个人头都是我们送的！')
                        write('你们在大礼堂里开了一场大会。')
                        write('他们也的确不算白来，至少每个人都带来了趁手的武器——羽毛拍。')
                        write('路易一世：这回真不愧是羽毛班了。')
                        write('路易一世：我们这儿有27个人，留几个在创新楼负责恢复，黄老板领队。')
                        write('路易一世：大队伍去把丧尸抓过来，战事部的几位领队。')
                        write('路易一世：我和抄抄负责指挥，用诺基亚联系！')
                        if war==1:
                            write('你带领着6个人又一次来到了主校区。')
                            write('你们采用包抄战术和人海战术，第一次抓住了包连长。')
                            write('你们接着又顺利地抓住了几个包连长和‘石头哥’。')
                            continueend=1
                        else:
                            while 1==1:
                                write('你决定：1去主校区  2留下')
                                answer15=input('填数字：')
                                if answer15=='1':
                                    print('你跟着一个7人小队又一次来到了主校区。')
                                    if fight>=1:
                                        write('你们采用包抄战术和人海战术，第一次抓住了包连长。')
                                        write('你们接着又顺利地抓住了几个包连长和‘石头哥’。')
                                        continueend=1
                                    elif fight==0:
                                        write('你牺牲了。')
                                        fakedie=1
                                elif answer15=='2':
                                    print('你留在了创新楼。')
                                    write('你恢复了一个奇怪的同学。')
                                    write('某个包连长：让我写代码！')
                                    write('某个包连长：让我写代码！')
                                    write('某个包连长：让我写代码！')
                                    write('你扔了一个电脑给她，她恢复了。')
                                    write('游戏制作者：想不出梗了，就这么结束吧！')
                                    continueend=1
                                else:
                                    print('请务必选一个！')
                    if continueend==1:
                        write('最后你们在垃圾堆会师，40名同学和二年级小学生全到了。')
                        write('高二学长尴尬地坐在垃圾堆上的破椅子。')
                        write('高二学长：你……你们，想干什么？！')
                        write('路易一世：我们当然想出去，回到正常的空间。')
                        write('高二学长：你们毁了我的上课不睡觉药水，又毁了我的丧失大军，你们还想得寸进尺？！')
                        write('路易一世：我们可以谈判。')
                        write('高二学长：呵，你们根本不懂我！')
                        write('高二学长：你们见过jm凌晨4点半的太阳吗？！')
                        write('高二学长：我为了上课不睡觉，特地研发了黑色药水，结果被你们搞坏了。')
                        write('高二学长：你们因为副作用变成了丧尸，进入了异化空间，那你们就乖乖当丧尸，感染整个jm啊！！！')
                        write('轩哥从人群中走出。')
                        write('轩哥：我见过！')
                        write('轩哥：话说你竟然不知道贝纳颂吗？')
                        write('轩哥：每天喝五瓶贝纳颂，五星上将麦克阿瑟喝了都说好！')
                        write('高二学长：啊！还有这样的好东西！快和我细说细说！')
                        write('高二学长高兴地跳下椅子，你们一个个跳过椅子，回到了正常的jm校园。')
                        write('你在这场奇妙的旅途中收获了一些奇怪的知识。 语数英物化生政史地+5')
                        chinese+=5
                        maths+=5
                        english+=5
                        physics+=5
                        chemistry+=5
                        biology+=5
                        politics+=5
                        history+=5
                        geography+=5
                    break
                elif answer=='2':
                    print('你拒绝了他们。')
                    write('晚自习时，班里居然少了近一半的人。')
                    write('小缪：嘿！2班的班长呢？你们班的人呢？')
                    write('唐：不知道。班长也不见了。')
                    write('小缪：哦！天哪！')
                    write('说着，她离开了。')
                    write('不一会儿，Erica急匆匆地赶了进来。')
                    write('Erica：他们人呢？')
                    write('大师：他们全不见了！')
                    write('Erica:大师，你出去吧！你带队出去找找他们？')
                    write('就这样，你们稀里糊涂地找到了垃圾堆，稀里糊涂地被一群石头哥和包连长追杀。')
                    write('哦！对了还有一大一小两匹马。')
                    write('突然一只飞马吸引了你们的注意力。')
                    write('它大叫着‘安静！’，飞过校门，瞬间消失了。')
                    write('你们怀疑那是马哥，追着它跳出了校门。')
                    write('你们没有降落到校门外，却跳到了创新楼前。')
                    write('津辰：啊！！！')
                    write('校霸：啊！！！')
                    write('马哥：安静！')
                    write('他盘旋在创新楼中。')
                    write('清奇姐和教父根本攻击不到他，其他人都在尖叫着逃窜。')
                    write('飞马马哥太强了！')
                    write('路易一世：完蛋了，临时危机处理部完蛋了。')
                    write('就在这时，一个羽毛球拍飞过，击中了飞马马哥。飞马马哥倒下了！')
                    write('你们涌入创新楼。大师：高一2班救援小队来也！')
                    write('大师：虽然不知道什么时候成立了个野鸡临时危机处理部，但坚持到现在还是要表扬你们一下。')
                    write('大师：你们流下的每一滴汗水都是你们流下的！')
                    write('黄老板：你废什么话呀！')
                    write('唐：队长，注意时间！')
                    write('大师：哦哟，别急嘛！我们浪费的每一秒时间的时间都是我们浪费的！')
                    write('路易一世：你们怎么来了？来送人头？')
                    write('大师：才不是！我们的到来是为了我们的到来！')
                    write('唐：队长，你快别说了！事实上是小缪发现2班晚自习时，教室空了一半，就去找Erica。')
                    write('唐：然后Erica就叫我们来找你们，结果一起跑到这儿来了。')
                    write('路易一世：那不就是来送人头的吗？')
                    write('大师：那不是，我们送的每一个人头都是我们送的！')
                    write('你们在大礼堂里开了一场大会。')
                    write('你们也的确不算白来，至少每个人都带来了趁手的武器——羽毛拍。')
                    write('路易一世：这回真不愧是羽毛班了。')
                    write('路易一世：我们这儿有27个人，留几个在创新楼负责恢复，黄老板领队。')
                    write('路易一世：大队伍去把丧尸抓过来，战事部的几位领队。')
                    write('路易一世：我和抄抄负责指挥，用诺基亚联系！')
                    while 1==1:
                        write('你决定：1去主校区  2留下')
                        answer15=input('填数字：')
                        if answer15=='1':
                            print('你跟着一个7人小队又一次来到了主校区。')
                            write('你牺牲了。')
                            fakedie=1
                            break
                        elif answer15=='2':
                            print('你留在了创新楼。')
                            write('你恢复了一个奇怪的同学。')
                            write('某个包连长：让我写代码！')
                            write('某个包连长：让我写代码！')
                            write('某个包连长：让我写代码！')
                            write('你扔了一个电脑给她，她恢复了。')
                            write('游戏制作者：想不出梗了，就这么结束吧！')
                            continueend=1
                            break
                        else:
                            print('请务必选一个！')
                    if continueend==1:
                        write('最后你们在垃圾堆会师，40名同学和二年级小学生全到了。')
                        write('高二学长尴尬地坐在垃圾堆上的破椅子。')
                        write('高二学长：你……你们，想干什么？！')
                        write('路易一世：我们当然想出去，回到正常的空间。')
                        write('高二学长：你们毁了我的上课不睡觉药水，又毁了我的丧失大军，你们还想得寸进尺？！')
                        write('路易一世：我们可以谈判。')
                        write('高二学长：呵，你们根本不懂我！')
                        write('高二学长：你们见过jm凌晨4点半的太阳吗？！')
                        write('高二学长：我为了上课不睡觉，特地研发了黑色药水，结果被你们搞坏了。')
                        write('高二学长：你们因为副作用变成了丧尸，进入了异化空间，那你们就乖乖当丧尸，感染整个jm啊！！！')
                        write('轩哥从人群中走出。')
                        write('轩哥：我见过！')
                        write('轩哥：话说你竟然不知道贝纳颂吗？')
                        write('轩哥：每天喝五瓶贝纳颂，五星上将麦克阿瑟喝了都说好！')
                        write('高二学长：啊！还有这样的好东西！快和我细说细说！')
                        write('高二学长高兴地跳下椅子，你们一个个跳过椅子，回到了正常的jm校园。')
                        write('你在这场奇妙的旅途中收获了一些奇怪的知识。 语数英物化生政史地+3')
                        chinese+=3
                        maths+=3
                        english+=3
                        physics+=3
                        chemistry+=3
                        biology+=3
                        politics+=3
                        history+=3
                        geography+=3
                    break
                else:
                    print('请务必选一个！')
        else:
            write('晚自习时，班里居然少了近一半的人。')
            write('小缪：嘿！2班的班长呢？你们班的人呢？')
            write('唐：不知道。班长也不见了。')
            write('小缪：哦！天哪！')
            write('说着，她离开了。')
            write('不一会儿，Erica急匆匆地赶了进来。')
            write('Erica：他们人呢？')
            write('大师：他们全不见了！')
            write('Erica:大师，你出去吧！你带队出去找找他们？')
            write('就这样，你们稀里糊涂地找到了垃圾堆，稀里糊涂地被一群石头哥和包连长追杀。')
            write('哦！对了还有一大一小两匹马。')
            write('突然一只飞马吸引了你们的注意力。')
            write('它大叫着‘安静！’，飞过校门，瞬间消失了。')
            write('你们怀疑那是马哥，追着它跳出了校门。')
            write('你们没有降落到校门外，却跳到了创新楼前。')
            write('津辰：啊！！！')
            write('校霸：啊！！！')
            write('马哥：安静！')
            write('他盘旋在创新楼中。')
            write('清奇姐和教父根本攻击不到他，其他人都在尖叫着逃窜。')
            write('飞马马哥太强了！')
            write('路易一世：完蛋了，临时危机处理部完蛋了。')
            write('就在这时，一个羽毛球拍飞过，击中了飞马马哥。飞马马哥倒下了！')
            write('你们涌入创新楼。大师：高一2班救援小队来也！')
            write('大师：虽然不知道什么时候成立了个野鸡临时危机处理部，但坚持到现在还是要表扬你们一下。')
            write('大师：你们流下的每一滴汗水都是你们流下的！')
            write('黄老板：你废什么话呀！')
            write('唐：队长，注意时间！')
            write('大师：哦哟，别急嘛！我们浪费的每一秒时间的时间都是我们浪费的！')
            write('路易一世：你们怎么来了？来送人头？')
            write('大师：才不是！我们的到来是为了我们的到来！')
            write('唐：队长，你快别说了！事实上是小缪发现2班晚自习时，教室空了一半，就去找Erica。')
            write('唐：然后Erica就叫我们来找你们，结果一起跑到这儿来了。')
            write('路易一世：那不就是来送人头的吗？')
            write('大师：那不是，我们送的每一个人头都是我们送的！')
            write('你们在大礼堂里开了一场大会。')
            write('你们也的确不算白来，至少每个人都带来了趁手的武器——羽毛拍。')
            write('路易一世：这回真不愧是羽毛班了。')
            write('路易一世：我们这儿有27个人，留几个在创新楼负责恢复，黄老板领队。')
            write('路易一世：大队伍去把丧尸抓过来，战事部的几位领队。')
            write('路易一世：我和抄抄负责指挥，用诺基亚联系！')
            while 1==1:
                write('你决定：1去主校区  2留下')
                answer15=input('填数字：')
                if answer15=='1':
                    print('你跟着一个7人小队又一次来到了主校区。')
                    write('你牺牲了。')
                    fakedie=1
                    break
                elif answer15=='2':
                    print('你留在了创新楼。')
                    write('你恢复了一个奇怪的同学。')
                    write('某个包连长：让我写代码！')
                    write('某个包连长：让我写代码！')
                    write('某个包连长：让我写代码！')
                    write('你扔了一个电脑给她，她恢复了。')
                    write('游戏制作者：想不出梗了，就这么结束吧！')
                    continueend=1
                    break
                else:
                    print('请务必选一个！')
            if continueend==1:
                write('最后你们在垃圾堆会师，40名同学和二年级小学生全到了。')
                write('高二学长尴尬地坐在垃圾堆上的破椅子。')
                write('高二学长：你……你们，想干什么？！')
                write('路易一世：我们当然想出去，回到正常的空间。')
                write('高二学长：你们毁了我的上课不睡觉药水，又毁了我的丧失大军，你们还想得寸进尺？！')
                write('路易一世：我们可以谈判。')
                write('高二学长：呵，你们根本不懂我！')
                write('高二学长：你们见过jm凌晨4点半的太阳吗？！')
                write('高二学长：我为了上课不睡觉，特地研发了黑色药水，结果被你们搞坏了。')
                write('高二学长：你们因为副作用变成了丧尸，进入了异化空间，那你们就乖乖当丧尸，感染整个jm啊！！！')
                write('轩哥从人群中走出。')
                write('轩哥：我见过！')
                write('轩哥：话说你竟然不知道贝纳颂吗？')
                write('轩哥：每天喝五瓶贝纳颂，五星上将麦克阿瑟喝了都说好！')
                write('高二学长：啊！还有这样的好东西！快和我细说细说！')
                write('高二学长高兴地跳下椅子，你们一个个跳过椅子，回到了正常的jm校园。')
                write('你在这场奇妙的旅途中收获了一些奇怪的知识。 语数英物化生政史地+3')
                chinese+=3
                maths+=3
                english+=3
                physics+=3
                chemistry+=3
                biology+=3
                politics+=3
                history+=3
                geography+=3
        if fakedie==1:
            write('当你再次清醒过来时，你已经在医务室里了。')
            write('陌生的天花板让你对不久前的经历感到一阵恍惚。')
            write('你知道，你马上就要回归正常的学习生活了。')
            continueend=1
        if continueend==1:
            write('你又回归了无聊的学习生活。')
            write('期末考后课业难度增加。  语数英物化生政史地-30')
            chinese-=30
            maths-=30
            english-=30
            physics-=30
            chemistry-=30
            biology-=30
            politics-=30
            history-=30
            geography-=30
            week=0
            while week<=8:
                print()
                print('你的成绩： 语文',chinese,'数学',maths,'英语',english,'物理',physics,'化学',chemistry,'生物',biology,'政治',politics,'历史',
                     history,'地理',geography,'信息',computer)
                print('生命值:',life,'压力:',stress)
                input()
                print('今天距离期末考还有',8-week,'周,请确保每科成绩都在及格线以上，','你成功存活了',week+7,'周')
                input('press enter to continue')
                for i in range(1,11):
                    print()
                    print('现在是第',classjm,'节课,','请选择你想好好上的课（填数字）：')
                    print('1语文,2数学,3英语,4物理,5化学,6生物,7政治,8历史,9地理,10信息,11睡觉')
                    classchoose=input('number:')
                    if classchoose=='1':
                        joke=random.randint(1,5)
                        if joke==1:
                            print('作业可以晚交，但不可以交')
                        else:
                            print('作业可以晚交，但不可以不交')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','语文+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','语文+5，生命值-5')
                            chinese+=5
                            life-=5
                    elif classchoose=='2':
                        joke=random.randint(1,5)
                        if joke<=3:
                            print('昨天的作业不多吧？隔壁班一天要做6页呢！')
                        else:
                            print('这道题很简单的啊？')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','数学+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','数学+5，生命值-5')
                            maths+=5
                            life-=5
                    elif classchoose=='3':
                        joke=random.randint(1,5)
                        if joke<=3:
                            print(name,'，你承认吧？')
                        else:
                            print(name,'，你出去吧！')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','英语+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','英语+5，生命值-5')
                            english+=5
                            life-=5
                    elif classchoose=='4':
                        joke=random.randint(1,5)
                        if joke<=4:
                            print('傻孩子们，不会了吧？')
                        else:
                            print('我打死我自己！')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','物理+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','物理+5，生命值-5')
                            physics+=5
                            life-=5
                    elif classchoose=='5':
                        joke=random.randint(1,4)
                        if joke==1:
                            print('在我的老家——河南……')
                        elif joke==2:
                            print('OK不OK？')
                        else:
                            print('抠手的抠手，不知道干什么的不知道干什么！')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','化学+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','化学+5，生命值-5')
                            chemistry+=5
                            life-=5
                    elif classchoose=='6':
                        joke=random.randint(1,5)
                        if joke<=3:
                            print('')
                        else:
                            print('')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','生物+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','生物+5，生命值-5')
                            biology+=5
                            life-=5
                    elif classchoose=='7':
                        joke=random.randint(1,5)
                        if joke<=3:
                            print('习的思想……')
                        else:
                            print('我斗胆再拖两分钟啊。')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','政治+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','政治+5，生命值-5')
                            politics+=5
                            life-=5
                    elif classchoose=='8':
                        joke=random.randint(1,5)
                        print('老师：有的同学在默写里瞎写，下课到办公室来。')
                        print('你往旁边一看，你的同桌的默写纸上赫然写着“汉朝重男轻女”（重农抑商）')
                        print('你又回头看教父的杰作：汉武帝习近平，任用拳击手打击地方豪强……')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','历史+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','历史+5，生命值-5')
                            history+=5
                            life-=5
                    elif classchoose=='9':
                        joke=random.randint(1,5)
                        if joke<=3:
                            print('')
                        else:
                            print('')
                        classquality=random.randint(1,5)
                        if classquality==1:
                            print('一不小心睡着了……','地理+0，生命值-2')
                            life-=2
                        else:
                            print('好累啊。','地理+5，生命值-5')
                            geography+=5
                            life-=5
                    elif classchoose=='10':
                        joke=random.randint(1,5)
                        if joke<=3:
                            print('一个ASCII码几个bit!')
                        else:
                            print('一节课只有40分钟！这节课不听以后就只能听天书了！！！')
                        classquality=random.randint(1,5)
                        if classquality<=2:
                            print('美美地睡了一觉','生命值+2')
                            life+=2
                        else:
                            print('计算机课写作业太爽了！','信息-5，语数英+3，生命值-5')
                            chinese+=3
                            maths+=3
                            english+=3
                            computer-=5
                            life-=5
                    elif classchoose=='11':
                        classquality=random.randint(1,5)
                        if classquality<=4:
                            print('美美地睡了一觉','生命值+15')
                            life+=15
                        else:
                            print('老师送了你一根粉笔头','压力+5，生命值-5')
                            stress+=5
                            life-=5
                    else:
                        print('你企图旷课，但被年级组长抓了个正着。 压力+20 处分+1（集齐三份处分，即可召唤退学）')
                        stress+=20
                        warning+=1
                    classjm+=1
                print()
                print('10：00了，你终于回到了寝室')
                input('press enter to continue')
                print('你今晚要：（填数字）')
                print('1谁也不能阻止我睡觉  2卷作业  3与舍友聊天')
                choicenight=input('数字：')
                if choicenight=='2':
                    print('朋友！你见过jm凌晨4点的太阳吗？！')
                    print('生命-30 语数英物化生政史地+3')
                    chinese+=3
                    maths+=3
                    english+=3
                    physics+=3
                    chemistry+=3
                    biology+=3
                    politics+=3
                    history+=3
                    geography+=3
                    life-=30
                elif choicenight=='3':
                    print('你们聊了一晚上的天。 压力-8  生命值+10')
                    stress-=8
                    life+=10
                else:
                    print('美美地睡了一觉。 生命值+20')
                    life+=20
                input()
                if life<=0:
                    print('第二天早晨6：15，你的舍友发现你猝死在了土耳其进行曲中……  （生命值小于等于0）')
                    root = tk.Tk()
                    root.wm_attributes('-topmost', True)
                    img = PhotoImage(file="die.gif")
                    panal = tk.Label(root, image=img)
                    panal.pack(side='bottom', fill='both', expand=True)
                    root.geometry('500x520')
                    root.mainloop()
                    break
                if stress>=60:
                    print('3号楼五楼的风真凉爽……')
                    input()
                    print('你从教学楼顶一跃而下，终于得到了解脱。 （压力大于等于60）')
                    root = tk.Tk()
                    root.wm_attributes('-topmost', True)
                    img = PhotoImage(file="exemple.gif")
                    panal = tk.Label(root, image=img)
                    panal.pack(side='bottom', fill='both', expand=True)
                    root.geometry('500x520')
                    root.mainloop()
                    write('温馨提示：真实情况下，如果压力太大，建议去心理看老师，切勿做出上述图片中的行为！')
                    write('本作纯属搞笑，无任何不良引导！')
                    break
                if warning>=3:
                    print('你被退学了。')
                    break
                print('一夜过去，许多知识似乎再次离你而去了…… 语数英物化生政史地-3')
                if choicenight!='2':
                    write('没写完作业，被老师骂了一顿。  压力+5')
                    stress+=5
                chinese-=3
                maths-=3
                english-=3
                physics-=3
                chemistry-=3
                biology-=3
                politics-=3
                history-=3
                geography-=3
                classjm=1
                week+=1
            if week==9:
                input()
                print('期中考时间到')
                input()
                if chinese>=90 and maths>=90 and english>=90 and physics>=60 and chemistry>=60 and biology>=60 and politics>=60 and history>=60 and geography>=60 and computer>=60:
                    print('你安全地度过了期末考')
                    continue1+=1
                else:
                    print('你考砸了，被老爸老妈臭骂了一顿，压力骤增。 压力+50')
                    stress+=50
                    if stress>=60:
                        input()
                        print('3号楼五楼的风真凉爽……')
                        input()
                        print('你从教学楼顶一跃而下，终于得到了解脱。 （压力大于等于60）')
                        root = tk.Tk()
                        root.wm_attributes('-topmost', True)
                        img = PhotoImage(file="exemple.gif")
                        panal = tk.Label(root, image=img)
                        panal.pack(side='bottom', fill='both', expand=True)
                        root.geometry('500x520')
                        root.mainloop()
                        write('温馨提示：真实情况下，如果压力太大，建议去心理看老师，切勿做出上述图片中的行为！')
                        write('本作纯属搞笑，无任何不良引导！')
                    else:
                        write('恭喜你！在jm存活了一个学期！')
input()
print('GAME OVER')
input()
print('游戏策划：张林萱(交闵26届2班)')
input()
print('程序：张林萱，张林萱，张林萱')
write('编程顾问：赵鑫（位育）')
input()
print('文案：张林萱，张林萱')
input()
print('美术：交闵2026届新生群')
write('bug测试员：洪语瞳（复附），王思语（进才），陆卿旖（交闵26届2班）')
input()
print('原著：大学先修课《最后的晚餐》，女寝507《7个石头哥与5个包连长》')


# In[ ]:





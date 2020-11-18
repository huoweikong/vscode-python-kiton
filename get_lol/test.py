import requests
import re
import bs4
import tkinter as tk

def opgg(champion_name,web_champion):
    #对应英雄查询具体信息
    r1=requests.get(web_champion[champion_name],headers=headers)
    soup1=bs4.BeautifulSoup(r1.text,'html.parser')
    champion_main=soup1.find('div',class_="l-champion-statistics-content__main")
    champion_text=champion_main.table

    #获取召唤师技能和技能加点
    skill_tbody=champion_main.table.tbody   #得到第一个tbody也就是包含召唤师技能和加点
    #正则匹配召唤师技能名字
    skill_name=[]
    pattern2=re.compile('(<img .*?>)')
    user_skill=re.findall(pattern2,str(skill_tbody))
    for skill in user_skill:
        skill_soup=bs4.BeautifulSoup(skill,'html.parser')
        skill_name_soup=bs4.BeautifulSoup(skill_soup.img['title'],'html.parser')
        name=skill_name_soup.b.string
        if name in item.keys():
            name=item[name]
        skill_name.append(name)
    #正则匹配召唤师技能的登场率和胜率
    skill_rate=[]
    pattern3=re.compile('<strong>(.*?)</strong>')
    rate_ls=re.findall(pattern3,str(skill_tbody))
    for rate in rate_ls:
        skill_rate.append(rate)
    #skill_rate为登场率胜率


    content=''

    skill='召唤师技能'.ljust(20)+'登场率'.ljust(10)+'胜率'.ljust(10)+'\n'
    content+=skill


    for i in range(0,len(skill_name),2):
        skill=(skill_name[i]+' + '+skill_name[i+1]).ljust(20)+skill_rate[i].ljust(10)+skill_rate[i+1].ljust(10)+'\n'
        content+=skill

    #获取技能加点
    skillAdd=skill_tbody.find_next_siblings('tbody')
    pattern4=re.compile(r'<td>([\s,\S]*?)</td>')
    skill_add=re.findall(pattern4,str(skillAdd))
    skill_add=''.join(skill_add)
    pattern5=re.compile('(\w*?)')
    skill_add=re.findall(pattern5,skill_add)
    skill_add=''.join(skill_add)
    skill_master=[skill_add[3],skill_add[10]]    #skill_master为主技能，副技能

    # 1 2 3 4 5 6 7 8 10 11 12 14 15

    skill='\n\n'+'主技能'.ljust(15)+'副技能'.ljust(15)+'\n'
    content+=skill
    skill=skill_master[0].ljust(15)+skill_master[1].ljust(15)+'\n'
    content+=skill



    #获取装备信息
    equipment_tbody=champion_text.find_next_siblings('table')[0].tbody
    equipment=[]
    pattern6=re.compile(r'(<tr[\s,\S]*?</tr>)')
    equipment_text=re.findall(pattern6,str(equipment_tbody))
    for text in equipment_text:
        tmp=[]
        #获取装备名
        pattern6=re.compile('(<li class="champion-stats__list__item tip"[\s,\S]*?</li>)')
        tmp_equipment=re.findall(pattern6,text)
        ls=[]
        for i in tmp_equipment:
            temp=bs4.BeautifulSoup(i,'html.parser')
            temp1=bs4.BeautifulSoup(temp.li['title'],'html.parser')
            if temp1.b.string in item.keys():
                ls.append(item[temp1.b.string])
            else:
                ls.append(temp1.b.string)
        tmp.append(ls)
        #获取登场率和胜率
        pattern7=re.compile(r'<strong>(.*?)</strong>')
        tmp.append(re.findall(pattern7,text))
        equipment.append(tmp)

    equip_name='装备'.ljust(50)+'登场率'.ljust(10)+'胜率'.ljust(10)+'\n'
    content+='\n\n'+equip_name
    o=0
    #equipment格式为:[[[装备],[登场率，胜率]]]
    for equip in equipment:
        equip_name=''
        equip_rate=''
        for i in equip[0]:
            equip_name+=i.ljust(10)
        for j in equip[1]:
            equip_rate+=j.ljust(10)
        content+=equip_name.ljust(50)+equip_rate+'\n'
        o+=1




    #获取符文信息
    runes_tbody=champion_text.find_next_siblings('div')[0].tbody
    runes_tag=runes_tbody.tr.td.div
    runes_div=runes_tag.div.find_next_siblings('div')
    runes_div.append(runes_tag.div)
    rune_ls=[]
    for rune in runes_div:
        tmp=[]
        #匹配符文名
        pattern8=re.compile(r'<div class="champion-stats-summary-rune__name">(.*?)</div>')
        z=[]
        for i in re.findall(pattern8,str(rune.a)):
            s=i.split(' + ')
            if s[0] in item.keys():
                s[0]=item[s[0]]
            if s[1] in item.keys():
                s[1]=item[s[1]]
            z=' + '.join(s)
        tmp.append(z)
        pattern9=re.compile(r'<strong>(.*?)</strong>')
        tmp.append(re.findall(pattern9,str(rune.a)))
        pattern10=re.compile(r'<span>(\d.*?)</span>')
        tmp.append(re.findall(pattern10,str(rune.a)))
        rune_ls.append(tmp)
    #rune_ls格式为[[[符文名],[登场率],[胜率]]]

    rune_name='\n\n'+'符文'.ljust(35)+'登场率'.ljust(10)+'胜率'.ljust(10)+'\n'
    content+=rune_name
    o=0
    for rune in rune_ls:
        for j,k in zip(rune[1],rune[2]):
            rune_name=rune[0].ljust(30)+j.ljust(10)+k.ljust(10)+'\n'
            content+=rune_name
        o+=1
    return content
#print(rune_ls)

def weburl_get():
    url='http://www.op.gg'
    addtion='/champion/statistics'
    r=requests.get(url+addtion,headers=headers)
    soup=bs4.BeautifulSoup(r.text,'html.parser')

    #获取到英雄列表
    championList=soup.find('div',class_='champion-index__champion-list')

    #单个英雄div格式匹配
    pattern1=re.compile('(<div class="champion-index__champion-item .*?</div>)')
    champion_list=re.findall(pattern1,str(championList))

    #将英雄名和网址作为一个字典
    web_champion={}
    for champion in champion_list:
        champion_soup=bs4.BeautifulSoup(champion,'html.parser')
        if (champion_soup.div)!=None and (champion_soup.div.a)!=None:
            web_champion[champion_soup.div['data-champion-key']]=url+champion_soup.div.a['href']
    return web_champion



headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3739.400'}
#'Cookie':'customLocale=zh_CN',
#en_US英语版面     zh_CN中文版面

###翻译
legend={}
with open('./translation_legend.txt','r',encoding='utf-8') as f:
    ls=f.read().split('\n')
    for i in ls:
        if i!='':
            tmp=i.split('：')
            legend[tmp[1]]=tmp[0]
#legend

item={}
with open('./translation_item.txt','r',encoding='utf-8') as f:
    ls=f.read().split('\n')
    for i in ls:
        if i!='':
            tmp=i.split('：')
            item[tmp[0]]=tmp[1]
#item

web_champion=weburl_get()

root=tk.Tk()
root.title('LOL')
root['width']=600
root['height']=400

def opgg_get():
    champion_name=legend[v.get()]
    text.delete(1.0,'end')
    if champion_name in web_champion.keys():
        content=opgg(champion_name,web_champion)
        text.insert(1.0,content)
    else:
        text.insert(1.0,'i can\'t get anything!!!')
    

v=tk.StringVar()
entry=tk.Entry(root,width=100,textvariable=v)
entry.grid(row=0,column=0,sticky=tk.W)
button=tk.Button(root,width=10,text="获取")
button['command']=opgg_get
button.grid(row=0,column=1)


text=tk.Text(root,width=100,height=30)
text.grid(row=1,column=0,sticky=tk.W)



root.mainloop()


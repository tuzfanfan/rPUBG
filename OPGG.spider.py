# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:38:31 2018

@author: Fan
"""
from requests_html import HTMLSession
import xlsxwriter
import re

class OPGG():
    def __init__(self):       
        self.f = xlsxwriter.Workbook('g:\elearning\gg2.xlsx')
        self.sheet1=self.f.add_worksheet()
        self.rowsTitle = [ u'序号',u'名字',u'排名',u'比赛场数',u'胜率',u'前十率',u'KDA','伤害',u'平均排名']
        self.sheet1.write_row('A1',self.rowsTitle)


    def getURL(self):   
        self.session = HTMLSession()
        #server=as,kr,jp,kakao,na,sa,eu,oc,sea
        #mode=fpp,tpp
        #queue_size=1,2,4
        url="https://pubg.op.gg/leaderboard/?server=as&mode=tpp&queue_size=1"
        r = self.session.get(url)
        post=r.html
        return post
     
    def HeadSpider(self):
        b=1
        for k in range(3):
            playername=self.getURL().find('li.leader-board-top3__item')[k].text
        #rank=self.getURL().find('li.leader-board-top3__item')[0].find('span.leader-board-top3__rating-value')[0]
        #gameplay=self.getURL().find('li.leader-board-top3__item')[0].find('span.leader-board-top3__matches-cnt-value')[0]
            player_split=playername.split("\n")
            t_name=re.findall(r'[0-9\n] (.*)',player_split[0])[0]
            t_rank=re.findall(r'[A-Z\n]+ (.*) Rating',player_split[1])[0]
            t_times=re.findall(r'[0-9]+',player_split[2])[0]
            t_winrate=re.findall(r'win (.*?)%',player_split[3])[0]
            t_top10rate=re.findall(r'top10 (.*)%',player_split[4])[0]
            t_damage=re.findall(r'[0-9]+',player_split[6])[0]
            t_Headshot=re.findall(r'% (.*)%',player_split[7])[0]
            t_mostkill=re.findall(r'[0-9]+',player_split[8])[0]
            t_KDA=re.findall(r'KDA (.*)',player_split[9])[0]
            t_avgrank=re.findall(r'#(.*)',player_split[10])[0]                               
            self.sheet1.write('A{}'.format(b+1),b)
            self.sheet1.write('B{}'.format(b+1),t_name)
            self.sheet1.write('C{}'.format(b+1),t_rank)
            self.sheet1.write('D{}'.format(b+1),t_times)
            self.sheet1.write('E{}'.format(b+1),t_winrate)
            self.sheet1.write('F{}'.format(b+1),t_top10rate)
            self.sheet1.write('G{}'.format(b+1),t_KDA)
            self.sheet1.write('H{}'.format(b+1),t_damage)
            self.sheet1.write('I{}'.format(b+1),t_avgrank)
            b+=1
        
          
    def Spider(self):
        name_list=self.getURL().find('a.leader-board__nickname')
        m=1
        for i in range(len(name_list)):
            Playername=name_list[i].text
            self.sheet1.write('A{}'.format(m+4),m+3)
            self.sheet1.write('B{}'.format(m+4),Playername)         
            m+=1          
        score_list=self.getURL().find('div.leader-board__table-content')
        n=1
        for j in range(0,len(score_list),7):
            rank=score_list[0+j].text
            matches_time=score_list[1+j].text
            win_rate=score_list[2+j].text
            Top10_rate=score_list[3+j].text
            KDA=score_list[4+j].text
            Damage=score_list[5+j].text
            Avg_rank=score_list[6+j].text   
            self.sheet1.write('C{}'.format(n+4),rank)
            self.sheet1.write('D{}'.format(n+4),matches_time)
            self.sheet1.write('E{}'.format(n+4),win_rate)
            self.sheet1.write('F{}'.format(n+4),Top10_rate)
            self.sheet1.write('G{}'.format(n+4),KDA)
            self.sheet1.write('H{}'.format(n+4),Damage)
            self.sheet1.write('I{}'.format(n+4),Avg_rank)
            n+=1
        self.f.close()

opgg=OPGG()
opgg.HeadSpider()
opgg.Spider()

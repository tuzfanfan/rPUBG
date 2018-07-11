# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:50:54 2018

@author: June♡
"""
import scrapy
from opgg.items import OpggItem
from bs4 import BeautifulSoup
#from requests_html import HTMLSession
from scrapy.http import Request

class OpggSpiderSpider(scrapy.Spider):
    name = 'opgg_solo'
    allowed_domains = ['https://pubg.op.gg']
    start_urls = ['https://pubg.op.gg/leaderboard']
    custom_settings = {'ITEM_PIPELINES':{'opgg.pipelines.OpggSoloPipeline':400}}


    def parse(self, response):
        servers = ['as','kakao','jp','sea','eu','oc','na','sa']
        #mode = ['tpp','fpp']
        #size = ['1','2','4']
        for sv in servers:           
            bash_url = 'https://pubg.op.gg/leaderboard/?server=pc-{}&mode=tpp&queue_size=1'.format(sv) 
            yield Request(bash_url,callback = self.get_Top3itemInfo,dont_filter=True)
        
    def get_Top3itemInfo(self,response): 
        item = OpggItem()
        content = response.body
        soup = BeautifulSoup(content,'html.parser')
        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
       
        index = 0
        in_list = []
        serv_name = []

          
        for i in range(3):
            ser_name = " "
            index +=1
            NickName = soup.find_all('a',attrs={"class":"leader-board-top3__nickname"})[i]
            Rating = soup.find_all('span',attrs={"class":"leader-board-top3__rating-value"})[i]
            Matches = soup.find_all('span',attrs={"class":"leader-board-top3__matches-cnt-value"})[i]
            Win = soup.find_all('div',attrs={"class":"leader-board-top3__grades leader-board-top3__grades--win"})[i]
            Ten = soup.find_all('div',attrs={"class":"leader-board-top3__grades leader-board-top3__grades--top10"})[i]
            Kda = response.xpath('/html/body/div[1]/section/div/div/div/div[4]/ul/li[{}]/ul/li[1]/span[2]/text()'.format(i+1)).extract()[0]
            Damage = response.xpath('/html/body/div[1]/section/div/div/div/div[4]/ul/li[1]/ul/li[2]/span[2]/text()'.format(i+1)).extract()[0]
            Rank = response.xpath('/html/body/div[1]/section/div/div/div/div[4]/ul/li[{}]/ul/li[6]/span[2]/text()'.format(i+1)).extract()[0]
            a.append(NickName.get_text())       
            b.append(float(Rating.get_text().replace(r",","")))
            c.append(int(Matches.get_text()))
            d.append(float(Win.get_text().replace("\n","").replace(r"%","").replace(r"win","").strip())/100)
            e.append(float(Ten.get_text().replace("\n","").replace(r"%","").replace(r"top10","").strip())/100)
            f.append(float(Kda))
            g.append(float(Damage))
            h.append(float(Rank.replace(r"#","")))
            in_list.append(index)
            serv_name.append(ser_name)
            
            
        for num2 in range(1,10):
            ser_name = " "
            index +=1
            table = response.xpath('//*[@id="playerRankingTable"]') 
            Name = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[2]/div/a//text()'.format(num2)).extract()[0]
            rating = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[3]/div//text()'.format(num2)).extract()[0]
            matches = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[4]/div//text()'.format(num2)).extract()[0]
            win = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[5]/div/span[2]//text()'.format(num2)).extract()[0]
            ten = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[6]/div/div[2]//text()'.format(num2)).extract()[0]
            kd = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[7]/div//text()'.format(num2)).extract()[0].strip()
            damage = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[8]/div/div[2]//text()'.format(num2)).extract()[0]
            rank = table.xpath('//*[@id="playerRankingTable"]/tbody/tr[{}]/td[9]/div//text()'.format(num2)).extract()[0].strip()
            a.append(Name)
            b.append(float(rating.replace(r",","")))
            c.append(int(matches))
            d.append(float(win.replace(r"%",""))/100)
            e.append(float(ten.replace(r"%",""))/100)
            f.append(float(kd))
            g.append(float(damage))
            h.append(float(rank))
            in_list.append(index)
            serv_name.append(ser_name)
        
        item['Top3NickName'] = a
        item['Top3WinRate'] = d
        item['Top3Rating'] = b
        item['Top3Matches'] = c
        item['Top3TenRate'] = e
        item['Top3Damage'] = g
        item['Top3Kda'] = f
        item['Top3AvgRank'] = h
        item['Index'] = in_list
        item['Serv_name'] = serv_name
                        
        yield item
                


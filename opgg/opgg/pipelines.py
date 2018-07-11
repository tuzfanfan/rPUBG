# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook


class OpggSqudPipeline(object):   
    wb = Workbook()
    ws = wb.active
    

    def process_item(self, item, spider):                                
        title = [u'Server',u'Index',u'Name',u'WinRate',u'Rating',u'Matches',u'TenRate',u'Damage',u'Kda',u'Rank']
        self.ws.append(title)
        
        for num in range(500):           
            line = [item['Serv_name'][num],item['Index'][num],item['Top3NickName'][num],
        item['Top3WinRate'][num],
        item['Top3Rating'][num],
        item['Top3Matches'][num],
        item['Top3TenRate'][num],
        item['Top3Damage'][num],
        item['Top3Kda'][num],
        item['Top3AvgRank'][num]]    
            self.ws.append(line)
            self.wb.save('e:/opgg_squd.xlsx')
        return item

class OpggSoloPipeline(object):   
    wb = Workbook()
    ws = wb.active
    

    def process_item(self, item, spider):                                
        title = [u'Server',u'Index',u'Name',u'WinRate',u'Rating',u'Matches',u'TenRate',u'Damage',u'Kda',u'Rank']
        self.ws.append(title)
        
        for num in range(500):           
            line = [item['Serv_name'][num],item['Index'][num],item['Top3NickName'][num],
        item['Top3WinRate'][num],
        item['Top3Rating'][num],
        item['Top3Matches'][num],
        item['Top3TenRate'][num],
        item['Top3Damage'][num],
        item['Top3Kda'][num],
        item['Top3AvgRank'][num]]    
            self.ws.append(line)
            self.wb.save('e:/opgg_solo.xlsx')
        return item
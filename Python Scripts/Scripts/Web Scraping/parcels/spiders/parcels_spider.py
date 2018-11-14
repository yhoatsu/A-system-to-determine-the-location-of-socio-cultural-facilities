import scrapy
import numpy as np
import pandas as pd

tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto Spatial\Pruebas\urls_non_sense.csv',sep=',',header=None,engine="python", encoding="latin_1")

class QuotesSpider(scrapy.Spider):
    name = "parcels"
    start_urls = []
    for nrow in range(0,(tabla.shape[0])): #(tabla.shape[0])
        start_urls.append(tabla.ix[nrow,0])

    def parse(self, response):

        num=response.xpath('//div[@class="panel-heading amarillo"]/text()').extract()		
     
        if len(num)==1 :

            parcela=num[0][21:35]
            a=response.xpath('//span[@data-toggle="tooltip"]/text()').extract()
            dicc={}
            if (len(a)-4)%5 != 0:
                dicc={a[4]:[int(a[2][:-2].replace(".", ""))]}
                yield { parcela : dicc }
            else:            
                elementos=int((len(a)-4)/5)
                if elementos==0:
                    dicc={a[5]:[int(a[3][:-2])]}
                    yield { parcela : dicc }
                else:
                    for i in range(1,elementos+1):
                        if a[5*i] not in dicc.keys():
                            dicc[a[5*i]]=[]
                        dicc[a[5*i]].append(int(a[5*i+1][0:15].replace(".", "")))
                    yield { parcela : dicc }

        elif len(num)==0:

            parcela=response.url[165:-33]
            yield { parcela : {} }
			
        else:
            
            b=response.xpath('//label[@class="control-label black text-left"]/text()').extract()
            parcela=b[0][0:14]
            d=response.css('td span').extract()
            d=d[2:len(d)]
            if len(d)%7 != 0: d=d[1:len(d)]
            elementos=int(len(d)/7)
            dicc={}
            if elementos==0:
                dicc={b[4]:[int(b[7][:-2].replace(".", ""))]}
                yield { parcela : dicc }
            else:
                for i in range(elementos):
                    if d[7*i][6:-7] not in dicc.keys():
                        dicc[d[7*i][6:-7]]=[]
                    dicc[d[7*i][6:-7]].append(int(d[7*i+4][6:-7].replace(".", "")))               
                yield { parcela : dicc }
            
       # else:
#
 #           c=response.xpath('//label[@class="control-label black text-left"]/text()').extract()
  #          parcela=c[0][0:14]
   #         d=response.css('td span').extract()
    #        d=d[2:len(d)]
     #       elementos=int(len(d)/7)
      #      dicc={}
       #     for i in range(elementos):
        #        if d[7*i][6:-7] not in dicc.keys():
         #           dicc[d[7*i][6:-7]]=[]
          #      dicc[d[7*i][6:-7]].append(int(d[7*i+4][6:-7]))               
           # yield { parcela : dicc }
					
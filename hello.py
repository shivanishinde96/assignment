from bs4 import BeautifulSoup
import re
import json
with open("index.html", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')
    #print(soup.table)
    table=soup.find('table')
    tablerows=table.find_all('tr')
    for tr in tablerows:
        tdata=tr.find_all('td')
        for td in tdata:
            font=td.find_all('font')
            for a in font:
                adata=a.find_all('a',href='mailto:testlead@gmail.com')
                
                
                for data in adata:
                    print(data.string)
                    
                   
            for strongdata in font:
                sdata=strongdata.find_all(re.compile('strong'),text='Test Lead')
                
                for stdata in sdata:
                    print(stdata.string)

            for addressdata in font:
                addata=addressdata.find_all('a',href='http://email.realtor.com/ls/click?upn=T-2BrPmNnZCl0v01IEKBYMXN-2F3Bn6-2FgbDoc8oDZ5vcNx7m0Escvkk7O6ByWDxaL9gv1nbODQxTpHliY8BwbzYjztsfr4Xe-2By8Yw72K3Ed4IgY-3DbCiM_FQC2LT8GxayrM161hhHVAkNUS2YanNVGLy6uAfbjyl2QFRNCjLovmmBjDMRn8hwdBTnYgI-2FiSrC6mt6i-2BB0F-2BQDIBo8Wa9v7enXj4prLSbQubAx8zvDmV-2F3ZZC3z4MRGXEZCzl5dIwWa-2F8Ht47mU-2FZi6ZRJeOHcrozXuDAh-2Bro7U836brpdbrQhSK6a-2F1LFy4U-2F-2FxeuY1tYJpsCXzUYGph5kA6zLx5TA1gw-2BqcJSqnRIvzdEyqCgVQuOcikXPnFikObfgo-2Fe5nSzx8vcziqxFv7mR65ukJZAu9uCKAlktm-2BRLBZk1zw3vst0kJAeNh-2Fjo3hEWeuOyLoYjRx7T16JAEKDTLvKdtIAT0Ke9pNaipr7-2F0xz8X44OS14Upywdp7o06s5KV0ZgKatHhao-2FsPY-2ByCN-2Fk-2BTAT-2FO6y1-2FSNUWINo-3D')

                for adddata in addata:
                    print(adddata.string)
                
            for bedsdata in font:
                bdata=bedsdata.find_all(re.compile('strong'),text='2')
                
                for bedata in bdata:
                    print(bedata.string)

            for bathsdata in font:
                bathdata=bathsdata.find_all(re.compile('strong'),text='3')
                
                for batata in bathdata:
                    print(batata.string)
            
           

        
with open('output.json', 'w') as json_file:
   print(json.dump({'email':data.string,'name':stdata.string,'address':adddata.string,'beds':bedata.string,'baths':batata.string},json_file,separators=(',', ':')))     

#phone=soup.find('a').text
#print(phone)
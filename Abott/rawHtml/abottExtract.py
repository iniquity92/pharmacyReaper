from bs4 import BeautifulSoup
import os

#fileList = ['a.html','b.html','c.html','d.html','e.html','f.html','g.html','h.html','i.html','j.html','k.html','l.html','m.html','n.html','o.html','p.html','q.html','r.html','s.html','t.html','u.html','v.html','w.html','x.html','y.html','z.html'];

fileList  = ['a.html']

print('{')

for fl in fileList:
    if (os.path.getsize(fl)!=0):
        with open(fl,'r') as content:
            soup = BeautifulSoup(content,'html')
            
            fl_drug_cabinet = soup.find_all("drug");
            
            for drug in fl_drug_cabinet:
                
                print ('\t{')
                print ('\t'+drug.text)
                print ('\t}')
                
            
            content.close()
    

print('}')
                

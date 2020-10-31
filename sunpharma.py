from bs4 import BeautifulSoup

medicine_file = open('1.1','r')

soup = BeautifulSoup(medicine_file,'html')

medicine_ul = soup.find("ul",attrs={"id":"api-list"})

medicine_store = medicine_ul.find_all("tr")

print ("{")

for medicine in medicine_store:
    
    #getAllColumns 
    columns = medicine.find_all("td")
    
    print("{")
    x=1
    for td in columns:
        if (x==1):
            printStr = "name : "
                
        elif(x==2):
            printStr = "strength : "
            
        elif (x==3):
            printStr = "salt : "
            
        elif (x==4):
            printStr = "therapy-area : "
            
        elif (x==5):
            printStr = "form : "
            
        elif (x==6):
            printStr = "pack-size : "
            
        print(printStr+td.text)
        x=x+1
    
    print("}")
    
print("}")

            


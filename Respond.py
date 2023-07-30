import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from random import randint,choice

# Go to the bottom to update the PATH variable

def show_menu():
    print('----------------------------------------------------------------------------------')
    print('''\tNote:if you would like to provide some emails but not all,
             then the Rest of them will be auto generated.Please make 
             sure to match the indexing of Names and males of your input.
             Name no 1 will be used with Email no 1 and so on...\n''')
    print('***********************************************************************************')
    print("\n\t\tEnter your choice after reading the menu carefully: ")
    print("\t\t\t 1.Form has Name and Mail field.")
    print("\t\t\t 2.Form has Name field only.")
    print("\t\t\t 3.Form has Mail field only.")
    print("\t\t\t 4.Form has NO Name or Mail field.")
    print('\n----------------------------------------------------------------------------------')
    Res=int(input("Enter your choice: "))
    if Res==1:
        choice=[i.strip() for i in input("\tWould you like the Emails to be generated from names?(Y/N): ").split()]
        Yes=['yes','y']
        if choice[0].lower() in Yes:
            return 5
        return Res
    return Res
    
def main(PATH):
    # launch URL
    Res=show_menu()
    if Res not in range(0,6):
        print("Please give the right choice.!!")
        return
    form = input("Enter your Form Link: ")
    N = int(input("Enter number of responses you want: "))
    EMAILS = []
    NAMES=[]
    if Res!=3 and Res!=4:
        NAMES = [i.strip() for i in input(f"Give {N} names separated by ';'(spaces between name and title is allowed) : ").split(';')]
        if(len(NAMES)!=N):
            print("Please give corrent number of names or in correct format!!")
            return
    if Res==1 or Res==3:
        EMAILS = [(''.join(i.split(' '))).strip() for i in input(f"Give {N} or less MAils separated by ';' : ").split(';')]
        
    # set chromodriver.exe path
    
    service = Service(executable_path=PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(service=service, options=options)
    # ...
    i = 0
    while(N):
        driver.get(form)
        driver.implicitly_wait(0.25)
        # identify text box
        time.sleep(1)
        flag1,flag2=0,0
        try:
            l = driver.find_elements(By.XPATH, '*//input[@type="text"]')
            flag1=1
        except:
            pass
        try:
            L2 = driver.find_elements(By.XPATH, '*//input[@type="email"]')
            L2=L2[:2]
            flag2=1
        except:
            pass
        if i<len(NAMES):
            NAME=NAMES[i]
        else:
            NAME=""
        if i<len(EMAILS):
            EMAIL=EMAILS[i]
        else:
            Mail_name=''.join([i.strip() for i in NAME.split()])
            EMAIL=Mail_name+str(randint(10,1000))+'@'+choice(['gmail','yahoo','outlook'])+'.com'
        i+=1
        if Res==4:
            c=1
        else:
            c=0
        if flag1:
            for X in l:
                if (c == 0 and i < len(NAMES)):
                    X.send_keys(NAME)
                    X.send_keys(Keys.RETURN)
                    c+=1
                else:
                    X.send_keys("others")
                    X.send_keys(Keys.RETURN)
                    c += 1             
        if flag2:
            for X in L2:
                X.send_keys(EMAIL)
                # send keyboard input
                X.send_keys(Keys.RETURN)
                
        with open(r'./Main.js', 'r') as f:
            ext_js = f.read()
        driver.execute_script(ext_js)
        #// Before you try to switch to the so given alert, it needs to be present.
        try:
            time.sleep(0.75)
            alert = Alert(driver)
            alert.accept()
        except:
            pass
    
        N-=1
        if(N==0):
            time.sleep(2)
            
if __name__=='__main__':
    # please change this to correct chromedriver path
    PATH = r"C:\Users\pinak\chromedriver.exe"
    if os.path.exists(PATH) and os.path.isfile(PATH):
        main(PATH)
    else:
        print("PLEASE PROVIDE CORRECT chromedriver PATH!!!")
        
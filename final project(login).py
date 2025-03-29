import random
import os
pagenumber = 1
def startpage():
  global pagenumber
  pagenumber =1
  print('Social media account')
  print('1. Login')
  print('2. Register')
  inp = input('Whcih one: ')
  if inp == '1':
    loginpage()
      
  elif inp =='2':
    signuppage()
  else:
    print('Wrong input')
  goback()

def loginpage():
  global data
  global name1
  global pagenumber
  pagenumber = 2
  for i in range(100):
     print('')
  name1 = input('Username:')
  try:
    file = open(name1+'.txt','r')
    data = file.readlines()
    password = input('Password:') + '\n'
    if password == data[1]:
      print('Full name:',data[0])
      print('Date of birth:',data[2])
      print('What do you want to do?\n','1. Edit profil\n','2. Open app\n')
      inp = input('Which one? ')
      if inp =='1':
        fixprofil()
        goback()
      elif inp == '2':
        openapp()
    else:
      print('Wrong password')
  except:
    print('Not yet register')

def signuppage():
  global pagenumber
  pagenumber = 2
  name1 = input('New Username:')
  if os.path.exists(name1+'.txt'):
    print('Username exist already')
  else:
    password = input('New password:')
    fname = input('Full name:')
    bday = input('Birthday:')
    file = open(name1+'.txt','w')
    file.write(fname+'\n')
    file.write(password+'\n')
    file.write(bday+'\n')
    file.close()

def goback():
  global pagenumber
  inp = input('Press enter to go back')
  for i in range(100):
     print('')
  if pagenumber ==1:
    startpage()
  elif pagenumber == 2:
    startpage()
  elif pagenumber == 3:
    startpage()
  elif pagenumber ==4:
    openapp()

def fixprofil():
  global data
  global name1
  global pagenumber
  pagenumber = 3
  for i in range(100):
     print('')
  print('1. Change username\n'+'2. Change password\n'+'3. Change full name\n'+'4. Change Date of birth\n')
  inp = input('Which one? ')
  if inp == '1':
    inp = input('Change username into: ')
    if os.path.exists(inp+'.txt'):
      print('Username exist already')
    else:
      file = open(inp+'.txt','w')
      for i in range(len(data)):
        file.write(data[i])
      file.close()
      os.remove(name1+'.txt')
  if inp == '2':
    inp = input('Change password into: ') + '\n'
    data[1] = inp
    file = open(name1+'.txt','w')
    for i in range(len(data)):
      file.write(data[i])
    file.close()
  if inp == '3':
    inp = input('Change full name into: ') + '\n'
    data[0] = inp
    file = open(name1+'.txt','w')
    for i in range(len(data)):
      file.write(data[i])
    file.close()
  if inp == '4':
    inp = input('Change date of brith into: ') + '\n'
    data[2] = inp
    file = open(name1+'.txt','w')
    for i in range(len(data)):
      file.write(data[i])
    file.close()

def openapp():
  global pagenumber
  pagenumber =3
  for i in range(100):
     print('')
  print('1.Calculator\n'+'2.Tic tac toe\n'+'3.Hangman\n'+'4.Math quiz\n'+'5.go back')
  inp = input('Which one: ')
  if inp == '1':
    pagenumber =4
    startcalculator()
  elif inp =='2':
    pagenumber =4
    initialtictactoe()
    goback()
  elif inp == '3':
    pagenumber =4
    starthangman()
    goback()
  elif inp == '4':
    mathquiz()
  else:
    goback()




  
def starttictactoe():
  global a
  global x
  global tic
  global ticround
  for i in range(3):
    print('|{:1}|{:1}|{:1}|'.format(tic[i+i+i],tic[i+1+i+i],tic[i+2+i+i]))
  for i in range(3):
    if tic[i+i+i]  == 'O' and tic[i+1+i+i] =='O' and tic[i+2+i+i] =='O' :
     x = x+1
    elif tic[i+i+i]  == 'X' and tic[i+1+i+i] =='X' and tic[i+2+i+i] =='X' :
      x = x+2
    elif tic[i]  == 'O' and tic[3+i] =='O' and tic[6+i] =='O' :
      x = x+1
    elif tic[i]  == 'X' and tic[3+i] =='X' and tic[6+i] =='X' :
      x = x+2
  if tic[0] == 'O' and tic[4] =='O' and tic[8] =='O':
    x =x+1
  elif tic[0] == 'X' and tic[4] =='X' and tic[8] =='X':
    x =x+2
  elif tic[2] == 'X' and tic[4] =='X' and tic[6] =='X':
    x =x+2
  elif tic[2] == 'O' and tic[4] =='O' and tic[6] =='O':
    x =x+1
  if ticround ==9 and x<1:
    print('draw')
    x =3
      


  if x < 1:
    turn()
    
  elif x == 1:
    print('O win')
  elif x == 2:
    print('X win')
    
def turn():
  global a 
  global tic
  global x
  global ticround
  
  if a%2 == 1:
    print('O turns')
    ask = int(input('Which number :'))
    if ask <= 9 and ask > 0:
      if tic[ask-1] =='O' or tic[ask-1] =='X':
        print('cannot')
      else:
        tic.insert(ask,'O')
        tic.pop(ask-1)
        a = a+1
        ticround = ticround+1
    else:
      print('number can only from 1-9') 
      
    starttictactoe()
    
  elif a%2 == 0:
    print('X turns')
    ask = int(input('Which number :'))
    if ask <= 9:
      if tic[ask-1] =='O' or tic[ask-1] =='X':
        print('cannot')
      else:
        tic.insert(ask,'X')
        tic.pop(ask-1)
        a = a+1
        ticround = ticround+1
    else:
      print('number can only from 1-9')
    starttictactoe()
    
    

def initialtictactoe():
  global x
  global a
  global tic
  global ticround
  tic = [1,2,3,4,5,6,7,8,9]
  ticround =0
  a=0
  x =0
  starttictactoe()

def startcalculator():
  for i in range(100):
     print('')
  print('----Calculator-----')
  value1 = int(input('Input value 1:'))
  value2 = int(input('Input value 2:'))
  operator = input('Which operation(+ or - or * or /): ')
  if operator == '+':
    total = value1 + value2
    print(value1,'+',value2,'=',total)
  if operator == '-':
    total = value1 - value2
    print(value1,'-',value2,'=',total)
  if operator == '*':
    total = value1 * value2
    print(value1,'*',value2,'=',total)
  if operator == '/':
    total = value1 / value2
    print(value1,'/',value2,'=',total)
  repeat = input('Next value? y/n: ')
  if repeat == 'y':
    startcalculator()
  elif repeat == 'n':
    goback()


def starthangman():
  for i in range(100):
     print('')
  words = ['cat','dog','eraser','pencil','banana','bird']
  word = random.choice(words)
  lengthofword = len(word)
  count = 0
  attempts = ''
  print('---Hangman---')
  print('Guess the word: ',"*" * lengthofword)
  chance = 10
  while True:
    print('Number of chance:',chance,'left')
    print('Used Words:',attempts)
    letter = input("Input letter : ")
    while len(letter) > 1 or letter in attempts:
      letter = input("Input letter : ")
    if letter in word:
      count += 1
    attempts += letter
    if letter not in word:
      print("incorrect")
      chance -= 1
    if chance == 0:
      print("GAME OVER")
      print("The word was",word)
      goback()
    for letter in word:
      if letter in attempts:
        print(letter, end ='')
      else:
        print('*',end='')
    print('')
    if count == lengthofword:
      print('You Win')
      break
      goback()
  
  
def mathquiz():
  global pagenumber
  for i in range(100):
     print('')
  pagenumber =4
  print('---Math Quiz--')
  print('All values are integers')
  print('Score 10 points to win')
  answer = 0
  total_value=0
  point =0
  while point <10:
    value1 = random.randint(1,100)
    value2 = random.randint(1,100)
    operator = random.randint(1,4)
    if operator ==1:
      print('Your point is',point)
      print(value1,'+',value2)
      total_value= value1+value2
      answer =int(input("What is the answer?"))
      if total_value==answer:
        print('Correct')
        point =point+1
      else:
        print('Incorrect')
        print('The answer is',total_value)
        point =point-1
    if operator ==2:
      print('Your point is',point)
      print(value1,'-',value2)
      total_value= value1-value2
      answer =int(input("What is the answer?"))
      if total_value==answer:
        print('Correct')
        point =point+1
      else:
        print('Incorrect')
        print('The answer is',total_value)
        point =point-1
    if operator ==3:
      print('Your point is',point)
      print(value1,'*',value2)
      total_value= value1*value2
      answer =int(input("What is the answer?"))
      if total_value==answer:
        print('Correct')
        point =point+1
      else:
        print('Incorrect')
        print('The answer is',total_value)
        point =point-1
    if operator ==4:
      print('Your point is',point)
      print(value1,'/',value2)
      total_value= value1//value2
      answer =int(input("What is the answer?"))
      if total_value==answer:
        print('Correct')
        point =point+1
      else:
        print('Incorrect')
        print('The answer is',total_value)
        point =point-1
  print('You Win')
  print('Your point is',point)
  goback()
  
  
  
  
  
startpage()


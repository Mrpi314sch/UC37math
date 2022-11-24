import os
import time
import random
import sys
import pyttsx3
import mathdata
correct=mathdata.correct
incorrect=mathdata.incorrect
level=correct//60 + 1
cset=0
engine=pyttsx3.init()
engine.setProperty('voice', 'english-us')
def speak(say):
    engine.say(say)
    engine.runAndWait()
file_location=os.path.expanduser('~')
numbers=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
digits=[0,1,2,3,4,5,6,7,8,9]
def multiplication(num1, num2):
    global numbers
    global digits
    if num1 <= 10 or num2 <= 10:
        mnum1=random.choice(digits)
        mnum2=random.choice(digits)
        global cset
        if cset == 0:
            screen(str(mnum1)+' times '+str(mnum2)+' equals '+str(mnum1*mnum2))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' times '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1*num2:
                screen('correct!')
                global correct
                
                cset+=1
                correct+=1
            else:
                screen('incorrect.')
                global incorrect
                incorrect +=1
        except:
            screen('type only the answer')
            time.sleep(1)
            screen('no extra words!')
    else:
        mnum1=random.choice(numbers)
        mnum2=random.choice(numbers)
        if cset == 0:
            screen(str(mnum1)+' times '+str(mnum2)+' equals '+str(mnum1*mnum2))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' times '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1*num2:
                screen('correct!')
                correct+=1
            else:
                screen('incorrect.')
                incorrect +=1
        except:
            screen('type only the answer')
            time.sleep(1)
            screen('no extra words!')
def division(num1, num2):
    global numbers
    global digits
    if not num1 <= 10 or num2 <= 10:
        mnum1=random.choice(numbers)
        mnum2=random.choice([2,3,4,5,6,7,8,9,10])
        while True:
            if mnum1%mnum2 == 0:
                break
            else:
                mnum1=random.choice(numbers)
                mnum2=random.choice([2,3,4,5,6,7,8,9,10])
        if mnum2 == 0:
            mnum2 = 1
        global cset
        if cset == 0:
            screen(str(mnum1)+' divided by '+str(mnum2)+' equals '+str(mnum1//mnum2))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' divided by '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1/num2:
                screen('correct!')
                global correct
                cset+=1
                correct+=1
            else:
                screen('incorrect.')
                global incorrect
                incorrect +=1
        except:
            screen('type only the answer')
            time.sleep(1)
            screen('no extra words!')
    else:
        mnum1=random.choice(numbers)
        mnum2=random.choice([2,3,4,5,6,7,8,9,10])
        while True:
            if mnum1%mnum2 == 0:
                break
            else:
                mnum1=random.choice(numbers)
                mnum2=random.choice([2,3,4,5,6,7,8,9,10])
        if mnum2 == 0:
            mnum2 = 1
        if cset == 0:
            screen(str(mnum1)+' divided by '+str(mnum2)+' equals '+str(mnum1//mnum2))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' divided by '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1/num2:
                screen('correct!')
                correct+=1
            else:
                screen('incorrect.')
                incorrect +=1
        except:
            screen('type only the answer')
            time.sleep(1)
            screen('no extra words!')
def subtraction(num1, num2):
    global numbers
    global digits
    if num1 <= 10 or num2 <= 10:
        mnum1=random.choice(digits)
        mnum2=random.choice(digits)
        if num1-num2 <= 0:
            prevnum1=num1
            num1=num2
            num2=prevnum1
        global cset
        if cset == 0:
            if not mnum1-mnum2 <=0:
                screen(str(mnum1)+' minus '+str(mnum2)+' equals '+str(mnum1-mnum2))
            else:
                screen(str(mnum2)+' minus '+str(mnum1)+' equals '+str(mnum2-mnum1))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' minus '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1-num2:
                screen('correct!')
                global correct
                
                cset+=1
                correct+=1
            else:
                screen('incorrect.')
                global incorrect
                incorrect +=1
        except:
            screen('type only the answer')
            time.sleep(1)
            screen('no extra words!')
    else:
        mnum1=random.choice(numbers)
        mnum2=random.choice(numbers)
        if num1-num2 <= 0:
            prevnum1=num1
            num1=num2
            num2=prevnum1
        if cset == 0:
            if not mnum1-mnum2 <=0:
                screen(str(mnum1)+' minus '+str(mnum2)+' equals '+str(mnum1-mnum2))
            else:
                screen(str(mnum2)+' minus '+str(mnum1)+' equals '+str(mnum2-mnum1))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' minus '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1-num2:
                screen('correct!')
                
                cset+=1
                correct+=1
            else:
                screen('incorrect.')
                incorrect +=1
        except:
            screen('type only the answer')
            time.sleep(1)
            screen('no extra words!')
def addition(num1, num2):
    global numbers
    global digits
    if not num1+num2 >= 20:
        mnum1=random.choice(digits)
        mnum2=random.choice(digits)
        global cset
        if cset == 0:
            screen(str(mnum1)+' plus '+str(mnum2)+' equals '+str(mnum1+mnum2))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' plus '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1+num2:
                screen('correct!')
                global correct
                
                cset+=1
                correct+=1
            else:
                screen('incorrect.')
                global incorrect
                incorrect +=1
        except:
            screen('type only the answer')
            time.sleep(1)
            screen('no extra words!')
    else:
        mnum1=random.choice(numbers)
        mnum2=random.choice(numbers)
        if cset == 0:
            screen(str(mnum1)+' plus '+str(mnum2)+' equals '+str(mnum1+mnum2))
            time.sleep(0.5)
            screen('your turn: ')
            time.sleep(0.5)
        screen('what is '+str(num1)+' plus '+str(num2)+'? ')
        user_text=''
        brk=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
  
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        brk=1
            # Unicode standard is used for string
            # formation
                    else:
                        user_text += event.unicode
                    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(user_text+'   ', True, white, blue), (50, 220))
                    pygame.display.update()
            if brk == 1:
                break
        giveans=user_text
        try:
            if int(giveans) == num1+num2:
                screen('correct!')
                correct+=1
            else:
                screen('incorrect.')
                incorrect +=1
        except:
            screen('type only the answer')
            screen('no extra words!')
import pygame
file_location=os.path.expanduser('~')
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 800
Y = 400
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('UC37 math')
pygame.display.set_icon(pygame.image.load(file_location+'/UC37software/images/UC37.png'))
font = pygame.font.Font('freesansbold.ttf', 32)
header = font.render('UC37 math', True, white, blue)
textRect = header.get_rect()
textRect.center = (180, 20)
display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Welcome to UC37 math!", True, blue, white), (50, 0))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("x", True, blue, white), (250, 100))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("÷", True, blue, white), (250, 250))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("+", True, blue, white), (450, 100))
display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("−", True, blue, white), (450, 250))
pygame.display.update()
def screen(text):
    text=text+'                                                                '
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(text, True, white, blue), (50, 150))
    pygame.display.update()
    speak(text)
    print(text)
def multiply():
    global numbers
    global digits
    display_surface.fill(blue)
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Multiplication", True, blue, white), (50, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(str(cset), True, blue, white), (750, 0))
    pygame.display.update()
    if level >= 7:
        muldif =numbers
    else:
        muldif=digits
    multiplication(random.choice(muldif),random.choice(muldif))
def divide():
    global numbers
    display_surface.fill(blue)
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Division", True, blue, white), (50, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(str(cset), True, blue, white), (750, 0))
    pygame.display.update()
    divisor1=random.choice(numbers)
    divisor2=random.choice([2,3,4,5,6,7,8,9,10])
    while True:
        if divisor1%divisor2 == 0:
            break
        else:
            divisor1=random.choice(numbers)
            divisor2=random.choice([2,3,4,5,6,7,8,9,10])
    division(divisor1,divisor2)
def add():
    global numbers
    global digits
    display_surface.fill(blue)
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Addition", True, blue, white), (50, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(str(cset), True, blue, white), (750, 0))
    pygame.display.update()
    if level >= 7:
        addif=numbers
    else:
        addif=digits
    addition(random.choice(addif),random.choice(addif))
def subtract():
    global numbers
    global digits
    display_surface.fill(blue)
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Subtraction", True, blue, white), (50, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render(str(cset), True, blue, white), (750, 0))
    pygame.display.update()
    if level >= 7:
        subdif = numbers
    else:
        subdif= digits
    subtraction(random.choice(subdif),random.choice(subdif))
while True:
    level=correct//60 + 1
    display_surface.fill(blue)
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 60).render("Welcome to UC37 math!", True, blue, white), (50, 0))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("x", True, blue, white), (250, 100))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("÷", True, blue, white), (250, 250))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("+", True, blue, white), (450, 100))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render("−", True, blue, white), (450, 250))
    if level <= 9:
        display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render(str(level), True, blue, white), (750, 310))
    else:
        display_surface.blit(pygame.font.Font('freesansbold.ttf', 100).render(str(level), True, blue, white), (690, 310))
    display_surface.blit(pygame.font.Font('freesansbold.ttf', 35).render("recommended", True, blue, white), (260, 370))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            file1 = open(file_location+"/UC37math/mathdata.py", "w")
            file1.write("correct="+str(correct)+"\nincorrect="+str(incorrect))
            file1.close()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x >=250 and x<= 300 and y >= 100 and y <= 200:
                cset=0
                while True:
                    if cset == 10:
                        break
                    multiply()
            if x >=250 and x<= 300 and y >= 250 and y <= 350:
                cset=0
                while True:
                    if cset == 10:
                        break
                    divide()
            if x >=450 and x<= 500 and y >= 100 and y <= 200:
                cset=0
                while True:
                    if cset == 10:
                        break
                    add()
            if x >=450 and x<= 500 and y >= 250 and y <= 350:
                cset=0
                while True:
                    if cset == 10:
                        break
                    subtract()
            if x >=260 and x<= 500 and y >= 370 and y <= 400:
                if level == 1 or level == 7:
                    cset=0
                    while True:
                        if cset == 10:
                            break
                        subtract()
                elif level == 2 or level == 8:
                    cset=0
                    while True:
                        if cset == 10:
                            break
                        add()
                elif level == 3 or level == 9:
                    cset=0
                    while True:
                        if cset == 10:
                            break
                        adsu=random.choice([1,2])
                        if adsu == 1:
                            add()
                        else:
                            subtract()
                elif level == 4 or level == 10:
                    cset=0
                    while True:
                        if cset ==10:
                            break
                        divide()
                elif level == 5 or level == 11:
                    cset=0
                    while True:
                        if cset == 10:
                            break
                        multiply()
                elif level == 6 or level == 12:
                    cset=0
                    while True:
                        if cset == 10:
                            break
                        mudi=random.choice([1,2])
                        if mudi == 1:
                            multiply()
                        else:
                            divide()
                elif level >= 13:
                    cset=0
                    while True:
                        if cset == 10:
                            break
                        mudias=random.choice([1,2])
                        if mudias == 1:
                            add()
                        elif mudias == 2:
                            subtract()
                        elif mudias == 3:
                            multiply()
                        else:
                            divide()
    pygame.display.update()
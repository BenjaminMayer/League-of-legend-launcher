import pyautogui
import sys
import os
import numpy as np
from  pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as ctrl, Listener
import time


def on_press(key):
    pass

def on_release(key):
    
    if key == Key.esc:
        # Stop listener
        sys.exit()
        return False

path = os.getcwd()
print("path")
path = path + "/Documents/Autoclient"
   
(largeur_pixel,hauteur_pixel) = pyautogui.size()
#dimension = open(path + '/dim.txt', "r")
#contentdim = dimension.read()
#params = contentdim.split('\n')
global largeur
global hauteur
global a
global b
global x2
global y2
global l2
global h2
#largeur = float(params[0])
#hauteur = float(params[1])
#dpil = largeur_pixel/largeur
#dpih = hauteur_pixel/hauteur

#a=dpil/40.42
#b=dpih/40.75

fichier = open('config.txt', "r")
content = fichier.read()



global creator
global name_map
global gameName
global passwordGame
global teamSize
global gameType
global allowSpectator
global mode

parametres = content.split('\n')
creator = parametres[0]
name_map = parametres[1]
nameGame = parametres[2]
passwordGame = parametres[3]
teamSize = parametres[4]
gameType = parametres[5]
allowSpectator = parametres[6]
mode = parametres[7]


if name_map=='1':
    name_map = 'SUMMONER\'s RIFT'
if name_map=='2':
    name_map = 'TWISTED TREELINE'
if name_map=='3':
    name_map= 'HOWLING ABYSS'
mouse = Controller()
keyboard = ctrl()
(larg,long)=pyautogui.size()


#RECONNAISSANCE PATTERN
n=0
while(True):
    if (pyautogui.locateOnScreen("screen.png", grayscale=True, confidence=.8) != None and pyautogui.locateOnScreen("play.png", grayscale=True, confidence=.8) != None and pyautogui.locateOnScreen("scarabe.png", grayscale=True, confidence=.8) != None):
        (x,y,l,h)=pyautogui.locateOnScreen( "screen.png", grayscale=True, confidence=.8)
        (x2,y2,l2,h2)=pyautogui.locateOnScreen("play.png", grayscale=True, confidence=.8)
        (x3,y3,l3,h3)=pyautogui.locateOnScreen("scarabe.png", grayscale=True, confidence=.8)
        a=x-x2
        b=y3-y
        break
    else:
        if(os.name== 'nt'):
            with keyboard.pressed(Key.alt):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                time.sleep(0.2)
                for i in range(n):
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    time.sleep(0.1)
                    if n==10:
                        n=1
        if(os.name=='posix'):
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                time.sleep(0.2)
                for i in range(n):
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    time.sleep(0.1)
                    if n==10:
                        n=1
          
          
    n=n+1
    time.sleep(0.2)
                
#print('YES')
if(x-1100 < 0):
    mouse.position = (x-400,y)
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.position =(x+500,y)
    time.sleep(0.1)
    mouse.release(Button.left)
    x = x+900
    
    
if(y+720 > hauteur_pixel):
    d = y+720-largeur_pixel
    mouse.position = (x-400,y)
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.position =(x-400,y+d-250)
    mouse.release(Button.left)
    y=y+d-250
    
#PLAY DIRECT
def play_direct():
        time.sleep(0.7)
        mouse.position = (x2+0.5*l2,y2+0.5*h2)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

#Create Customer
def create_customer():
    while(True):
        if(pyautogui.locateOnScreen("playgrey.png", grayscale=True, confidence=.8) != None):
            time.sleep(0.05)
            break
    time.sleep(1)
    mouse.position = (x-0.66*a,y+0.13*b)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

#Join Game
def join_game():
    while(True):
        if(pyautogui.locateOnScreen("playgrey.png", grayscale=True, confidence=.8) != None):
            break
    time.sleep(1)
    mouse.position = (x-0.55*a,y+0.13*b)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

#Find Game
def find_game():

        time.sleep(0.5)
        mouse.position = (x-0.885*a,y+0.277*b)
        time.sleep(0.1)
        mouse.click(Button.left,1)
        time.sleep(0.1)
        keyboard.type(nameGame)
        time.sleep(1)
        mouse.position = (x-1.011*a,y+0.408*b)
        time.sleep(0.1)
        mouse.click(Button.left,2)
        time.sleep(2)
        keyboard.type(passwordGame)
        time.sleep(0.5)
        mouse.position=(x-0.498*a,y+0.60*b)
        time.sleep(0.1)
        mouse.click(Button.left,1)

        
#Choice map
def choice_map():
        time.sleep(0.5)
        if name_map == 'SUMMONER\'s RIFT':
            mouse.position = (x-0.84*a,y+0.31*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if name_map == 'TWISTED TREELINE':
            mouse.position = (x-0.58*a,y+0.31*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if name_map == 'HOWLING ABYSS':
            mouse.position = (x-0.29*a,y+0.31*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)

    
#Game type
def game_type():
        time.sleep(0.5)
    
        if gameType=='Blind Pick':
            mouse.position = (x-0.49*a,y+0.651*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if gameType=='Draft Mode':
            mouse.position = (x-0.357*a,y+0.651*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if gameType=='All Random':
            mouse.position = (x-0.214*a,y+0.651*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if gameType=='Tournament Draft':
            mouse.position = (x-0.492*a,y+0.651*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)

            
#Allow Spectator
def allow_spectator():
     
        time.sleep(0.2)
        if allowSpectator=='Lobby Only':
            mouse.position = (x-0.49*a,y+564*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if allowSpectator=='Friend List Only':
            mouse.position = (x-0.357*a,y+564*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if allowSpectator=='All':
            mouse.position = (x-0.214*a,y+564*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        if allowSpectator=='None':
            mouse.position = (x-0.492*a,y+598*b)
            time.sleep(0.1)
            mouse.click(Button.left, 1)

#NAME

def name_game():
        time.sleep(0.2)
    
        mouse.position = (x-0.846*a,y+0.642*b)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        for i in range(1,30):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        keyboard.type(nameGame)

#TEAM SIZE
def team_size():
        mouse.position = (x-0.854*a,y+0.76*b)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        if(name_map=='TWISTED TREELINE'):
            if teamSize=='3':
                
                mouse.position = (x-0.80*a,y+0.92*b)
                time.sleep(0.5)
                mouse.click(Button.left, 1)
            if teamSize=='2':
                
                mouse.position = (x-0.80*a,y+0.86*b)
                time.sleep(0.5)
                mouse.click(Button.left, 1)
            if teamSize=='1':
                
                mouse.position = (x-0.80*a,y+0.811*b)
                time.sleep(0.5)
                mouse.click(Button.left, 1)
        else:    
            if teamSize=='5':
                mouse.position = (x-0.80*a,y+1.002*b)
                time.sleep(0.2)
                mouse.scroll(0,-100)
                time.sleep(0.1)
                mouse.click(Button.left, 1)
            if teamSize=='4':
                mouse.position = (x-0.80*a,y+0.934*b)
                time.sleep(0.2)
                mouse.scroll(0,-100)
                time.sleep(0.1)
                mouse.click(Button.left, 1)
            if teamSize=='3':
                mouse.position = (x-0.80*a,y+0.881*b)
                time.sleep(0.2)
                mouse.scroll(0,-100)
                time.sleep(0.1)
                mouse.click(Button.left, 1)
            if teamSize=='2':
                mouse.position = (x-0.80*a,y+0.836*b)
                time.sleep(0.2)
                mouse.scroll(0,-100)
                time.sleep(0.1)
                mouse.click(Button.left, 1)
            if teamSize=='1':
                mouse.position = (x-0.80*a,y+0.811*b)
                time.sleep(0.2)
                mouse.scroll(0,100)
                time.sleep(0.1)
                mouse.click(Button.left, 1)

#Password
def password_game():
        time.sleep(0.5)
   
        mouse.position = (x-0.868*a,y+0.881*b)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        keyboard.type(passwordGame)
#Confirm
def confirm():
        time.sleep(0.2)
    
        mouse.position = (x-0.545*a,y+0.979*b)
        time.sleep(0.1)
        mouse.click(Button.left, 1)

def complete_game():
        if teamSize=='1':
            time.sleep(2.5)
            a2 = 1000
            while(True):
                time.sleep(0.1)
                im = pyautogui.screenshot(region=(x-0.524*a,y+0.33*b,0.014*a,0.116*b)  )
                im_np=np.array(im)
                
                if(np.sum(im_np)/im_np.size>1+a2):
                    break
                else:
                    a2=np.sum(im_np)/im_np.size
            time.sleep(0.1)         
            mouse.position = (x-0.545*a,y+0.979*b)
            time.sleep(0.1) 
            mouse.click(Button.left, 1)
        if teamSize=='2':
            time.sleep(2.5)
            a2 = 1000
            b2 = 1000
            c=True
            d=True
            while(True):
                time.sleep(0.1)
                if(c==True):
                    im = pyautogui.screenshot(region=(x-0.524*a,y+0.407*b,0.014*a,0.116*b))
                    im_np=np.array(im)
                if(d==True):
                    im2 = pyautogui.screenshot(region=(x-0.967*a,y+0.407*b,0.014*a,0.116*b))
                    im2_np=np.array(im2)
                if(np.sum(im_np)/im_np.size>1+a2):
                    c=False
                if(np.sum(im2_np)/im2_np.size>1+b2):
                    d=False

                if(c==False and d==False):
                    break
                else:
                    a2=np.sum(im_np)/im_np.size
                    b2=np.sum(im2_np)/im2_np.size
            time.sleep(0.1)         
            mouse.position = (x-0.545*a,y+0.979*b)
            time.sleep(0.1) 
            mouse.click(Button.left, 1)
        if teamSize=='3':
            time.sleep(2.5)
            a2 = 1000
            b2 = 1000
            c=True
            d=True
            while(True):
                time.sleep(0.1)
                if(c==True):
                    im = pyautogui.screenshot(region=(x-0.524*a,y+0.4759*b,0.014*a,0.116*b))
                    im_np=np.array(im)
                if(d==True):
                    im2 = pyautogui.screenshot(region=(x-0.967*a,y+0.4759*b,0.014*a,0.116*b))
                    im2_np=np.array(im2)
                if(np.sum(im_np)/im_np.size>1+a2):
                    c=False
                if(np.sum(im2_np)/im2_np.size>1+b2):
                    d=False

                if(c==False and d==False):
                    break
                else:
                    a2=np.sum(im_np)/im_np.size
                    b2=np.sum(im2_np)/im2_np.size
            time.sleep(0.1)        
            mouse.position = (x-0.545*a,y+0.979*b)
            time.sleep(0.1) 
            mouse.click(Button.left, 1)
        if teamSize=='4':
            time.sleep(2.5)
            a2 = 1000
            b2 = 1000
            c=True
            d=True
            while(True):
                time.sleep(0.1)
                if(c==True):
                    im = pyautogui.screenshot(region=(x-0.524*a,y+0.544*b,0.014*a,0.116*b))
                    im_np=np.array(im)
                if(d==True):
                    im2 = pyautogui.screenshot(region=(x-0.967*a,y+0.544*b,0.014*a,0.116*b))
                    im2_np=np.array(im2)
                if(np.sum(im_np)/im_np.size>1+a2):
                    c=False
                if(np.sum(im2_np)/im2_np.size>1+b2):
                    d=False

                if(c==False and d==False):
                    break
                else:
                    a2=np.sum(im_np)/im_np.size
                    b2=np.sum(im2_np)/im2_np.size
            time.sleep(0.1)        
            mouse.position = (x-0.545*a,y+0.979*b)
            time.sleep(0.1) 
            mouse.click(Button.left, 1)
        if teamSize=='5':
            time.sleep(2.5)
            a2 =1000
            b2 =1000
            c=True
            d=True
            while(True):
                time.sleep(0.1)
                if(c==True):
                    im = pyautogui.screenshot(region=(x-0.524*a,y+0.613*b,0.014*a,0.116*b))
                    im_np=np.array(im)
                if(d==True):
                    im2 = pyautogui.screenshot(region=(x-0.967*a,y+0.613*b,0.014*a,0.116*b))
                    im2_np=np.array(im2)
                if(np.sum(im_np)/im_np.size>1+a2):
                    c=False
                if(np.sum(im2_np)/im2_np.size>1+b2):
                    d=False

                if(c==False and d==False):
                    break
                else:
                    a2=np.sum(im_np)/im_np.size
                    b2=np.sum(im2_np)/im2_np.size
            time.sleep(0.1)        
            mouse.position = (x-0.545*a,y+0.979*b)
            time.sleep(0.1) 
            mouse.click(Button.left, 1)
    
        
        

def createAGame():
    play_direct()
    a=1
    b=1
    create_customer()
    choice_map()
    game_type()
    allow_spectator()
    name_game()
    team_size()
    password_game()
    confirm()
    complete_game()
def joinAGame():
    
    play_direct()
    join_game()
    find_game()
    
if creator=='1':
        createAGame()
if creator=='2':
        joinAGame()

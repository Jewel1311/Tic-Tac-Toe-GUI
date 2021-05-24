import pygame ,sys,time
from pygame import mixer
from pygame.locals import *
pygame.init()
width,height=300,300
FPS=60
white=(255,255,255)
blue=(0,0,255)
tblue=(0,0,0,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
gray=(128,128,128)
silver=(192, 192, 192)
aqua=(0,255,255)
var=False
xwins=0
owins=0
tie=0
WIN=pygame.display.set_mode((width,height))
pygame.display.set_caption('TIC-TAC-TOE')
clock=pygame.time.Clock()
dict={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

#print X wins
fontObj = pygame.font.Font('freesansbold.ttf', 70)
textSurfaceObj = fontObj.render('X  WINS', True, green,black)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (150,150)

#print O wins
fontObj=pygame.font.Font('freesansbold.ttf', 70)
textSurface=fontObj.render('O  WINS', True, green,black)
textRectObj=textSurface.get_rect()
textRectObj.center=(150,150)

#print tie
fontObj = pygame.font.Font('freesansbold.ttf', 70)
text=fontObj.render('TIE', True, green,black)
textRect=text.get_rect()
textRect.center = (150,150)


def X_Wins():
     global xwins
     xwins=1
     mixer.music.load('sound/tone1.mp3')
     mixer.music.play()

def O_Wins():
     global owins
     owins=1
     mixer.music.load('sound/tone1.mp3')
     mixer.music.play()

def Tie():
     global tie
     tie=1
     mixer.music.load('sound/tone2.mp3')
     mixer.music.play()


#create background
def create_background():
    pygame.draw.line(WIN,gray,(0,100),(300,100),5)
    pygame.draw.line(WIN,gray,(0,200),(300,200),5)
    pygame.draw.line(WIN,gray,(200,0),(200,300),5)
    pygame.draw.line(WIN,gray,(100,0),(100,300),5)

#check who wins and draw a line

def check():
    global t
    global xwins
    global owins
    if dict[1]==dict[2]==dict[3] and dict[1]==dict[2]==dict[3]!=' ' :
        pygame.draw.line(WIN,aqua,(20,45),(280,45),10)
        if dict[2]==1:
            X_Wins()
        else:
            O_Wins()
    if dict[4]==dict[5]==dict[6] and dict[4]==dict[5]==dict[6]!=' ':
        pygame.draw.line(WIN,aqua,(20,148),(275,148),10)
        if dict[5]==1:
            X_Wins()
        else:
            O_Wins()
    if dict[7]==dict[8]==dict[9] and dict[7]==dict[8]==dict[9]!=' ':
        pygame.draw.line(WIN,aqua,(20,250),(275,250),10)
        if dict[8]==1:
            X_Wins()
        else:
            O_Wins()
    if dict[1]==dict[4]==dict[7] and dict[1]==dict[4]==dict[7]!=' ':
        pygame.draw.line(WIN,aqua,(45,20),(45,275),10)
        if dict[4]==1:
            X_Wins()
        else:
            O_Wins()
    if dict[2]==dict[5]==dict[8] and dict[2]==dict[5]==dict[8]!=' ':
        pygame.draw.line(WIN,aqua,(150,20),(150,275),10)
        if dict[5]==1:
            X_Wins()
        else:
            O_Wins()
    if dict[3]==dict[6]==dict[9] and dict[3]==dict[6]==dict[9]!=' ':
        pygame.draw.line(WIN,aqua,(250,20),(250,275),10)
        if dict[6]==1:
            X_Wins()
        else:
            O_Wins()
    if dict[3]==dict[5]==dict[7] and dict[3]==dict[5]==dict[7]!=' ':
        pygame.draw.line(WIN,aqua,(275,20),(20,275),10)
        if dict[5]==1:
            X_Wins()
        else:
            O_Wins()
    if dict[1]==dict[5]==dict[9] and dict[1]==dict[5]==dict[9]!=' ':
        pygame.draw.line(WIN,aqua,(20,20),(275,275),10)
        if dict[5]==1:
            X_Wins()
        else:
            O_Wins()
    if t==9 and xwins==0 and owins==0:
        Tie()

#drawing symbols by checking dict[] is 1 or 2
t=0
def draw():
    global t
    t+=1
    if dict[1]==1:
        pygame.draw.line(WIN,blue,(20,20),(70,70),10)
        pygame.draw.line(WIN,blue,(70,20),(20,70),10)
        check()
    elif dict[1]==2:
        pygame.draw.ellipse(WIN,red,(30,20, 40,50),7)
        check()
    if dict[2]==1:
        pygame.draw.line(WIN,blue,(125,20),(175,70),10)
        pygame.draw.line(WIN,blue,(175,20),(125,70),10)
        check()
    elif dict[2]==2:
        pygame.draw.ellipse(WIN,red,(130,20,40,50),7)
        check()
    if dict[3]==1:
        pygame.draw.line(WIN,blue,(225,20),(275,70),10)
        pygame.draw.line(WIN,blue,(275,20),(225,70),10)
        check()
    elif dict[3]==2:
        pygame.draw.ellipse(WIN,red,(230,20,40,50),7)
        check()
    if dict[4]==1:
        pygame.draw.line(WIN,blue,(20,125),(70,175),10)
        pygame.draw.line(WIN,blue,(70,125),(20,175),10)
        check()
    elif dict[4]==2:
        pygame.draw.ellipse(WIN,red,(30,125, 40,50),7)
        check()
    if dict[5]==1:
        pygame.draw.line(WIN,blue,(125,125),(175,175),10)
        pygame.draw.line(WIN,blue,(175,125),(125,175),10)
        check()
    elif dict[5]==2:
        pygame.draw.ellipse(WIN,red,(130,125, 40,50),7)
        check()
    if dict[6]==1:
        pygame.draw.line(WIN,blue,(225,125),(275,175),10)
        pygame.draw.line(WIN,blue,(275,125),(225,175),10)
        check()
    elif dict[6]==2:
        pygame.draw.ellipse(WIN,red,(230,125, 40,50),7)
        check()
    if dict[7]==1:
        pygame.draw.line(WIN,blue,(20,225),(70,275),10)
        pygame.draw.line(WIN,blue,(70,225),(20,275),10)
        check()
    elif dict[7]==2:
        pygame.draw.ellipse(WIN,red,(30,225, 40,50),7)
        check()
    if dict[8]==1:
        pygame.draw.line(WIN,blue,(125,225),(175,275),10)
        pygame.draw.line(WIN,blue,(175,225),(125,275),10)
        check()
    elif dict[8]==2:
        pygame.draw.ellipse(WIN,red,(130,225, 40,50),7)
        check()
    if dict[9]==1:
        pygame.draw.line(WIN,blue,(225,225),(275,275),10)
        pygame.draw.line(WIN,blue,(275,225),(225,275),10)
        check()
    elif dict[9]==2:
        pygame.draw.ellipse(WIN,red,(230,225, 40,50),7)
        check()

#assigning values to dict[]=1 for player X
def player_X(row,col):
    if row==0 and col==0:
      if dict[1]==' ':
       dict[1]=1
       draw()
    elif row==0 and col==1:
      if dict[2]==' ':
       dict[2]=1
       draw()
    elif row==0 and col==2:
      if dict[3]==' ':
       dict[3]=1
       draw()
    elif row==1 and col==0:
      if dict[4]==' ':
       dict[4]=1
       draw()
    elif row==1 and col==1:
      if dict[5]==' ':
       dict[5]=1
       draw()
    elif row==1 and col==2:
      if dict[6]==' ':
       dict[6]=1
       draw()
    elif row==2 and col==0:
      if dict[7]==' ':
       dict[7]=1
       draw()
    elif row==2 and col==1:
      if dict[8]==' ':
       dict[8]=1
       draw()
    elif row==2 and col==2:
      if dict[9]==' ':
       dict[9]=1
       draw()

#assigning values to dict[]=2 for player O
def player_O(row,col):
    if row==0 and col==0:
      if dict[1]==' ':
       dict[1]=2
       draw()
    elif row==0 and col==1:
      if dict[2]==' ':
       dict[2]=2
       draw()
    elif row==0 and col==2:
      if dict[3]==' ':
       dict[3]=2
       draw()
    elif row==1 and col==0:
      if dict[4]==' ':
       dict[4]=2
       draw()
    elif row==1 and col==1:
      if dict[5]==' ':
       dict[5]=2
       draw()
    elif row==1 and col==2:
      if dict[6]==' ':
       dict[6]=2
       draw()
    elif row==2 and col==0:
      if dict[7]==' ':
       dict[7]=2
       draw()
    elif row==2 and col==1:
      if dict[8]==' ':
       dict[8]=2
       draw()
    elif row==2 and col==2:
      if dict[9]==' ':
       dict[9]=2
       draw()

#main function
def main():
 i=1
 WIN.fill(silver)
 create_background()
 run=True
 while run:
   for event in pygame.event.get():
         if event.type==pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type==pygame.MOUSEBUTTONDOWN:
                 mouseX=event.pos[0]
                 mouseY=event.pos[1]
                 clicked_row=int(mouseY // 100)
                 clicked_col=int(mouseX // 100)
                #giving players alternate chance
                 if i<=9:
                  if i%2==0:
                   player_O(clicked_row,clicked_col)
                  else:
                   player_X(clicked_row,clicked_col)
                  i+=1
   #display message win,lose or tie
   if xwins==1:
        WIN.blit(textSurfaceObj, textRectObj)
   if owins==1:
        WIN.blit(textSurface, textRectObj)
   if tie==1:
        WIN.blit(text, textRect)

   pygame.display.update()
   clock.tick(FPS)
main()

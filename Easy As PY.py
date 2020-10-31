#Daksh Malhotra
#https://github.com/DakshChan

import pygame
from math import *
pygame.init()
WIDTH = 1000
HEIGHT= 450
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Easy As PY')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (100,100,100)
mousePos = (0,0)
mouseLeftClick = False
mouseRightClick = False
shapes = []
shapesExport = []
points = []
font = pygame.font.SysFont("Impact",30)
font2 = pygame.font.SysFont("Impact",15)
colourInput = '0,0,0'
colour = (0,0,0)
thicknessInput = '0'
thickness = 0
screenFill = (255,255,255)

def drawUI():
    pygame.draw.rect(screen,BLACK,(0,0,200,450))
    graphics = font.render('Easy As PY',1,WHITE)
    screen.blit(graphics,(50,20))
    pygame.draw.rect(screen,GREY,(40,80,125,60))
    graphics = font.render('POLYGON',1,WHITE)
    screen.blit(graphics,(50,90))
    pygame.draw.rect(screen,GREY,(40,160,125,60))
    graphics = font.render('CIRCLE',1,WHITE)
    screen.blit(graphics,(50,170))
    pygame.draw.rect(screen,GREY,(50,400,100,30))
    graphics = font2.render('Thickness',1,WHITE)
    screen.blit(graphics,(50,380))
    graphics = font2.render(thicknessInput,1,WHITE)
    screen.blit(graphics,(55,405))
    pygame.draw.rect(screen,GREY,(50,350,100,30))
    graphics = font2.render('Colour',1,WHITE)
    screen.blit(graphics,(50,330))
    graphics = font2.render(colourInput,1,WHITE)
    screen.blit(graphics,(55,355))
    pygame.draw.rect(screen,WHITE,(18,349,32,32))
    pygame.draw.rect(screen,colour,(19,350,30,30))
    pygame.draw.rect(screen,GREY,(50,300,100,30))
    graphics = font2.render('Screen Fill',1,WHITE)
    screen.blit(graphics,(60,305))
    #pygame.display.update()

def drawPoints():
    if len(points) != 0:
        for i in range(0,len(points)):
            pygame.draw.circle(screen,BLACK,(points[i]),2)
            pygame.draw.circle(screen,RED,(points[i]),1)

def drawShapes():
    if len(shapes) != 0:
        for i in range(0,len(shapes)):
            eval(shapes[i])

while True:
    screen.fill(BLACK)
    pygame.draw.rect(screen,screenFill,(200,0,800,450))
    drawShapes()
    drawPoints()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseLeftClick = True
            if event.button == 3:
                mouseRightClick = True
        if event.type == pygame.KEYDOWN and mousePos[0] in range(50,150) and mousePos[1] in range(350,380):
            if event.key == pygame.K_0:
                colourInput += '0'
            if event.key == pygame.K_1:
                colourInput += '1'
            if event.key == pygame.K_2:
                colourInput += '2'
            if event.key == pygame.K_3:
                colourInput += '3'
            if event.key == pygame.K_4:
                colourInput += '4'
            if event.key == pygame.K_5:
                colourInput += '5'
            if event.key == pygame.K_6:
                colourInput += '6'
            if event.key == pygame.K_7:
                colourInput += '7'
            if event.key == pygame.K_8:
                colourInput += '8'
            if event.key == pygame.K_9:
                colourInput += '9'
            if event.key == pygame.K_COMMA:
                colourInput += ','
            if event.key == pygame.K_BACKSPACE:
                if len(colourInput)!= 0:
                    colourInput = colourInput[0:len(colourInput)-1]
        if event.type == pygame.KEYDOWN and mousePos[0] in range(50,150) and mousePos[1] in range(400,430):
            if event.key == pygame.K_0:
                thicknessInput += '0'
            if event.key == pygame.K_1:
                thicknessInput += '1'
            if event.key == pygame.K_2:
                thicknessInput += '2'
            if event.key == pygame.K_3:
                thicknessInput += '3'
            if event.key == pygame.K_4:
                thicknessInput += '4'
            if event.key == pygame.K_5:
                thicknessInput += '5'
            if event.key == pygame.K_6:
                thicknessInput += '6'
            if event.key == pygame.K_7:
                thicknessInput += '7'
            if event.key == pygame.K_8:
                thicknessInput += '8'
            if event.key == pygame.K_9:
                thicknessInput += '9'
            if event.key == pygame.K_BACKSPACE:
                if len(thicknessInput)!= 0:
                    thicknessInput = thicknessInput[0:len(thicknessInput)-1]
        if event.type == pygame.KEYDOWN and mousePos[0] in range(200,1000) and mousePos[1] in range(0,450):
            if event.key == pygame.K_BACKSPACE:
                if len(shapes)> 0:
                    shapes.pop()
                    shapesExport.pop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if len(shapesExport) == 0:
                    pygame.quit()
                else:
                    f = open('export.py', 'w')
                    f.write('#Daksh Malhotra\n')
                    f.write('#https://github.com/DakshChan\n')
                    f.write('import pygame\n')
                    f.write('pygame.init()\n')
                    f.write('screen=pygame.display.set_mode((800,450))\n')
                    f.write('')
                    f.write('#drawing shapes\n')
                    f.write('screen.fill('+str(screenFill)+')\n')
                    for i in range(len(shapesExport)):
                        f.write(shapesExport[i]+'\n')
                    f.write('')
                    f.write('pygame.display.update()\n')
                    f.write('')
                    f.write('# if Esc key pressed exit\n')
                    f.write('while True:\n')
                    f.write('   for event in pygame.event.get():\n')
                    f.write('       if event.type == pygame.KEYDOWN:\n')
                    f.write('           if event.key == pygame.K_ESCAPE:\n')
                    f.write('               pygame.quit()\n')
                    f.close()
                    pygame.quit()
    if mousePos[0] in range(200,1001) and mousePos[1] in range(0,451):
        pygame.draw.line(screen,BLACK,(mousePos[0],0),(mousePos[0],HEIGHT),4)
        pygame.draw.line(screen,RED,(mousePos[0],0),(mousePos[0],HEIGHT),2)
        pygame.draw.line(screen,BLACK,(200,mousePos[1]),(WIDTH,mousePos[1]),4)
        pygame.draw.line(screen,RED,(200,mousePos[1]),(WIDTH,mousePos[1]),2)
        if mouseLeftClick == True:
            points.append([mousePos[0],mousePos[1]])
        if mouseRightClick == True:
            if len(points) != 0:
                points.pop()
        graphics = font2.render('('+str(mousePos[0]-200)+','+str(mousePos[1])+')',1,WHITE)
        screen.blit(graphics,(125,5))
        if len(points) >= 1:
            pygame.draw.line(screen,BLACK,points[len(points)-1],mousePos,4)
            pygame.draw.line(screen,RED,points[len(points)-1],mousePos,2)
    if len(points) > 1:
        for i in range(len(points)-1):
            pygame.draw.line(screen,BLACK,points[i],points[i+1],4)
            pygame.draw.line(screen,RED,points[i],points[i+1],2)
    if mousePos[0] in range(40,165) and mousePos[1] in range(80,140) and len(points)>= 2 and mouseLeftClick == True:
        if len(points) == 2:
            if thickness < 1:
                thickness = 1
            shapes.append('pygame.draw.line(screen,'+str(colour)+',('+str(points[0][0])+','+str(points[0][1])+'),('+str(points[1][0])+','+str(points[1][1])+'),'+str(thickness)+')')
            for i in range(0,len(points)):
                points[i][0] -= 200
            shapesExport.append('pygame.draw.line(screen,'+str(colour)+',('+str(points[0][0])+','+str(points[0][1])+'),('+str(points[1][0])+','+str(points[1][1])+'),'+str(thickness)+')')
            points = []
        else:
            shapesTemp = 'pygame.draw.polygon(screen,'+str(colour)+',('
            for i in range(0,len(points)):
                shapesTemp += '('+str(points[i][0])+','+str(points[i][1])+'),'
            shapesTemp = shapesTemp[0:len(shapesTemp)-1]
            shapesTemp += '),'+str(thickness)+')'
            shapes.append(shapesTemp)
            for i in range(0,len(points)):
                points[i][0] -= 200
            shapesTemp = 'pygame.draw.polygon(screen,'+str(colour)+',('
            for i in range(0,len(points)):
                shapesTemp += '('+str(points[i][0])+','+str(points[i][1])+'),'
            shapesTemp = shapesTemp[0:len(shapesTemp)-1]
            shapesTemp += '),'+str(thickness)+')'
            shapesExport.append(shapesTemp)
            points = []
    if mousePos[0] in range(40,165) and mousePos[1] in range(160,220) and len(points) == 2 and mouseLeftClick == True:
        radius = int(sqrt(((points[0][0]-points[1][0])**2)+((points[0][1]-points[1][1])**2)))
        shapes.append('pygame.draw.circle(screen,'+str(colour)+',('+str(points[0][0])+','+str(points[0][1])+'),'+str(radius)+','+str(thickness)+')')
        for i in range(0,len(points)):
            points[i][0] -= 200
        shapesExport.append('pygame.draw.circle(screen,'+str(colour)+',('+str(points[0][0])+','+str(points[0][1])+'),'+str(radius)+','+str(thickness)+')')
        points = []
    if mousePos[0] in range(50,150) and mousePos[1] in range(300,330) and mouseLeftClick == True:
        screenFill = colour
    if thicknessInput != '':
        if eval(thicknessInput)<= 100000:
            thickness = eval(thicknessInput)
    if colourInput != '':
        colourTemp = []
        colourTemp2 = ''
        for i in colourInput:
            if i != ',':
                colourTemp2 += i
            else:
                colourTemp.append(colourTemp2)
                colourTemp2 = ''
        colourTemp.append(colourTemp2)
        if len(colourTemp) == 3 and colourTemp[0] != '' and colourTemp[1] != '' and colourTemp[2] != '':
            colourTemp[0] = eval(colourTemp[0])
            colourTemp[1] = eval(colourTemp[1])
            colourTemp[2] = eval(colourTemp[2])
            if colourTemp[0] in range(0,256) and colourTemp[1] in range(0,256) and colourTemp[2] in range(0,256):
                colour = colourTemp
    drawUI()
    pygame.display.update()
    mouseLeftClick = False
    mouseRightClick = False
    pygame.time.delay(30)

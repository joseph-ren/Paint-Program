#Joseph Ren #Joseph Ren - Paint Project.py #basic paint program with colour palette to choose colours. User draws and stamps items on the white canvas. Default tool is pencil.
                                           #Other stencils include spray paint, brush, and eraser tool. You can draw ellipses and rectangles, both filled and unfilled, along with the line tool.
                                           #You can also stamp from 6 of the images, where you click and then stamp your picture onto the canvas. Choosing background images will clear the entire
                                           #and replace it with the chosen background. User can open pictures from their files, and save their canvas.
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog
font.init()
root=Tk()
root.withdraw()
spaceFont=font.Font("EdgeOfTheGalaxyRegular.otf", 18)
titleFont=font.Font("EdgeOfTheGalaxyRegular.otf", 48)
screen=display.set_mode((800, 600))
#images
space=image.load("space.jpg")
blackHole=image.load("blackHole.png")
blackHoleStamped=image.load("blackHoleStamped.png")
galaxy=image.load("galaxy.png")
galaxyStamped=image.load("galaxyStamped.png")
meteor=image.load("meteor.png")
meteorStamped=image.load("meteorStamped.png")
moon=image.load("moon.png")
moonStamped=image.load("moonStamped.png")
saturn=image.load("saturn.png")
saturnStamped=image.load("saturnStamped.png")
star=image.load("star.png")
starStamped=image.load("starStamped.png")
earthBackground=image.load("earthBackground.jpg")
mars=image.load("mars.jpg")
stars=image.load("stars.jpg")
earthBackgroundCanvas=image.load("earthBackground1.jpg")
marsCanvas=image.load("mars1.jpg")
starsCanvas=image.load("stars1.jpg")
palette=image.load("palette.jpg")
pencil=image.load("pencil.png")
brush=image.load("brush.png")
sprayPaint=image.load("sprayPaint.png")
eraser=image.load("eraser.png")
save=image.load("save.png")
Open=image.load("open.png")
ellipse=image.load("ellipse.png")
ellipseFilled=image.load("ellipseFilled.png")
rect=image.load("rect.png")
rectFilled=image.load("rectFilled.png")
line=image.load("line.png")
#button positions
canvas=Rect(145, 60, 510, 500)
blackHoleButton=Rect(20, 60, 50, 50)
meteorButton=Rect(75, 60, 50, 50)
galaxyButton=Rect(20, 115, 50, 50)
moonButton=Rect(75, 115, 50, 50)
saturnButton=Rect(20, 170, 50, 50)
starButton=Rect(75, 170, 50, 50)
clearButton=Rect(600, 565, 55, 25)
earthBackgroundButton=Rect(675, 400, 105, 50)
marsButton=Rect(675, 455, 105, 50)
starsButton=Rect(675, 510, 105, 50)
paletteArea=Rect(675, 104, 105, 136)
colourBox=Rect(675, 245, 105, 30) #shows current colour
pencilButton=Rect(675, 285, 50, 50)
sprayPaintButton=Rect(675, 340, 50, 50)
brushButton=Rect(730, 285, 50, 50)
eraserButton=Rect(730, 340, 50, 50)
saveButton=Rect(195, 15, 35, 35)
openButton=Rect(150, 15, 35, 35)
lineButton=Rect(20, 400, 50, 50)
ellipseButton=Rect(20, 455, 50, 50)
ellipseFilledButton=Rect(75, 455, 50, 50)
rectButton=Rect(20, 510, 50, 50)
rectFilledButton=Rect(75, 510, 50, 50)
#default colour positions
red=Rect(675, 60, 17, 17)
orange=Rect(697, 60, 17, 17)
yellow=Rect(719, 60, 17, 17)
green=Rect(741, 60, 17, 17)
blue=Rect(763, 60, 17, 17)
purple=Rect(675, 82, 17, 17)
pink=Rect(697, 82, 17, 17)
black=Rect(719, 82, 17, 17)
white=Rect(741, 82, 17, 17)
gray=Rect(763, 82, 17, 17)
#default items
selectedTool="default pencil" #default tool
col=(0, 0, 0) #default stencil/shape colour
sticker=None #no default sticker
clear=spaceFont.render("Clear", True, (255, 255, 255)) #text for clear button
title=titleFont.render("Astronomical Art", True, (255, 255, 255)) #title text
screen.blit(space, (0, 0)) #space background
draw.rect(screen, (255, 255, 255), canvas) #canvas
display.set_caption("Astronomical Art") #default program title
#light blue background for stickers
draw.rect(screen, (153, 217, 234), blackHoleButton)
draw.rect(screen, (153, 217, 234), meteorButton)
draw.rect(screen, (153, 217, 234), galaxyButton)
draw.rect(screen, (153, 217, 234), moonButton)
draw.rect(screen, (153, 217, 234), saturnButton)
draw.rect(screen, (153, 217, 234), starButton)

def stickers(button, stickerType): #changes sticker variable when a sticker is clicked
    draw.rect(screen, (200, 50, 40), button, 1) #hover outline
    if mb[0]:
        global selectedTool
        selectedTool=None
        global sticker
        sticker=stickerType
def tools(button, tool, position): #changes tool variable when a tool clicked
    draw.rect(screen, (200, 50, 40), button, 1)
    if mb[0]:
        global selectedTool
        selectedTool=tool
def colours(colour, button): #changes colour
     draw.rect(screen, (200, 50, 40), button, 1)
     if mb[0]:
         global col
         col=colour
def HighlightedTool(pos): #highlights the selected tool
    selected=Surface((50, 50), SRCALPHA)
    draw.rect(selected, (255, 0, 0, 150), (0, 0, 50, 50))
    screen.blit(selected, (pos))
def HighlightedColour(pos): #highlights the selected colour
    selected=Surface((50, 50), SRCALPHA)
    draw.rect(selected, (150, 150, 150, 200), (0, 0, 17, 17))
    screen.blit(selected, (pos))
def selectedSticker(pos): #shows selected sticker by "removing" it from box until pasted onto canvas
    selectedTool=None
    draw.rect(screen, (153, 217, 234), pos)
def shapes(shape): #draws shapes
    screen.blit(backgroundRefresh, (0, 0))
    loc=Rect(sx, sy, mx-sx, my-sy)#shape location
    loc.normalize()
    if shape=="line":
        draw.line(screen, (col), (sx, sy), (mx, my), 5)
    if shape=="ellipse":
        draw.ellipse(screen, (col), loc, 2)
    if selectedTool=="filled ellipse":
        draw.ellipse(screen, (col), loc)
    if selectedTool=="rectangle":
        draw.rect(screen, (col), loc, 2)
    if selectedTool=="filled rectangle":
        draw.rect(screen, (col), loc)
def canvasFill(button, background ): #fills/clears canvas
    draw.rect(screen, (200, 50, 40), button, 1)
    if mb[0]:
        draw.rect(screen, (200, 50, 40, 0), button)
        if button==clearButton:
            draw.rect(screen, (255, 255, 255), canvas)
        else:
            screen.blit(background, (145, 60))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            sx, sy=e.pos
            backgroundRefresh=screen.copy()
    mx, my=mouse.get_pos()
    mb=mouse.get_pressed()

    #image/button display
    screen.blit(blackHole, (25, 65))
    screen.blit(galaxy, (25, 120))
    screen.blit(saturn, (25, 175))
    screen.blit(meteor, (83, 62))
    screen.blit(moon, (81, 120))
    screen.blit(star, (81, 175))
    screen.blit(earthBackground, (675, 400))
    screen.blit(mars, (675, 455))
    screen.blit(stars, (675, 510))
    draw.rect(screen, (111, 111, 111), clearButton)
    draw.rect(screen, (111, 111, 111), (145, 565, 100, 25))
    screen.blit(clear, (611, 569))
    screen.blit(title, (247, 7))
    screen.blit(palette, (675, 104))
    screen.blit(pencil, (675, 285))
    screen.blit(sprayPaint, (675, 340))
    screen.blit(brush, (730, 285))
    screen.blit(eraser, (730, 340))
    screen.blit(save, (195, 15))
    screen.blit(Open, (150, 15))
    screen.blit(line, (20, 400))
    screen.blit(ellipse, (20, 455))
    screen.blit(rect, (20, 510))
    screen.blit(ellipseFilled, (75, 455))
    screen.blit(rectFilled, (75, 510))

    #colour button display with outlines
    draw.rect(screen, (255, 0, 0), red)
    draw.rect(screen, (255, 128, 0), orange)
    draw.rect(screen, (255, 255, 0), yellow)
    draw.rect(screen, (0, 255, 0), green)
    draw.rect(screen, (0, 0, 255), blue)
    draw.rect(screen, (128, 0, 128), purple)
    draw.rect(screen, (255, 110, 180), pink)
    draw.rect(screen, (0), black)
    draw.rect(screen, (255, 255, 255), white)
    draw.rect(screen, (150, 150, 150), gray)
    draw.rect(screen, (255, 255, 255), red, 1)
    draw.rect(screen, (255, 255, 255), orange, 1)
    draw.rect(screen, (255, 255, 255), yellow, 1)
    draw.rect(screen, (255, 255, 255), green, 1)
    draw.rect(screen, (255, 255, 255), blue, 1)
    draw.rect(screen, (255, 255, 255), purple, 1)
    draw.rect(screen, (255, 255, 255), pink, 1)
    draw.rect(screen, (255, 255, 255), black, 1)
    draw.rect(screen, (255, 255, 255), white, 1)
    draw.rect(screen, (255, 255, 255), gray, 1)
    draw.rect(screen, (col), colourBox)
    draw.rect(screen, (255, 255, 255), colourBox, 1)
    
    #default outlines
    draw.rect(screen, (255, 255, 255), blackHoleButton, 1)
    draw.rect(screen, (255, 255, 255), meteorButton, 1)
    draw.rect(screen, (255, 255, 255), galaxyButton, 1)
    draw.rect(screen, (255, 255, 255), moonButton, 1)
    draw.rect(screen, (255, 255, 255), saturnButton, 1)
    draw.rect(screen, (255, 255, 255), starButton, 1)
    draw.rect(screen, (255, 255, 255), clearButton, 1)
    draw.rect(screen, (255, 255, 255), earthBackgroundButton, 1)
    draw.rect(screen, (255, 255, 255), marsButton, 1)
    draw.rect(screen, (255, 255, 255), starsButton, 1)
    draw.rect(screen, (255, 255, 255), paletteArea, 1)
    draw.rect(screen, (255, 255, 255), pencilButton, 1)
    draw.rect(screen, (255, 255, 255), sprayPaintButton, 1)
    draw.rect(screen, (255, 255, 255), brushButton, 1)
    draw.rect(screen, (255, 255, 255), eraserButton, 1)
    draw.rect(screen, (255, 255, 255), saveButton, 1)
    draw.rect(screen, (255, 255, 255), openButton, 1)
    draw.rect(screen, (255, 255, 255), lineButton, 1)
    draw.rect(screen, (255, 255, 255), ellipseButton, 1)
    draw.rect(screen, (255, 255, 255), ellipseFilledButton, 1)
    draw.rect(screen, (255, 255, 255), rectButton, 1)
    draw.rect(screen, (255, 255, 255), rectFilledButton, 1)
    
    #choosing colour
    if paletteArea.collidepoint(mx, my) and mb[0]:
        col=screen.get_at((mx, my))
    if red.collidepoint(mx, my):
        colours((255, 0, 0), red)
    if orange.collidepoint(mx, my):
        colours((255, 128, 0), orange)
    if yellow.collidepoint(mx, my):
        colours((255, 255, 0), yellow)
    if green.collidepoint(mx, my):
        colours((0, 255, 0), green)
    if blue.collidepoint(mx, my):
        colours((0, 0, 255), blue)
    if purple.collidepoint(mx, my):
        colours((128, 0, 128), purple)
    if pink.collidepoint(mx, my):
        colours((255, 110, 180), pink)
    if black.collidepoint(mx, my):
        colours((0), black)
    if white.collidepoint(mx, my):
        colours((255, 255, 255), white)
    if gray.collidepoint(mx, my):
        colours((150, 150, 150), gray)

    #highlighting selected colour
    if col==(255, 0, 0):
        HighlightedColour((675, 60))
    if col==(255, 128, 0):
        HighlightedColour((697, 60))
    if col==(255, 255, 0):
        HighlightedColour((719, 60))
    if col==(0, 255, 0):
        HighlightedColour((741, 60))
    if col==(0, 0, 255):
        HighlightedColour((763, 60))
    if col==(128, 0, 128):
        HighlightedColour((675, 82))
    if col==(255, 110, 180):
        HighlightedColour((697, 82))
    if col==(0):
        HighlightedColour((719, 82))
    if col==(255, 255, 255):
        HighlightedColour((741, 82))
    if col==(150, 150, 150):
        HighlightedColour((763, 82))

    #stencil and shape tools
    if pencilButton.collidepoint(mx, my):
        tools(pencilButton, "pencil", (675, 285))
    if sprayPaintButton.collidepoint(mx, my):
        tools(sprayPaintButton, "spray paint", (675, 340))
    if brushButton.collidepoint(mx, my):
        tools(brushButton, "brush", (730, 285))
    if eraserButton.collidepoint(mx, my):
        tools(eraserButton, "eraser", (730, 340))
    if lineButton.collidepoint(mx, my):
        tools(lineButton, "line", (20, 400))
    if ellipseButton.collidepoint(mx, my):
        tools(ellipseButton, "ellipse", (20, 455))
    if ellipseFilledButton.collidepoint(mx, my):
        tools(ellipseFilledButton, "filled ellipse", (75, 455))
    if rectButton.collidepoint(mx, my):
        tools(rectButton, "rectangle", (20, 510))
    if rectFilledButton.collidepoint(mx, my):
        tools(rectFilledButton, "filled rectangle", (75, 510))

    #drawing/stamping on canvas
    if canvas.collidepoint(mx, my):
        mouseLoc=spaceFont.render(str(mx)+", "+str(my), True, (255, 255, 255)) #pixel of mouse location
        screen.blit(mouseLoc, (169, 570))
        if mb[0]:
            screen.set_clip(canvas)
            display.set_caption("Astronomical Art")
            if selectedTool=="line":
                shapes(selectedTool)
            if selectedTool=="ellipse":
                shapes(selectedTool)
            if selectedTool=="filled ellipse":
                shapes(selectedTool)
            if selectedTool=="rectangle":
                shapes(selectedTool)
            if selectedTool=="filled rectangle":
                shapes(selectedTool)
            if selectedTool=="pencil" or selectedTool=="default pencil":
                draw.line(screen, (col), (omx, omy), (mx, my), 2)
            if selectedTool=="spray paint":
                for i in range(2):
                    spot=(randint(mx-4, mx+4), randint(my-4, my+4))
                    if dist(spot, (mx, my))<=5:
                        draw.circle(screen, (col), (spot), 1)
            if selectedTool=="brush":
                col=col[:3]+(20,)
                brushOnCanvas=Surface((60, 60), SRCALPHA)
                distance=dist((omx, omy), (mx, my)) #distance of (omx, omy) to (mx, my)
                for i in range(int(distance)):
                    brushX=mx-omx #change in x
                    brushY=my-omy #change in y
                    amountX=i*brushX//distance #amount added to each point between brushX
                    amountY=i*brushY//distance #amount added to each point between brushY
                    newX=omx+amountX #new x coordinate
                    newY=omy+amountY #new y coordinate
                    draw.circle(brushOnCanvas, (col), (30, 30), 10)
                    screen.blit(brushOnCanvas, (newX-30, newY-30))
                col=col[:3]
            if selectedTool=="eraser":
                draw.line(screen, (255, 255, 255), (omx, omy), (mx, my), 20)
            if sticker!=None:
                selectedTool=None
                if sticker==blackHoleStamped or sticker==galaxyStamped or sticker==moonStamped or sticker==saturnStamped:
                    screen.blit(sticker, (mx-75, my-75))
                elif sticker==meteorStamped:
                    screen.blit(sticker, (mx-50, my-50))
                else:
                    screen.blit(sticker, (mx-35, my-35))
                sticker=None
            screen.set_clip(None)
    omx, omy=mx, my
    
    #highlighting clicked tool buttons
    if selectedTool=="line":
        HighlightedTool((20, 400))
    if selectedTool=="ellipse":
        HighlightedTool((20, 455))
    if selectedTool=="filled ellipse":
        HighlightedTool((75, 455))
    if selectedTool=="rectangle":
        HighlightedTool((20, 510))
    if selectedTool=="filled rectangle":
        HighlightedTool((75, 510))
    if selectedTool=="pencil":
        HighlightedTool((675, 285))
    if selectedTool=="spray paint":
        HighlightedTool((675, 340))
    if selectedTool=="brush":
        HighlightedTool((730, 285))
    if selectedTool=="eraser":
        HighlightedTool((730, 340))
        
    #choosing stickers
    if blackHoleButton.collidepoint(mx, my):
        stickers(blackHoleButton, blackHoleStamped)
    if galaxyButton.collidepoint(mx, my):
        stickers(galaxyButton, galaxyStamped)
    if meteorButton.collidepoint(mx, my):
        stickers(meteorButton, meteorStamped)
    if moonButton.collidepoint(mx, my):
        stickers(moonButton, moonStamped)
    if saturnButton.collidepoint(mx, my):
        stickers(saturnButton, saturnStamped)
    if starButton.collidepoint(mx, my):
        stickers(starButton, starStamped)

    #highlighting a clicked sticker
    if sticker==blackHoleStamped:
        selectedSticker(blackHoleButton)
    if sticker==galaxyStamped:
        selectedSticker(galaxyButton)
    if sticker==meteorStamped:
        selectedSticker(meteorButton)
    if sticker==moonStamped:
        selectedSticker(moonButton)
    if sticker==saturnStamped:
        selectedSticker(saturnButton)
    if sticker==starStamped:
        selectedSticker(starButton)

    #choosing replaceable background and clearing
    if earthBackgroundButton.collidepoint(mx, my):
        canvasFill(earthBackgroundButton, earthBackgroundCanvas)
    if marsButton.collidepoint(mx, my):
        canvasFill(marsButton, marsCanvas)
    if starsButton.collidepoint(mx, my):
        canvasFill(starsButton, starsCanvas)
    if clearButton.collidepoint(mx, my):
        canvasFill(clearButton, (255, 255, 255))

    #save/open file
    if saveButton.collidepoint(mx, my):
        draw.rect(screen, (200, 50, 40), saveButton, 1);
        if mb[0]:
            savedCanvas=screen.subsurface(canvas)
            image.save(savedCanvas, ".jpg")
            display.set_caption("Astronomical Art - Saved")
    if openButton.collidepoint(mx, my):
        draw.rect(screen, (200, 50, 40), openButton, 1);
        if mb[0]:
            insert=filedialog.askopenfilename(filetypes=[("Picture files", "*.png;*.jpg*.jpeg*")])#inserts picture
            screen.blit(image.load(insert), (145, 60))
    display.flip()
quit()

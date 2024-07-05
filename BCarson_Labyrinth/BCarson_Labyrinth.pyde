# TITLE:Labyrinth

# AUTHOR:Blaire Carson

# DATE DUE:2/3/21

# DATE SUBMITTED:2/2/21

# COURSE TITLE:Game Design

# MEETING TIME(S):N/A

# DESCRIPTION: Find your way through a maze, and pick up items on the way. 
    
# HONOR CODE:I have neither given nor received any unauthorized aid on this assignment. Alaina B Carson

# HOWTO:Open in proccessing, click sketch, click add file, and open the following files. Click tools, click create font, choose Gabriola in size 30. Then run. For each concurrent run, close and reopen processing before running again.

# INPUT FILE:Cottage.jpg, Howl.mp3, Scream.mp3, SpookyForest.mp3, The Labyrinth.jpeg, TreeTop.png, Wolf.mp3

# OUTPUT FILE:N/A

# BIBLIOGRAPHY:https://py.processing.org/tutorials & SoundBible.com & images.fineartamerica.com & www.freeiconspng.com

# TUTORS:N/A

# COMMENTS: There are multiple lose cases and two win cases. I also included sound effects, and imported graphics. The sound won't play for any run after the first. Processing has to be closed and reopened.
#########################################################################################################################################


add_library("sound") #brings in the sound library

########################## global variables
s = 0
m1 = ""
m2 = ""
m3 = ""
l = [0,0,0,0]
axe = False
talisman = False
game = False
count = 0 
t = 0
current = 3

#########################

def setup(): #Initializes the first screen and sets the text font
    size(900,900)
    frameRate(30)
    c = color(10,50,10)
    background(c)

    f = loadFont("Gabriola-30.vlw") #load in, size and center font
    textFont(f)
    textSize(40)
    textAlign(CENTER)
    
    c = color(255,255,255) #draw the image and it's border
    fill(c)
    rect(190,90,520,420)
    img = loadImage("The Labyrinth.jpeg")
    image(img,200,100,500,400)
    
    text("You see a figure in the distance...",450,600) #initialize the first text
    text("It looks like a girl.",450,650)
    text("Her blond hair disappears around a tree.",450,700)
    text("Click to follow.",450,800)
     
     
     
def draw(): #draw the current screen
    global s, t, m1, m2, m3
    if s == 1:
        textScreen(t) 
    if s == 2:
        gameScreen()
    if s == 3:
        loseScreen()
    if s == 4:
        winScreen()
        
        
        
def mouseClicked(): #controls changing from text screen to game screen
    global s, t, game, m1, m2, m3
    
    if game == False: #if not out of the instructions...
        if s == 0: #if on the first screen...
            s = 1 #move to the next screen
            
        elif s == 1:
            t = 1
            
    if game == True: #once into gameplay...
        if s == 1: #if on the text screen...
            s = 2 #move to the game screen
            
        elif s == 3: #if on the lose screen...
            m1 = "" #change the given messages
            m2 = ""
            m3 = "YOU LOSE"
            
        elif s == 4: #if on the win screen...
            m1 = "YOU WIN!" #change the given messages
            m2 = "You saved the girl."
            m3 = "She is so thankful that she gives you her basket of treats."


def keyTyped(): #if a key is typed...
    global l, s, game
    
    if s == 1 and game == False: #if on the text screen and the gameplay has not started...
        s = 2 #change to the game screen
        music = SoundFile(this,"SpookyForest.mp3") #start the music
        music.amp(0.3)
        music.loop()
        game = True #change gameplay to true
            
    elif game == True and s == 2: #if gameplay is true and on the gamescreen...
        if key == 'w':
            l = move(l,0) 
        if key == 'a':
            l = move(l,1)
        if key == 's':
            l = move(l,3)
        if key == 'd':
            l = move(l,2)     
       
                         
                                
def gameScreen(): #display the game screen of the current location
    
    c = color(50,40,40) #draw a background and load an image
    background(c)
    img = loadImage("TreeTop.png")
    
    c = color(0,30,0) #create rectangles for the corners
    fill(c)
    rect(0,0,300,300)
    rect(600,0,300,300)
    rect(0,600,300,300)
    rect(600,600,300,300)
    
    image(img,0,0,300,300) #create images for the corners
    image(img,600,0,300,300)
    image(img,0,600,300,300)
    image(img,600,600,300,300)
    
    location(img)
    

    
def textScreen(t): #draws a text screen with a gradient text box
    
    c = color(0,0,0) #draw a background
    background(c)
    
    for i in range(0,200,10): #create ever smaller squares of gradient color black to white
        c = color(0+i,0+i,0+i)
        fill(c)
        rect(0+i,0+i,900-2*i,900-2*i)
        
    c = color(0,0,0) #display the current messages
    fill(c)
    story(t)
    text(m1,450,350)
    text(m2,450,450)
    text(m3,450,550)
    
    
    
def loseScreen(): #display a lose screen with the given messages on a gradient text box
    
    c = color(0,0,0) #draw a background
    background(c)
    
    for i in range(0,200,10): #create ever smaller squares of gradient color red to black
        c = color(200-i,10,10)
        fill(c)
        rect(0+i,0+i,900-2*i,900-2*i)
    
    c = color(255,255,255) #print the given text
    fill(c)
    textSize(40)
    text(m1,451,401)
    text(m2,451,501)
    textSize(60)
    text(m3,451,451)
    
    c = color(255,0,0) #print the given text on top of the prior text offset by one pixel
    fill(c)
    textSize(40)
    text(m1,450,400)
    text(m2,450,500)
    textSize(60)
    text(m3,450,450)



def winScreen(): #draw a win screen with the given text
    
    c = color(10,50,10) #draw a background
    background(c)
    
    c = color(255,255,255) #draw an image and it's border
    fill(c)
    rect(140,40,620,420)
    img = loadImage("Cottage.jpg")
    image(img,150,50,600,400)
    
    text(m1,450,500) #print the given text
    text(m2,450,600)
    text(m3,450,700)
        
    
def location(img): #
    global l
    
    if l[0] == 1: #if the top is to be filled, draw a rectangle and a tree
        rect(300,0,300,300)
        image(img,300,0,300,300)
        
    if l[1] == 1: #if the left is to be filled, draw a rectangle and a tree
        rect(0,300,300,300)
        image(img,0,300,300,300)
        
    if l[2] == 1: #if the right is to be filled, draw a rectangle and a tree
        rect(600,300,300,300)
        image(img,600,300,300,300)
        
    if l[3] == 1: #if the bottom is to be filled, draw a rectangle and a tree
        rect(300,600,300,300)
        image(img,300,600,300,300)

            
            
            
def move(l,x): #change the location to the new one, and keep track of encounters
    global s, t, current, count, m1, m2, m3, axe, talisman
    
    if l[x] == 0: #only move in a direction with an opening
        count = count + 1 #count the number of moves made
        current = track(current,x) #keep track of the current display
        
        
############################# change the location for the appropriate square, change to the appropriate screen, and display the given text
        if current == 1:
            talisman = True
            l = [1,1,0,1]
            s = 1
            t = 10
            
        elif current == 2:
            l = [0,0,0,1]
            s = 1
            t = 2
            
        elif current == 3:
            l = [0,0,0,0]
            s = 1
            t = 11
            
        elif current == 4:
            l = [0,0,1,1]
            s = 1
            t = 2
            
        elif current == 5:
            l = [0,1,0,1]
            s = 1
            t = 2
            
        elif current == 6:
            l = [0,0,1,0]
            s = 1
            t = 3
            
        elif current == 7:
            l = [1,1,0,0]
            s = 1
            t = 2
            
        elif current == 8:
            l = [0,0,1,0]
            s = 1
            t = 4
            
        elif current == 9:
            l = [0,1,0,0]
            s = 1
            t = 2
            
        elif current == 10:
            l = [1,0,0,0]
            s = 1
            t = 12
            
        elif current == 11:
            music = SoundFile(this,"Howl.mp3")
            music.amp(0.5)
            music.play()
            l = [0,0,0,1]
            s = 1      
            t = 6
            
        elif current == 12:
            l = [1,0,1,0]
            s = 1
            t = 2  
                          
        elif current == 13:
            axe = True
            l = [1,1,1,0]
            s = 1
            t = 8
            
        elif current == 14:
            l = [0,1,0,1]
            s = 1
            t = 9
            
        elif current == 15:
            l = [1,0,0,0]
            s = 1    
            t = 7
            
        elif current == 16:
            l = [1,0,1,1]
            s = 1
            t = 5
            
        elif current == 18:
            if axe == True:
                s = 4
                m1 = "As you enter the clearing, you see the girl cowering near a cottage."
                m2 = "Suddenly, a wolf attacks you! You swing the axe."
                m3 = "The axe becomes embedded in the skull of the wolf. It is slain."
                
            elif talisman == True:
                s = 4
                m1 = "As you enter the clearing, you see a house and the girl."
                m2 = "Suddenly, a wolf attacks you! But it can't get near you."
                m3 = "You are safe from its snapping jaws. You escort the girl to safety."
                
            else:
                s = 3
                music = SoundFile(this,"Wolf.mp3")
                music.amp(0.5)
                music.play()
                m1 = "You enter the clearing only to be mauled by a wolf."
                m2 = "You are dead. If only you had found a weapon..."
                m3 = ""
              
        elif current == -1:
            music = SoundFile(this,"Scream.mp3")
            music.amp(0.5)
            music.play()
            s = 3
            m1 = "You stumble out where you first entered."
            m2 = "You hear a girl scream in the distance..."
            m3 = ""  
            
        if count == 20:
            music = SoundFile(this,"Wolf.mp3")
            music.amp(0.5)
            music.play()
            s = 3 
            m1 = "You collapse from exhaustion."
            m2 = "You cower as the wolves descend..."
            m3 = ""       
            
    return l
        
        
def track(c,x): #change the current square based on the typed input
    
    if x == 0:
        c = c + 4
        
    elif x == 1:
        c = c - 1
        
    elif x == 2:
        c = c + 1
        
    elif x == 3:
        c = c - 4
                
    return c            
            
        
            
def story(t): #change the current text depending on which square is entered
    global m1,m2,m3
    
    if t == 0:
        m1 = "You come to the edge of the forest..."
        m2 = "It is dark inside..."
        m3 = "But you are determined."
        
    elif t == 1:
        m1 = "You walk forward..."
        m2 = "Press w, a, s, or d to walk"
        m3 = "(w-up, a-left, s-down, d-right)"
        
    elif t == 2:
        m1 = "You keep walking."
        m2 = "The trees rustle overhead."
        m3 = "Click to continue."
        
    elif t == 3:
        m1 = "It is dark and cold."
        m2 = "You feel a chill go down your spine."
        
    elif t == 4:
        m1 = "You hear a twig snap."
        m2 = "A rabbit hops across your path."
        
    elif t == 5:
        m1 = "You come across a well."
        m2 = "You toss a penny in. Nothing happens."
        
    elif t == 6:
        m1 = "You hear a wolf howl..."
        m2 = "You start moving faster."
        
    elif t == 7:
        m1 = "You see something red on the ground."
        m2 = "It looks like a cloak..."
        
    elif t == 8:
        m1 = "You see an axe stuck in a tree stump."
        m2 = "You wrench it free. You are now armed."
        
    elif t == 9:
        m1 = "You smell baked goods."
        m2 = "Your stomach rumbles."
        
    elif t == 10:
        m1 = "You find a talisman of some sort."
        m2 = "You put it on. You are now protected."
        
    elif t == 11:
        m1 = "This place looks familiar."
        m2 = "You think you have been here before."
        
    elif t == 12:
        m1 = "It is getting late."
        m2 = "The sky is darker."

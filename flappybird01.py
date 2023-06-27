import turtle
import turtle as t
import time
import winsound
import operator

wn = turtle.Screen()
wn.title("FLY HIGH")
wn.setup(1.0,1.0)

bgl=turtle.Turtle()
bgl.hideturtle()
wn.addshape('bgloop.gif')
bgl.shape('bgloop.gif')
bgl.penup()
bgl.setpos(0,0)
bgl.showturtle()
loop="r"
start="no"
tim=time.time()+2
d={}


wn.addshape('bgl.gif')
turtle.shape('bgl.gif')
turtle.penup()
turtle.setpos(0,0)
while time.time()<tim:
        bgl.forward(-3)
bgl.hideturtle()      

wn.addshape('select.gif')
turtle.shape('select.gif')    
turtle.penup()
turtle.delay(0)
wn.bgpic('mm.gif')
turtle.goto(460,-170)
turtle.delay(10)
 
turtle.showturtle()
turtle.left(90)

def up(): 
  if turtle.pos()==(460,-170) or turtle.pos()==(460,-20):
    turtle.forward(150)

def dn():
  if turtle.pos()==(460,130) or turtle.pos()==(460,-20):
    turtle.backward(150)

def left():
  if wn.bgpic()=="quit.gif":
      if t.pos()!=(-90,-50):
          t.delay(10) 
          t.goto(-90,-50)

def right():
  if wn.bgpic()=="quit.gif":
      if t.pos()!=(90,-50):
          t.delay(10)
          t.goto(90,-50)
      
def bs():
  if wn.bgpic()=="about.gif" :
    wn.bgpic('mm.gif')
    turtle.showturtle()

def q():
  if wn.bgpic()=="mm.gif":
      wn.bgpic("quit.gif")
      t.delay(0)
      t.hideturtle()
      t.goto(90,-50)
      t.showturtle()
      t.left(90)    
                          
                      
def en():
  wn = turtle.Screen()
  if turtle.pos()==(460,130) and wn.bgpic()=="mm.gif" :
    t.hideturtle()
    #winsound.PlaySound("ARCADE.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    turtle.hideturtle()

    wn.bgpic('bg.gif')
    wn.title("Flappy Bird")
    wn.bgcolor("light blue")
    wn.tracer(0)
    
    # Register Shapes
    wn.register_shape("fb.gif")
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color("white")
    pen.goto(0, 250)
    pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

    swrite=turtle.Turtle()
    swrite.penup()
    swrite.speed(0)
    swrite.color("black")
    swrite.goto(-600,100)
    swrite.hideturtle()
    
    player = turtle.Turtle()
    player.speed(0)
    player.penup()
    #player.color("yellow")
    player.shape("fb.gif")
    player.goto(-200, 0)
    player.dx = 0
    player.dy = 1
    
    pipe1_top = turtle.Turtle()
    pipe1_top.speed(0)
    pipe1_top.penup()
    wn.addshape("bu.gif")
    pipe1_top.shape("bu.gif")
    pipe1_top.goto(300, 250)
    pipe1_top.dx = -2
    pipe1_top.dy = 0
    pipe1_top.value = 1
    
    pipe1_bottom = turtle.Turtle()
    pipe1_bottom.speed(0)
    pipe1_bottom.penup()
    wn.addshape("bd.gif")
    pipe1_bottom.shape("bd.gif")
    pipe1_bottom.goto(300, -250)
    pipe1_bottom.dx = -2
    pipe1_bottom.dy = 0
    
    pipe2_top = turtle.Turtle()
    pipe2_top.speed(0)
    pipe2_top.penup()
    wn.addshape("bu.gif")
    pipe2_top.shape("bu.gif")
    pipe2_top.goto(600, 280)
    pipe2_top.dx = -2
    pipe2_top.dy = 0
    pipe2_top.value = 1
    
    pipe2_bottom = turtle.Turtle()
    pipe2_bottom.speed(0)
    pipe2_bottom.penup()
    wn.addshape("bd.gif")
    pipe2_bottom.shape("bd.gif")
    pipe2_bottom.goto(600, -220)
    pipe2_bottom.dx = -2
    pipe2_bottom.dy = 0
    
    pipe3_top = turtle.Turtle()
    pipe3_top.speed(0)
    pipe3_top.penup()
    wn.addshape("bu.gif")
    pipe3_top.shape("bu.gif")
    pipe3_top.goto(900, 320)
    pipe3_top.dx = -2
    pipe3_top.dy = 0
    pipe3_top.value = 1
    
    pipe3_bottom = turtle.Turtle()
    pipe3_bottom.speed(0)
    pipe3_bottom.penup()
    wn.addshape("bd.gif")
    pipe3_bottom.shape("bd.gif")
    pipe3_bottom.goto(900, -180)
    pipe3_bottom.dx = -2
    pipe3_bottom.dy = 0

    pipe4_top = turtle.Turtle()
    pipe4_top.speed(0)
    pipe4_top.penup()
    wn.addshape("bu.gif")
    pipe4_top.shape("bu.gif")
    pipe4_top.goto(1200, 320)
    pipe4_top.dx = -2
    pipe4_top.dy = 0
    pipe4_top.value = 1
    
    pipe4_bottom = turtle.Turtle()
    pipe4_bottom.speed(0)
    pipe4_bottom.penup()
    wn.addshape("bd.gif")
    pipe4_bottom.shape("bd.gif")
    pipe4_bottom.goto(1200, -180)
    pipe4_bottom.dx = -2
    pipe4_bottom.dy = 0
    
    gravity = -0.3
    
    # Define function / method
    def go_up():
        player.dy += 8
        
        
        if wn.bgpic()=="quitrun.gif":
            if t.pos()==(-90,-50):
                  turtle.bye()
            elif t.pos()==(90,-50):
                  turtle.hideturtle()
                  wn.delay(0)
                  wn.bgpic('bg.gif')    
        elif player.dy > 8:
            player.dy = 8
            
    count=ct=0
    
    # Initialize game variables
    player.score = 0
    
    pipes = [(pipe1_top, pipe1_bottom), (pipe2_top, pipe2_bottom), (pipe3_top, pipe3_bottom), (pipe4_top, pipe4_bottom)]
    
    # Main Game Loop
    while True:
        def q():
          if wn.bgpic()=="bg.gif":
            wn.bgpic("quitrun.gif")
            t.delay(0)
            t.goto(90,-50)
            t.showturtle()
            t.left(90)

        def left():
          if wn.bgpic()=="quitrun.gif":
            if t.pos()!=(-90,-50):
                t.delay(10) 
                t.goto(-90,-50)

        def right():
          if wn.bgpic()=="quitrun.gif":
            if t.pos()!=(90,-50):
                t.delay(10)
                t.goto(90,-50)
                
        # Keyboard binding
        wn.listen()
        wn.onkey(left,"Left")
        wn.onkey(right,"Right")
        wn.onkeypress(q,"q")
        wn.onkeypress(go_up,"space")
        # Pause
        time.sleep(0.02)
        # Update the screen
        wn.update()
        
        # Add gravity
        player.dy += gravity
        
        # Move player
        y = player.ycor()
        y += player.dy
        player.sety(y)
        
        # Bottom Border
        if player.ycor() < -390:
            player.dy = 0
            player.sety(-390)
    
    
        # Iterate through pipes
        for pipe_pair in pipes:
            pipe_top = pipe_pair[0]
            pipe_bottom = pipe_pair[1]
            
            # Move Pipe 1
            x = pipe_top.xcor()
            x += pipe_top.dx
            pipe_top.setx(x) 
            
            x = pipe_bottom.xcor()
            x += pipe_bottom.dx
            pipe_bottom.setx(x)
            
            # Return pipes to start
            if pipe_top.xcor() < -600:
                pipe_top.setx(600)
                pipe_bottom.setx(600)
                pipe_top.value = 1
    
            # Check for collisions with pipes
            # Pipe 1
            if (player.xcor() + 10 > pipe_top.xcor() - 30) and (player.xcor() - 10 < pipe_top.xcor() + 30) and wn.bgpic()!="sb.gif" and wn.bgpic()!="quitgo.gif":
                if (player.ycor() + 10 > pipe_top.ycor() - 180) or (player.ycor() - 10 < pipe_bottom.ycor() + 180):
                    pen.clear()
                    pipe1_top.hideturtle()
                    pipe2_top.hideturtle()
                    pipe3_top.hideturtle()
                    pipe4_top.hideturtle()
                    pipe1_bottom.hideturtle()
                    pipe2_bottom.hideturtle()
                    pipe3_bottom.hideturtle()
                    pipe4_bottom.hideturtle()
                    player.hideturtle()
                    wn.bgpic("go.gif")               
                    wn.update()
                    time.sleep(0.1)

                    if player.score!=0:
                        #GETTING NAME
                        screen = turtle.getscreen()
                        getname=screen.textinput(player.score, "ENTER YOUR NAME:")
                        d[getname]=player.score
                        # Reset score
                        player.score = 0

                    def g():
                          if wn.bgpic()=="go.gif":
                              pipe1_top.setpos(300, 250)
                              pipe1_bottom.setpos(300, -250)
                              pipe2_top.setpos(600, 280)
                              pipe2_bottom.setpos(600, -220)
                              pipe3_top.setpos(900, 320)
                              pipe3_bottom.setpos(900, -180)
                              pipe4_top.setpos(1200, 320)
                              pipe4_bottom.setpos(1200, -180)                                             
                              #show objects
                              pipe1_top.showturtle()
                              pipe2_top.showturtle()
                              pipe3_top.showturtle()
                              pipe4_top.showturtle()
                              pipe1_bottom.showturtle()
                              pipe2_bottom.showturtle()
                              pipe3_bottom.showturtle()
                              pipe4_bottom.showturtle()
                              player.showturtle()
                              wn.bgpic("bg.gif")
                              # Move Pipes Back
                              pipe_top.setx(650)
                              pipe_bottom.setx(650)
                              # Move Player back
                              player.goto(-200, 0)
                              player.dy = 0
                              # Reset the pen
                              pen.clear()
                              pen.write("0", move=False, align="center", font=("Arial", 32, "normal"))                          
                    
                    def r():
                          if wn.bgpic()=="go.gif":
                              wn.bgpic("sb.gif")                                              
                              d1 = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
                              swrite.goto(-600,100)
                              ct=0
                              for i in (d1):
                                ct+=1
                                swrite.write(ct, align="left", font=("Arial", 30, "normal"))
                                swrite.forward(50) 
                                swrite.write(i,".", align="left", font=("Arial", 30, "normal"))
                                swrite.goto(400,swrite.ycor())                                                
                                swrite.write(d1[i], align="left", font=("Arial", 30, "normal"))
                                swrite.goto(-600,swrite.ycor())
                                swrite.right(90)
                                swrite.forward(50)
                                swrite.left(90)             
                    def bs():
                          #turtle.clearscreen()
                          swrite.clear()
                          wn.bgpic("go.gif")
                    
                    def q():
                          if wn.bgpic()=="go.gif":
                              wn.bgpic("quitgo.gif")
                              t.delay(0)
                              t.hideturtle()
                              t.goto(90,-50)
                              t.showturtle()
                              t.left(90)  
                              
                    def en():
                          if wn.bgpic()=="quitgo.gif":
                              if t.pos()==(-90,-50):
                                  turtle.bye()
                              elif t.pos()==(90,-50):
                                turtle.hideturtle()
                                t.delay(0)
                                wn.bgpic('go.gif')
                                                                     
                    def left():
                          if wn.bgpic()=="quitgo.gif":
                              if t.pos()!=(-90,-50):
                                  t.delay(10) 
                                  t.goto(-90,-50)

                    def right():
                          if wn.bgpic()=="quitgo.gif":
                              if t.pos()!=(90,-50):
                                  t.delay(10)
                                  t.goto(90,-50)            
                                
                                                                 
                    wn.listen()
                    wn.onkeypress(g,"g")
                    wn.onkeypress(r,"r")
                    wn.onkeypress(bs,"BackSpace")
                    wn.onkeypress(q,"q")
                    wn.onkey(left,"Left")
                    wn.onkey(right,"Right")
                    wn.onkey(en,"space")
                    
            # Check for score        
            if pipe_top.xcor() + 30 < player.xcor() - 10 and player.isvisible()==True:
                  player.score += pipe_top.value
                  pipe_top.value = 0
                  pen.clear()
                  pen.write(player.score, move=False, align="center", font=("Arial", 32, "normal"))

        if wn.bgpic()=="mm.gif":
            break  
    wn.mainloop()


  elif turtle.pos()==(460,-170) and wn.bgpic()=="mm.gif" :
    turtle.hideturtle()
    wn.bgpic('about.gif')

  elif wn.bgpic()=="quit.gif":
      if turtle.pos()==(-90,-50):
          t.bye()
      elif t.pos()==(90,-50):
        turtle.hideturtle()
        t.delay(0)
        wn.bgpic('mm.gif')
        turtle.goto(460,130)
        turtle.showturtle()
        t.delay(10)
        t.right(90)



# Keyboard binding
wn.listen()
#wn.onkeypress(go_up,"space")
wn.onkeypress(up,"Up")
wn.onkeypress(dn,"Down")
wn.onkeypress(en,"space")
wn.onkeypress(q,"q")
wn.onkey(left,"Left")
wn.onkey(right,"Right")
wn.onkeypress(bs,"BackSpace")

        


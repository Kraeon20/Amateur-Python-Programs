import turtle
turtle.speed(3)
turtle.color('pink')
turtle.pensize(3)
turtle.bgcolor('black')
turtle.setup(500, 600)
turtle.penup()
turtle.hideturtle()

LEFTSHOULDER_X = -70
LEFTSHOULDER_Y = 200

RIGHTSHOULDER_X = 80
RIGHTSHOULDER_Y = 180

LEFTBELTSTAR_X = -40
LEFTBELTSTAR_Y = -20

MIDDLEBELTSTAR_X = 0
MIDDLEBELTSTAR_Y = 0

RIGHTBELTSTAR_X = 40
RIGHTBELTSTAR_Y = 20

LEFTKNEE_X = -90
LEFTKNEE_Y = -180

RIGHTKNEE_X = 120
RIGHTKNEE_Y = -140

turtle.goto(LEFTSHOULDER_X, LEFTSHOULDER_Y)
turtle.dot()
turtle.goto(RIGHTSHOULDER_X, RIGHTSHOULDER_Y)
turtle.dot()
turtle.goto(LEFTBELTSTAR_X, LEFTBELTSTAR_Y)
turtle.dot()
turtle.goto(MIDDLEBELTSTAR_X, MIDDLEBELTSTAR_Y)
turtle.dot()
turtle.goto(RIGHTBELTSTAR_X, RIGHTBELTSTAR_Y)
turtle.dot()
turtle.goto(LEFTKNEE_X, LEFTKNEE_Y)
turtle.dot()
turtle.goto(RIGHTKNEE_X, RIGHTKNEE_Y)
turtle.dot()

turtle.goto(LEFTSHOULDER_X, LEFTSHOULDER_Y)
turtle.write('BETEGEUSE')
turtle.goto(RIGHTSHOULDER_X, RIGHTSHOULDER_Y)
turtle.write('MEISSA')
turtle.goto(LEFTBELTSTAR_X, LEFTBELTSTAR_Y)
turtle.write('ALNITAK')
turtle.goto(MIDDLEBELTSTAR_X,MIDDLEBELTSTAR_Y)
turtle.write('ALNILAM')
turtle.goto(RIGHTBELTSTAR_X,RIGHTBELTSTAR_Y)
turtle.write('MINTAKA')
turtle.goto(LEFTKNEE_X,LEFTKNEE_Y)
turtle.write('SAIPH')
turtle.goto(RIGHTKNEE_X,RIGHTKNEE_Y)
turtle.write('RIGEL')

turtle.goto(LEFTSHOULDER_X,LEFTSHOULDER_Y)
turtle.pendown()
turtle.goto(LEFTBELTSTAR_X, LEFTBELTSTAR_Y)
turtle.goto(LEFTKNEE_X, LEFTKNEE_Y)

turtle.penup()
turtle.goto(RIGHTSHOULDER_X, RIGHTSHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHTBELTSTAR_X, RIGHTBELTSTAR_Y)
turtle.goto(RIGHTKNEE_X, RIGHTKNEE_Y)

turtle.penup
turtle.goto(RIGHTBELTSTAR_X, RIGHTBELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFTBELTSTAR_X, LEFTBELTSTAR_Y)
turtle.done()

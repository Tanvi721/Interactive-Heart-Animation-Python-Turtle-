import turtle
import time
import random

# ---------------- SCREEN SETUP ----------------
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor("white")
wn.tracer(0)
wn.colormode(255)

# ---------------- TURTLES ----------------
heart_t = turtle.Turtle()
glow_t = turtle.Turtle()
text_t = turtle.Turtle()
bg_t = turtle.Turtle()

for t in (heart_t, glow_t, text_t, bg_t):
    t.hideturtle()
    t.speed(0)
    t.penup()

# ---------------- HEART DRAW FUNCTION ----------------
def draw_heart(turtle_obj, size, color):
    turtle_obj.clear()
    turtle_obj.goto(0, -40)
    turtle_obj.setheading(0)
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    turtle_obj.left(140)
    turtle_obj.forward(size)
    turtle_obj.circle(-size/2, 200)
    turtle_obj.left(120)
    turtle_obj.circle(-size/2, 200)
    turtle_obj.forward(size)
    turtle_obj.end_fill()
    turtle_obj.setheading(0)

# ---------------- GLOW EFFECT ----------------
def draw_glow(size):
    glow_colors = [
        (255, 180, 200),
        (255, 120, 150),
        (255, 60, 100)
    ]
    glow_t.clear()
    for i, color in enumerate(glow_colors):
        draw_heart(glow_t, size + (i * 10), color)

# ---------------- CENTERED TEXT ----------------
def draw_text():
    text_t.clear()
    text_t.color("red")

    lines = [
        "Roses are red,",
        "Violets are blue,",
        "I love coding,",
        "Do you love it too? 💻💖"
    ]

    start_y = -180   # 👈 this controls how far below the heart the text appears
    spacing = 30

    for i, line in enumerate(lines):
        text_t.goto(0, start_y - (i * spacing))
        text_t.write(line, align="center", font=("Arial", 16, "bold"))

        

# ---------------- FLOATING MINI HEARTS ----------------
mini_hearts = []

for _ in range(20):
    mini = turtle.Turtle()
    mini.shape("circle")
    mini.shapesize(0.4)
    mini.color("blue violet")
    mini.penup()
    mini.speed(0)
    mini.goto(random.randint(-320, 320), random.randint(-320, 320))
    mini_hearts.append(mini)

def animate_background():
    for mini in mini_hearts:
        mini.sety(mini.ycor() + random.uniform(0.5, 1.5))
        if mini.ycor() > 350:
            mini.sety(-350)

# ---------------- HEARTBEAT LOOP ----------------
def heartbeat():
    while True:
        # small beat
        draw_glow(120)
        draw_heart(heart_t, 120, (255, 0, 80))
        draw_text()
        animate_background()
        wn.update()
        time.sleep(0.4)

        # big beat
        draw_glow(135)
        draw_heart(heart_t, 135, (255, 0, 80))
        draw_text()
        animate_background()
        wn.update()
        time.sleep(0.4)

# ---------------- TITLE ----------------
title_t = turtle.Turtle()
title_t.hideturtle()
title_t.penup()
title_t.goto(0, 260)
title_t.color("red")
title_t.write("Hey! This is for you ❤️", align="center", font=("Arial", 20, "bold"))

# Run
heartbeat()
wn.mainloop()

exploded = False
particles = []

def explode(x, y):
    global exploded
    if exploded:
        return

    exploded = True

    # Clear main heart + glow + text
    heart_t.clear()
    glow_t.clear()
    text_t.clear()

    # Create explosion particles
    for _ in range(60):
        p = turtle.Turtle()
        p.shape("circle")
        p.shapesize(0.4)
        p.color("red")
        p.penup()
        p.goto(0, -40)
        p.speed(0)

        # Random direction + speed
        angle = random.randint(0, 360)
        speed = random.uniform(2, 6)
        p.setheading(angle)
        particles.append((p, speed))

    animate_explosion()
    def animate_explosion():
        for _ in range(80):
         wn.tracer(0)
        for p, speed in particles:
            p.forward(speed)
        wn.update()
        time.sleep(0.02)
    wn.onclick(explode)




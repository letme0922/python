import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# 화면 설정
wn = turtle.Screen()
wn.title("뱀 게임")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# 뱀 머리
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 먹이
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# 점수판
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("점수: 0  최고점수: 0", align="center", font=("Arial", 24, "normal"))

# 함수들
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 키보드 바인딩
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# 메인 게임 루프
while True:
    wn.update()

    # 벽에 부딪힘
    if (head.xcor()>290 or head.xcor()<-290 or 
        head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # 꼬리 초기화
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        scoreboard.clear()
        scoreboard.write(f"점수: {score}  최고점수: {high_score}", align="center", font=("Arial", 24, "normal"))

    # 먹이를 먹었는지 확인
    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # 꼬리 추가
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write(f"점수: {score}  최고점수: {high_score}", align="center", font=("Arial", 24, "normal"))

    # 꼬리 이동
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # 자기 몸에 부딪힘
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            scoreboard.clear()
            scoreboard.write(f"점수: {score}  최고점수: {high_score}", align="center", font=("Arial", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
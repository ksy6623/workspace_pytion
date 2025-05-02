from tkinter import *
from PIL import Image, ImageTk
# pip install pillow

app = Tk()
canvas = Canvas(app, width=400, height=400)
canvas.pack()
x = 20
y = 20
jump_height = 10
tk_tiger = None
def create_img(canvas):
    global tk_tiger  # 전역변수 사용
    img = Image.open('tiger.png')
    img = img.resize((50,50)) # 사이즈 조정
    tk_tiger = ImageTk.PhotoImage(img)
    canvas.create_image(100,350, image=tk_tiger,tag='tiger')
def move_right(event):
    canvas.move('tiger',x,0)
    canvas.after(10)
    canvas.update()
def move_left(event):
    canvas.move('tiger',-x,0)
    canvas.after(10)
    canvas.update()
def move_up(event):
    canvas.move('tiger',0,-y)
    canvas.after(10)
    canvas.update()
def move_down(event):
    canvas.move('tiger',0,y)
    canvas.after(10)
    canvas.update()

# up, down을 만들어주세요 up, down 바인드 100, 150 왼쪽 상단모서리, 150,200 오른쪽 상단 모서리
create_img(canvas)
canvas.bind('<Right>',move_right)
canvas.bind('<Left>',move_left)
canvas.bind('<Up>',move_up)
canvas.bind('<Down>',move_down)
canvas.focus_set()
app.mainloop()
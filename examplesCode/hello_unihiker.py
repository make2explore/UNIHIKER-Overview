from unihiker import GUI
import time 


gui = GUI()

Text = gui.draw_text(text='Hello , Unihiker !',x=15,y=120,font_size=20)
Text.config(color='#0000FF')


while True:
    time.sleep(1)


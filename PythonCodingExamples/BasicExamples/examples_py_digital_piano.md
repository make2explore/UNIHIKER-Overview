## **Project Introduction**
The UNIHIKER is equipped with a buzzer that can emit different tones by setting different frequencies. This feature allows for the creation of an electronic piano. In this project, a simple user interface is created where users can play different notes by pressing buttons on the screen. Below is an example of an electronic piano.   

![18.1.gif](img/18.Digital Piano/1717471127904-dd09691b-67c5-42ce-bd06-fbb4f4c3023b.gif){width=500, style="display:block;margin: 0 auto"} 

## **Hardware Required**

- [UNIHIKER](https://www.dfrobot.com/product-2691.html)
## **Code**
In this example, UNIHIKER is initialized with Board().begin().   

Then, a GUI object is instantiated, and multiple black and white rectangles (representing different piano keys) are created using the fill_rect() function.   

Next, a series of event callback functions are defined, each corresponding to a musical note. 

Within the callback functions, the buzzer is controlled to emit a sound of a specific frequency and duration using the buzzer.pitch(frequency, duration) function.   

Each musical note is bound to a piano key, and when the key is pressed, the corresponding callback function is executed, and the buzzer plays the respective note.   

Additionally, a text box displays the name of the currently playing note, allowing the user to identify which note is being played. This creates a simple user interface for an electronic piano on UNIHIKER.  


```python
#  -*- coding: UTF-8 -*-

# MindPlus
# Python
from pinpong.extension.unihiker import *
from pinpong.board import Board,Pin
from unihiker import GUI
import time

# Event callback function
def button_click1():
    buzzer.pitch(262,1)
    text.config(text="C4")
def button_click2():
    buzzer.pitch(294,1)
    text.config(text="D4")
def button_click3():
    buzzer.pitch(330,1)
    text.config(text="E4")
def button_click4():
    buzzer.pitch(349,1)
    text.config(text="F4")
def button_click5():
    buzzer.pitch(392,1)
    text.config(text="G4")
def button_click6():
    buzzer.pitch(440,1)
    text.config(text="A4")
def button_click7():
    buzzer.pitch(494,1)
    text.config(text="B4")
def button_click8():
    buzzer.pitch(277,1)
    text.config(text="C#4")
def button_click9():
    buzzer.pitch(311,1)
    text.config(text="D#4")
def button_click10():
    buzzer.pitch(370,1)
    text.config(text="F#4")
def button_click11():
    buzzer.pitch(415,1)
    text.config(text="G#4")
def button_click12():
    buzzer.pitch(466,1)
    text.config(text="A#4")


u_gui=GUI()
Board().begin()

bg=u_gui.fill_rect(x=0,y=0,w=240,h=320,color="#CCCCFF")
text = u_gui.draw_text(x=185,y=160,text="Musical Scale",origin="center",font_size=30,angle=270)
do=u_gui.fill_rect(x=0,y=3,w=130,h=43,color="#FFFFFF",onclick=button_click1)
re=u_gui.fill_rect(x=0,y=48,w=130,h=43,color="#FFFFFF",onclick=button_click2)
mi=u_gui.fill_rect(x=0,y=93,w=130,h=43,color="#FFFFFF",onclick=button_click3)
fa=u_gui.fill_rect(x=0,y=138,w=130,h=43,color="#FFFFFF",onclick=button_click4)
so=u_gui.fill_rect(x=0,y=183,w=130,h=43,color="#FFFFFF",onclick=button_click5)
la=u_gui.fill_rect(x=0,y=228,w=130,h=43,color="#FFFFFF",onclick=button_click6)
xi=u_gui.fill_rect(x=0,y=273,w=130,h=43,color="#FFFFFF",onclick=button_click7)
bian1=u_gui.fill_rect(x=50,y=32,w=80,h=30,color="#000000",onclick=button_click8)
bian2=u_gui.fill_rect(x=50,y=77,w=80,h=30,color="#000000",onclick=button_click9)
bian3=u_gui.fill_rect(x=50,y=167,w=80,h=30,color="#000000",onclick=button_click10)
bian4=u_gui.fill_rect(x=50,y=212,w=80,h=30,color="#000000",onclick=button_click11)
bian5=u_gui.fill_rect(x=50,y=257,w=80,h=30,color="#000000",onclick=button_click12)


while True:
    time.sleep(1)
```
## **Demo Effect**
![18.2.gif](img/18.Digital Piano/1717471136431-517a5898-d799-4ff9-a4bb-6eece70bdc05.gif){width=500, style="display:block;margin: 0 auto"}  

## **Extend**  
Here is a more detailed explanation of the different uses of the buzzer.  
  
#### Playing Pre-set Melodies  
The onboard buzzer of the UNIHIKER board can play a range of pre-set melodies. For example:  

```python
buzzer.play(buzzer.DADADADUM, buzzer.Once) # Play the "DADADADUM" melody once
```
This line of code will make the buzzer play a melody named "DADADADUM." The buzzer.Once indicates that this melody will be played only once.

- Other Melodies: DADADADUM, ENTERTAINER, PRELUDE, ODE, NYAN, RINGTONE, FUNK, BLUES, BIRTHDAY, WEDDING, FUNERAL, PUNCHLINE, BADDY, CHASE, BA_DING, WAWAWAWAA, JUMP_UP, JUMP_DOWN, POWER_UP, POWER_DOWN.
- Play Modes: Once (play once), Forever (play continuously), OnceInBackground (play once in the background), ForeverInBackground (play continuously in the background).  

   
#### Setting the Tempo
You can set the buzzer's tempo, including the number of notes per beat and the number of beats per minute:
```python
buzzer.set_tempo(4, 60) # Set the number of notes per beat to 4, and the number of beats per minute to 60
```
This sets a standard 4/4 time signature with 60 beats per minute.  

#### Playing a Note in the Background
The buzzer can also play notes in the background, allowing other tasks to be performed simultaneously while the note is playing:
```python
buzzer.pitch(494) # Play a note at 494Hz frequency in the background
```
This line of code will play a note at 494Hz in the background until it is stopped.  

#### Stopping Playback
Whether playing in the foreground or background, playback can be stopped at any time:
```python
buzzer.stop() # Stop playback
```  

#### Redirecting Pins
If needed, the buzzer's output can be redirected to other PWM (Pulse Width Modulation) compatible pins:
```python
buzzer.redirect(Pin.P0) # Redirect the buzzer output to pin P0
```
This line of code redirects the buzzer's signal output from the default pin to pin P0.  


---  
 


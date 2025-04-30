## **Download and Install Thonny**
In this tutorial, we will demonstrate how to download and install Thonny on your Windows, Mac, or Linux computer.  

### **Thonny**
Thonny is an IDE specifically designed for Python beginners, featuring a friendly user interface and robust code editing, running, and debugging capabilities. It simplifies Python code writing, making it straightforward and easy. Thonny also supports connecting and programming the UNIHIKER through its built-in SSH remote functionality.  
### **Download the Editor**
Download the Thonny application that supports UNIHIKER.  

!!! tip 
    Thonny does not support Python versions below version 3.8 starting from version 4.x, which may prevent the UNIHIKER from connecting. Please use the link provided to download and install version 3.3.13.  

● for Windows : [[Download]](https://img.dfrobot.com.cn/wiki/none/49990b1e1e72cb7c95f161be759c86ba.zip).  
● for Linux and MacOS:[ [Select and download Thonny from the official Website]](https://thonny.org/)(Version 3.3.13 is better).  

![image.png](img/Thonny - Python/1696923314677-c1bac993-661a-45ca-b763-2453d3a8b857.png)  
  
### **Installation and open Thonny**
#### Windows 
![image.png](img/Thonny - Python/1696923350459-41c2c222-fa59-4e2b-86db-61eac1930fdf.png)
#### macOS
![image.png](img/Thonny - Python/1696925110080-dbb9f2e1-4791-4311-9fa0-e335a69bf40e.png){style="display:block;margin: 0 auto"}
#### Linux
![thonny_on_linux-new.jpg](img/Thonny - Python/1696925603096-159acc24-7341-44b5-8a9b-eb074bf8a69c.jpeg)
## **Starting up the UNIHIKER**
### **Connect the UNIHIKER**
Connect the UNIHIKER to your computer using the Type-C to USB cable. Once connected and powered on, the UNIHIKER logo will appear on the screen.   

![](img/Thonny - Python/1691476703505-51223828-f994-438e-a0a5-f4577792ea1e.png){style="display:block;margin: 0 auto"}    

!!! note
    1. Please ensure that you plug the USB cable directly into the computer's USB port without using an extension cord or dock. If you encounter any issues with the connection, please refer to the FAQ for a solution.  
    2. When the UNIHIKER is connected to your PC via USB, the IP address is fixed at 10.1.2.3. You can find the IP address in the "Home" menu of the UNIHIKER.  

## **Run a simple example with Thonny**
The Thonny software supports programming the UNIHIKER through Python code, you can create a simple example as follows.  

(1) Launch Thonny and check the "Files" and "Shell" options in the "View" menu.   

![image.png](img/Thonny - Python/1696929781312-e3dcc886-3f4c-4d1d-9dc0-3f9274e5d7cc.png){width=500, style="display:block;margin: 0 auto"}  

(2) After completing the previous step, you will see a screen like this. The left side is the file directory area, and the right side consists of the code editing area and the terminal area.    

![image.png](img/Thonny - Python/1696930215817-ac2e66e7-5f2b-4676-a6d7-4a8956d82817.png){style="display:block;margin: 0 auto"}  

(3) To connect UNIHIKER using Thonny, you may follow these steps:

1. Click on "Select interpreter" in the "Run" menu.
2. Choose "Remote Python 3 (SSH)".
3. Input the Host (IP address) and Username as follows:
   - Host: 10.1.2.3
   - Username: root

This allows Thonny to connect to UNIHIKER via SSH for Python programming.  

![image.png](img/Thonny - Python/1696930628166-afa456e5-f53c-4b4a-9793-b64311afd57c.png)  
  {width=300, style="display:block;margin: 0 auto"}  

After that, it will prompt for a password. Enter the default password 'dfrobot' and select 'Save password' to remember it.  
  
![image.png](img/Thonny - Python/1696930697833-c61e486e-42c5-4323-8594-ccaa98f4f191.png){width=300, style="display:block;margin: 0 auto"}   

!!! note
    1. When connecting UNIHIKER to the computer via a USB cable, the default IP address is '10.1.2.3', the default username is 'root', and the default password is 'dfrobot'.  
    2. If it prompts "Can't connect to '10.1.2.3' with user 'root': [WinError 10060]", you should verify whether the board is properly connected to the computer.    
  
Upon successful connection, the file directory will display the files within the board, and the terminal will switch to the remote terminal of the board.  

![image.png](img/Thonny - Python/1696932050928-d469342d-67de-4401-b7e5-76f4ca7325a6.png)  
  
(4) Then, we can click "new" option and "save" option to create a new file named "Hi UNIHIKER.py"   

![image.png](img/Thonny - Python/1696933077847-5e6d1dcc-5b8a-471e-82d3-0df553f54a6c.png)
![image.png](img/Thonny - Python/1696933140344-ef1f0282-0f7c-44eb-b9b0-7cdfdc8cf9ae.png)  
  
(5) After creating the file,  you may insert this code into the code editing area of the file "Hi UNIHIKER.py" .Here's a code snippet that will display "HI UNIHIKER" on the screen.  

```python
from unihiker import GUI
import time

gui = GUI()
#unihiker text
gui.draw_text(text="HI UNIHIKER",origin="center",x=120,y=160,color="#0066CC")

while True:
    time.sleep(1)
```
(6) Click the button as follows to run the program on the UNIHIKER.  

![image.png](img/Thonny - Python/1696933538272-f10cb588-74a8-4e12-9120-8a6bf59281f2.png)  

After running the code, the board will execute it, and you can observe the running result directly on the board itself.  

![image.png](img/Thonny - Python/1697095978856-12c182bd-0395-4e0c-a842-25b2f6f909d4.png){width=300, style="display:block;margin: 0 auto"}   
  
---  
**Congratulations, you have successfully implemented programming control for the UNIHIKER. Now, you can explore exciting projects or understanding deeper of UNIHIKER.The possibilities are endless with UNIHIKER. Have fun exploring and learning!**  

**1. Discover more programming exercises: [Examples](../Examples/PythonCodingExamples/index.md)**  
**2. Explore Python libraries related to UNIHIKER: [Reference](../LanguageReference/UNIHIKER_Library/index.md)**  
**3. Gain insights into the built-in hardware of UNIHIKER: [Hardware ](../HardwareReference/hardware_reference_introduction.md)**    

---  

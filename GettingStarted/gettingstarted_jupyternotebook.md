In this tutorial, you will learn about Jupyter Notebook and how to program in it using UNIHIKER.
<a name="RMpys"></a>
## **Getting started with Jupyter Notebook**
<a name="C3Tuh"></a>
### **Concept**
Jupyter Notebook is a open-source web application that enables users to create and share documents that include real-time code, equations, visualizations, and explanatory text. It provides an interactive interface for writing and running code in languages such as Python, making it valuable for tasks like data analysis, machine learning, and statistical modeling. The "cell" structure allows for running code independently and easily observing the results, making it an excellent tool for teaching and demonstrations.<br />![image.png](img/Jupyter Notebook(build-in) - Python/1694761069647-6dd94387-1520-42d6-8135-eaeb71680814.png)
<a name="lZdFc"></a>
### **Installation**
Jupyter Notebook is already built-in for UNIHIKER, so there is no need to install the application on your computer.
<a name="w8vW2"></a>
### **Requirements** 
Jupyter Notebook is a web-based application, so it requires the use of a computer's web browser. It is compatible with most common browsers, except for Internet Explorer. Some recommended browsers include:

- Google Chrome
- Mozilla Firefox
- Safari
- Microsoft Edge

!!! Note
    Jupyter Notebook can be used on any platform, including Windows, Linux, and macOS, as long as one of the recommended browsers is installed. This allows for seamless utilization of the application.<br />

![image.png](img/Jupyter Notebook(build-in) - Python/1695698225050-8d611862-9fba-4aa6-9ece-b1ca8cdc074f.png)
<a name="crSyD"></a>
## **Starting up the UNIHIKER**
<a name="dJkok"></a>
### **Connect the UNIHIKER**
To begin, connect the UNIHIKER board to your computer using the Type-C to USB cable. Once connected and powered on, the UNIHIKER logo will appear on the screen.<br />![](img/Jupyter Notebook(build-in) - Python/1691476703505-51223828-f994-438e-a0a5-f4577792ea1e.png){width=800, style="display:block;margin: 0 auto"}  
!!! Note
    1. For optimal performance, please ensure that you plug the USB cable directly into your computer's USB port without using an extension cord or dock. If you encounter any connection issues, please refer to the FAQ section for possible solutions.
    2. When the UNIHIKER is connected to your computer via USB, the IP address will be fixed at 10.1.2.3. You can find this IP address in the "Home" menu on the UNIHIKER board.
<a name="PX7es"></a>
## **Run a simple example with Python code**
（1）To access the local web page menu on the UNIHIKER, open a browser (not IE) and enter the website address 10.1.2.3. This will take you to the UNIHIKER's local web page.<br />  
![image.png](img/Jupyter Notebook(build-in) - Python/1694773604607-b2c829db-8e51-412f-9e01-58ad69b8126b.png)<br />Note: To go directly to the Jupyter page, enter 10.1.2.3:8888 in your browser (make sure to enable the Jupyter service first).<br />  
（2）The UNIHIKER's local web page menu has four sections: 'Home', 'Application Services', 'Network Settings', and 'File Upload'. We will go over each of these sections in more detail later. For now, select the "Service Toggle" and check the status of Jupyter. If it is disabled, click on "Start" and wait for the status to change to "Enabled". Then, click on "Open Page" to access the Jupyter programming page.<br />  
![image.png](img/Jupyter Notebook(build-in) - Python/1694774664508-543daeab-3721-4ca0-bfdc-bc6c8d490542.png)

（3）Once Jupyter is enabled, click on "New" and then select "Python 3 (ipykernel)" to create a new project. This will open a Jupyter project on the UNIHIKER board.<br />  
![image.png](img/Jupyter Notebook(build-in) - Python/1694774537761-c581bc57-769d-4cdc-8627-3f4698f706dc.png)<br />  

（4）Once you have completed the previous step, you will see a screen like this. The top line is the project name, followed by the menu bar on the second line and the toolbar on the third line. The bottom section is the Cell, which is where you can edit and write code for your project.<br />  
![image.png](img/Jupyter Notebook(build-in) - Python/1694776170047-eee9f6a6-54ed-4073-8bef-f24c9ca08fab.png)<br />  
（5）To rename the project, click on the project name on the top line and enter "Hi UNIHIKER". This will change the name of your project.<br />    

![image.png](img/Jupyter Notebook(build-in) - Python/1694769451735-f647c54c-44ec-47ce-b164-169dea49c43c.png)<br />  （6）After that,  let's insert this code into the cell of the project. Here's a code snippet that will display "HI UNIHIKER" on the screen.  
```python
from unihiker import GUI
import time

gui = GUI()
#unihiker text
gui.draw_text(text="HI UNIHIKER",origin="center",x=120,y=160,color="#0066CC")

while True:
    time.sleep(1)
```  

（7）To run your program on the UNIHIKER, click on the "Run" button on the toolbar or use the shortcut "Shift + Enter". This will execute the code in the current cell and display the output.<br />  
![image.png](img/Jupyter Notebook(build-in) - Python/1694775762908-a6ba240c-f4c1-442d-a40e-0007f64638c0.png)<br />  

!!! note
    To end your program, click on the "Interrupt Kernel" button or go to "Kernel" and select "Restart". This will stop the code execution and allow you to make changes or start a new program.<br />  
    When you click on the "Run" button, the code will run in the Python environment on the UNIHIKER board and the output will be displayed on the screen.<br />  
![](img/Jupyter Notebook(build-in) - Python/1691567717568-d78f0d3e-111f-46d9-858a-b32a8aec528c.png){width=300, style="display:block;margin: 0 auto"}<br />  

  


---  
**Congratulations, you have successfully implemented programming control for the UNIHIKER. Now, you can explore exciting projects or understanding deeper of UNIHIKER.The possibilities are endless with UNIHIKER. Have fun exploring and learning!**  

**1. Discover more programming exercises: [Examples](../Examples/PythonCodingExamples/index.md)**  
**2. Explore Python libraries related to UNIHIKER: [Reference](../LanguageReference/UNIHIKER_Library/index.md)**  
**3. Gain insights into the built-in hardware of UNIHIKER: [Hardware ](../HardwareReference/hardware_reference_introduction.md)**    

---  



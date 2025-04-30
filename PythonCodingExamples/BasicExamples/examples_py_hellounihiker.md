## **Project Introduction**
This project utilizes the dynamic display features of a flexible panel, providing the flexibility to adjust font color, size, and placement. It enables the presentation of any desired text. Below is an example that showcases the display of the phrase "Hello, Unihiker" on the screen.  

![image.png](img/1.Hello,Unihiker/1720601927362-99abc270-44b8-4898-8d68-2dfb6641d512.png){width=300, style="display:block;margin: 0 auto"}  

## **Hardware Required**

- [UNIHIKER](https://www.dfrobot.com/product-2691.html)  

## **Code**
When utilizing the unihiker library to display text on the screen, the initial step is to create a GUI object. Then, the draw_text() function of the GUI object is used to generate a text object, specifying the desired content, coordinate position, font size, color, and other attributes of the text. In cases where certain attributes of the text need to be updated or modified, the config() function of the text object can be directly used to achieve this.  


````python title="hello_unihiker"
--8<-- "examplesCode/hello_unihiker.py"
````


## **Demo Effect**
![image.png](img/1.Hello,Unihiker/1720601923889-30aab991-42a1-40f7-869f-5bbd7f1729a9.png){width=300, style="display:block;margin: 0 auto"}  

---  



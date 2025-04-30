## **Project Introduction**
Utilizing the screen display function of UNIHIKER, it is possible to generate and display a QR code. This project primarily utilizes the draw_qr_code() function to implement the display of a QR code on the UNIHIKER screen. The QR code in this project links to UNIHIKER's wiki, providing a better demonstration of the capabilities of the draw_qr_code() function for educational purposes.  

![7.1.png](img/7. QR code display/1717472727639-8571be88-4778-40c1-b3ae-6bd0dd8402bd.png){width=300, style="display:block;margin: 0 auto"}   

## **Hardware Required**

- [UNIHIKER](https://www.dfrobot.com/product-2691.html)  

## **Code**
In order to display a QR code on the UNIHIKER screen, the instantiated GUI object should be used to call the draw_qr_code() function and the desired URL should be filled in as the text parameter.  

```python
from unihiker import GUI

u_gui=GUI()
QR=u_gui.draw_qr_code(text="https://www.unihiker.com/wiki/",x=70,y=100,w=100)

while True:
    pass
```  

## **Demo Effect**
![](img/7. QR code display/1717472395674-e84581c5-a4bf-413d-ac75-b030728f4a79.png){width=300, style="display:block;margin: 0 auto"}  

---  



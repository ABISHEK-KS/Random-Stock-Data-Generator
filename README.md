# Random-Stock-Data-Generator


Hello everybody !  
I created a random stock generator using random module in python. Basically , it creates a dataframe and does the following   
1) Create profiling reports in html covering variable overviews   
2) Write data to excel sheet   
3) Create a pdf report demonstrating seasonal dependencies (TSA) and scatter and line plots for four parameters (high,low,open close) using mpdf  

POINTS TO NOTE:   

 I have tested the code over 50 times , and I have found few critical points for which I shall update my code as soon as possible  
 
 1) There are some discrepancies in the values of high and low. For instance , the value of high on one particular day might be the lowest of the set of all four parameters on the given date  
 2) There's a difference between close value on a given day and the opening value for the next day , this again is due to random module's degree of randomness (or as people call it entropy)  
 
 2)----> can be attributed to hypothetical corporate scenarios in the generation   
 
 NOTE :  
 
 The four graphs (line plots named DvH , DvL , DvO , DvC ) and seasonal dependancy plots (MDO,MDC,MDH,MDL) seem to appear very , very similar  
 Upon closer inspection , there are certain peaks which do not occur in each of the aforementioned graphs and constitues their uniqueness.  
 Please have a closer look.  
 
 Here are some snaps 
 
 ![image](https://user-images.githubusercontent.com/97246536/213772913-37d911a7-da4d-4be7-a084-288f1a05872d.png)
 
 ![image](https://user-images.githubusercontent.com/97246536/213773089-81a0356d-85f6-4fb6-88c9-9a7c601b5132.png)

![DvO](https://user-images.githubusercontent.com/97246536/213773145-93f7a791-0a87-4012-8308-e80438257bff.png)

PLEASE DO NOT COPY OR STEAL MY CODE.   


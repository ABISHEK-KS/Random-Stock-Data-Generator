import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_profiling as pp
from statsmodels.tsa.seasonal import seasonal_decompose
from fpdf import FPDF
datelist=[]
size=int(input('ENTER SIZE/NO: OF DAYS : '))


yearlist=[x for x in range(1980,2024)]
monthlist=[x for x in range(1,13)]
daylist=[x for x in range(1,32)]
year=random.choice(yearlist)
month=random.choice(monthlist)
day=random.choice(daylist)


for j in range(size): 
    if month==8 and day==30: 
        day=31
    if month==2 and year%4==0 and day==28:
        day+=1
    if month==2 and year%4==0 and day==29: 
        month+=1
        day=1
    if month==2 and year%4!=0 and day==29: 
        day=1
        month+=1        

    if month%2==0 and month!=8 and day>30: 
        month+=1
        day=1
    if month==8 and day>31:
        day=1
        month+=1    
    if month%2==1 and day>31: 
        month+=1
        day=1
    if month>12: 
        month=month%12
        year+=1
    if month==12 and day>31: 
        day=1     
        month=1  
        year+=1
                      
    date=str(day)+'-'+str(month)+'-'+str(year)
    datelist.append(date)
    day+=1
openlist=[]
closelist=[]
highlist=[]
lowlist=[]
openval=[]
randomopenval=round(random.uniform(0.0,99999.0),2)

upperbound=randomopenval-(randomopenval*0.095)
lowerbound=randomopenval+(randomopenval*0.095)

randomcloseval=round(random.uniform(upperbound,lowerbound),2)
randomhighval=round(random.uniform(upperbound,lowerbound),2)

lb2=randomhighval-(randomhighval*0.095)
randomlowval=round(random.uniform(randomopenval,lb2))

highlist.append(randomhighval)
lowlist.append(randomlowval)

openlist.append(randomopenval)
closelist.append(randomcloseval)

for j in range(size-1):
 upperbound=randomopenval-(randomopenval*0.095)
 lowerbound=randomopenval+(randomopenval*0.095)

 randomcloseval=round(random.uniform(upperbound,lowerbound),2)
 randomopenval=round(random.uniform(upperbound,lowerbound),2)

 openlist.append(randomopenval)
 closelist.append(randomcloseval)

 randomhighval=round(random.uniform(upperbound,lowerbound),2)

 lb2=randomhighval-(randomhighval*0.095)
 randomlowval=round(random.uniform(randomopenval,lb2))

 highlist.append(randomhighval)
 lowlist.append(randomlowval)
df=pd.DataFrame(list(zip(datelist,openlist,highlist,lowlist,closelist)),columns=['Date','Open','High','Low','Close'])
df.to_excel('RANDOM_STOCK_DATA.xlsx')
profrep=pp.ProfileReport(df)
profrep.to_file('RSD_PROFILING.html')


plt.plot(df['Date'],df['Open'])
plt.xlabel('Date')
plt.ylabel('Open')
plt.title('DvO - Date vs Open')
plt.savefig('DvO.png')
plt.close()


plt.plot(df['Date'],df['Close'])
plt.xlabel('Date')
plt.ylabel('Close')
plt.title('DvC - Date vs Close')
plt.savefig('DvC.png')
plt.close()


plt.plot(df['Date'],df['High'])
plt.xlabel('Date')
plt.ylabel('High')
plt.title('DvH - Date vs High')
plt.savefig('DvH.png')
plt.close()


plt.plot(df['Date'],df['Low'])
plt.xlabel('Date')
plt.ylabel('Low')
plt.title('DvL - Date vs Low')
plt.savefig('DvL.png')
plt.close()

plt.scatter(df['Date'],df['Open'])
plt.xlabel('Date')
plt.ylabel('Open')
plt.title('DvO - Date vs Open')
plt.savefig('openscatter.png')
plt.close()

plt.scatter(df['Date'],df['Close'])
plt.xlabel('Date')
plt.ylabel('Close')
plt.title('DvC - Date vs Close')
plt.savefig('closescatter.png')
plt.close()

plt.scatter(df['Date'],df['High'])
plt.xlabel('Date')
plt.ylabel('High')
plt.title('DvH - Date vs High')
plt.savefig('highscatter.png')
plt.close()

plt.scatter(df['Date'],df['Low'])
plt.xlabel('Date')
plt.ylabel('Low')
plt.title('DvL - Date vs Low')
plt.savefig('lowscatter.png')
plt.close()

seasdec=seasonal_decompose(df['Open'],model='multiplicative', period=1)
seasdec.plot()
plt.savefig('MDO.png')
plt.close()

seasdec=seasonal_decompose(df['Close'],model='multiplicative', period=1)
seasdec.plot()
plt.savefig('MDC.png')
plt.close()

seasdec=seasonal_decompose(df['High'],model='multiplicative', period=1)
seasdec.plot()
plt.savefig('MDH.png')
plt.close()

seasdec=seasonal_decompose(df['Low'],model='multiplicative', period=1)
seasdec.plot()
plt.savefig('MDL.png')
plt.close()
mpdf=FPDF()

firstfive=df.head()
lastfive=df.tail()
mpdf.add_page()
mpdf.set_font('Arial','B',20)
mpdf.cell(50,10,'STOCK REPORT')
mpdf.ln(30)

mpdf.set_title('STOCK REPORT')

mpdf.text(10,30,'Script written by ABISHEK.K.S') 
mpdf.text(10,50,'Studying at Sri Sairam Engineering College , Chennai')

mpdf.text(20,70,'Tech used  ')
mpdf.text(20,80,'*Statistics Module'  )
mpdf.text(20,90,'*Random (Python)  ')
mpdf.text(20,100,'*Pandas Profiling  ')
mpdf.text(20,110,'*Numpy  ')
mpdf.text(20,120,'*Sklearn for ML implementation: ')
mpdf.text(20,130,'*Numpy  ')
mpdf.text(20,140,'*Pandas  ')
mpdf.text(20,150,'*Matplotlib  ')
mpdf.text(20,160,'*Statsmodels   ')
mpdf.text(20,170,'*FPDF   ')
mpdf.text(20,180,'*Seasonal decomposition plot present in dependancy   ')
mpdf.text(10,200,'NOTE :')
mpdf.text(20,220,'*Open and close values vary')
mpdf.text(20,230,'Script discrepancies are due to ')
mpdf.text(20,240,'Random module selection ')
mpdf.text(20,250,'Please do not duplicate script')
mpdf.text(20,260,'Subgraphs may look similar')
mpdf.text(20,270,'But differences are present')



mpdf.add_page()
mpdf.set_font('Arial','B',16)
mpdf.text(10,120,'MDO-MULTIPLICATIVE SEASONAL DECOMPOSTION')
mpdf.text(10,130,'OF OPEN PARAMETER')
mpdf.image('MDO.png',10,10,100,100)
mpdf.image('openscatter.png',10,150,100,100)
mpdf.image('DvO.png',100,150,100,100)
mpdf.text(70,260,'Scatter Plot and Line plot')

mpdf.add_page()
mpdf.set_font('Arial','B',16)
mpdf.text(10,120,'MDC-MULTIPLICATIVE SEASONAL DECOMPOSTION')
mpdf.text(10,130,'OF CLOSE PARAMETER')
mpdf.image('MDC.png',10,10,100,100)
mpdf.image('closescatter.png',10,150,100,100)
mpdf.image('DvC.png',100,150,100,100)
mpdf.text(70,260,'Scatter Plot and Line plot')

mpdf.add_page()
mpdf.set_font('Arial','B',16)
mpdf.text(10,120,'MDC-MULTIPLICATIVE SEASONAL DECOMPOSTION')
mpdf.text(10,130,'OF HIGH PARAMETER')
mpdf.image('MDH.png',10,10,100,100)
mpdf.image('highscatter.png',10,150,100,100)
mpdf.image('DvH.png',100,150,100,100)
mpdf.text(70,260,'Scatter Plot and Line plot')

mpdf.add_page()
mpdf.set_font('Arial','B',16)
mpdf.text(10,120,'MDC-MULTIPLICATIVE SEASONAL DECOMPOSTION')
mpdf.text(10,130,'OF LOW PARAMETER')
mpdf.image('MDL.png',10,10,100,100)
mpdf.image('lowscatter.png',10,150,100,100)
mpdf.image('DvL.png',100,150,100,100)
mpdf.text(70,260,'Scatter Plot and Line plot')

mpdf.output('PDF_REPORT.PDF','F')




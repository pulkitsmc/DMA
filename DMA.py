import pandas as pd

import numpy as np
import matplotlib.pyplot as plt



class strategy_1():
    # This strategy calculates n day DMA and returns plots of daily trend lines

    def loadData(self):
        data = pd.read_csv("Nifty_2003.csv")
        return data

    # Calculates n Day Moving Average

    def Simple_Moving_Average(self, n, data):

        ma = [None] * n
        for i in range(len(data) - n):
            ma.append(np.mean(data["Close"][i:i + n]))

        return ma
    
    
  
    
    def EMA_Cal(self,n,data):
        
        ema=[None]*n
        
        
        sma=np.mean(data["Close"][0:200])
        
        ema.append(sma)
        
        factor=2/(n+1)
        
        for i in range(len(data)-n-1):
            sma=np.mean(data["Close"][i+1:i+n+1])
            
            ema.append(factor*(data["Close"][i+n+1]-ema[i+n])+ema[i+n])
            
        return ema    
        

            

    # Plots curve of a time series
    def plot(x, data):
        plt.plot(data["Close"][200:])
        plt.plot(x)

    def trend_line(self, n, data):

        ma = self.EMA_Cal(n, data)
        trend = [None] * n
        for i in range(n, len(ma)):

            if (data["Close"][i] - ma[i]) / (data["Close"][i]) > 0.005:
                trend.append(1)
            elif (data["Close"][i] - ma[i]) / (data["Close"][i]) < -0.005:
                trend.append(0)
            else:
                trend.append(trend[i - 1])
        plt.figure(figsize=(30, 15))
        plt.plot(data["Close"])
        plt.plot(ma,linewidth=5)
        flag = 0
        for i in range(len(trend)):

            if trend[i] == None:
                continue

            if trend[i] == trend[i - 1] and flag == 0:
                
                flag = 1
                start = i

            if trend[i] == trend[i - 1] and flag == 1:
                continue

            if trend[i] != trend[i - 1] and flag == 1:

                end = i
                flag = 0
                x = []
                for k in range(start, end):
                    x.append(int(k))
                y = []
                for j in range(start, end):
                    y.append(data["Close"][j])

                x = np.array(x)
                y = np.array(y)
                m = (((np.mean(x) * np.mean(y)) - np.mean(x * y)) / ((np.mean(x) * np.mean(x)) - np.mean(x * x)))
                m = round(m, 2)
                b = (np.mean(y) - np.mean(x) * m)
                b = round(b, 2)
                
               
                if trend[i-1]==0 and trend[i]==1:
                    
                    
                    plt.plot(x, (m * x) + b,linewidth=3,color='red')
                    
                    
                else:
                    plt.plot(x, (m * x) + b,linewidth=3,color='green')
                    


if __name__ == "__main__":
    s = strategy_1()

    data = s.loadData()

    s.trend_line(200, data)-
 
    plt.show()







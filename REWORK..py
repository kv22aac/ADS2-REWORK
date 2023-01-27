# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:16:01 2023

@author: keert
"""


# importing pandas library
import pandas as pd
# importing numpy library
import numpy as np
# importing matplotlib library
import matplotlib.pyplot as plt

# function to read the file
def read_file(dfile):
    
    
    """
    

    Parameters
    ----------
    dfile : csv fiel
    

    Returns
    -------
    df : data frame with years as columns
        
    dttranspose : dataframe with countries as columns
        
    """
    df = pd.read_csv(dfile)
    print("standard deviation",np.std(df))
    #transposing the file
    dttranspose= df.set_index('Country Name').transpose()
    
    return df, dttranspose
    
#choosing few countries
coun_list1= ['Australia','Bulgaria','Cyprus','Iraq']

coun_list2= ['Australia','Bulgaria','Cyprus','Iraq']

#plot bardata

def filter_bar_data(df):
    df=df[['Country Name','2000','2002','2004','2006','2008']]
    df = df [(df["Country Name"]=="Australia") | 
                 (df["Country Name"]=="Bulgaria") | 
                 (df["Country Name"]=="Cyprus") |
                 (df["Country Name"]=="Iraq")]
            
                
                              
    return df
#filtering the data to plot linedata
def filter_line_plot(df):
    """
    

    Parameters
    ----------
    df : data frame with years as columns.

    Returns
    -------
    df : plot bardata
    """
    df=df[['Country Name','Indicator Name','2000','2003','2006','2009','2012']]
    df =df  [(df["Country Name"]=="Australia") | 
                 (df["Country Name"]=="Bulgaria") | 
                 (df["Country Name"]=="Cyprus") |
                 (df["Country Name"]=="Iraq")]
                
                 
                
    return df

    
  #drow a vertical bar chart  
def barplot(df, label1, label2):
    plt.figure(figsize=(25,20))
    # creating subplots 
    ax= plt.subplot(1,1,1)
    x = np.arange(4)
    width= 0.2

    bar1= ax.bar(x, df["2000"],width,label= 2000)
    bar2= ax.bar(x+width, df["2004"], width, label=2004)
    bar3= ax.bar(x+width*2, df["2008"], width, label=2008)
    
    ax.set_xlabel("Country Names", fontsize= 40)
    ax.set_ylabel(label1, fontsize= 35)
    ax.set_title(label2, fontsize=35)
    ax.set_xticks(x, coun_list1, fontsize=35, rotation=90)
    ax.legend(fontsize=25)
             
    ax.bar_label(bar1, padding=2, rotation=14, fontsize= 16)
    ax.bar_label(bar2, padding=2, rotation=14, fontsize= 16)
    ax.bar_label(bar3, padding=2, rotation=14, fontsize= 16)
    plt.show()    
     
 #drow a line graph          
def line_plot(df,label1,label2):
    plt.figure(figsize=(25,20))
    dd = df.set_index('Country Name')
    tran = dd.transpose()
    tran = tran.drop(index=['Indicator Name'])
    for i in range(len(coun_list2)):
        plt.plot(tran.index, tran[coun_list2[i]], label=coun_list2[i])
        
    plt.title(label2, size=20)
    plt.xlabel("Years", size=15)
    plt.ylabel(label1, size=15)
    plt.xticks(rotation=90)
    plt.legend(fontsize=15)
    plt.savefig("lineplot.png")
    plt.show()
#locating each path for each data  
#reading the 1st file         
population_data, population_data1 = read_file("C:/Users/keert/Desktop/Assignment/assignment 2/pop.csv")
population_data = filter_bar_data(population_data)
#reading the 2nd file  
energyuse_data, energyuse_data1 = read_file("C:/Users/keert/Desktop/Assignment/assignment 2/energ.csv") 
energyuse_data= filter_bar_data(energyuse_data)
#reading the 3rd file  
CO2_data, CO2_data1=read_file("C:/Users/keert/Desktop/Assignment/assignment 2/co2.csv")   
CO2_data= filter_line_plot(CO2_data)
#reading the 4th file  
greenhouse_data, greenhouse_data1 = read_file("C:/Users/keert/Desktop/Assignment/assignment 2/green.csv")             
greenhouse_data= filter_line_plot(greenhouse_data)          
#assigning the x axis, y axis names
barplot(population_data, "population in total","population")
barplot(energyuse_data, "Energy use in kg","Energy use") 

line_plot(CO2_data,"CO2 Emission(KT)","CO2 Emission")
line_plot(greenhouse_data,"Total greenhouse gas emmission in %","Total greenhouse gas emmission ")
#function to find the mean
def CO2_emission_mean():
    
    
    """
    

    Returns
    -------
    Meandata: dataframe with average of CO2 emissions of 4 countries

    """
    #reading the dataframes from green emission data
    df,ttranspose = read_file("C:/Users/keert/Desktop/Assignment/assignment 2/co2.csv")
    data = df.set_index('Country Name')
    
    dtrans=data.transpose()
    dtrans = dtrans.drop(index='Indicator Name')
    dtrans = dtrans.drop(index='Indicator Code')
    dtrans = dtrans.drop(index='Country Code')
    #replacing the NaN values
    clean_data = dtrans.fillna(0)
    meandata = clean_data[['Australia','Bulgaria','Cyprus','Iraq']].mean()
    
    return meandata
#calling the function   
meandata= CO2_emission_mean()
meandata = meandata.to_csv("meanCO2.csv")
    
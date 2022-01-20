import csv
import plotly_express as px
import plotly.figure_factory as pf
import pandas as pd
import statistics
import plotly.graph_objects as pg
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#Below is the figure for OVERALL POPULATION DATA
#fig = pf.create_distplot([data],["Math Score"],show_hist=False)
#fig.show()

Mean = statistics.mean(data)
print("Mean is: "+ str(Mean))

StdDeviation = statistics.stdev(data)
print("Standard Deviation is: "+ str(StdDeviation))

def random_set_of_mean(counter): 
    dataset = []

    for i in range(0, counter): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 

    mean = statistics.mean(dataset) 
    return mean

#Pass the number of times you want the mean of the datapoint as a parameter in range() of the for loop
mean_list = []

#loop it 1000 times
for i in range(0,1000):
    #take random 100 scores
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

#Calculating mean and std deviation of sampling distribution
mean = statistics.mean(mean_list)
print("This is the mean of the sample: "+ str(mean))

stdDeviation = statistics.stdev(mean_list)
print("This is the standard deviation of the sample: "+ str(stdDeviation))

#Below is to plot DATA for the SPECIFIC sample
#fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False) 
#fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="Mean")) 
#fig.show() 

#Standard deviation of the sampling distribution = Standard deviation of the population / sqrt (100)

#Finding the standard deviation starting and ending values 
first_std_deviation_start, first_std_deviation_end = Mean-StdDeviation, Mean+StdDeviation 
second_std_deviation_start, second_std_deviation_end = Mean-(2*StdDeviation), Mean+(2*StdDeviation) 
third_std_deviation_start, third_std_deviation_end = Mean-(3*StdDeviation), Mean+(3*StdDeviation)

#Separating data into 3 segments SO THAT we can find where MOST POINTS/VALUES OF THE STANDARD DEVIATION LIE
print("Std 1 (Start & End): ",first_std_deviation_start, first_std_deviation_end) 
print("Std 2 (Start & End): ",second_std_deviation_start, second_std_deviation_end) 
print("Std 3 (Start & End): ",third_std_deviation_start,third_std_deviation_end)

#Plotting the final graph (FOR 3 DIFFERENT SAMPLES) with traces 
#fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False) 
#fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
#fig.add_trace(pg.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="Std Deviation 1 Start")) 
#fig.add_trace(pg.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Std Deviation 1 End")) 
#fig.add_trace(pg.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="Std Deviation 2 Start")) 
#fig.add_trace(pg.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="Std Deviation 2 End")) 
#fig.add_trace(pg.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="Std Deviation 3 Start")) 
#fig.add_trace(pg.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="Std Deviation 3 End"))

#fig.show()

#Finding the mean of the FIRST data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df = pd.read_csv("TechMethod.csv")
data = df["Math_score"].tolist() 
mean_of_sample1 = statistics.mean(data) 
print("Mean of sample 1:- ",mean_of_sample1) 

fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(pg.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="Mean of sample"))  
fig.add_trace(pg.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Std Deviation 1 End")) 

fig.show()

#Finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
df = pd.read_csv("ExtraClass.csv") 
data = df["Math_score"].tolist() 
mean_of_sample2 = statistics.mean(data) 
print("Mean of sample 2:- ",mean_of_sample2) 

fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(pg.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD EXTRA CLASSES")) 
fig.add_trace(pg.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(pg.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 

fig.show()

#Finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot. 
df = pd.read_csv("FunMaths.csv") 
data = df["Math_score"].tolist() 
mean_of_sample3 = statistics.mean(data) 
print("Mean of sample 3:- ",mean_of_sample3) 

fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(pg.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS")) 
fig.add_trace(pg.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(pg.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 

fig.show()

#Z-Score = Mean of sample-Total Mean/Total StdDeviation
#Z-Score only goes from -1, 0 to 1. It tells the ACCURACY of the OVERALL data representation
ZScore = (mean_of_sample3-Mean)/StdDeviation
print("This is the Z-Score: "+ str(ZScore))

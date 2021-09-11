import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")

data = df["claps"].tolist()

population_mean = statistics.mean(data)
population_standard_devation = statistics.stdev(data)

print("mean: ",population_mean)
print("deviation: ",population_standard_devation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([mean_list], ["claps"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.006],mode = "lines",name = "MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        setOfMeans = random_set_of_mean(100)
        mean_list.append(setOfMeans)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("mean of sampling disturbution: ", mean)

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        setOfMeans = random_set_of_mean(100)
        mean_list.append(setOfMeans)

    standard_deviation = statistics.stdev(mean_list)
    print("standard deviation of sampling disturbution: ", standard_deviation)

standard_deviation()
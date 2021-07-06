import csv
from typing import Sized
import plotly.express as px
import numpy as np

with open('data.csv', newline='') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Size", y="averageTime")
    fig.show()


def getDataSource(data_path):
    size = []
    averageTime = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size.append(float(row["Size"]))
            averageTime.append(float(row["averageTime"]))

    return {"x": size, "y": averageTime}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation)
    print("Correlation between Size of TV and Watching Time is :  ",
          correlation[1, 0])


def setup():
    data_path = "data.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()

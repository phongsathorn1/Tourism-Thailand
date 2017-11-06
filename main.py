"""
    Plot graph from dataset
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pygal

def plotgraph(filename):
    """
        plot graph
    """
    dataframe = pd.read_excel(filename)
    lst_year = dataframe.ix[0].index.values[1:].tolist()
    country = dataframe['Country']

    bar_chart = pygal.Line()
    bar_chart.title = 'South Asia'
    bar_chart.x_labels = map(str, lst_year)

    for i in range(len(dataframe)):
        bar_chart.add(country[i], dataframe.ix[i][1:])

    bar_chart.render_to_file("chart/"+filename[7:-5]+".svg")

def main():
    """
        main function
    """
    files = [filename for filename in open("dataset/file.txt")]
    for item in files:
        plotgraph("dataset/" + item.strip("\n"))

main()
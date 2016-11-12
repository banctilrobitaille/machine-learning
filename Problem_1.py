from Dataset import Dataset
from DecisionTreeUtils import DecisionTreeUtils
from Node import Node
from DecisionTreeBuilder import DecisionTreeBuilder

if __name__ == '__main__':
    initialDataSet = Dataset.from_csv_file("02_homework_dataset.csv")
    DecisionTreeBuilder().buildWith(initialDataSet, depth=2).toString()
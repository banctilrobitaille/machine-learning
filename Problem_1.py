from Dataset import Dataset
from DecisionTreeUtils import DecisionTreeUtils
from Node import Node
from DecisionTreeBuilder import DecisionTreeBuilder

if __name__ == '__main__':
    initialDataSet = Dataset.from_csv_file("02_homework_dataset.csv")
    DecisionTreeBuilder().buildWith(initialDataSet, depth=2).toString()



    """rootNode = Node(initialDataSet)
    rootNode.giniIndex = DecisionTreeUtils.computeGiniIndexOf(rootNode)
    splitCondition = DecisionTreeUtils.findOptimalSplitConditionFor(rootNode)
    splitCondition2 = DecisionTreeUtils.findOptimalSplitConditionFor(splitCondition.rightNode)
    splitCondition3 = DecisionTreeUtils.findOptimalSplitConditionFor(splitCondition2.leftNode)

    print(splitCondition)
    print("Left Node")
    print(splitCondition.leftNode)
    print("Right Node")
    print(splitCondition.rightNode)
    print("\n")
    print("-------------------------------------------------------")
    print("\n")
    print(splitCondition2)
    print("Left Node")
    print(splitCondition2.leftNode)
    print("Right Node")
    print(splitCondition2.rightNode)
    print("\n")
    print("-------------------------------------------------------")
    print("\n")
    print(splitCondition3)
    print("Left Node")
    print(splitCondition3.leftNode)
    print("Right Node")
    print(splitCondition3.rightNode)"""

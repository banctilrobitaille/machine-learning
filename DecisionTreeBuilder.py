from Node import Node
from DecisionTree import DecisionTree
from DecisionTreeUtils import DecisionTreeUtils


class DecisionTreeBuilder:
    def buildWith(self, initialDataSet, depth):
        decisionTree = DecisionTree().withRootNode(Node(initialDataSet))

        while decisionTree.depth is not depth and not decisionTree.isOptimal:
            newNodes = []
            for node in decisionTree.unsplittedNodes:
                node.giniIndex = DecisionTreeUtils.computeGiniIndexOf(node)
                node.split(DecisionTreeUtils.findOptimalSplitConditionFor(node))
                newNodes.extend(node.childs)
            decisionTree.addNodes(newNodes)

        return decisionTree
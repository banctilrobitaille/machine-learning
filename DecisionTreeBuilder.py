from Node import Node
from DecisionTree import DecisionTree
from DecisionTreeUtils import DecisionTreeUtils


class DecisionTreeBuilder:
    def buildWith(self, initialDataSet, depth=10):
        decisionTree = DecisionTree().withRootNode(Node(initialDataSet))

        while decisionTree.depth is not depth and not decisionTree.isOptimal:
            newNodes = []
            for node in decisionTree.unpureNodes:
                node.giniIndex = DecisionTreeUtils.computeGiniIndexOf(node)
                node.splitFromCondition(DecisionTreeUtils.findOptimalSplitConditionFor(node))
                newNodes.extend(node.childs)
            decisionTree.addNodes(newNodes)

        return decisionTree
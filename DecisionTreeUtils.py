import math
from Node import Node
from Dataset import Dataset
from SplitCondition import SplitCondition
from operator import attrgetter


class DecisionTreeUtils:
    @staticmethod
    def computeGiniIndexOf(node):
        probabilitySummation = 0

        for value in node.numbersOfValueByClass.values():
            probabilitySummation += math.pow(value / node.numberOfInstances, 2)

        return 1.0 - probabilitySummation

    @staticmethod
    def findOptimalSplitConditionFor(node):
        optimalSplitCondition = SplitCondition(None, None)

        for feature in node.features:
            for threshold in node.dataSet.getInstancesValueFromFeature([feature]):
                leftNode = Node(Dataset(node.features, list(
                        filter(lambda instance: instance.valueByFeature[feature] <= threshold, node.instances))))
                rightNode = Node(Dataset(node.features, list(
                        filter(lambda instance: instance.valueByFeature[feature] > threshold, node.instances))))

                leftNode.giniIndex = DecisionTreeUtils.computeGiniIndexOf(leftNode)
                rightNode.giniIndex = DecisionTreeUtils.computeGiniIndexOf(rightNode)

                splitCondition = SplitCondition(feature, threshold).withLeftNode(leftNode).withRightNode(rightNode)
                splitCondition.gain = DecisionTreeUtils.computeGain(node, splitCondition)

                if splitCondition.isBetterThan(optimalSplitCondition):
                    optimalSplitCondition = splitCondition

        return optimalSplitCondition

    @staticmethod
    def computeGain(parentNode, splitCondition):
        leftNode = splitCondition.leftNode
        rightNode = splitCondition.rightNode
        return parentNode.giniIndex - (leftNode.numberOfInstances / parentNode.numberOfInstances) * leftNode.giniIndex \
               - (rightNode.numberOfInstances / parentNode.numberOfInstances) * rightNode.giniIndex

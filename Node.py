import numpy as np


class Node:
    __giniIndex = 0
    __numberOfValueByClass = {}
    __dataSet = None
    __parentNode = None
    __leftNode = None
    __rightNode = None
    __splitCondition = None
    __isPure = False

    def __init__(self, dataSet, parentNode=None):
        self.__dataSet = dataSet
        self.__numberOfValueByClass = dataSet.getNumberOfInstancesByClass()
        self.__parentNode = parentNode

    @property
    def giniIndex(self):
        return self.__giniIndex

    @giniIndex.setter
    def giniIndex(self, value):
        self.__giniIndex = value

    @property
    def numbersOfValueByClass(self):
        return self.__numberOfValueByClass

    @numbersOfValueByClass.setter
    def numbersOfValueByClass(self, value):
        self.__numberOfValueByClass = value

    @property
    def numberOfInstances(self):
        return self.__dataSet.getNumberOfInstances()

    @property
    def parentNode(self):
        return self.__parentNode

    @parentNode.setter
    def parentNode(self, node):
        self.__parentNode = node

    @property
    def childs(self):
        childs = []
        if self.__leftNode is not None:
            childs.append(self.__leftNode)
        if self.__rightNode is not None:
            childs.append(self.__rightNode)

        return childs

    @property
    def dataSet(self):
        return self.__dataSet

    @property
    def features(self):
        return self.__dataSet.features

    @property
    def instances(self):
        return self.__dataSet.instances

    @property
    def splitCondition(self):
        return self.__splitCondition

    @property
    def isPure(self):
        return self.__isPure

    @splitCondition.setter
    def splitCondition(self, splitCondition):
        self.__splitCondition = splitCondition

    def split(self, splitCondition):
        if splitCondition.gain is not None and splitCondition.gain > 0.0:
            self.__leftNode = splitCondition.leftNode
            self.__rightNode = splitCondition.rightNode
            self.__leftNode.parentNode = self
            self.__rightNode.parentNode = self
            self.__splitCondition = splitCondition

        self.__isPure = True

    def __str__(self):
        return str(np.vstack(list(map(lambda instance: str(instance), self.__dataSet.instances))))

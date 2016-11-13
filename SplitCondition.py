class SplitCondition:
    __feature = None
    __threshold = None
    __leftNode = None
    __rightNode = None
    __gain = None

    def __init__(self, feature, threshold):
        self.__gain = 0
        self.__feature = feature
        self.__threshold = threshold

    @property
    def feature(self):
        return self.__feature

    @property
    def threshold(self):
        return self.__threshold

    @property
    def gain(self):
        return self.__gain

    @gain.setter
    def gain(self, value):
        self.__gain = value

    @property
    def leftNode(self):
        return self.__leftNode

    @property
    def rightNode(self):
        return self.__rightNode

    def withLeftNode(self, node):
        self.__leftNode = node
        return self

    def withRightNode(self, node):
        self.__rightNode = node
        return self

    def isBetterThan(self, splitCondition):
        return self.__gain > splitCondition.gain

    def __str__(self):
        return "Gain: " + str(self.__gain) + " Feature: " + self.__feature + " Threshold: " + str(self.__threshold)

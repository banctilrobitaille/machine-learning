class DecisionTree:
    __rootNode = None
    __nodes = None
    __depth = 0

    def __init__(self):
        self.__nodes = []

    @property
    def numberOfNodes(self):
        return len(self.__nodes)

    @property
    def depth(self):
        return self.__depth

    @property
    def rootNode(self):
        return self.__rootNode

    @property
    def nodes(self):
        return self.__nodes

    @property
    def unsplittedNodes(self):
        return list(filter(lambda node: node.isPure is False, self.__nodes))

    @property
    def isOptimal(self):
        return len(self.unsplittedNodes) is 0

    def withRootNode(self, node):
        self.__rootNode = node
        self.__nodes.append(self.__rootNode)
        return self

    def addNodes(self, nodes):
        self.__nodes.extend(nodes)
        self.__depth += 1

    def toString(self):
        for node in self.__nodes:
            print("\n")
            print(node.splitCondition)
            print(node)
            print("\n")

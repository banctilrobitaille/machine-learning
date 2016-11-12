class Instance:
    __id = None
    __valueByFeature = None
    __class = None

    def __init__(self, id, featuresNames, values):
        self.__valueByFeature = {}
        self.__id = id
        self.__class = values[-1]
        for featureName in featuresNames:
            self.__valueByFeature[featureName] = values[featuresNames.index(featureName)]

    @property
    def clazz(self):
        return self.__class

    @property
    def valueByFeature(self):
        return self.__valueByFeature

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return "ID: " + str(self.__id) + " " + str(self.__valueByFeature) + " class: " + str(self.__class)

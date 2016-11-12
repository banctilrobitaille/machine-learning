import numpy as np
from CSVUtils import CsvUtils
from Instance import Instance
from collections import Counter


class Dataset:
    __features = None
    __instances = None

    def __init__(self, features, instances):
        self.__features = features
        self.__instances = instances

    @classmethod
    def from_csv_file(cls, csv_file_path):
        rawData = CsvUtils.extractInstancesAndFeaturesFrom(csv_file_path)
        instances = []
        features = rawData.dtype.names[:-1]

        for instance in rawData:
            instances.append(Instance(list(rawData).index(instance), features, instance))

        return cls(features, instances)

    @property
    def features(self):
        return self.__features

    @property
    def instances(self):
        return self.__instances

    @property
    def classesDistributionVector(self):
        return list(map(lambda instance: instance.clazz, self.__instances))

    def getInstancesValueFromFeature(self, features, withClass=False):
        instanceValues = None

        for feature in features:
            if instanceValues is None:
                instanceValues = list(map(lambda instance: instance.valueByFeature[feature], self.__instances))
            else:
                instanceValues = np.column_stack((instanceValues, list(
                        map(lambda instance: instance.valueByFeature[feature], self.__instances))))
        if withClass:
            instanceValues = np.column_stack((instanceValues, self.classesDistributionVector))

        return instanceValues

    def getNumberOfInstancesByClass(self):
        return Counter(list(map(lambda instance: instance.clazz, self.__instances)))

    def getNumberOfInstances(self):
        return len(self.__instances)

import numpy as np


class CsvUtils:
    DATA_DELIMITER = ","

    @staticmethod
    def extractInstancesAndFeaturesFrom(csvFilePath):
        return np.genfromtxt(csvFilePath, delimiter=CsvUtils.DATA_DELIMITER, names=True)

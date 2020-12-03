import pandas as pd
from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException
from com.bridgelabz.censusanalyser.CensusAnalysisHeader import CensusAnalysisHeader


class CensusAnalyzer:

    def __init__(self, path):
        self.path = path

    def record_counter(self):
        """

        :return: number of records in file
        """
        try:
            col_names = repr(CensusAnalysisHeader()).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalysisException("Invalid File Path")
        except ValueError:
            raise CensusAnalysisException("Wrong Delimiter or Invalid Columns Name")


if __name__ == "__main__":
    read_csv = CensusAnalyzer(path="C:/Users/KatK/PycharmProjects/StateCensusAnalyser/Data/IndiaStateCensusData.csv")
    length = read_csv.record_counter()
    print(length)

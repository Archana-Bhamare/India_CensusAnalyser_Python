import pandas as pd
from com.bridgelabz.censusanalyser.CensusAnalyserStateCode import CensusAnalyserStateCode
from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException


class CensusAnalyzer:

    def __init__(self, path):
        self.path = path

    def load_state_code(self):
        """

        :return: number of records in file
        """
        try:
            col_names = repr(CensusAnalyserStateCode()).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalysisException("Invalid File Path")
        except ValueError:
            raise CensusAnalysisException("Wrong Delimiter or Invalid Columns Name")


if __name__ == "__main__":
    read_statecode = CensusAnalyzer(path="C:/Users/KatK/PycharmProjects/StateCensusAnalyser/Data/IndiaStateCode.csv")
    print(read_statecode.load_state_code())

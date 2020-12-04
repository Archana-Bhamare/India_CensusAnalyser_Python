import pandas as pd
from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException


class CensusAnalyzer:

    def __init__(self, path, obj):
        self.path = path
        self.obj = obj

    def record_counter(self):
        """
        :return: number of records in file
        """
        try:
            col_names = repr(self.obj).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalysisException("Invalid File Path")
        except ValueError:
            raise CensusAnalysisException("Wrong Delimiter or Invalid Columns Name")
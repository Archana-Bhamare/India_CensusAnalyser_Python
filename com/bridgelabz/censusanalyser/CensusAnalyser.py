import pandas as pd
from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException
from com.bridgelabz.censusanalyser.CensusAnalysisHeader import CensusAnalysisHeader
<<<<<<< HEAD
from com.bridgelabz.censusanalyser.CensusAnalyserStateCode import CensusAnalyserStateCode
=======
>>>>>>> 4634800e9f8c590650e6f3eaef1c8254e7fa9a14


class CensusAnalyzer:

    def __init__(self, path):
        self.path = path
        
    def record_counter(self):
        """

<<<<<<< HEAD
    def record_counter(self):
        """

=======
>>>>>>> 4634800e9f8c590650e6f3eaef1c8254e7fa9a14
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
<<<<<<< HEAD

=======
    
>>>>>>> 4634800e9f8c590650e6f3eaef1c8254e7fa9a14
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
    read_csv = CensusAnalyzer(path="C:/Users/KatK/PycharmProjects/StateCensusAnalyser/Data/IndiaStateCensusData.csv")
<<<<<<< HEAD
    read_statecode = CensusAnalyzer(path="C:/Users/KatK/PycharmProjects/StateCensusAnalyser/Data/IndiaStateCode.csv")
    length = read_csv.record_counter()
    print(length)
=======
    length = read_csv.record_counter()
    print(length)
    read_statecode = CensusAnalyzer(path="C:/Users/KatK/PycharmProjects/StateCensusAnalyser/Data/IndiaStateCode.csv")
>>>>>>> 4634800e9f8c590650e6f3eaef1c8254e7fa9a14
    print(read_statecode.load_state_code())

from com.bridgelabz.censusanalyser.censusanalyser import CensusAnalyzer
from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException
from com.bridgelabz.censusanalyser.CensusAnalysisHeader import CensusAnalysisHeader
from com.bridgelabz.censusanalyser.CensusAnalyserStateCode import CensusAnalyserStateCode


class CSVLoader(CensusAnalyzer):

    def record_counter(self):
        try:
            return super(CSVLoader, self).record_counter()
        except FileNotFoundError:
            raise CensusAnalysisException("Invalid File Path")
        except ValueError:
            raise CensusAnalysisException("Wrong Delimiter or Invalid Columns Name")

    def load_csv_file_in_list(self):
        return super(CSVLoader, self).load_csv_file_in_list()

    def sort_file(self):
        return super(CSVLoader, self).sort_file()

    def sort_file_by(self, sort_by=None, asc=True):
        return super(CSVLoader, self).sort_file_by(sort_by, asc)


if __name__ == "__main__":
    print("----CSV File----")
    path_csv_file = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCensusData.csv"
    read_csvfile = CSVLoader(path_csv_file, obj=CensusAnalysisHeader())
    print("Number of Records : ", read_csvfile.record_counter())
    print(read_csvfile.load_csv_file_in_list())
    print("Sorted CSV File is : \n", read_csvfile.sort_file())
    print("Sort By Population : \n", read_csvfile.sort_file_by(sort_by='Population', asc=False))
    print("----StateCode File----")
    path_statecode_file = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCode.csv"
    read_statecode = CSVLoader(path_statecode_file, obj=CensusAnalyserStateCode())
    print("Number of Records : ", read_statecode.record_counter())
    print(read_statecode.load_csv_file_in_list())
    print("Sorted State Code File is : \n", read_statecode.sort_file())

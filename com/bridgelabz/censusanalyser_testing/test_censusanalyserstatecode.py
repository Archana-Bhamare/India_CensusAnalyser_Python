from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException
from com.bridgelabz.censusanalyser.censusanalyser import CensusAnalyzer
from com.bridgelabz.censusanalyser.CensusAnalyserStateCode import CensusAnalyserStateCode
import pytest

FILE_PATH = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCode.csv"
WRONG_FILE_PATH = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data1/IndiaStateCode.csv"
WRONG_FILE_TYPE = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCode.txt"
WRONG_FILE_DELIMITER = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCodeInvalidDelimiter.csv"
WRONG_FILE_HEADER = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCodeHeader.csv"

# Test Case 2.1-To ensure the number of records
def test_check_file_record():
    csv_loader = CensusAnalyzer(FILE_PATH, CensusAnalyserStateCode())
    assert csv_loader.record_counter() == 29


# Test Case 2.2-if file incorrect return a custom Exception
def test_check_wrong_file_path():
    csv_loader = CensusAnalyzer(WRONG_FILE_PATH, CensusAnalyserStateCode)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test Case 2.3-file correct but type incorrect returns exception
def test_wrong_file_type():
    csv_loader = CensusAnalyzer(WRONG_FILE_TYPE, CensusAnalyserStateCode)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test case 2.4-file correct but delimiter incorrect return exception
def test_wrong_file_delimiter():
    csv_loader = CensusAnalyzer(WRONG_FILE_DELIMITER, CensusAnalyserStateCode)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test case 2.5-file correct but Header incorrect return exception
def test_wrong_file_header():
    csv_loader = CensusAnalyzer(WRONG_FILE_HEADER, CensusAnalyserStateCode)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()

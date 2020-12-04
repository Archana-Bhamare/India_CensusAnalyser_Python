from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException
from com.bridgelabz.censusanalyser.censusanalyser import CensusAnalyzer
from com.bridgelabz.censusanalyser.CensusAnalysisHeader import CensusAnalysisHeader

import pytest

FILE_PATH = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCensusData.csv"
WRONG_FILE_PATH = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data1/IndiaStateCensusData.csv"
WRONG_FILE_TYPE = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCensusData.txt"
WRONG_FILE_DELIMITER = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCensusWrongDelimeter.csv"
WRONG_FILE_HEADER = "C:/Users/KatK/PycharmProjects/IndiaStateCensusAnalyser/Data/IndiaStateCensusDataHeader.csv"

# Test Case 1.1-To ensure the number of records
def test_check_file_record():
    csv_loader = CensusAnalyzer(FILE_PATH, CensusAnalysisHeader())
    assert csv_loader.record_counter() == 29


# Test Case 1.2-if file incorrect return a custom Exception
def test_check_wrong_file_path():
    csv_loader = CensusAnalyzer(WRONG_FILE_PATH, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test Case 1.3-file correct but type incorrect returns exception
def test_wrong_file_type():
    csv_loader = CensusAnalyzer(WRONG_FILE_TYPE, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test case 1.4-file correct but delimiter incorrect return exception
def test_wrong_file_delimiter():
    csv_loader = CensusAnalyzer(WRONG_FILE_DELIMITER, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()

# Test case 1.5-file correct but Header incorrect return exception
def test_wrong_file_header():
    csv_loader = CensusAnalyzer(WRONG_FILE_HEADER, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()
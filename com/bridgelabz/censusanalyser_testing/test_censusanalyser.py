from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException
from com.bridgelabz.censusanalyser.censusanalyser import CensusAnalyzer
from com.bridgelabz.censusanalyser.CensusAnalysisHeader import CensusAnalysisHeader
from com.bridgelabz.censusanalyser.CSVLoader import CSVLoader
import pytest
import json

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
def test_csvfile_for_wrong_file_path():
    csv_loader = CensusAnalyzer(WRONG_FILE_PATH, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test Case 1.3-file correct but type incorrect returns exception
def test_csvfile_for_wrong_file_type():
    csv_loader = CensusAnalyzer(WRONG_FILE_TYPE, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test case 1.4-file correct but delimiter incorrect return exception
def test_csvfile_for_wrong_file_delimiter():
    csv_loader = CensusAnalyzer(WRONG_FILE_DELIMITER, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


# Test case 1.5-file correct but Header incorrect return exception
def test_csvfile_for_wrong_file_header():
    csv_loader = CensusAnalyzer(WRONG_FILE_HEADER, CensusAnalysisHeader)
    with pytest.raises(CensusAnalysisException):
        csv_loader.record_counter()


def test_csvfile_sorted_file_by_state():
    csv_loader = CensusAnalyzer(FILE_PATH, CSVLoader)
    sorted = csv_loader.sort_file()
    json_dict = json.loads(sorted)
    assert list(json_dict)[0] == "Andhra Pradesh"


def test_csvfile_sorted_file():
    csv_loader = CensusAnalyzer(FILE_PATH, CSVLoader)
    sorted = csv_loader.sort_file()
    json_dict = json.loads(sorted)
    assert list(json_dict)[-1] == "West Bengal"


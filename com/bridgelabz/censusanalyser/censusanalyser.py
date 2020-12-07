import pandas as pd
import csv
import json
from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException


class CensusAnalyzer:
    list_file = []

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

    def load_csv_file_in_list(self):
        r = open(self.path, 'r')
        reader = csv.reader(r)
        for row in reader:
            CensusAnalyzer.list_file.append(row)
        for item in CensusAnalyzer.list_file:
            print(item)

    def sort_file(self):
        data_dict = {}
        r = open(self.path, 'r')
        reader = csv.reader(r)
        sort = sorted(reader)
        for record in sort:
            data_list = list(record)
            data_dict[data_list[0]] = data_list
        return json.dumps(data_dict)

    def sort_file_by(self, sort_by=None, asc=True):
        data = pd.read_csv(self.path)
        data = data.sort_values(sort_by, ascending=asc)
        json_format = data.to_json()
        return json_format

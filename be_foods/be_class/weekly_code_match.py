import pandas as pd
import numpy as np
import math
import re


class WeeklyCodeMatch:

    def __init__(self, inputData):
        self.font_size = 12
        self.normal_column_width = 10
        self.matching_data = '/be_class/matching_data/nav_vs_pronto_item.xlsx'
        self.input_data = '/input/' + inputData

    def data_cleaning(self):
        data = pd.read_excel(self.input_data, header=3)
        data = data.loc[:, ~data.columns.str.contains("^Unnamed")]
        return data.shape

import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import logging as LOG


class CSVReader:
    def __init__(self, file=None):
        self.file = file

    def mydata(self):
        df = pd.read_csv(self.file)
        new_df = df.dropna()
        print(new_df.columns.values)
        return new_df

    def getIDes(self):
        return self.mydata().columns

    def get_base64_chart(self, x_value, y_value, kind):
        df = self.mydata()
        self.validate(df.columns.values, x_value
                      , y_value)
        plt.figure()
        df.plot(kind=kind, x=x_value, y=y_value)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        encoded_string = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()
        plt.close()
        return encoded_string

    def validate(self, values, x, y):
        if x and y not in values:
            raise Exception(f"x  y is not in values {values}")

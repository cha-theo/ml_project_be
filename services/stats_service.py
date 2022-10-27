import csv
import os
import pandas as pd


def get_all_data():
    with open(os.getcwd() + '/repo/listings_test-Copy.csv') as raw_data_file:

        reader = csv.DictReader(raw_data_file)
        data_to_return = list(reader)

        return {
                "data": data_to_return,
                "meta": {
                    "count": len(data_to_return)
                }
            }


def max_host_id():
    dataframe = pd.read_csv(os.getcwd() + "/repo/listings_test-Copy.csv")
    return {
                "id": int(dataframe["id"].max()),
                
            }
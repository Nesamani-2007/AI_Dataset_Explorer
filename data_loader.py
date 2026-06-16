import pandas as pd


class DataLoader:

    @staticmethod
    def load_csv(file):

        return pd.read_csv(file)

    @staticmethod
    def dataset_info(df):

        memory = round(
            df.memory_usage(
                deep=True
            ).sum() / (1024 * 1024),
            2
        )

        return {
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Memory": memory
        }
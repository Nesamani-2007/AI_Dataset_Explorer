import pandas as pd


class EDA:

    @staticmethod
    def data_types(df):

        return pd.DataFrame({
            "Column": df.columns,
            "Data Type":
            df.dtypes.astype(str)
        })

    @staticmethod
    def missing_values(df):

        return pd.DataFrame({
            "Missing Count":
            df.isnull().sum(),

            "Missing %":
            round(
                (
                    df.isnull().sum()
                    / len(df)
                ) * 100,
                2
            )
        })

    @staticmethod
    def numerical_summary(df):

        numerical_df = df.select_dtypes(
            include="number"
        )

        if numerical_df.empty:
            return pd.DataFrame()

        return numerical_df.describe().T

    @staticmethod
    def categorical_summary(df):

        categorical_df = df.select_dtypes(
            include=[
                "object",
                "category"
            ]
        )

        if categorical_df.empty:
            return pd.DataFrame()

        return categorical_df.describe().T

    @staticmethod
    def outlier_summary(df):

        numerical_df = df.select_dtypes(
            include="number"
        )

        results = []

        for col in numerical_df.columns:

            q1 = numerical_df[col].quantile(
                0.25
            )

            q3 = numerical_df[col].quantile(
                0.75
            )

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            count = (
                (
                    numerical_df[col]
                    < lower
                )
                |
                (
                    numerical_df[col]
                    > upper
                )
            ).sum()

            results.append(
                {
                    "Column": col,
                    "Outliers": count
                }
            )

        return pd.DataFrame(results)
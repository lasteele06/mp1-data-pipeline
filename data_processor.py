# data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    before_count = len(df)
    df_cleaned = df.drop_duplicates()
    after_count = len(df_cleaned)
    logger.info(f"Removed {before_count - after_count} duplicate rows.")
    return df_cleaned


def handle_missing(df, axis="rows"):
    missing_count = df.isnull().sum().sum()
    df = df.dropna(axis=0 if axis == "rows" else 1)
    logger.info(f"Removed {missing_count} missing values by dropping {axis}.")
    return df


def remove_outliers(df, column, method, threshold):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df


def process_data(df, config):
     processing = config["processing"]
     if processing.get("remove_duplicates"):
        df = remove_duplicates(df)
    
     if processing["missing"]["enabled"]:
        axis = processing["missing"]["axis"]
        df = handle_missing(df, axis)
    
     if processing["outliers"]["enabled"]:
        columns = processing["outliers"]["columns"]
        method = processing["outliers"]["method"]
        threshold = processing["outliers"]["threshold"]
        for column in columns:
            df = remove_outliers(df, column, method, threshold)
   



     return df


def create_cleaning_report(df_before, df_after):
    report = {
        "initial_row_count": len(df_before),
        "final_row_count": len(df_after),
        "rows_removed": len(df_before) - len(df_after),
        "initial_missing_values": df_before.isnull().sum().sum(),
        "final_missing_values": df_after.isnull().sum().sum(),
        "missing_values_removed": df_before.isnull().sum().sum() - df_after.isnull().sum().sum(),
        "initial_duplicates": df_before.duplicated().sum(),
        "final_duplicates": df_after.duplicated().sum(),
        "duplicates_removed": df_before.duplicated().sum() - df_after.duplicated().sum()
    }
    return report
# data_preprocessing.py

import pandas as pd

def load_data(file_path):
    """Loads transaction data from CSV."""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

def check_missing_values(df):
    """Displays missing value summary."""
    print("\n🔍 Missing Values:")
    print(df.isnull().sum())

def basic_statistics(df):
    """Shows basic info and statistical summary."""
    print("\n📊 Basic Info:")
    print(df.info())
    print("\n📈 Statistical Summary:")
    print(df.describe())

def main():
    file_path = "final_synthetic_mule_transactions.csv"  # Adjust as needed
    df = load_data(file_path)
    if df is not None:
        check_missing_values(df)
        basic_statistics(df)

if __name__ == "__main__":
    main()
import pandas as pd

def load_recruiters(csv_file):
    try:
        df = pd.read_csv(csv_file)
        expected_columns = ["Name", "Email", "Company"]

        for col in expected_columns:
            if col not in df.columns:
                raise KeyError(f"Missing column: {col}. Ensure CSV has 'Name', 'Email', 'Company'.")

        return df[expected_columns].dropna()
    
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

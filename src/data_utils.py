import pandas as pd
import os

def load_data(file_path):
    """Loads data with error handling for mixed date formats."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found at {file_path}")
        df = pd.read_csv(file_path)
        df['observation_date'] = pd.to_datetime(df['observation_date'], format='mixed')
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def get_indicator_data(df, indicator_code, exclude_notes=None):
    if df is None: return None
    subset = df[df['indicator_code'] == indicator_code].copy()
    if exclude_notes and not subset.empty:
        subset = subset[~subset['notes'].str.contains(exclude_notes, na=False)]
    return subset.sort_values('observation_date')
import numpy as np
import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of df with features derived from existing columns."""
    # For reference if you want to see the original data.
    features = df.copy()

    # Numeric combinations and safe ratios.
    if {"price", "area"}.issubset(features.columns):
        features["price_per_area"] = features["price"] / features["area"].replace(0, np.nan)
        features["price_area_product"] = features["price"] * features["area"]
        features["price_per_area_log"] = np.log1p(features["price_per_area"].clip(lower=0))

    # Build calendar features from a date column.
    if "listed_on" in features.columns:
        date = pd.to_datetime(features["listed_on"], errors="coerce")
        features["listing_year"] = date.dt.year
        features["listing_month"] = date.dt.month
        features["listing_day_of_week"] = date.dt.dayofweek
        features["listing_is_weekend"] = date.dt.dayofweek.isin([5, 6]).astype("int8")

    # Simple text and category features.
    if "location" in features.columns:
        location = features["location"].fillna("").astype(str).str.strip()
        features["location_length"] = location.str.len()
        features["location_is_missing"] = location.eq("").astype("int8")
        features = pd.get_dummies(features, columns=["location"], prefix="location", dtype="int8")

    # Missingness indicators preserve information before imputing values.
    for column in df.columns:
        features[f"{column}_was_missing"] = df[column].isna().astype("int8")
    return features

def trial():
    """A simple trial function to demonstrate feature creation."""
    sample = pd.DataFrame({
        "price": [120_000, 150_000, 135_000],
        "area": [800, 950, 875],
        "listed_on": ["2025-01-10", "2025-02-12", "2025-02-20"],
        "location": ["Pune", "Pune", "Mumbai"],
    })
    return create_features(sample).head()

if __name__ == "__main__":
    sample = pd.DataFrame({
        "price": [120_000, 150_000, 135_000],
        "area": [800, 950, 875],
        "listed_on": ["2025-01-10", "2025-02-12", "2025-02-20"],
        "location": ["Pune", "Pune", "Mumbai"],
    })
    print(create_features(sample).head())
import pandas as pd

# Input Data
data = {
    "id": [1, 2, 3, 4],
    "recordDate": ["2015-01-01", "2015-01-02", "2015-01-03", "2015-01-04"],
    "temperature": [10, 25, 20, 30]
}

weather = pd.DataFrame(data)
weather["recordDate"] = pd.to_datetime(weather["recordDate"])

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by="recordDate")

    # Date difference from previous row
    date_diff = weather["recordDate"].diff().dt.days

    # Temp difference from previous row
    temp_diff = weather["temperature"].diff()

    # Select rows where both conditions match
    df = weather[(date_diff == 1) & (temp_diff > 0)] # type: ignore

    return df[["id"]]

print(rising_temperature(weather))

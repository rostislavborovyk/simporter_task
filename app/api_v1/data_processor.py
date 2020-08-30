import datetime
from typing import Optional

import pandas as pd
from copy import deepcopy

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class DataProcessor:
    WEEKLY_GROUPING: str = "weekly"
    BIWEEKLY_GROUPING: str = "bi-weekly"
    MONTHLY_GROUPING: str = "monthly"

    CUMULATIVE_TYPE: str = "cumulative"
    USUAL_TYPE: str = "usual"

    def __init__(self):
        self._data: pd.DataFrame = pd.read_csv("data.csv", sep=";")

    def _filter_by_attrs(self, data: pd.DataFrame, attrs: dict) -> pd.DataFrame:
        asin: Optional[str] = attrs.get("asin", None)
        brand: Optional[str] = attrs.get("brand", None)
        stars: Optional[str] = attrs.get("stars", None)

        if asin is not None:
            data = data[data["asin"] == asin]

        if brand is not None:
            data = data[data["brand"] == brand]

        if stars is not None:
            data = data[data["stars"] == int(stars)]

        return data

    def get_data(self,
                 start_date: Optional[int] = None,
                 end_date: Optional[int] = None,
                 grouping: str = WEEKLY_GROUPING,
                 data_type: str = USUAL_TYPE,
                 **attrs
                 ) -> pd.DataFrame:

        # deepcopying because self._data object is changed if not doing this
        tmp_data = deepcopy(self._data)

        # filtering by date
        if start_date is not None and end_date is not None:
            tmp_data = tmp_data[tmp_data["timestamp"] >= start_date]
            tmp_data = tmp_data[tmp_data["timestamp"] <= end_date]

        tmp_data = self._filter_by_attrs(tmp_data, attrs)

        # translating timestamp to date, counting values and ordering by date
        tmp_data["timestamp"] = tmp_data["timestamp"].apply(datetime.datetime.fromtimestamp)
        tmp_data = tmp_data.groupby(by="timestamp").agg("count").sort_values(by="timestamp")

        # grouping data
        if not tmp_data.empty:
            if grouping == self.WEEKLY_GROUPING:
                tmp_data = tmp_data.resample("W").sum()
            elif grouping == self.BIWEEKLY_GROUPING:
                tmp_data = tmp_data.resample("2W").sum()
            elif grouping == self.MONTHLY_GROUPING:
                tmp_data = tmp_data.resample("M").sum()
            else:
                tmp_data = tmp_data.resample("W").sum()

        # changing to cumulative type if cumulative type is set
        if data_type == self.CUMULATIVE_TYPE:
            tmp_data = tmp_data.cumsum()

        return tmp_data


dp = DataProcessor()

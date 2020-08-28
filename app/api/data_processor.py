import pandas as pd
import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class DataProcessor:
    WEEKLY_GROUPING: str = "weekly"
    BIWEEKLY_GROUPING: str = "bi-weekly"
    MONTHLY_GROUPING: str = "monthly"

    CUMULATIVE_TYPE = "cumulative"
    USUAL_TYPE = "usual"

    def __init__(self):
        # todo move data.csv to the top level directory
        self._data = pd.read_csv("data.csv", sep=";")
        self._start_date = self._data["timestamp"].min()
        self._end_date = self._data["timestamp"].max()
        # print(datetime.datetime.fromtimestamp(self._start_date))
        # print(datetime.datetime.fromtimestamp(self._end_date))

        self.get_data(
            start_date=1548799200,
            end_date=1577750400,
            grouping=self.MONTHLY_GROUPING
        )

    def _process_all_data(self):
        pass

    def get_data(self,
                 start_date: int = None,
                 end_date: int = None,
                 grouping: str = WEEKLY_GROUPING,
                 data_type: str = USUAL_TYPE
                 ) -> pd.DataFrame:

        tmp_data = self._data[:200]

        # filtering by date
        if start_date is not None and end_date is not None:
            # print("Filtered by date")
            tmp_data = tmp_data[tmp_data["timestamp"] >= start_date]
            tmp_data = tmp_data[tmp_data["timestamp"] <= end_date]

        # todo write here optional changing to cumulative type

        # translating timestamp to date, counting values and ordering by date
        tmp_data["timestamp"] = tmp_data["timestamp"].apply(datetime.datetime.fromtimestamp)
        tmp_data = tmp_data.groupby(by="timestamp").agg("count").sort_values(by="timestamp")

        # grouping data
        if grouping == self.WEEKLY_GROUPING:
            tmp_data = tmp_data.resample("W").sum()
        elif grouping == self.BIWEEKLY_GROUPING:
            tmp_data = tmp_data.resample("2W").sum()
        elif grouping == self.MONTHLY_GROUPING:
            tmp_data = tmp_data.resample("M").sum()
        else:
            tmp_data = tmp_data.resample("W").sum()

        # print(tmp_data)
        # print(len(tmp_data))

        # todo write filters by attr values
        return tmp_data


dp = DataProcessor()

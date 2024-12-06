import ray
import pandas as pd


@ray.remote
def process_dataframe(df):
    return df.mean()


dataframes = [pd.DataFrame({"a": range(10)}), pd.DataFrame({"a": range(10, 20)})]
results = ray.get([process_dataframe.remote(df) for df in dataframes])
print(results)

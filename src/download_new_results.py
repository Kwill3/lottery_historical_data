from urllib.request import urlretrieve
import polars as pl
from datetime import datetime as dt

results_page = "https://www.national-lottery.co.uk/results/"


def main():
    def download_csv_to_df(draw: str):
        # url for csv download
        url = results_page + f"{draw}/draw-history/csv"
        # output file name concatenated with date of download
        filename = f"../data/raw/{draw}-draw-history-" + str(dt.date(dt.now())) + ".csv"

        urlretrieve(url, filename)
        df = pl.read_csv(filename)
        return df

    def sort_df_rows(df: pl.DataFrame):
        sorted_df = df.sort("DrawNumber", descending=False)
        return sorted_df

    def master_df(draw: str):
        m_df = pl.read_csv(f"../data/derived-csv/{draw}-draw-history.csv", has_header=True)
        return m_df
    
    def union_dfs(df1: pl.DataFrame, df2: pl.DataFrame):
        unioned_df = pl.concat([df1, df2], how='align')
        return unioned_df
    
    def update_csv_data(draw: str):
        new_df = download_csv_to_df(draw)
        sorted_df = sort_df_rows(new_df)
        m_df = master_df(draw)
        result_df = union_dfs(m_df, sorted_df)
        sorted_result_df = sort_df_rows(result_df)

        # sink df to master record file
        sorted_result_df.write_csv(f"../data/derived-csv/{draw}-draw-history.csv", include_header=True)

    update_csv_data("euromillions")
    update_csv_data("lotto")
    update_csv_data("set-for-life")
    update_csv_data("thunderball")

if __name__ == "__main__":
    main()

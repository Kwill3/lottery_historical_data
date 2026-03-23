from urllib.request import urlretrieve
import polars as pl
from datetime import datetime as dt

# New API endpoint for National Lottery
api_base = "https://api-dfe.national-lottery.co.uk/draw-game/results/"

# Mapping of draw names to game IDs
game_ids = {
    "euromillions": 33,
    "lotto": 1,
    "set-for-life": 3,
    "thunderball": 4
}


def main():
    def download_csv_to_df(draw: str):
        # Get the game ID for this draw
        game_id = game_ids.get(draw)
        if game_id is None:
            raise ValueError(f"Unknown draw type: {draw}")
        
        # url for csv download from new API
        url = api_base + f"{game_id}/download"
        # output file name concatenated with date of download
        filename = f"data/raw/{draw}-draw-history-" + str(dt.date(dt.now())) + ".csv"

        urlretrieve(url, filename)
        df = pl.read_csv(filename)
        return df

    def sort_df_rows(df: pl.DataFrame):
        sorted_df = df.sort("DrawNumber", descending=False)
        return sorted_df

    def master_df(draw: str):
        m_df = pl.read_csv(f"data/derived-csv/{draw}-draw-history.csv", has_header=True)
        return m_df
    
    def union_dfs(df1: pl.DataFrame, df2: pl.DataFrame):
        # Ensure all columns have matching dtypes before concat
        # Convert all columns to string to avoid dtype mismatches
        df1_str = df1.with_columns([pl.col(col).cast(pl.Utf8) for col in df1.columns])
        df2_str = df2.with_columns([pl.col(col).cast(pl.Utf8) for col in df2.columns])
        unioned_df = pl.concat([df1_str, df2_str], how='align')
        return unioned_df
    
    def update_csv_data(draw: str):
        # get new draw data from website
        new_df = download_csv_to_df(draw)
        # sort draws by draw number
        sorted_df = sort_df_rows(new_df)
        # get master draw data
        m_df = master_df(draw)
        # union new and master data
        result_df = union_dfs(m_df, sorted_df)
        # sort by draw number
        sorted_result_df = sort_df_rows(result_df)
        # remove duplicates
        deduped_sorted_df = sorted_result_df.unique(maintain_order=True)

        # sink df to master record file
        deduped_sorted_df.write_csv(f"data/derived-csv/{draw}-draw-history.csv", include_header=True)

    update_csv_data("euromillions")
    update_csv_data("lotto")
    update_csv_data("set-for-life")
    update_csv_data("thunderball")

if __name__ == "__main__":
    main()

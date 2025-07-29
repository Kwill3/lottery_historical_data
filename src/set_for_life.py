import polars as pl
from lottery_class import Draw_Type, Lottery

fetch_sfl = Lottery(Draw_Type.SFL)
fetch_sfl.get_numbers()
pl_sfl = pl.DataFrame({
    "draw_date": fetch_sfl.draw_date,
    "draw_day": fetch_sfl.draw_day,
    "main_numbers": ','.join(fetch_sfl.main_numbers),
    "special_number": fetch_sfl.special_number
})

with open("data/derived-csv/sfl.csv", mode="a", encoding="utf-8") as f:
   pl_sfl.write_csv(f, include_header=False)
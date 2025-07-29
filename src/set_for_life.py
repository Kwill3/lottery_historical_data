import polars as pl
from lottery_class import Draw_Type, Lottery

fetch_sfl = Lottery(Draw_Type.SFL)
fetch_sfl.get_numbers()
pl_sfl = pl.DataFrame({
    # date of the draw in format: DD MMM YYYY. (e.g: 28 Jul 2025)
    "draw_date": fetch_sfl.draw_date,
    # day of the week (Mon/Thu)
    "draw_day": fetch_sfl.draw_day,
    # 5 main numbers from 1 to 47 (e.g: 02,04,07,22,34)
    "main_numbers": ','.join(fetch_sfl.main_numbers),
    # 1 special number from 1 to 10 (e.g: 02)
    "life_ball": ','.join(fetch_sfl.special_numbers)
})

with open("data/derived-csv/sfl.csv", mode="a", encoding="utf-8") as f:
   pl_sfl.write_csv(f, include_header=False)
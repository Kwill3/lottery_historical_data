import polars as pl
from lottery_class import Draw_Type, Lottery

fetch_lotto = Lottery(Draw_Type.LOTTO)
fetch_lotto.get_numbers()
pl_lotto = pl.DataFrame({
    "draw_date": fetch_lotto.draw_date,
    "draw_day": fetch_lotto.draw_day,
    "main_numbers": ','.join(fetch_lotto.main_numbers),
    "special_number": fetch_lotto.special_number
})

with open("data/derived-csv/lotto.csv", mode="a", encoding="utf-8") as f:
   pl_lotto.write_csv(f, include_header=False)
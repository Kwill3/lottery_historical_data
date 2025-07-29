import polars as pl
from lottery_class import Draw_Type, Lottery

fetch_lotto = Lottery(Draw_Type.LOTTO)
fetch_lotto.get_numbers()
pl_lotto = pl.DataFrame({
    # date of the draw in format: DD MMM YYYY. (e.g: 26 Jul 2025)
    "draw_date": fetch_lotto.draw_date,
    # day of the week (Wed/Sat)
    "draw_day": fetch_lotto.draw_day,
    # 6 main numbers from 1 to 59 (e.g: 09,23,24,28,42,57)
    "main_numbers": ','.join(fetch_lotto.main_numbers),
    # 1 extra number from same pool as above (e.g: 18)
    "bonus_ball": ','.join(fetch_lotto.special_numbers)
})

with open("data/derived-csv/lotto.csv", mode="a", encoding="utf-8") as f:
   pl_lotto.write_csv(f, include_header=False)
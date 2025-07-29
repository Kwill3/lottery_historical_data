import polars as pl
from lottery_class import Draw_Type, Lottery

fetch_thunderball = Lottery(Draw_Type.THUNDERBALL)
fetch_thunderball.get_numbers()
pl_thunderball = pl.DataFrame({
    # date of the draw in format: DD MMM YYYY. (e.g: 26 Jul 2025)
    "draw_date": fetch_thunderball.draw_date,
    # day of the week (Tue/Wed/Fri/Sat)
    "draw_day": fetch_thunderball.draw_day,
    # 5 main numbers from 1 to 39 (e.g: 02,05,28,38,39)
    "main_numbers": ','.join(fetch_thunderball.main_numbers),
    # 1 special number from 1 to 14 (e.g: 03)
    "thunderball": ','.join(fetch_thunderball.special_numbers)
})

with open("data/derived-csv/thunderball.csv", mode="a", encoding="utf-8") as f:
   pl_thunderball.write_csv(f, include_header=False)
import polars as pl
from lottery_class import Draw_Type, Lottery

fetch_euromillions = Lottery(Draw_Type.EUROMILLIONS)
fetch_euromillions.get_numbers()
pl_euromillions = pl.DataFrame({
    # date of the draw in format: DD MMM YYYY. (e.g: 25 Jul 2025)
    "draw_date": fetch_euromillions.draw_date,
    # day of the week (Tue/Fri)
    "draw_day": fetch_euromillions.draw_day,
    # 5 main numbers from 1 to 50 (e.g: 06,07,23,32,36)
    "main_numbers": ','.join(fetch_euromillions.main_numbers),
    # 2 special numbers from 1 to 12 (e.g: 11, 12)
    "lucky_stars": ','.join(fetch_euromillions.special_numbers)
})

with open("data/derived-csv/euromillions.csv", mode="a", encoding="utf-8") as f:
   pl_euromillions.write_csv(f, include_header=False)
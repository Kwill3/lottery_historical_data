import polars as pl
from lottery_class import Draw_Type, Lottery, NumberOutOfRangeError, ListLenMismatchError

def main():
    csv = "data/derived-csv/thunderball.csv"
    new_draw = Lottery(Draw_Type.THUNDERBALL)
    new_draw.scrape_website()
    new_draw.get_numbers()
    output = loadThunderball(new_draw)

    # append to csv
    with open(csv, mode="a", encoding="utf-8") as f:
        output.write_csv(f, include_header=False)

def loadThunderball(thunderball: Lottery):
    # DQ check for main numbers
    if len(thunderball.main_numbers) != 5 or not thunderball.main_numbers:
        raise ListLenMismatchError("Main numbers list length not equal to 5")
    for num in thunderball.main_numbers:
        if int(num) < 1 or int(num) > 39:
            raise NumberOutOfRangeError("One or more of main numbers not within acceptable range")
    # DQ check for special number
    if len(thunderball.special_numbers) != 1 or not thunderball.special_numbers:
        raise ListLenMismatchError("Thunderball list length not equal to 1")
    for num in thunderball.special_numbers:
        if int(num) < 1 or int(num) > 14:
            raise NumberOutOfRangeError("Thunderball not within acceptable range")
        
    # turn into polars dataframe
    pl_thunderball = pl.DataFrame({
        # date of the draw in format: DD MMM YYYY. (e.g: 26 Jul 2025)
        "draw_date": thunderball.draw_date,
        # day of the week (Tue/Wed/Fri/Sat)
        "draw_day": thunderball.draw_day,
        # 5 main numbers from 1 to 39 (e.g: 02,05,28,38,39)
        "main_numbers": ','.join(thunderball.main_numbers),
        # 1 special number from 1 to 14 (e.g: 03)
        "thunderball": ','.join(thunderball.special_numbers)
    })

    return pl_thunderball

if __name__ == "__main__":
    main()
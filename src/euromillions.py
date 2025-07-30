import polars as pl
from lottery_class import Draw_Type, Lottery, NumberOutOfRangeError, ListLenMismatchError

def main():
    csv = "data/derived-csv/euromillions.csv"
    new_draw = Lottery(Draw_Type.EUROMILLIONS)
    new_draw.scrape_website()
    new_draw.get_numbers()
    output = loadEuromillions(new_draw)

    # append to csv
    with open(csv, mode="a", encoding="utf-8") as f:
        output.write_csv(f, include_header=False)

def loadEuromillions(euromillions: Lottery):
    # DQ check for main numbers
    if len(euromillions.main_numbers) != 5 or not euromillions.main_numbers:
        raise ListLenMismatchError("Main numbers list length not equal to 5")
    for num in euromillions.main_numbers:
        if int(num) < 1 or int(num) > 50:
            raise NumberOutOfRangeError("One or more of main numbers not within acceptable range")
    # DQ check for special number
    if len(euromillions.special_numbers) != 2 or not euromillions.special_numbers:
        raise ListLenMismatchError("Euromillions list length not equal to 1")
    for num in euromillions.special_numbers:
        if int(num) < 1 or int(num) > 12:
            raise NumberOutOfRangeError("Euromillions not within acceptable range")
        
    pl_euromillions = pl.DataFrame({
        # date of the draw in format: DD MMM YYYY. (e.g: 25 Jul 2025)
        "draw_date": euromillions.draw_date,
        # day of the week (Tue/Fri)
        "draw_day": euromillions.draw_day,
        # 5 main numbers from 1 to 50 (e.g: 06,07,23,32,36)
        "main_numbers": ','.join(euromillions.main_numbers),
        # 2 special numbers from 1 to 12 (e.g: 11, 12)
        "lucky_stars": ','.join(euromillions.special_numbers)
    })

    return pl_euromillions

if __name__ == "__main__":
    main()
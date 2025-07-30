import polars as pl
from lottery_class import Draw_Type, Lottery, ListLenMismatchError, NumberOutOfRangeError

def main():
    csv = "data/derived-csv/sfl.csv"
    new_draw = Lottery(Draw_Type.SFL)
    new_draw.scrape_website()
    new_draw.get_numbers()
    output = loadSetForLife(new_draw)

    # append to csv
    with open(csv, mode="a", encoding="utf-8") as f:
        output.write_csv(f, include_header=False)

def loadSetForLife(sfl: Lottery):
    # DQ check for main numbers
    if len(sfl.main_numbers) != 5 or not sfl.main_numbers:
        raise ListLenMismatchError("Main numbers list length not equal to 5")
    for num in sfl.main_numbers:
        if int(num) < 1 or int(num) > 47:
            raise NumberOutOfRangeError("One or more of main numbers not within acceptable range")
    # DQ check for special number
    if len(sfl.special_numbers) != 1 or not sfl.special_numbers:
        raise ListLenMismatchError("SFL list length not equal to 1")
    for num in sfl.special_numbers:
        if int(num) < 1 or int(num) > 10:
            raise NumberOutOfRangeError("SFL not within acceptable range")

    pl_sfl = pl.DataFrame({
        # date of the draw in format: DD MMM YYYY. (e.g: 28 Jul 2025)
        "draw_date": sfl.draw_date,
        # day of the week (Mon/Thu)
        "draw_day": sfl.draw_day,
        # 5 main numbers from 1 to 47 (e.g: 02,04,07,22,34)
        "main_numbers": ','.join(sfl.main_numbers),
        # 1 special number from 1 to 10 (e.g: 02)
        "life_ball": ','.join(sfl.special_numbers)
    })

    return pl_sfl

if __name__ == "__main__":
    main()
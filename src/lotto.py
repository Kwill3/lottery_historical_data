import polars as pl
from lottery_class import Draw_Type, Lottery, ListLenMismatchError, NumberOutOfRangeError, BonusNumberInMainError

def main():
    csv = "data/derived-csv/lotto.csv"
    new_draw = Lottery(Draw_Type.LOTTO)
    new_draw.scrape_website()
    new_draw.get_numbers()
    output = loadLotto(new_draw)

    # append to csv
    with open(csv, mode="a", encoding="utf-8") as f:
        output.write_csv(f, include_header=False)

def loadLotto(lotto: Lottery):
    # DQ check for main numbers
    if len(lotto.main_numbers) != 6 or not lotto.main_numbers:
        raise ListLenMismatchError("Main numbers list length not equal to 6")
    for num in lotto.main_numbers:
        if int(num) < 1 or int(num) > 59:
            raise NumberOutOfRangeError("One or more of main numbers not within acceptable range")
    # DQ check for special number
    if len(lotto.special_numbers) != 1 or not lotto.special_numbers:
        raise ListLenMismatchError("Lotto list length not equal to 1")
    for num in lotto.special_numbers:
        if int(num) < 1 or int(num) > 59:
            raise NumberOutOfRangeError("Lotto not within acceptable range")
    # Check bonus number not in main numbers
    if lotto.special_numbers[0] in lotto.main_numbers:
        raise BonusNumberInMainError("Bonus number in main numbers")
        
    pl_lotto = pl.DataFrame({
        # date of the draw in format: DD MMM YYYY. (e.g: 26 Jul 2025)
        "draw_date": lotto.draw_date,
        # day of the week (Wed/Sat)
        "draw_day": lotto.draw_day,
        # 6 main numbers from 1 to 59 (e.g: 09,23,24,28,42,57)
        "main_numbers": ','.join(lotto.main_numbers),
        # 1 extra number from same pool as above (e.g: 18)
        "bonus_ball": ','.join(lotto.special_numbers)
    })

    return pl_lotto
   
if __name__ == "__main__":
    main()
# Lottery Historical Data

Personal project that scrapes winning numbers from The National Lottery [website](https://www.national-lottery.co.uk/results) and stores a historical record.

## Pipeline details
Pipeline runs automatically 9PM on draw days to scrape draw results from the website and will populate the csv data store.

## Output Data
- draw_date: String - format of DD MMM YYYY (e.g: 25 Jul 2025)
- draw_day: String - format for day of the week (Mon/Tue/Wed/Thu/Fri/Sat/Sun) 
- main_numbers: String representation of a(n) list/array of numbers (e.g: 06,07,23,32,36)
- special_numbers: String representation of a(n) list/array of numbers (e.g: 11, 12)

## Draws Types and Details

### Set For Life
Draws every Monday and Thursday

Numbers consists of:
- 5 main numbers from 1 to 47
- 1 life ball from 1 to 10

Game procedures, prizes and odds can be found [here](https://www.national-lottery.co.uk/games/set-for-life/game-procedures)

### Lotto
Draws every Wednesday and Saturday

Numbers consists of:
- 6 main numbers from 1 to 59
- 1 bonus ball from same pool as above

Game procedures, prizes and odds can be found [here](https://www.national-lottery.co.uk/games/lotto/game-procedures)

### Euromillions
Draws every Tuesday and Friday

Numbers consists of:
- 5 main numbers from 1 to 50
- 2 lucky stars from 1 to 12

Game procedures, prizes and odds can be found [here](https://www.national-lottery.co.uk/games/euromillions/game-procedures)

### Set For Life
Draws every Tuesday, Wednesday, Friday and Saturday

Numbers consists of:
- 5 main numbers from 1 to 39
- 1 thunderball from 1 to 14

Game procedures, prizes and odds can be found [here](https://www.national-lottery.co.uk/games/thunderball/game-procedures)

## Number Validation
This pipeline tests for valid numbers from the draws before loading to csv, tests check for correct range of numbers and amount of numbers. For lotto draws, there is a test to check that the bonus number is not in the main numbers.
"""
CP1404 Programming II
A program the wimbledon champion, how many times they have won
and the champions country
"""


# CONSTANTS
filename = "wimbledon.csv"
with open(filename, "r", encoding="utf-8-sig") as in_file:
    for line in in_file:
        strip_line = line.strip()
        split_line = strip_line.split(',')
        # print(split_line)
        years = split_line[0]
        champion_countries = split_line[1]
        champion_name = split_line[2]
        runnerup_countries = split_line[3]
        runnerup = split_line[4]
        winnings_split = strip_line.split('"')
    print(winnings_split)
    print(split_line)
        # print(f"{years} {champion_countries} {champion_name} {runnerup_countries} {runnerup}")
    # print("Wimbledon Champions:")
    # print(f"{split_line[1]}")

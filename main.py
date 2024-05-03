print(
    """you want to calculate the number of seconds in a NORMAL YEAR or LEAP YEAR ?\n
    -----MAKE SURE YOUR INPUT MUST BE IN LOWER CASE-----\n
    """)
year = input('''Please write "leap year" or "normal year" \n''')

if year == "leap year":
  seconds = 60
  minutes = 60
  hours = 24
  # days = 31
  # months = 12
  years_day = 366
  final_seconds = (((seconds * minutes) * hours) * years_day)
  print("\033[32m", "\nThere are", final_seconds, "seconds in a LEAP year.😮😲🤯",
        "\033[0m")

elif year == "normal year":
  seconds = 60
  minutes = 60
  hours = 24
  years_day = 365
  final_seconds = (((seconds * minutes) * hours) * years_day)
  print("\033[32m", "\nThere are", final_seconds,
        "seconds in a NORMAL year.😮😲🤯", "\033[0m")
else:
  print("\033[31m", "\nwrong input😒😕😕", "\033[0m")
  print(
      "\033[31m",
      "make sure you manually write text leap year or normal year in lower case properly",
      "\033[0m")

day = input("What day of the week is it?:")
match day:
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("Weekday")
    case "Saturday"|"Sunday":
        print("Weekend")

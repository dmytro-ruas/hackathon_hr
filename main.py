from csv_connector import CsvConnector, ClockHour

# Example usage (uncomment to run)
# Creates a CsvConnector instance to interact with the CSV file
# dataSource = get_clockhour_connector()
# Adds a new time entry. You provide it with a ClockHour object
# dataSource.add_entry()
# Retrieves all time entries
# dataSource.all()
# Filters entries by year
# dataSource.filter_by_month()
# Filters entries by employee ID
# dataSource.filter_by_employee()
# Filters entries using a custom predicate function (A Lambda)
# dataSource.filter()
# Saves any changes back to the CSV file
# dataSource.save()

def main():
    print("Good luck with your Hackathon project!")
    input("Press Enter to continue...")


def get_clockhour_connector() -> CsvConnector | None:
    try:
        return CsvConnector("clockhour.csv")
    except FileNotFoundError:
        print("CSV file not found. Make sure 'clockhour.csv' exists.")
        return None
    
if __name__ == "__main__":
    main()

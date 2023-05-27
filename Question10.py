from datetime import datetime, timedelta

def calculate_previous_date(date, n):
    # Convert the date string to a datetime object
    datetime_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the previous date by subtracting n days
    previous_date = datetime_obj - timedelta(days=n)

    # Format the previous date as a string in the 'yy-mm-dd' format
    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str

# Example usage
date = '16-12-10'
n = 11

result = calculate_previous_date(date, n)
print(result)


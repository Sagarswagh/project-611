from datetime import datetime
from collections import defaultdict

def time_to_update(issues):
    """
    This function calculates the time difference (in seconds) between the issue's creation and the first update.
    """
    time_differences = defaultdict(int)

    for issue in issues:
        created_date_str = issue.get('created_date')
        updated_date_str = issue.get('updated_date')

        if created_date_str and updated_date_str:
            try:
                # Parse the 'created_date' and 'updated_date'
                created_date = datetime.strptime(created_date_str, "%Y-%m-%dT%H:%M:%S%z")
                updated_date = datetime.strptime(updated_date_str, "%Y-%m-%dT%H:%M:%S%z")
                
                # Calculate the time difference in seconds
                time_diff = updated_date - created_date
                time_differences[issue['number']] = time_diff.total_seconds()
            except ValueError:
                continue  # Skip if date parsing fails

    return time_differences

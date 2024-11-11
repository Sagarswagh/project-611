from collections import defaultdict
from datetime import datetime

def contributors_activity(issues):
    contributors = defaultdict(lambda: defaultdict(int))

    for issue in issues:
        created_at_str = issue.get('created_at', '')
        closed_at_str = issue.get('closed_at', '')

        if not created_at_str:
            print(f"Missing created_at for issue ID: {issue.get('id')}")  # Debugging message
        if not closed_at_str:
            print(f"Missing closed_at for issue ID: {issue.get('id')}")  # Debugging message

        # Handle missing or empty 'created_at' and 'closed_at'
        created_at = None
        closed_at = None
        
        if created_at_str:
            try:
                created_at = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%SZ')
            except ValueError:
                created_at = None  # If the date is invalid, keep it None

        if closed_at_str:
            try:
                closed_at = datetime.strptime(closed_at_str, '%Y-%m-%dT%H:%M:%SZ')
            except ValueError:
                closed_at = None  # If the date is invalid, keep it None

        assignees = issue.get('assignees', [])
        if assignees:
            for assignee in assignees:
                user = assignee.get('login')
                if user:
                    if created_at:
                        contributors[user][created_at.date()] += 1
                    if closed_at:
                        contributors[user][closed_at.date()] += 1

    if not contributors:
        print("No contributors to plot.")  # Debugging message
    else:
        print("Contributors Activity Data:", contributors)  # Debugging message

    return contributors

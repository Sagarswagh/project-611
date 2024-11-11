from typing import List
import matplotlib.pyplot as plt
from data_loader import DataLoader
from model import Issue, Event
import config

class IssueResponseTimeAnalysis:
    """
    Implements an analysis to calculate and visualize issue response times.
    """

    def __init__(self):
        """
        Constructor
        """
        self.USER: str = config.get_parameter('user')

    def run(self):
        """
        Starting point for this analysis.
        """
        issues: List[Issue] = DataLoader().get_issues()

        # List to store response times (in days)
        response_times = []

        for issue in issues:
            # Find the first response event (comment or other event) after issue creation
            first_response_date = None

            for event in issue.events:
                if event.event_date and event.event_date > issue.created_date:
                    first_response_date = event.event_date
                    break

            # Calculate the response time if a response was found
            if first_response_date:
                response_time = (first_response_date - issue.created_date).days
                response_times.append(response_time)

        ### PLOT ###
        
        if response_times:
            # Calculate statistics
            avg_response_time = sum(response_times) / len(response_times)
            min_response_time = min(response_times)
            max_response_time = max(response_times)

            # Plot a histogram of response times without x-axis restrictions
            plt.hist(response_times, bins=50, edgecolor='black')
            plt.title('Distribution of Issue Response Times')
            plt.xlabel('Response Time (days)')
            plt.ylabel('Number of Issues')

            # Add text annotations for average, minimum, and maximum response times inside plot area.
            stats_text = f'Average Response Time: {avg_response_time:.2f} days\n' \
                         f'Minimum Response Time: {min_response_time} days\n' \
                         f'Maximum Response Time: {max_response_time} days'
            
            # Positioning text inside plot area (adjust coordinates as needed) and reducing font size for cleaner look
            plt.text(max(response_times) * 0.6, max(response_times) // 10, stats_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

            # Display the plot instead of saving it
            plt.tight_layout()
            plt.show()

if __name__ == '__main__':
    analysis = IssueResponseTimeAnalysis()
    analysis.run()
    
    #stats
#     Loaded 5573 issues from C:\Users\balak\Desktop\FallSem\ENPM611\PROJECT\poetry_issues_all.json.
# Average Response Time: 26.47 days
# Minimum Response Time: 0 days
# Maximum Response Time: 1412 days
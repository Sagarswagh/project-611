




from typing import List, Dict
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import DataLoader
from model import Issue, Event
import config

class TopCommentersVsCreatorsAnalysis:
    """
    Implements an analysis to compare top issue creators and top commenters.
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

        # Dictionary to store issue creators and their issue counts
        creator_counts: Dict[str, int] = {}
        
        # Dictionary to store commenters and their comment counts
        commenter_counts: Dict[str, int] = {}

        # Loop through each issue and count the number of issues created by each user
        for issue in issues:
            creator = issue.creator
            if creator not in creator_counts:
                creator_counts[creator] = 0
            creator_counts[creator] += 1

            # Loop through each event (comment) in the issue and count comments by each user
            for event in issue.events:
                if event.event_type == 'commented':
                    commenter = event.author
                    if commenter not in commenter_counts:
                        commenter_counts[commenter] = 0
                    commenter_counts[commenter] += 1

        # Convert dictionaries to DataFrames for easier plotting
        df_creators = pd.DataFrame(list(creator_counts.items()), columns=['User', 'Issues Created'])
        df_commenters = pd.DataFrame(list(commenter_counts.items()), columns=['User', 'Comments Made'])

        # Sort both DataFrames by count values (descending)
        df_creators = df_creators.sort_values(by='Issues Created', ascending=False).head(11)
        df_commenters = df_commenters.sort_values(by='Comments Made', ascending=False).head(11)

        ### PLOT ###
        
        # Plot Top 11 Issue Creators
        plt.figure(figsize=(14, 6))
        
        plt.subplot(1, 2, 1)  # First subplot for Issue Creators
        plt.barh(df_creators['User'], df_creators['Issues Created'], color='skyblue')
        plt.title('Top 11 Issue Creators')
        plt.xlabel('Number of Issues Created')
        
        # Plot Top 10 Commenters
        plt.subplot(1, 2, 2)  # Second subplot for Commenters
        plt.barh(df_commenters['User'], df_commenters['Comments Made'], color='lightgreen')
        plt.title('Top 11 Commenters')
        plt.xlabel('Number of Comments Made')

        # Adjust layout and show plot
        plt.tight_layout()
        plt.show()
        
        
 # Convert dictionaries to DataFrames for easier plotting
        df_creators = pd.DataFrame(list(creator_counts.items()), columns=['User', 'Issues Created'])
        df_commenters = pd.DataFrame(list(commenter_counts.items()), columns=['User', 'Comments Made'])
 # Sort both DataFrames by count values (descending)
        df_creators = df_creators.sort_values(by='Issues Created', ascending=False).head(25)
        df_commenters = df_commenters.sort_values(by='Comments Made', ascending=False).head(25)

        ### PLOT ###
        
        # Plot Top 25 Issue Creators
        plt.figure(figsize=(14, 6))
        
        plt.subplot(1, 2, 1)  # First subplot for Issue Creators
        plt.barh(df_creators['User'], df_creators['Issues Created'], color='skyblue')
        plt.title('Top 25 Issue Creators')
        plt.xlabel('Number of Issues Created')
        
        # Plot Top 10 Commenters
        plt.subplot(1, 2, 2)  # Second subplot for Commenters
        plt.barh(df_commenters['User'], df_commenters['Comments Made'], color='lightgreen')
        plt.title('Top 25 Commenters')
        plt.xlabel('Number of Comments Made')

        # Adjust layout and show plot
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    # Invoke run method when running this module directly
    TopCommentersVsCreatorsAnalysis().run()
    
    ##Top Commenters vs Top Issue Creators

# Top Commenters vs Top Issue Creators
# Insight: Compare the top issue creators with the top commenters. Are the people who create the most issues also the most active in commenting on them? Or do other contributors take over once an issue is created?
# Why it's interesting: This can reveal different types of engagement within the project — some contributors might be more focused on reporting problems, while others focus on providing feedback or solutions.
# How to visualize: Two side-by-side bar charts comparing top issue creators and top commenters.
# Feature 5: Aditi

import json
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

class MonthlyIssueAnalysis:
    """
    Analyzes the number of issues created each month and plots them interactively.
    """
    
    def __init__(self, json_file='poetry_issues_all.json'):
        # Load the JSON data
        with open(json_file, 'r') as file:
            self.issues = json.load(file)
        self.df = pd.DataFrame(self.issues)
        
    def run(self):
        # Ensure 'created_date' is in datetime format
        self.df['created_date'] = pd.to_datetime(self.df['created_date'], errors='coerce')

        # Group by month and count issues
        monthly_issues = self.df.groupby(self.df['created_date'].dt.to_period('M')).size().reset_index(name='issue_counts')
        monthly_issues['created_date'] = monthly_issues['created_date'].dt.to_timestamp()

        # Create a line plot using Plotly
        fig = px.bar(
            monthly_issues, 
            x='created_date', 
            y='issue_counts',
            title="Number of Issues Created per Month",
            labels={'created_date': 'Date', 'issue_counts': 'Number of Issues'}
        )

        # Make the plot scrollable and zoomable
        fig.update_xaxes(rangeslider_visible=True)
        fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])),
            type="date"
        ))

        # Show the interactive plot
        fig.show()

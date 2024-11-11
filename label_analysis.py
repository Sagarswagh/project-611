
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import DataLoader
from model import Issue,Event
import config

class LabelAnalysis:
    """
    Implements an top 5 issue analysis over time with
    average issues resolution and creation over a month
    """
    
    def __init__(self):
        """
        Constructor
        """
        # Parameter is passed in via command line (--user)
        self.USER:str = config.get_parameter('user')
    
    def run(self):
        """
        Starting point for this analysis.
        """
        issues:List[Issue] = DataLoader().get_issues()
        # Converting issues to a pandas dataframe
        data=[]
        for issue in issues:
            data.append({
                "created_date": issue.created_date,
                "updated_date": issue.updated_date,
                "labels":issue.labels,
                "state":issue.state,
                "title": issue.title})
        df=pd.DataFrame(data)

        # Converting the data into pandas datatime fields
        df["created_date"]=pd.to_datetime(df["created_date"])
        df["updated_date"] = pd.to_datetime(df["updated_date"])
        # Removing TimeZone
        df["created_date"]=df["created_date"].dt.tz_localize(None)
        df["year"]= df["created_date"].dt.to_period("Y")
        df=df.explode("labels")

        # counting the labels
        label_count=df.groupby("labels").size().reset_index(name="count")
        # Top 5 labels
        labels=label_count.sort_values(by="count",ascending=False).head(3)['labels']

        label_data=[]
        for label in labels:
            df_label= df[(df["labels"]==label) & (df["state"]=="closed")]
            # group data by year
            group_data= df_label.groupby("year").size().reset_index(name="completed_count")
            group_data["label"]=label
            label_data.append(group_data)
        final_data=pd.concat(label_data)
        # Plotting
        fig,axes= plt.subplots(3, 1, figsize=(12, 10), sharex=True)
        fig.suptitle("Yearly Analysis of Top Three Issue Labels Completed Count")
        for i,label in enumerate(labels):
            axis=axes[i]
            label_data=final_data[final_data["label"]==label]
            x=label_data["year"].astype(str)
            completed_count=label_data["completed_count"]
            # Bar graph for each label
            axis.bar(x,completed_count,label=f"Completed Count", color='blue')
            axis.set_ylabel("Completed Count")
            axis.set_title(f"{label}")
            axis.legend(loc="upper left")
            axis.grid(True, linestyle="--", alpha=0.7)

        plt.xlabel("Year")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout(rect=[0, 0, 1, 0.97])
        plt.subplots_adjust(hspace=0.4)
        plt.show()

if __name__ == '__main__':
    # Invoke run method when running this module directly
    IssueAnalysis().run()
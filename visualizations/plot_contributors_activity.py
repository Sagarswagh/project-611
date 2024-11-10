import matplotlib.pyplot as plt

def plot_contributors_activity(contributors):
    for contributor, activity in contributors.items():
        dates = sorted(activity.keys())
        activity_counts = [activity[date] for date in dates]

        plt.plot(dates, activity_counts, label=contributor)

    plt.title("Contributor Activity Over Time")
    plt.xlabel("Date")
    plt.ylabel("Issue Count")
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

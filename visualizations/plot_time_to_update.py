import matplotlib.pyplot as plt

def plot_time_to_update(time_differences):
    """
    This function will plot the distribution of time taken from creation to the first update for each issue.
    """
    if not time_differences:
        print("No data to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.hist(list(time_differences.values()), bins=10, color='blue', edgecolor='black')
    plt.title("Time to Update (Creation to First Update)")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

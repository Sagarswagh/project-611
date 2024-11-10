# visualizations/plot_labels.py
import matplotlib.pyplot as plt

def plot_label_distribution(label_counts):
    labels, counts = zip(*label_counts.items())  # Unpack the dictionary into two lists
    plt.figure(figsize=(10, 5))  # Set the figure size
    plt.bar(labels, counts, color='skyblue')  # Create a bar chart
    plt.title("Issue Label Distribution")  # Set the title
    plt.xlabel("Labels")  # Label for the x-axis
    plt.ylabel("Count")  # Label for the y-axis
    plt.xticks(rotation=45, ha='right')  # Rotate x-tick labels for better visibility
    plt.tight_layout()  # Adjust layout to avoid clipping
    plt.show()  # Display the plot


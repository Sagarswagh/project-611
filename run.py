import argparse
from data.load_data import load_issues
from analysis.label_analysis import analyze_issue_labels
from visualizations.plot_labels import plot_label_distribution
from analysis.time_to_update_analysis import time_to_update
from visualizations.plot_time_to_update import plot_time_to_update
from label_analysis import LabelAnalysis
from top_commenters_vs_creators_analysis import TopCommentersVsCreatorsAnalysis

def main():
    parser = argparse.ArgumentParser(description='Analyze GitHub issues data.')
    parser.add_argument('--feature', type=int, choices=[1, 2, 3, 4, 5], required=True, help='Choose feature to run')
    args = parser.parse_args()

    issues = load_issues()

    if args.feature == 1:
        print('hi')
        label_counts = analyze_issue_labels(issues)
        print("Label Counts:", label_counts)
        plot_label_distribution(label_counts)

    elif args.feature == 2:
        time_differences = time_to_update(issues)
        # Plot the results
        plot_time_to_update(time_differences)
    elif args.feature ==3:
        LabelAnalysis().run()
    elif args.feature ==4:
        TopCommentersVsCreatorsAnalysis().run()


    

if __name__ == '__main__':
    main()
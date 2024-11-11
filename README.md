# ENPM611 Project Application Template

This is the template for the ENPM611 class project. Use this template in conjunction with the provided data to implement an application that analyzes GitHub issues for the [poetry](https://github.com/python-poetry/poetry/issues) Open Source project and generates interesting insights.

This application template implements some of the basic functions:

- `data_loader.py`: Utility to load the issues from the provided data file and returns the issues in a runtime data structure (e.g., objects)
- `model.py`: Implements the data model into which the data file is loaded. The data can then be accessed by accessing the fields of objects.
- `config.py`: Supports configuring the application via the `config.json` file. You can add other configuration paramters to the `config.json` file.
- `run.py`: This is the module that will be invoked to run your application. Based on the `--feature` command line parameter, one of the three analyses you implemented will be run. You need to extend this module to call other analyses.
- `label_analysis.py`: This module runs a top-three issue label analysis over time, examining issue creation and resolution patterns. The run() method loads issues from a data source, processes them into a DataFrame, identifies the top three labels based on frequency, and plots a yearly bar chart showing the number of resolved issues for each top label.

With the utility functions provided, you should focus on implementing creative analyses that generate intersting and insightful insights.

In addition to the utility functions, an example analysis has also been implemented in `example_analysis.py`. It illustrates how to use the provided utility functions and how to produce output.

## Setup

To get started, your team should create a fork of this repository. Then, every team member should clone your repository to their local computer. 


### Install dependencies

In the root directory of the application, create a virtual environment, activate that environment, and install the dependencies like so:

```
pip install -r requirements.txt
```

### Download and configure the data file

Download the data file (in `json` format) from the project assignment in Canvas and update the `config.json` with the path to the file. Note, you can also specify an environment variable by the same name as the config setting (`ENPM611_PROJECT_DATA_PATH`) to avoid committing your personal path to the repository.


### Run an analysis

With everything set up, you should be able to run the existing example analysis:

```
python run.py --feature 0
```

That will output basic information about the issues to the command line.


## VSCode run configuration

To make the application easier to debug, runtime configurations are provided to run each of the analyses you are implementing. When you click on the run button in the left-hand side toolbar, you can select to run one of the three analyses or run the file you are currently viewing. That makes debugging a little easier. This run configuration is specified in the `.vscode/launch.json` if you want to modify it.

The `.vscode/settings.json` also customizes the VSCode user interface sligthly to make navigation and debugging easier. But that is a matter of preference and can be turned off by removing the appropriate settings.

---- feature 3

`label_analysis.py`: This module runs a top-three issue label analysis over time, examining issue creation and resolution patterns. The run() method loads issues from a data source, processes them into a DataFrame, identifies the top three labels based on frequency, and plots a yearly bar chart showing the number of resolved issues for each top label.

------
Explanation of "Top Commenters vs Top Issue Creators"  -- feature 4

What the Graph Shows:
-Left Chart (Top Issue Creators): This bar chart shows the top 25 contributors who have created the most issues in the project. Each bar represents a contributor, and the length of the bar indicates how many issues they have created.
-Right Chart (Top Commenters): This bar chart shows the top 25 contributors who have made the most comments on issues. Each bar represents a contributor, and the length of the bar indicates how many comments they have made.

Why It’s Interesting:
-Different Roles in the Project: This comparison allows us to see how different contributors engage with the project. Some contributors may be more focused on reporting issues (issue creators), while others are more active in providing feedback or solutions through comments (commenters).

Notable Observations:
-abn appears in both charts, indicating that they are not only active in creating issues but also in commenting on them. This suggests that abn is a highly engaged contributor who participates in both identifying and discussing issues.
dimbleby is primarily engaged in commenting, with over 3000 comments but fewer issue creations. This suggests that dimbleby plays a key role in discussions and providing feedback rather than reporting new issues.
ghost is a top issue creator but does not appear as prominently in the commenter chart, indicating their focus is more on reporting rather than discussing issues.

Insight into Contributor Behavior: This analysis helps us understand the roles different contributors play in the project. Some may specialize in identifying problems (issue creators), while others focus on discussing and resolving them (commenters). For example, contributors like github-actions[bot], which appears prominently as a top commenter, likely automate responses or perform routine tasks.

---

 Explanation of "Distribution of Issue Response Times"  --- feature 6

What the Graph Shows:
-This histogram shows how quickly issues receive their first response after being created. The x-axis represents response time in days, and the y-axis represents the number of issues. The graph includes response times ranging from 0 to over 1400 days.

Why It’s Interesting:
-Quick Responses for Most Issues: The graph reveals that a large majority of issues receive a response very quickly, with over 5000 issues being responded to within just a few days. This suggests that the project is actively maintained, with contributors responding promptly to new issues.

Outliers with Long Response Times: However, we also see a small number of outliers where issues took much longer to receive a response — some even taking up to 1412 days. These outliers could indicate lower-priority or more complex issues that took longer to address.

Project Health Indicator: A quick response time is often a sign of an active and well-maintained project. However, identifying long-standing unresolved issues could help prioritize future work and improve overall project health. The presence of outliers suggests there may be areas where certain issues are being overlooked or delayed.

Additional Insights:
    Engagement Patterns:
-By comparing these two graphs (Top Commenters vs Top Issue Creators and Distribution of Issue Response Times), we can see how engagement varies among contributors. Some are more focused on creating new issues, while others are more involved in discussions and resolving existing ones.

    Project Responsiveness:
-The quick response times shown in the second graph suggest that this project is actively maintained, with most issues being addressed promptly. However, identifying long-standing unresolved issues could help improve overall project efficiency.

----
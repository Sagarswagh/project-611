# # data/load_data.py
# import json

# def load_issues(file_path='poetry_issues_all.json'):
#     with open(file_path, 'r') as f:
#         data = json.load(f)
#     return data
import json

def load_issues():
    with open('poetry_issues_all.json', 'r') as file:
        issues = json.load(file)
    return issues

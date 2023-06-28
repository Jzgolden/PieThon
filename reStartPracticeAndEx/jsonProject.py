import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Map of userId to number of complete TODOs per user
todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1

# Create list, sorted of (userId, num_complete) pairs
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

# Get max number of completed TODOs
max_complete = top_users[0][1]

# Create list of all users who have completed the max TODOs
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

# Define function to filter out completed TODOs of users with max completed todos
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Filter todos list to keep only completed TODOs of users with max completed todos
filtered_todos = list(filter(keep, todos))

# Write filtered version to file
with open("filtered_data.json", "w") as data_file:
    json.dump(filtered_todos, data_file, indent=2)


"""
The provided code performs the following actions:

1. Imports the necessary modules: `json` for JSON-related operations and `requests` for making HTTP requests.
2. Sends an HTTP GET request to the "https://jsonplaceholder.typicode.com/todos" URL using the `requests.get()` function and stores the response.
3. Parses the response text as JSON using `json.loads()` and assigns it to the `todos` variable.
4. Creates a mapping of the number of completed TODOs per user ID in the `todos_by_user` dictionary.
5. Sorts the `todos_by_user` dictionary by the number of completed TODOs in descending order and stores it in the `top_users` list.
6. Determines the maximum number of completed TODOs by retrieving the count from the first item in the `top_users` list.
7. Identifies all the users who have completed the maximum number of TODOs and stores their user IDs in the `users` list.
8. Defines a `keep()` function that filters out completed TODOs of users who have not completed the maximum number of TODOs.
9. Filters the `todos` list using the `keep()` function and stores the filtered TODOs in the `filtered_todos` list.
10. Writes the `filtered_todos` list to the "filtered_data.json" file using `json.dump()`. The file is opened in write mode using the `with` statement, and the JSON data is indented for readability.

Overall, this code retrieves a list of TODOs from a JSON API, calculates the number of completed TODOs per user, identifies the users with the maximum number of completed TODOs, filters out the completed TODOs of users who haven't completed the maximum, and writes the filtered TODOs to a JSON file.
"""
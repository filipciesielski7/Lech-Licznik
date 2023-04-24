# Part 2

## Code Explanation
1. `import json`: imports the built-in json module, which is used to encode and decode JSON data.
2. `import requests`: imports the third-party requests module, which is used to make HTTP requests.
3. `from utils import getDate`: imports the getDate function from the utils module, which is used to convert a Unix timestamp to a human-readable date and time.
4. `s = requests.session()`: creates a new requests session object.
5. `s.get(f'https://bilety.lechpoznan.pl/Stadium/Index?eventId={eventId}')`: sends a GET request to the specified URL, which sets up a session cookie for future requests.
6. The functions from `sectors.py` file handle the computation of sector data and capacities.

## Uploading zip
1. In your local development environment, create a zip file containing all the necessary *.py files by running the `zip -r function.zip *.py` command.
2. When uploading the zip file to AWS Lambda, make sure to include any required dependencies or libraries such as the requests library. If you receive an error message like "Unable to import module 'lambda_function': No module named 'requests'", you can fix it by installing the library and adding it to the zip file using the command `pip install requests -t .` and then `zip -r function.zip *.py */`.

## Timeout
1. If you receive an error message like "Task timed out after 3.06 seconds", you can fix it by increasing the timeout value for the Lambda function. By default, Lambda functions have a timeout of 3 seconds, which may not be enough for some tasks. You can increase the timeout value up to a maximum of 15 minutes.
2. Click the "Configuration" tab.
3. Under "General configuration", click "Edit".
4. Increase the "Timeout" value (in seconds) to the desired value.
5. Click "Save".

## Running function locally
1. You can run the lambda_function.py script locally using the command `python3 lambda_function.py`. This will allow you to test the script and debug any issues that may arise before deploying it to AWS Lambda. (Note that you will need to have the requests library installed in your local environment in order to run the script successfully).
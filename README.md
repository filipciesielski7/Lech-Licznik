<h1 align="center">
    Lech Licznik 🔵
</h1>

# Part 1

## Creation of Lambda function
1. Open the AWS Management Console and navigate to the Lambda service.
2. Click the "Create function" button.
Choose the option to "Author from scratch".
3. Give your function a name and select the runtime you want to use (e.g. Lech-Licznik and Python 3.10).
4. Click the "Create function" button.

## Test function and CloudWatch logs
1. In the Lambda console, navigate to the "Function overview" page.
2. Click the "Test" button in the top right corner.
3. Select the "Create new test event" option and give your test event a name.
4. In the JSON editor, specify the input data that your function will receive (if any).
5. Click "Create".
6. Click the "Test" button again to run the test.
7. Once the test has finished, navigate to the CloudWatch Logs console.
8. Click the log group for your function and then click the log stream for the latest invocation.
9. View the logs to see the output of your function and any errors.

## First modification via console
1. In the Lambda console, navigate to the "Function overview" page.
2. Click the "Edit code" button.
3. Make your changes to the code in the console editor.
4. Click "Save" to save your changes.
5. Click "Deploy" to deploy the updated function.

## First modification via zip upload
1. In your local development environment, create a zip file containing your code by running the `zip -r function.zip *.py` command.
2. In the Lambda console, navigate to the "Function overview" page.
3. Click the "Upload" button in the "Function code" section.
4. Choose the option to upload a .zip file and select the zip file you created.
5. Click "Save" to save your changes and deploy the updated function.

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

# Part 3

## Code Explanation
1. The `stadium_capacity()` function calculates the total seating capacity of all sectors in sale and not in sale.
2. The `free_seats()` function calculates the total number of free seats in sectors in sale.
3. The `not_available_seats()` function calculates the total number of not available seats in sectors not in sale.
4. Finally, the calculated metrics are used to calculate the number of sold tickets, and a message with this information is printed to the console.


# Part 4

## Adding an API Gateway URL
1. Open the AWS Management Console and navigate to the Lambda service.
2. Select the function that you want to add an API Gateway trigger to.
3. Click on the "Add trigger" button.
4. Select "API Gateway" as the trigger type.
5. Select "REST API" as the API type and choose "Create a new API".
6. Choose the "Open" security option to allow unauthenticated access to your API.
7. Click on the "Add" button to add the trigger to your Lambda function.
8. Once the trigger has been added, you will see a new API Gateway icon in the designer view of your Lambda function. Click on this icon to open the API Gateway console.
9. In the "Method Execution" section of the API Gateway console, select the method you want to add the URL query string parameter to.
10. Click on the "Method Request" card to open the method request settings.
11. Scroll down to the "URL Query String Parameters" section and click the "Add query string" button.
12. Enter the name of the query string parameter you want to add (in this case, "id").
13. Click the "Save" button to save the changes.

## Handling different invocation methods in AWS Lambda Function
* The purpose of this code is to check if the event was invoked via API Gateway or through the test button in the Lambda console. When the event is invoked through API Gateway, the id parameter is passed in as a query string parameter, which is retrieved in step 5. If the id parameter is not present in the query string, a 400 Bad Request response is returned.
* On the other hand, when the event is invoked through the test button in the Lambda console, the id parameter is not passed in as a query string parameter. In this case, a default value of 2250 is assigned to the id variable in step 8. The tweet variable is also set to True to indicate that the event was not invoked through API Gateway.

## Adding CloudWatch Events Trigger to Lambda Function
1. Open the AWS Management Console and navigate to the Lambda service.
2. Select the function that you want to add a trigger to.
3. Click on the "Add trigger" button.
4. Select "CloudWatch Events" as the trigger type.
5. Choose "Create a new rule" for the rule dropdown menu.
6. In the "Rule name" field, enter a name for your rule.
7. In the "Schedule expression" field, enter a valid cron expression. You can use tools like Cron Guru to generate a valid expression. (in this case, `*/10 * * * ? *`)
8. Click on the "Add" button to add the trigger to your Lambda function.

# Part 5

## Creating KMS key

1. Open the AWS Management Console and navigate to the KMS service.
2. Click the "Create key" button.
3. Select "Symmetric key" as the key type and click "Next".
4. Choose "KMS generated key" as the key material origin and click "Next".
5. Enter a name for your key (e.g. "Twitter Auth Keys") in the "Alias" field and click "Next".
6. On the "Define key usage permissions" page, choose role of the lambda function You want to use key in.
7. Review your key settings and click "Finish".
8. After creating the key, copy the ARN (Amazon Resource Name) of the key, which can be found on the key details page.

## Encrypting an Environment Variable in Lambda using KMS Key.

1. Open the AWS Management Console and navigate to the Lambda service.
2. Select the function that you want to add an encrypted environment variable to.
3. Click on the "Configuration" tab and scroll down to the "Environment variables" section.
4. Click the "Edit" button to edit the environment variables.
5. Enter the name of the environment variable you want to encrypt and its value, then click the "Encrypt" checkbox next to the value field.
6. In the "KMS key ARN" field, paste the ARN of the KMS key you created earlier.
7. Click the "Save" button to save the encrypted environment variable.

## Twitter authentication

- This code block is used to retrieve and decrypt an environment variable named twitter_auth_keys that contains authentication keys for Twitter API.
- The os.environ method is used to retrieve the value of the twitter_auth_keys environment variable. This value is then passed to the boto3.client('kms').decrypt() method to decrypt the value.
- The decryption process requires the KMS key ID or ARN that was used to encrypt the environment variable. This is automatically handled by the EncryptionContext parameter, which specifies the AWS Lambda function's name.
- The decrypted value is then loaded as a JSON object using the json.loads() method and stored in the TWITTER_AUTH_KEYS variable. This variable is used to authenticate with the Twitter API using the Tweepy library.

## Links

* [Twitter profile](https://twitter.com/benebelnd1922)
* [Tweepy tutorial](https://realpython.com/twitter-bot-python-tweepy/)
* Others: [Pogoń Szczecin](https://ilunapogon.pl/), [Korona Kielce](https://koronnylicznik.pl/korrcz)

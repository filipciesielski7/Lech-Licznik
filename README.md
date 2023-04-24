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

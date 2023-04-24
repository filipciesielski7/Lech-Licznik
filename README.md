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
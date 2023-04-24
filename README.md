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

import os
import json
import boto3
import tweepy
from base64 import b64decode


ENCRYPTED_TWITTER_AUTH_KEYS = os.environ['twitter_auth_keys']

TWITTER_AUTH_KEYS = json.loads(
    boto3.client('kms').decrypt(
        CiphertextBlob=b64decode(ENCRYPTED_TWITTER_AUTH_KEYS),
        EncryptionContext={
            'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME'],
        },
    )['Plaintext'].decode('utf-8')
)

auth = tweepy.OAuthHandler(
    TWITTER_AUTH_KEYS['consumer_key'],
    TWITTER_AUTH_KEYS['consumer_secret'],
)

auth.set_access_token(
    TWITTER_AUTH_KEYS['access_token'],
    TWITTER_AUTH_KEYS['access_token_secret'],
)

api = tweepy.API(auth)

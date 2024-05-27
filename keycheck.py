import argparse
import requests
import subprocess
import os
from colorama import Fore, Style


def flags():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slack", action='store_true', help="Check Slack API Token")
    parser.add_argument("--twilio", action='store_true', help="Check Twilio Account_sid and Auth Token")
    parser.add_argument("--heroku", action='store_true', help="Check Heroku API Key")
    parser.add_argument("--zendesk", action='store_true', help="Check Zendesk Api Key")
    parser.add_argument("--circleci", action='store_true', help="Check Gitlab Personal Access Token")
    parser.add_argument("--aws", action='store_true', help="Check AWS Access Key ID and Secret Access Key")
    args = parser.parse_args()
    parser.parse_args()
    
    if not any([args.slack, args.twilio, args.heroku, args.zendesk, args.circleci, args.aws]):
        parser.error("Please provide at least one of the following options: --slack, --twilio, --zendesk, --circleci, --aws or --heroku")

    return args

def response_code(response):
    if 200 <= response.status_code < 300:
        print(f"\nResponse: {Fore.GREEN}{response.json()} {Style.RESET_ALL}")
    else:
        print(f"\nResponse: {Fore.RED}{response.json()} {Style.RESET_ALL}")

def slack_request(token):
    url = "https://slack.com/api/auth.test"
    params = {
        'token': token,
        'pretty': 1
    }
        
    response = requests.post(url=url, params=params)
        
    response_code(response)
    
def twilio_request(sid, token):
    account_sid = sid
    auth_token = token
    url = "https://api.twilio.com/2010-04-01/Accounts.json"
        
    response = requests.get(url, auth=(account_sid, auth_token))
    
    response_code(response)
    
def heroku_request(api_key):
    url = 'https://api.heroku.com/apps'
    headers = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.post(url, headers=headers)
        
    response_code(response)
    
def zendesk_request(target, token):
    target = target
    token = token
    url = f'https://{target}.zendesk.com/api/v2/users.json'
    email = f'support@{target}.com/token'

    response = requests.get(url, auth=(email, token))
        
    response_code(response)
    
def circleci_request(token):
    url = f"https://circleci.com/api/v1.1/me?circle-token={token}"
    response = requests.get(url)
        
    print(f"\nResponse: {response.text}")
    
if __name__ == "__main__":
    
    args = flags()
    
    if args.slack:
        slack_token = input("Please enter your Slack Token: ")
        slack_request(slack_token)
    
    if args.twilio:
        twilio_sid = input("Please enter your Account_sid: ")
        twilio_token = input("Please enter your Auth Token: ")
        twilio_request(twilio_sid, twilio_token)
    
    if args.heroku:
        heroku_token = input("Please enter your Heroku Token: ")
        heroku_request(heroku_token)
    
    if args.zendesk:
        zendesk_subdomain = input("Please enter your Zendesk Target: ")
        zendesk_token = input("Please enter your Zendesk Token: ")
        zendesk_request(zendesk_subdomain, zendesk_token)
        
    if args.circleci:
        circleci_token = input("Please enter your CircleCI Token: ")
        circleci_request(circleci_token)
        
    if args.aws:
        aws_access_key = input("Please enter your AWS Access KEY: ")
        aws_secret_access_key = input("Please enter your AWS Secret Access KEY: ")
        
        env_vars = {
            "AWS_ACCESS_KEY_ID": aws_access_key,
            "AWS_SECRET_ACCESS_KEY": aws_secret_access_key
        }
        
        result = subprocess.run(
            ["aws", "sts", "get-caller-identity"],
            env={**os.environ, **env_vars},
            capture_output=True,
            text=True
        )
    
        print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)

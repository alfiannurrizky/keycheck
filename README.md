# <center>keycheck</center>

Validate API Keys found on a Bug Bounty or a pentest. Thanks a bunch [keyhacks](https://github.com/streaak/keyhacks) for providing the API information used to validate access tokens or API keys. <br>

## Install

```
▶ git clone https://github.com/alfiannurrizky/keycheck.git

cd keycheck

python3 keycheck.py --heroku
```

## Basic Usage

Below is a list of commands and their descriptions for checking various API keys and tokens:

    --slack: Check Slack API Token.
    --twilio: Check Twilio Account_sid and Auth Token.
    --heroku: Check Heroku API Key.
    --zendesk: Check Zendesk Api Key.
    --circleci: Check Gitlab Personal Access Token.
    --aws: Check AWS Access Key ID and Secret Access Key.

## IMPORTANT!!

If you are using this tool and have not installed the AWS CLI, please install it first. Follow the steps below to ensure you have the AWS CLI installed:

```
sudo apt install python3-pip -y
sudo apt install awscli -y
pip3 install --upgrade awscli
```

Verify if AWS CLI has successfully installed

```
aws --version
```

#### Feel Free to Contribute

    1. Fork this repository.
    2. Clone your fork.
    3. Create new branch e.g (feature/new-feature).
    4. Commit your changes.
    4. Push to your fork e.g (git push -u origin feature/new-feature ).
    7. create a Pull Request

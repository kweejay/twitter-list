import argparse
import os
import pandas as pd
import tweepy
from dotenv import load_dotenv

# load .env file
load_dotenv()

parser = argparse.ArgumentParser(description = "Adds users from a .csv file to a Twitter list.")
parser.add_argument("list_id", help = "Provide the Twitter list id from the URL.")
parser.add_argument("csv", help = "Provide the path for the csv file.")

args = parser.parse_args()

list_id = args.list_id
csv = args.csv

# load list of twitter profile URLs and parse for Twitter handles
df = pd.read_csv(csv,header=None)
list_twitter_urls = df.to_dict(orient="list")[0]
edited_list = []

for account in list_twitter_urls:
    edited_list.append(account.replace("https://twitter.com/",""))

# set up tweepy client to interact with api
client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET_KEY"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
    wait_on_rate_limit=True,
)

# get all the users
responses = client.get_users(usernames = edited_list)

# iterate through responses and store user ids into the list
data = responses[0]
for user in data:
    client.add_list_member(list_id, user.id)

print(f"{len(edited_list)} users added successfully to the Twitter list.")
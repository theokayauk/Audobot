import logging
import os
import slack_token as tk
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
import csv

def hey():
    print('hey')

def info(dummy:list):
    
    for keyword in dummy:
        # WebClient instantiates a client that can call API methods
        print(tk.bot_token)
        client = WebClient(token= tk.bot_token)
        logger = logging.getLogger(__name__)
        try:
            # Call the conversations.list method using the WebClient
            conversation_ids = []
            for result in client.conversations_list():
                for channel in result["channels"]:
                    if channel['is_member'] == True:
                        conversation_ids.append(channel['id'])
                        
            print(conversation_ids)
            for convo in conversation_ids: 
                    result = client.conversations_history(channel=convo, inclusive=True, limit=1)
                    mess = client.chat_postMessage(channel=convo, text="Hello world!")
                    print(result)

    

        except SlackApiError as e:
            print(f"Error: {e}")

def discover(keywords:list):

    fields = ['Name','Date','Text']
    filename= ''.join(keywords) +'.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        for keyword in keywords:
            # WebClient instantiates a client that can call API methods
            print(tk.bot_token)
            client = WebClient(token= tk.bot_token)
            logger = logging.getLogger(__name__)
            try:
                # Call the conversations.list method using the WebClient
                conversation_ids = []
                for result in client.conversations_list():
                    for channel in result["channels"]:
                        if channel['is_member'] == True:
                            conversation_ids.append(channel['id'])
                            
                print(conversation_ids)
                for convo in conversation_ids: 
                        result = client.conversations_history(channel=convo, inclusive=True, limit=10000)
                        print(result)
                        for message in result['messages']:
                            text = message['text']
                            if text.find(keyword) != -1:
                                print('hit')
                                stamp = float(message['ts'])
                                stamp = round(stamp)
                                time = datetime.fromtimestamp(stamp)
                                user = message['user']
                                nameresp = client.users_profile_get(user=user)
                                name = nameresp['profile']['real_name']
                                newrow = [name, time, text]
                                csvwriter.writerow(newrow)
                                
                                continue
                            else:
                                pass

            except SlackApiError as e:
                print(f"Error: {e}")

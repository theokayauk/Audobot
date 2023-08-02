import logging
import os
import slack_token as tk
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def keyword_get(keywords:list):
    
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
                    result = client.conversations_history(channel=convo, inclusive=True, limit=1)
                    print(result)

    

        except SlackApiError as e:
            print(f"Error: {e}")

keyword_get(['hey'])
from rasa_sdk import Action
import os
import logging
import pprint, json
from rasa_sdk.events import SlotSet
from timefhuman import timefhuman
from slackclient import SlackClient
import requests
import yaml
from datetime import datetime

logger = logging.getLogger(__name__)
from pprint import pprint

def credentials():
  return yaml.load(open('./credentials.yml'))

def compamy_url():
  return "https://light.jntesting.net/"

def fetchUser(tracker):
  username = tracker.sender_id
  _creds = credentials()
  url = "https://slack.com/api/users.profile.get"
  userinfo = CompanyClient().post(url, {"token": _creds['slack']['slack_token'], "user": username}, '')
  print("ssssssss")
  emailid = userinfo['profile']['email']
  print(emailid)
  return username, emailid

def headers(email):
  _creds = credentials()
  headers = {
     'X-Meeting-Bot-Token': _creds['slack']['slack_token'],
     'X-Meeting-Bot-User-Emailid': "harshal.jain@jifflenow.com",
     'X-Mobile-User-UUID': "A-Ub9LsfZfR5ZS12E1oGmA",
     'content-type': 'application/json'
   }
  return headers

def getMeetings(tracker):
  # user_name, email = fetchUser(tracker)
  user_name, email = "asda", "asdasd"

  message = tracker.latest_message['text']
  
  print(message)
  date = timefhuman(message).strftime("%Y-%m-%d")
  base_url = "https://light.jntesting.net/api/portal/calendar/users?"
  params = "api_params[user_email]=" + "delhi.ganesan@jifflenow.info" + "&api_params[calendar_start_date]=" + str(date) +  "&api_params[calendar_end_date]=" + str(date)

  url = base_url + params
  # base_url = compamy_url() + "/api/portal/calendar/users?"
  # data = {"api_params": {"calendar_start_date": str(date), "calendar_end_date": str(date), "user_email": email }}
  response = CompanyClient().get(url, {}, email)
  print(response)
  return response

class ActionFetchMyCustomer(Action):
  def name(self):
    return 'action_fetch_my_customer'

  def run(self, dispatcher, tracker, domain):
    msg = 'people i am meeting'
    message = tracker.latest_message['text']
    date = timefhuman(message).strftime("%Y-%m-%d")

    response = getMeetings(tracker)
    meetings = response['data']['items'][0]['calendar']['meetings']
    meetings_for_date = meetings.get(date)
    logger.warn(meetings_for_date)
    msg = "Please find Schedule here \n"

    try:
      if meetings_for_date is not None:
        for meeting in meetings_for_date:
          msg = " meeting: " + y["meeting_with"] + " " + y["location"] + " \n " + msg
      else:
        msg = "No meetings found !!"
    except:
      msg = "Please try to frame the meeting date in another format"

    dispatcher.utter_message(msg)
    return []

class ActionFetchMeetings(Action):
  def name(self):
    return 'action_fetch_meetings'

  def run(self, dispatcher, tracker, domain):
    message = tracker.latest_message['text']
    date = timefhuman(message).strftime("%Y-%m-%d")
    response = getMeetings(tracker)
    print(response)
    meetings = response['data']['items'][0]['calendar']['meetings']
    meetings_for_date = meetings.get(date)
    logger.warn(meetings_for_date)
    msg = "Please find Schedule here \n"

    try:
      if meetings_for_date is not None:
        for meeting in meetings_for_date:
          start_time = datetime.strptime(meeting["start_time"], '%Y-%m-%dT%H:%M:%SZ').strftime("%H:%M")
          end_time = datetime.strptime(meeting["end_time"], '%Y-%m-%dT%H:%M:%SZ').strftime("%H:%M")
          msg += "Meeting With: " + meeting["meeting_with"] + " - " + meeting["location"] + " - " + start_time + " - " + end_time + "\n"
      else:
        msg = "No meetings found !!"
    except:
      msg = "Please try to frame the meeting date in another format"

    dispatcher.utter_message(msg)
    return []

class CompanyClient():
  
  def post(self, url, data, email):
    response = requests.post(url, data=data, headers=headers(email)).json()
    return response
  def get(self, url, data, email):
    response = requests.get(url, params=data, headers=headers(email))

    response = response.json()
    return response

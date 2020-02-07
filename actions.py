# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action
import os
import logging
import pprint, json
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from timefhuman import timefhuman
from slackclient import SlackClient
import requests
import yaml
from rasa_sdk.events import SlotSet
from datetime import datetime
from datetime import timedelta

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

class ActionAskMeetingdate(Action):
  def name(self):
    return 'action_ask_meetingdate'

  def run(self, dispatcher, tracker, domain):
    message_title = 'Please choose Meeting Date'

    url = "https://light.jntesting.net/api/mergetest/event_info?basic_info=true"
    response = CompanyClient().get(url, {}, "harshal.jain@jifflenow.com")

    #event_dates = [{"title": "21/02/2020", "payload": '/avaialabilityChoose{"avaialability": "21/02/2020"}'}, {"title": "22/02/2020", "payload": '/avaialabilityChoose{"avaialability": "22/02/2020"}'}]

    start_date = response["data"]["event"]["start_date"]
    start_date = datetime.strptime(start_date, '%Y-%m-%d')

    end_date = response["data"]["event"]["end_date"]
    end_date =  datetime.strptime(end_date, '%Y-%m-%d')

    event_dates = []
    for n in range(int ((end_date - start_date).days)):
      date = start_date + timedelta(n)
      date = date.strftime("%d/%m/%Y")
      _h = {}
      _h["title"] = date
      _h["payload"] = '/avaialabilityChoose{"avaialability":' + '"' +str(date)+ '"}'
      event_dates.append(_h)

    dispatcher.utter_message(text=message_title, buttons=event_dates)
    return []

class ActionAskMeetingTime(Action):
  def name(self):
    return 'action_ask_meetingtime'

  def run(self, dispatcher, tracker, domain):
    message_title = 'Please choose Meeting time'
    meeting_times = [{"title": "21:00", "payload": '/timeChoose{"time": "22:00"}'}, {"title": "22:00", "payload": '/timeChoose{"time": "22:00"}'}]
    dispatcher.utter_message(text=message_title, buttons=meeting_times)
    return []

class ActionFetchRooms(Action):
  def name(self):
    return 'action_fetch_rooms'

  def run(self, dispatcher, tracker, domain):
    message_title = 'Please choose Meeting time'
    event_date = tracker.get_slot("avaialability")

    #event_date = "07-02-2020"
    start_time = int(float(tracker.get_slot("time")))
    end_time = start_time + 30

    base_url = "https://light.jntesting.net/api/mergetest/activities_rooms?activity_uuid=Gp72-KVfWIBz6rmsDT1q8A"
    params = "&event_date=" + event_date + "&start_time=" + start_time + "&end_time=" + end_time
    url = base_url + params

    response = CompanyClient().get(url, {}, "harshal.jain@jifflenow.com")
    rooms_data = response["data"]["activity"]["rooms"]
    rooms = {}
    if rooms_data is not None:
      for room in rooms_data:
        _h = {}
        _h["title"] = room["name"]
        _h["payload"] = '/roomChoose{"room": ' + '"' + room["uuid"] + '"}'
        rooms.append(_h)
    else:
      rooms = "No Rooms found !! :("

    #rooms = [{"title": "Room1", "payload": '/roomChoose{"room": "room1"}'}, {"title": "room2", "payload": '/roomChoose{"room": "Room2"}'}]
    print("pringint message", rooms)
    dispatcher.utter_message(text=message_title, buttons=rooms)
    return []


class ActionCreateMeeting(Action):
  def name(self):
    return 'action_create_meeting'

  def run(self, dispatcher, tracker, domain):
    print("pringint message", tracker.get_slot('avaialability'))
    date = tracker.get_slot("avaialability")
    room = tracker.get_slot('room')
    time = tracker.get_slot('time')
    date_time = date + " " + time
    start_time = datetime.strptime(date_time, '%d/%m/%Y %H:%M')
    end_time = start_time + timedelta(minutes=30)

    start_time = start_time.strftime("%Y/%m/%d %I:%M %p")
    end_time = end_time.strftime("%Y/%m/%d %I:%M %p")

    meeting_create_url = "https://light.jntesting.net/api/mergetest/meeting_request/create"
    request_params = {
      "api_params": {
        "meeting_request": {
          "activity_uuid": "Gp72-KVfWIBz6rmsDT1q8A",
          "meeting_with": "test",
          "start_time": start_time,
          "end_time": end_time,
          "location_preference": {},
          "custom_fields": {
            "meeting_with": "test"
          },
          "requestor": "lbxqoATuWUPNsLcNlOdOqg",
          "room_uuid": "GPzzNyYctUTsZdgaDE61yg"
        }
      }
    }
    response = CompanyClient().post(meeting_create_url, json.dumps(request_params), '')

    msg = "Meeting created successfully with details: \n"
    msg = msg + "Meeting with: "
    dispatcher.utter_message("Meeting created successfully.")
    return []

class CompanyClient():
  def post(self, url, data, email):
    response = requests.post(url, data=data, headers=headers(email)).json()
    return response
  def get(self, url, data, email):
    response = requests.get(url, params=data, headers=headers(email))
    response = response.json()
    return response

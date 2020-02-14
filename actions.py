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
import requests
import yaml
from rasa_sdk.events import SlotSet
from datetime import datetime
from datetime import timedelta
from requests.models import PreparedRequest

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
  emailid = userinfo['profile']['email']
  print(emailid)
  return username, emailid

def headers(email):
  _creds = credentials()
  headers = {
     'X-Meeting-Bot-Token': _creds['slack']['slack_token'],
     'X-Meeting-Bot-User-Emailid': "<email of the user>",
     'X-Mobile-User-UUID': "<user_uuid>",
     'Content-Type': 'application/json',
     'authorization': '<Token>'
   }
  return headers

def getMeetings(tracker):
  # user_name, email = fetchUser(tracker)
  user_name, email = "asda", "asdasd"
  message = tracker.latest_message['text']
  date = timefhuman(message).strftime("%Y-%m-%d")
  base_url = "https://light.jntesting.net/api/portal/calendar/users?"
  params = "api_params[user_email]=" + "<email_address>" + "&api_params[calendar_start_date]=" + str(date) +  "&api_params[calendar_end_date]=" + str(date)

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

class ActionAskEvent(Action):
  def name(self):
    return 'action_ask_event'


  def run(self, dispatcher, tracker, domain):
    message_title = 'Please choose event'
    all_events = []
    event_url = 'https://light.jntesting.net/api/portal/users_events?page=self_serve'
    response = CompanyClient().get(event_url, {}, '')
    for event in response["data"]["events"]:
      if event['status'] == 'LIVE':
        _h = {}
        _h["title"] = event["event_name"]
        _h["payload"] = '/eventChoose{"event": ' + '"' + event["event_system_name"] + '"}'
        all_events.append(_h)

    dispatcher.utter_message(text=message_title, buttons=all_events)
    return []

class ActionAskMeetingtype(Action):
  def name(self):
    return 'action_ask_meetingtype'

  def run(self, dispatcher, tracker, domain):
    event_system_name = tracker.get_slot('event')
    message_title = 'Please choose Meeting type'
    meeting_types = []
    meeting_type_url = "https://light.jntesting.net/api/" + event_system_name + "/get_activities?entityType=MeetingRequest&per_page=10000"

    response = CompanyClient().get(meeting_type_url, {}, '')
    print(response)
    for activity in response['data']['activities']:
      _h = {}
      _h["title"] = activity["display_name"]
      _h["payload"] = '/meetingtypeChoose{"meetingtype": ' + '"' + activity["uuid"] + '"}'
      meeting_types.append(_h)
    dispatcher.utter_message(text=message_title, buttons=meeting_types)
    return []

class ActionAskMeetingdate(Action):
  def name(self):
    return 'action_ask_meetingdate'

  def run(self, dispatcher, tracker, domain):
    message_title = 'Please choose Meeting Date'
    event_system_name = tracker.get_slot('event')
    url = "https://light.jntesting.net/api/" + event_system_name + "/event_info?basic_info=true"
    response = CompanyClient().get(url, {}, "<email>")
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
    event_system_name = tracker.get_slot('event')
    meeting_type = tracker.get_slot('meetingtype')
    date = tracker.get_slot("avaialability")
    meeting_time_url = "https://light.jntesting.net/external-request/"+ event_system_name +"/api/meeting-types/" + meeting_type +"/calendar?duration=45"
    date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
    message_title = 'Please choose Meeting time'
    time_slots = []
    print('meeting timeslot url', meeting_time_url)
    response = CompanyClient().get(meeting_time_url, {}, '')
    for timeslot in response['data'][date]:
      display_label = datetime.strptime(timeslot, '%H:%M')
      t2 = datetime(1900,1,1)
      seconds = (display_label-t2).total_seconds()
      value = seconds / 60
      _h = {}
      _h["title"] = timeslot
      _h["payload"] = '/timeChoose{"time":' + '"' + str(value) + '"}'
      time_slots.append(_h)

    dispatcher.utter_message(text=message_title, buttons=time_slots)
    return []

class ActionFetchRooms(Action):
  def name(self):
    return 'action_fetch_rooms'

  def run(self, dispatcher, tracker, domain):
    message_title = 'Please choose Meeting room'
    event_system_name = tracker.get_slot('event')
    event_date = tracker.get_slot("avaialability")
    meeting_type = tracker.get_slot('meetingtype')
    #event_date = "07-02-2020"
    start_time = int(float(tracker.get_slot("time")))
    end_time = start_time + 30

    base_url = "https://light.jntesting.net/api/"+ event_system_name +"/activities_rooms?activity_uuid="+ meeting_type
    params = "&event_date=" + event_date + "&start_time=" + str(start_time) + "&end_time=" + str(end_time)
    url = base_url + params
    response = CompanyClient().get(url, {}, '')
    rooms_data = response["data"]["activity"]["rooms"]
    rooms = []
    if rooms_data is not None:
      for room in rooms_data:
        _h = {}
        _h["title"] = room["name"]
        _h["payload"] = '/roomChoose{"room": ' + '"' + room["uuid"] + '"}'
        rooms.append(_h)
    else:
      message_title = 'No rooms'
      rooms = []

    #rooms = [{"title": "Room1", "payload": '/roomChoose{"room": "room1"}'}, {"title": "room2", "payload": '/roomChoose{"room": "Room2"}'}]
    dispatcher.utter_message(text=message_title, buttons=rooms)
    return []


class ActionCreateMeeting(Action):
  def name(self):
    return 'action_create_meeting'

  def convert(self, minutes):
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d" % (hours, minutes)

  def run(self, dispatcher, tracker, domain):
    event_system_name = tracker.get_slot("event")
    meetingtype = tracker.get_slot("meetingtype")
    date = tracker.get_slot("avaialability")

    room = tracker.get_slot('room')
    meeting_with = "test"
    time = int(float(tracker.get_slot('time')))
    time = self.convert(time)

    date_time = date + " " + time
    start_time = datetime.strptime(date_time, '%d/%m/%Y %H:%M')
    end_time = start_time + timedelta(minutes=30)
    start_time = start_time.strftime("%Y/%m/%d %I:%M %p")
    end_time = end_time.strftime("%Y/%m/%d %I:%M %p")

    meeting_create_url = "https://light.jntesting.net/api/"+ event_system_name +"/meeting_request/create"
    request_params = {
      "api_params": {
        "meeting_request": {
          "activity_uuid": meetingtype,
          "meeting_with": meeting_with,
          "start_time": start_time,
          "end_time": end_time,
          "location_preference": {},
          "custom_fields": {
            "meeting_with": meeting_with
          },
          "requestor": "lbxqoATuWUPNsLcNlOdOqg",
          "room_uuid": room
        }
      }
    }
    print(request_params)
    response = CompanyClient().post(meeting_create_url, json.dumps(request_params), '')
    print(response)
    msg = "Meeting created successfully.\n"
    # msg = msg + "Meeting with: " + meeting_with

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

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
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from datetime import datetime
from datetime import timedelta

logger = logging.getLogger(__name__)


class ActionFetchMeetings(Action):
  def name(self):
    return 'action_fetch_meetings'

  def run(self, dispatcher, tracker, domain):
    message = tracker.latest_message['text']
    try:
      date = timefhuman(message).strftime("%Y-%m-%d")
      logger.info(date)
      user_uuid = "A-Ub9LsfZfR5ZS12E1oGmA"

      base_url = "https://light.jntesting.net/api/portal/calendar/users?"
      params = "api_params[calendar_start_date]=" + str(date) +  "&api_params[calendar_end_date]=" + str(date) + "&api_params[user_uuid]=" + user_uuid + "&api_params[current_location_uuid]=FIdWeyXx5XgB-RSrmo1jAA"

      url = base_url + params
      headers = {
        'X-Mobile-User-UUID': 'djiPw8pI-wUNBPvD9FfgGQ',
        'Authorization': 'Bearer acd997f37ba67c52892c72f59cbf2eaff8c38367535f166034ef846997049f1a'
      }

      response = requests.get(url, headers=headers).json()
      meetings = response['data']['items'][0]['calendar']['meetings']
      meetings_for_date = meetings.get(date)
      logger.info(meetings_for_date)
      msg = ""

      if meetings_for_date is not None:
        for y in meetings_for_date:
          msg = " meeting: " + y["meeting_with"] + " " + y["location"] + " \n " + msg
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
    event_dates = [{"title": "21/02/2020", "payload": '/avaialabilityChoose{"avaialability": "21/02/2020"}'}, {"title": "22/02/2020", "payload": '/avaialabilityChoose{"avaialability": "22/02/2020"}'}]
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
    rooms = [{"title": "Room1", "payload": '/roomChoose{"room": "room1"}'}, {"title": "room2", "payload": '/roomChoose{"room": "Room2"}'}]
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
    meeting_create_url = "https://light.jntesting.net/mergetest/meeting_request/create"
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

    print(request_params, 'meeting_request params')

    dispatcher.utter_message(msg)

    return []

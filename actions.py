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

logger = logging.getLogger(__name__)


class ActionFetchMeetings(Action):
  def name(self):
    return 'action_fetch_meetings'

  def run(self, dispatcher, tracker, domain):
    message = tracker.latest_message['text']
    try:
      date = timefhuman(message).strftime("%Y-%m-%d")
      logger.warn(date)
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
      logger.warn(meetings_for_date)
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

class ActionCreateMeeting(Action):
  def name(self):
    return 'action_create_meeting'

  def run(self, dispatcher, tracker, domain):
    print(tracker.get_slot('date'))
    logger.warn(tracker.get_slot('meetingdate'))
    logger.warn(tracker.get_slot('time'))
    logger.warn(tracker.get_slot('room'))
    msg = "Please try to frame the meeting date in another format"
    dispatcher.utter_message(msg)
    return []

# class MeetingRequestForm(FormAction):
#   def name(self):
#     return 'meeting_request_form'

#   @staticmethod
#   def required_slots(tracker: Tracker) -> List[Text]:
#     return ['date', 'time']


#   def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#     return {
#       "date": self.from_entity(entity="date"),
#       "time": self.from_entity(entity="time")
#     }

#   def submit(self, dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict]:
#         logger.warn(tracker)
#         dispatcher.utter_template('utter_submit', tracker)
#         return []

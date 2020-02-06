## happy path
* greet
  - utter_greet
  - utter_ask_howcanhelp

## sad path 2
* greet
  - utter_greet
  - utter_ask_howcanhelp
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## Fetch schedule
* greet
  - utter_greet
  - utter_ask_howcanhelp
* fetch_meetings
  - action_fetch_meetings

## Fetch schedule
* greet
  - utter_greet
* fetch_meetings
  - action_fetch_meetings

## Fetch schedule
* greet
  - utter_greet
  - utter_ask_howcanhelp
* fetch_meetings
  - action_fetch_meetings

## Fetch schedule
* greet
  - utter_greet
  - utter_ask_howcanhelp
* fetch_meetings
  - action_fetch_meetings

## interactive_story_1
* fetch_meetings
    - action_fetch_meetings
* greet
    - utter_greet
* fetch_meetings
    - action_fetch_meetings
* stop
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* fetch_meetings
    - action_fetch_meetings

## interactive_story_3
* affirm
    - utter_greet

## interactive_story_4
* affirm
    - utter_greet
* fetch_meetings
    - action_fetch_meetings

## interactive_story_5
* fetch_meetings
    - action_fetch_meetings

## BotEnquariy
* greet
  - utter_greet
* howareyou
  - utter_botgood
  - utter_ask_howcanhelp

## BotEnquariy
* greet
  - utter_greet
* sad
  - utter_cheer_up

## interactive_story_1
* fetch_meetings
    - action_fetch_meetings

## interactive_story_1
* greet
    - utter_greet
* utter_ask_howcanhelp
    - action_fetch_meetings
    - utter_cheer_up
* fetch_meetings
    - action_fetch_meetings

##Date 1
* greet
  - utter_greet
* request_meeting
  - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
  - slot{"date": "02-01-2020"}
  - action_ask_meetingtime
* timeChoose{"time": "12:00"}
  - slot{"time": "12:00"}
  - utter_choose_room
  - action_fetch_rooms
* roomChoose{"room": "room1"}
  - slot{"room": "xyz"}
  - action_create_meeting

##Date 2
* greet
  - utter_greet
* request_meeting
  - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
  - slot{"date": "02-01-2020"}
  - action_ask_meetingtime
* timeChoose{"time": "12:00"}
  - slot{"time": "12:00"}
  - utter_choose_room
  - action_fetch_rooms
* roomChoose{"room": "room2"}
  - slot{"room": "xyz"}
  - action_create_meeting

## Date time
* request_meeting
  - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
  - slot{"date": "02-01-2020"}
  - action_ask_meetingtime
* timeChoose{"time": "13:00"}
  - slot{"time": "13:00"}
  - utter_choose_room
  - action_fetch_rooms
* roomChoose{"room": "room2"}
  - slot{"room": "xyz"}
  - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingtime
* timeChoose{"time": "12:00"}
    - slot{"time": "12:00"}
    - utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "13:00"}
    - slot{"time": "13:00"}
    - utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "13:00"}
    - slot{"time": "13:00"}
    - utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "22:00"}
- utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "22:00"}
    - slot{"time": "22:00"}
    - utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "22:00"}
    - slot{"time": "22:00"}
    - utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "22:00"}
    - slot{"time": "22:00"}
    - utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "22:00"}
    - slot{"time": "22:00"}
    - utter_choose_room
    - action_fetch_rooms
* timeChoose{"room": "Room1"}
    - slot{"room": "Room1"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "22:00"}
    - slot{"time": "22:00"}
    - utter_choose_room
    - action_fetch_rooms
* timeChoose{"room": "Room1"}
    - slot{"room": "Room1"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - action_ask_meetingdate
* dateChoose{"date": "02-01-2020"}
    - slot{"date": "02-01-2020"}
    - action_ask_meetingtime
* timeChoose{"time": "22:00"}
    - slot{"time": "22:00"}
    - utter_choose_room
    - action_fetch_rooms
* roomChoose{"room": "Room1"}
    - slot{"room": "Room1"}
    - action_create_meeting

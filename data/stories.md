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
  - utter_ask_meetingdate
* meetingdateChoose{"meetingdate": "20/02/2020"}
  - slot{"meetingdate": "20/02/2020"}
  - utter_ask_time
* timeChoose{"time": "12:00"}
  - slot{"time": "12:00"}
  - utter_ask_room
* roomChoose{"room": "room1"}
  - slot{"room": "xyz"}
  - action_create_meeting

##Date 2
* greet
  - utter_greet
* request_meeting
  - utter_ask_meetingdate
* meetingdateChoose{"meetingdate": "21/02/2020"}
  - slot{"meetingdate": "21/02/2020"}
  - utter_ask_time
* timeChoose{"time": "12:00"}
  - slot{"time": "12:00"}
  - utter_ask_room
* roomChoose{"room": "room2"}
  - slot{"room": "xyz"}
  - action_create_meeting

## Date time
* request_meeting
  - utter_ask_meetingdate
* meetingdateChoose{"meetingdate": "21-02-2020"}
  - slot{"meetingdate": "21-02-2020"}
  - utter_ask_time
* timeChoose{"time": "13:00"}
  - slot{"time": "13:00"}
  - utter_ask_room
* roomChoose{"room": "room2"}
  - slot{"room": "xyz"}
  - action_create_meeting

## interactive_story_1
* request_meeting
    - utter_ask_meetingdate
* meetingdateChoose{"meetingdate": "21/02/2020"}
  - slot{"meetingdate": "21/02/2020"}
  - utter_ask_time
* timeChoose{"time": "12:00"}
    - slot{"time": "12:00"}
    - utter_ask_room
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - utter_ask_meetingdate
* meetingdateChoose{"meetingdate": "21/02/2020"}
    - slot{"meetingdate": "21/02/2020"}
    - utter_ask_time
* timeChoose{"time": "13:00"}
    - slot{"time": "13:00"}
    - utter_ask_room
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

## interactive_story_1
* request_meeting
    - utter_ask_meetingdate
* meetingdateChoose{"meetingdate": "21/02/2020"}
    - slot{"meetingdate": "21/02/2020"}
    - utter_ask_time
* timeChoose{"time": "13:00"}
    - slot{"time": "13:00"}
    - utter_ask_room
* roomChoose{"room": "Room2"}
    - slot{"room": "Room2"}
    - action_create_meeting

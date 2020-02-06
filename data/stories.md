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

## MeetingPeople
* greet
  - utter_greet
* who_all_am_i_meeting
  - action_fetch_my_customer
## interactive_story_1
* who_all_am_i_meeting
    - action_fetch_my_customer

## interactive_story_1
* who_all_am_i_meeting
    - action_fetch_my_customer

## interactive_story_1
* who_all_am_i_meeting
    - action_fetch_my_customer

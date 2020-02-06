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
* fetc_hmeetings
  - action_fetch_meetings

## Fetch schedule
* greet
  - utter_greet
* fetc_hmeetings
  - action_fetch_meetings

## Fetch schedule
* greet
  - utter_greet
  - utter_ask_howcanhelp
* fetc_hmeetings
  - action_fetch_meetings

## Fetch schedule
* greet
  - utter_greet
  - utter_ask_howcanhelp
* fetc_hmeetings
  - action_fetch_meetings

## interactive_story_1
* fetc_hmeetings
    - action_fetch_meetings
* greet
    - utter_greet
* fetc_hmeetings
    - action_fetch_meetings
* stop
    - utter_goodbye

# pomodoro
Repo for making a pomodoro timer.

Intention is to have a project to practice what I have learnt from Python-courses as well courses in selfimprovement / Monotasking.

# APIs
This project is using Google Tasks as backend. Thus it is using Googles Tasks v1 API. This requires setting up permissions using [Google Cloud Platform Console](https://console.developers.google.com/). As tasks are considered personal data, an OAuth has to be used. Google also has to verify the solution before publishing. The consent screen of a unverified solution will be very explicit that this is not a safe application. Though, as this is primarily a personal solution, this does not matter now.

To setup a OAuth client, follow the guide [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en)

Note that you also have to add the scope for the Tasks API. This is done in the "OAuth consent screen" under "Scopes for Google APIs". You might have to add scope manually, the scopes available are:
* https://www.googleapis.com/auth/tasks
* https://www.googleapis.com/auth/tasks.readonly

The API code in this project is based on the [Python Quickstart](https://developers.google.com/tasks/quickstart/python)

## Links of interest
[Google Tasks API Overview](https://developers.google.com/tasks)
[Tasks API References](https://developers.google.com/tasks/v1/reference)

# Timers
## Pomodoro
* Divide work time into 25-minute chunks called pomodoros — named after the tomato-shaped timer the inventor used to track his time.
* After each pomodoro, take a five-minute break.
* After four pomodoros, take a longer break — fifteen to thirty minutes or until you feel refreshed. Then repeat the cycle.

## 52–17 rule
https://www.fastcompany.com/3035605/the-exact-amount-of-time-you-should-work-every-day
* Work for 52 minutes
* Break for 17 minutes

## Ultradian Rhythms
https://medium.com/better-humans/avoid-burnout-and-increase-awareness-using-ultradian-rhythms-5e64158e7e19
* for every 90 minute work period, you should take 20 minutes of break time.

## Ideas
* Using YAML for configuration
* Pysimplegui as a GUI (https://pysimplegui.readthedocs.io/en/latest/)
* Possible to use Django or Flask (Flask probably preferable due to simplicity)
* Use Click (Python lib) for CLI

## Other
### PySimpleGUI
To install pysimplegui in an Anaconda dist, run the following command:

conda install -c conda-forge pysimplegui

### Playsound
https://pypi.org/project/playsound/

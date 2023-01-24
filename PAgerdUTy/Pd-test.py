import requests
import datetime
import json
# Update to match your API key
API_KEY = 'u+U6ykzZBZAo67gQuA-g'
startdate = datetime.date(2022,12,20)
# Update to match your chosen parameters
TIME_ZONE = 'Europe/Zurich'
INCLUDE = []
USER_IDS = ["PVHA0U2"]
ESCALATION_POLICY_IDS = []
SCHEDULE_IDS = []
SINCE = startdate
UNTIL = ''
EARLIEST = False


def list_oncalls():
    url = 'https://api.pagerduty.com/oncalls'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'time_zone': '',
        'include[]': INCLUDE,
        'user_ids[]': USER_IDS,
        'escalation_policy_ids[]': ESCALATION_POLICY_IDS,
        'schedule_ids[]': SCHEDULE_IDS,
        'since': SINCE,
        'until': UNTIL,
        'earliest': EARLIEST
    }
    r = requests.get(url, headers=headers, params=payload)
    print('Status Code: {code}'.format(code=r.status_code))
    dqte = datetime.datetime.strptime(r.json()["oncalls"][0]["start"], '%Y-%m-%dT%H:%M:%S+%f:%Z')
    print(dqte.day)#.astimezone(ZoneInfo('America/New_York')).strftime('%I:%M %p')
    #print(r.json()["oncalls"][0]["start"])

if __name__ == '__main__':
    list_oncalls()
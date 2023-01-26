import requests
import datetime
import json
import holidays
# Update to match your API key
API_KEY = 'u+U6ykzZBZAo67gQuA-g'
startdate = datetime.date(2022,12,1)
# Update to match your chosen parameters
TIME_ZONE = 'Europe/Zurich'
INCLUDE = []
USER_IDS = ["PVHA0U2"]
ESCALATION_POLICY_IDS = ["POKA16W"]
SCHEDULE_IDS = []
SINCE = startdate
UNTIL = ''
EARLIEST = False


CHVD_holidays = holidays.country_holidays('CH', subdiv='VD')
CHBE_holidays = holidays.country_holidays('CH', subdiv='BE')

CHZH_holidays = holidays.country_holidays('CH', subdiv='ZH')

RS_holidays = holidays.country_holidays('RS')
CH_holidays = holidays.country_holidays('CH')

pas = 1
dayProportion = pas/24

def defineDayType(startDate, endDate):
    weekDay = 0
    weekEndDay = 0
    publicHoliDay = 0
    while (startDate + datetime.timedelta(hours=pas) <= endDate ):
        if (startDate in CHVD_holidays) :
            publicHoliDay += dayProportion
        elif(startDate.weekday() == 5 or startDate.weekday() == 6 ) :
            weekEndDay += dayProportion
        else:
            weekDay += dayProportion
        startDate = startDate + datetime.timedelta(hours=pas)
    return round(weekDay * 2) / 2,round(weekEndDay * 2) / 2,round(publicHoliDay * 2) / 2

def list_oncalls():
    url = 'https://api.pagerduty.com/oncalls'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'time_zone': 'Europe/Zurich',
        'include[]': INCLUDE,
        'user_ids[]': USER_IDS,
        'escalation_policy_ids[]': ESCALATION_POLICY_IDS,
        'schedule_ids[]': SCHEDULE_IDS,
        'since': SINCE,
        'until': UNTIL,
        'earliest': EARLIEST
    }
    r = requests.get(url, headers=headers, params=payload)
    print('Status Code: {code}'.format(code=r.status_code) )

    # file = open("PAgerdUTy/lbl.json")
    # f = json.load(file)
    print(r.json())
    for el in r.json()["oncalls"] :
        dateD = datetime.datetime.fromisoformat(el["start"] )
        dateF = datetime.datetime.fromisoformat(el["end"] )

        if (dateF.month != dateD.month):
            newstartdate = datetime.date(dateF.year,dateF.month,1)
            newstartdate = datetime.time(0,0,0)

            defineDayType(dateD,newstartdate)
            #TODO INSERT SQL
            dateD = newstartdate

        defineDayType(dateD,dateF)
        #TODO INSERT SQL
        # print(defineDayType(dateD,dateF))

        # dateDif = dateF-dateD
        # #dqte = datetime.datetime.strptime(f["oncalls"][0]["start"], '%Y-%m-%dT%H:%M:%S%Z')#r.json()
        # print(dateD)#.astimezone(ZoneInfo('America/New_York')).strftime('%I:%M %p')
        # print(dateF)#.astimezone(ZoneInfo('America/New_York')).strftime('%I:%M %p')

if __name__ == '__main__':
    list_oncalls()
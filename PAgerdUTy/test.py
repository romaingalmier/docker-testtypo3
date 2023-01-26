import requests
import datetime
import json
import holidays
# Update to match your API key



startdate = datetime.date(2022,12,25)
enddate = datetime.date(2023,1,1)


if (enddate.month != startdate.month):
    newstartdate = datetime.date(enddate.year,enddate.month,1)
    newstartdate = datetime.time(0,0,0)

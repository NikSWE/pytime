from requests import get
from bs4 import BeautifulSoup
import json
import os

response = get("https://timezonedb.com/time-zones")
soup = BeautifulSoup(response.text, "lxml")

list_of_timezones = []

table_body = soup.body.tbody

for index, table_row in enumerate(table_body.find_all("tr")):

    table_data = list(filter(lambda x: x != '\n', table_row.contents))

    list_of_timezones.append({
        "index": index + 1,
        "country_code": table_data[0].string,
        "country_name": table_data[1].string,
        "page_link": table_data[2].a.get("href"),
        "time_zone": table_data[2].a.string,
        "gmt_offset": table_data[3].string,
        "abbreviation": None
    })

for index, timezone in enumerate(list_of_timezones):
    print("[" + str(index + 1) + "] Scrapping...")
    page_response = get("https://timezonedb.com{}".format(
        timezone["page_link"]))

    page_soup = BeautifulSoup(page_response.text, "lxml")

    timezone["abbreviation"] = page_soup.find_all("td",
                                                  attrs={"width":
                                                         "60%"})[0].string

print("Generating the json file..")

json_file = open("{}/data.json".format(os.getcwd()), "w")

json_file.write(json.dumps(list_of_timezones))

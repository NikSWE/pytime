import json
import os

data = json.loads(open("{}/data.json".format(os.getcwd())).read())
readme = open("README.md", "a")

for timezone in data:
    row = "| {} | {} | {} | [{}]({}) | {} | {} |\n".format(
        timezone["index"], timezone["country_code"], timezone["country_name"],
        timezone["time_zone"],
        "https://timezonedb.com{}".format(timezone["page_link"]),
        timezone["abbreviation"], timezone["gmt_offset"])
    readme.write(row)

readme.close()
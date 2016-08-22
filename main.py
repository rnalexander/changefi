### Author: RNAlexander
### Description: Allows you to set wifi name and password, defaults to emfcamp-insecure
### License: MIT

import os
import json
import pyb
import dialogs
import buttons
import ugfx


ugfx.init()
buttons.init()
ssid = dialogs.prompt_text("Enter ssid", init_text="emfcamp-insecure", width = 310, height = 220)
pw = dialogs.prompt_text("Enter pw (blank if none)", width = 310, height = 220)
if ssid:
    with open("wifi.json", "wt") as file:
        if pw:
            file.write(json.dumps({"ssid": ssid, "pw": pw}))
        else:
            file.write(json.dumps({"ssid": ssid}))     
    os.sync()

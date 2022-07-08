from twitch_test import TestDrive

browsers = TestDrive.Twitch(mobile_emulator={"deviceName": "iPhone XR"})

browsers.go_landing_page()
browsers.click_search_button()
browsers.search_for(keyword="Monster Hunter World")
browsers.switch_to_tab_channels()
browsers.find_user("CervelloneRe")
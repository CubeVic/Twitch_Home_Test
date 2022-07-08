from twitch_test import TestDrive
mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}
# mobile_emulator={"deviceName": "iPhone XR"}
browser = TestDrive.Twitch(mobile_emulator=mobile_emulation)

browser.go_landing_page()
browser.click_search_button()
browser.search_for(keyword="Monster Hunter World")
browser.switch_to_tab_channels()

browser.find_user("CervelloneRe")
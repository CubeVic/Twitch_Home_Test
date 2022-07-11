# Twitch Home Test

## Description 

Contains three files:

> By default, it uses the mobile emulator of a iPhone XR

* `page_object`: A file that contain the locations and allow an easy call from the other files, it allows re-usage of the same code with minimal changes.
* `utils`: contains extra functions that help with specific task, and they are not necessarily related with the test case.
* `TestDrive`: The test case with a syntax easy to read.

## How to run 
It requires the follow libraries.

* selenium>=4.3.0
* webdriver-manager>=3.8.0

## Test Case Description
1. Go to https://www.twitch.tv
2. Click in Search button.
3. Search for "Monster Hunter World".
4. Switch to Channels tab.
5. Scroll down 3 times. 
6. Search for "CervelloneRe" if no find choose random channel.
7. Close lightweight modal message.
8. If present click in start watching (Content Warning).
9. Wait for 5 seconds.
10. Take snapshot.

## ScreenCast
![ScreenCast](images/screencast.gif)


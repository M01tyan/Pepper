#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
#tablet = ALProxy("ALTabletService", "", 9559)

def viewTable():
    try:
        tabletService = session.service("ALTabletService")

        # Display the index.html page of a behavior name j-tablet-browser
        # The index.html must be in a folder html in the behavior folder
        tabletService.loadApplication("Pepper_1")
        tabletService.showWebview()

        time.sleep(3)

        # Hide the web view
        tabletService.hideWebview()
    except Exception, e:
        print "Error was: ", e

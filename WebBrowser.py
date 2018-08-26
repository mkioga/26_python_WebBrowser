
# ===============
# WebBrowser.py
# ===============

# WebBrowser is one of the simplest modules in the python library
# It helps you launch one of your installed web browsers and navigate to a URL

# we first import webbrowser library

import webbrowser

webbrowser.open("https://www.python.org/")   # will open default browser and take you to website specified

print("="*40)

help(webbrowser)   # Gives you help information about webbrowser

# you can also look at documentation in python website

print("="*40)


# Arguments in modules

# Modules and functions can take various arguments.
# If the argument starts with \ e.g. \n, then it can be modified
# while typing print, it will show you possible arguments.
# These are "values", "end", separator "sep", newline etc


for i in range(2):
    print(1,2,3,4,5)  # This uses default separator, which is space
    print(1,2,3,4,5, sep='=')  # We define a separator of =
    print(1,2,3,4,5, end=' ')  # Ends with space instead of default newline
    print()
    print("="*10)

print("="*40)


# WebBrowser arguments

# Best way to get arguments and other xstics of a module is on python website.
# https://docs.python.org/2/library/webbrowser.html

import webbrowser

webbrowser.open("https://www.python.org", new=1)  # new=1 opens browser in new tab if possible



# say we want to specify a browser to open with

# A lot of these commands do not work

# Not working

# chrome = webbrowser.get(using='google-chrome')
# chrome.open_new("https://www.python.org")

# Not working

# chrome = webbrowser.get(using='chrome')
# chrome.open_new("https://www.python.org")


# All these have no error but they do not open anything

# chrome = webbrowser.get('chrome %s').open("https://www.python.org")

# chrome = webbrowser.get('google-chrome %s').open("https://www.python.org")

# chrome = webbrowser.get('google-chrome %s').open_new("https://www.python.org")

# chrome = webbrowser.get('google-chrome %s').open_new_tab("https://www.python.org")

# chrome = webbrowser.get('chrome %s').open_new_tab("https://www.python.org")


# The code when using safari worked for the trainer
# Does not work for me because I don't have safari

# safari = webbrowser.get(using='safari')
# safari.open("https://www.python.org")


# This one using windows-default worked, but for some reason, it opened chrome
# I think because my PC is a windows PC with default browser chrome

explorer = webbrowser.get(using='windows-default')
explorer.open("https://www.python.org")






# Schoology Grade Updater

This is a webscraping project with Python that will (hopefully) be calibrated to pull up your Schoology grade report at a certain time every day. This script is powered using Python Selenium. The automation can be run headless in Chromedriver, but it will navigate through the pages of an RRISD based login system. This means that it will go through classlink and automate the button-pressing to navigate eventually to the grades page in Schoology. 

This project is a test for me to work with Python Selenium. **Still a work in progress right now**. I have not tested it much, the ending is not complete, and is very clunky as of now in terms of running development. 

## Dependencies

There are a few things you will need - open up your command prompt and type in the following commands:
```
pip install selenium
```
You will also need to have a functional chromedriver. Watch this video - https://www.youtube.com/watch?v=WnWQgUerR0c. You will need to add chromedriver to your PATH, and then modify the variable in the script before running this. 


## Changes

There are also a few changes you must make to the script - 
1. Firstly ensure that you have changed your PATH variable at the top of the script to match wherever you put chromedriver
2. Change your USERNAME and PASSWORD field to ensure that it logs into the correct account

These are all the changes you need to make as of now. Having everying else set up with these variables modified will allow the program to run correctly. 

## Disclaimers

This program is not complete. Mereley experimental testing with Python Selenium to see its capabilites. Did a little limits testing, and may return to this in the future to create and deliver a more usable version. 

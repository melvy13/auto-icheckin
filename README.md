# auto-icheckin
 Automatic iCheckin to reduce the hassle of logging into the website to take attendance.  Made with Python Selenium.

## How to Use

 1. Declare USERNAME, PASSWORD & DRIVERPATH variables in a local .env file with own login details & [chromedriver.exe](https://sites.google.com/chromium.org/driver/downloads?authuser=0) file path:

        # SAMPLE .env file
    
        USERNAME=12345678
        PASSWORD=password
        DRIVERPATH=C:/Users/user/Downloads/chromedriver.exe
      
 2. Run the file in terminal with the command:
 ```python izoneLogin.py #####``` (Replace ##### with the 5-digit iCheckIn code)

 3. After running the command, wait for the program to do its thing. It should take about 6 seconds.


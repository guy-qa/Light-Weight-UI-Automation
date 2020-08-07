Requirements:
    This project requires the following packages to run
    1. Python
    2. Behave
    3. Selenium

Folder Structure:
    1. features
            1. This folder will contain all the project files
            2. "survey_tests.feature" file contains all the BDD test cases
            3. "environment.py" file is responsible for setting up the webdriver instances before every scenario and closing them after every test run
        1.1. business_logic
            1. This folder contains all the methods that are actually performing the interactions with the application
        1.2. config
            1. The "setting.json" file contains the browser type and application URL
            2. "Config.py" file will read the data from the "settings.json" and will create a settings object
        1.3. steps
            1. This folder contains the implementation of the BDD steps written in the feature file
        1.4. webdrivers
            1. This folder contains the "webdriver.exe" files that are used to launch browser
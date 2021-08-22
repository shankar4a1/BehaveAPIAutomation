Steps:

Install Behave 
Install Professional Edition of PyCharm for BDD Plugins Support
intall allure behave 
Download ans set allure coommn line tools -https://github.com/allure-framework/allure2/releases

Genearting report :

$ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% 

allure serve %allure_result_folder%

Examples :

behave --no-capture --tags=library -f allure_behave.formatter:AllureFormatter -o AllureReports

allure serve C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation\AllureReports

Features :

1. Implemented with Behave 
2. Requests package 
3. Integrated with Allure report




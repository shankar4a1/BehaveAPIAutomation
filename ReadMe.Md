**Steps:**

Install Behave

Install Professional Edition of PyCharm for BDD Plugins Support

intall allure behave 

Download ans set allure coommn line tools -https://github.com/allure-framework/allure2/releases

set path example : C:\Users\ShankarFiles\Automation\Libraries\allure-2.14.0\bin

**Genearting report :**

$ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% 

allure serve %allure_result_folder%

Examples :

behave --no-capture --tags=library -f allure_behave.formatter:AllureFormatter -o AllureReports

allure serve C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation\AllureReports

**Features** :

1. Implemented with Behave 
2. Requests package 
3. Integrated with Allure report

**Future implementations:**
Poetry implementation 
Soft assertions
Integration with CSV/Excel
Logging customized messages
Request payload : csv/excel dynamically with positive negative combinations
Response validations : filed by filed or json to json
Schema validation :  filed by filed or json to json



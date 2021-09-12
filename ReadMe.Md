**Python 3 strongly recommends virtual environment.**

To create a python virtual env using venv (we can also use pyenv/virtual env/virtual env wrapper/pipenv)

#1 : To create requirements file by pulling the packages installed in the environment  whh can be used to install packages in the newly created virtual environment. 

pip freeze > requirements.txt

Example :
C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation>pip freeze > requirements.txt

#2 : Create a virtual environment using venv

python -m venv virtual_env 

Example :
C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation>python -m venv virtual_env

#3 Activate virtual environment

C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation>virtual_env\Scripts\activate

#4 Verify the packages installed in  newly created virtual environment  

pip list

Example :

(virtual_env) C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation>pip list

(virtual_env) C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation>pip list
Package    Version
---------- -------
pip        21.1.3
setuptools 56.0.0


#5 To install packages in virtual environment from requirements.txt

pip install -r requirements.txt

Example :

(virtual_env) C:\Users\ShankarFiles\Automation\Python\BehaveAPIAutomation>pip install -r requirements.txt

#6 Verify the packages installed in  newly created virtual environment  

pip list



Download and set allure coommn line tools -https://github.com/allure-framework/allure2/releases

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
1. Poetry implementation 
2. Soft assertions 
3. Integration with CSV/Excel
4. Logging customized messages
5. Request payload : csv/excel dynamically with positive negative combinations
6. Response validations : filed by filed or json to json
7. Schema validation :  filed by filed or json to json

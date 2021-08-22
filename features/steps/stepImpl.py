import json

import allure
import requests
from behave import *

from payLoad import *
from utilities.configurations import *
from utilities.resources import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    #
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("shank9", "4373")
    json_object = json.dumps(context.payLoad, indent=4)

    allure.attach(context.url, attachment_type=allure.attachment_type.TEXT)
    allure.attach(json_object, name='appURL', attachment_type=allure.attachment_type.JSON)
    allure.attach(context.payLoad, name='appURL1', attachment_type=allure.attachment_type.JSON)


# allure.attach(context.payLoad, name='payload2', attachment_type=allure.attachment_type.TEXT)
# allure.attach(json_object, name='payload3', attachment_type=allure.attachment_type.JSON)


# allure.attach(context.payLoad, name='payload', attachment_type=allure.attachment_type.__dict__)

# allure.description("ShankarTest")
# context.attach("text", context.payLoad)
# context.payLoad = addBookPayload(id_generator(), "4373");


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle);


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('rahulshettyacademy', getPassword())


@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then(u'status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

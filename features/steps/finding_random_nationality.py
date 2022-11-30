from behave import given, when, then
import requests
import re
from jsonpath_ng import jsonpath, parse

from hamcrest import assert_that, contains_string, equal_to


@given('a nationality {nat}')
def given_a_nationality(context, nat):
    context.nat = nat


@when('I call randomme API')
def when_call_API(context):
    response = requests.get('https://randomuser.me/api', {'nat': context.nat})
    context.response = response


@then('the response status code should be {status_code}')
def status_code_is(context, status_code):
    assert_that(context.response.status_code, equal_to(int(status_code)))


@then('the emails has an arrow')
def arrow_on_email(context):
    json_response = context.response.json()
    email_expression = parse('$.results[0].email')
    emails = email_expression.find(json_response)
    assert_that(emails[0].value, contains_string('@'))


@then('the email address should be valid')
def check_valid_email(context):
    email = 'qperez@gmail.com'
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return True

    else:
        return False


@then('the response header {header_name} should be {header_value}')
def status_code_is(context, header_name, header_value):
    value = context.response.headers.get(header_name)
    assert_that(value, contains_string(header_value))

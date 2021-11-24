from behave import *
from SatNav import *


@given(u'that a user is on the search page')
def step_impl(context):
    context.search_page = SearchPage()


@when(u'the user types a valid post code')
def step_impl(context):
    context.search_page.enter_post_code()


@when(u'the user clicks search')
def step_impl(context):
    context.search_page.click_search()


@then(u'a list of addresses within that post code should be displayed')
def step_impl(context):
    context.search_page.display_address()


# Navigating to an address
@given(u'that a user has selected an address')
def step_impl(context):
    context.search_page = SearchPage()
    context.search_page.select_address()


@when(u'the user selects Navigate')
def step_impl(context):
    context.search_page.navigate()


@then(u'the SatNav should display a route to the address')
def step_impl(context):
    context.search_page.display_route_map()

# Pull up a list of addresses visited.


@given(u'that a user is on the home page')
def step_impl(context):
    context.home_page = HomePage()


@when(u'the user selects History')
def step_impl(context):
    context.home_page.history()


@then(u'a list of last 10 addresses visited should be displayed')
def step_impl(context):
    context.home_page.show_history()

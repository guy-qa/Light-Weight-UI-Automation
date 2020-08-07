from behave import *
from features.business_logic.yuno_surveys_ui_logic import YunoSurveysUI

"""
    Author: Muhammad Umair
    Date: 12/6/2019
    Description:
    This file contains all implementation methods for the BDD commands written in the "survey_tests.feature"
"""

obj_survey = YunoSurveysUI()

@given(u'I open the test survey link')
def step_impl_open_survey_link(context):
    obj_survey.go_to_survey("https://surveyinterface-v2.opinionsample.com/#/surveys/ab320070-bbad-0134-bb62-0a6b3886cf3d/screens/page_1?publisher_user_id=07b59010-86d2-0131-c9a9-0a424708edaa&panel_user_id=PANEL_USER_TEST_22fd1640-d94b-0137-0d5b-029188bc54b8&panel_user_id_kind=PANEL_USER_KIND_TEST&pparam_offer_click_id=OFFER_CLICK_TEST_22fd1640-d94b-0137-0d5b-029188bc54b8&pparam_provider_user_id=%5Bprovider_user_uuid%5D&is_test&survey_id=ab320070-bbad-0134-bb62-0a6b3886cf3d&screen_id=page_1")

@given(u'I agree with the survey rewards statement')
def step_impl_undertaking(context):
    obj_survey.undertaking()

@when(u'I answer the question "{question}"')
def step_impl_answer_survey_question(context, question):
    obj_survey.get_answer(question)

@when(u'I select the option "{option}"')
def step_impl_select_option(context, option):
    obj_survey.select_option(option)

@when(u'I set the answer to "{ans}"')
def step_impl_set_ans(context, ans):
    obj_survey.write_answer(ans)

@then(u'I should be on the survey done page')
def step_impl_survey_done(context):
    survey_end = obj_survey.verify_survey_ended()
    assert survey_end == "All done!"


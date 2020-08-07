@dalia @survey
Feature: survey acceptance test
    As a QE
    I want to run an automated acceptance test
    So as to verify opening of survey and the flow of answering questions

Background: Open the test survey link
    Given I open the test survey link
    And I agree with the survey rewards statement

    @priority_high @ui @automated
    Scenario: Verify survey with pre defined answers
      When I answer the question "How many hours per day do you spend on reading the news?"
      And I answer the question "Which of these social media platforms do you use at least once a week?"
      And I answer the question "Which of the following media do you use at least once a week?"
      And I answer the question "If given the chance to learn all the secrets of one PROMINENT PERSON, whose secrets would you like to know?"
      And I answer the question "Do you agree or disagree: In general, I trust the information I get from the media."
      And I answer the question "What is five plus two?"
      And I answer the question "Do you live in a city or in a rural area?"
      And I answer the question "Which is your favourite from these award-winning films?"
      And I answer the question "What do you like most about Gandhi?"
      Then I should be on the survey done page

    @priority_high @ui @automated
    Scenario: Verify survey with user defined answers
      When I select the option "1-3 hours"
      And I select the option "Facebook"
      And I select the option "Instagram"
      And I select the option "Youtube"
      And I select the option "Television"
      When I set the answer to "JohnDoe"
      And I select the option "Somewhat agree"
      And I set the answer to "7"
      And I select the option "City"
      And I select the option "Gandhi"
      And I select the option "Editing"
      Then I should be on the survey done page


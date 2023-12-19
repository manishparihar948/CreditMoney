Feature: Credmudra Personal Loan Contact Verification

    Background:
        Given I launch chrome browser

    @negativeCase
    Scenario: Presence of Credmudra Home page with invalid contact number
        Given I launch chrome browser
        When  I open the Credmudra homepage
        And   Verify the Personal loan feature button
        And   Enter invalid contact number
        Then  Show error for invalid contact number

    @positiveCase
    Scenario: Presence of Credmudra Home page with valid contact number
        Given I launch chrome browser
        When  I open the Credmudra homepage
        And   Verify the Personal loan feature button
        And   Enter valid contact number
        And   Click to apply button
        Then  Show OTP Page





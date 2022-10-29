@webbrowser_required
Feature: Main page view

    Check what is displayed on the main page. What functionality I have

    Scenario: Main page title contains 'FilesList' string
    When I'm on the 'home' page
    Then Page title contains 'FilesList'

    # Scenario: Main page title contains Login button for non-logged user
    # Given I'm logged out
    # When I'm on the 'home' page
    # Then I see 'login' button

    # Scenario: Main page title contains Logout button for logged user
    # Given I'm logged in
    # When I'm on the 'home' page
    # Then I see 'logout' button
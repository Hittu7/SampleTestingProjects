Feature: User Login
Registered User should be able to login to access account details

Scenario: Login with Valid Credentials
Given User has opened the Application URL
And Navigated to the login Page
When User enters valid email address "*******************"
And Enters valid password "********************"
And Clicks on login button
Then User should be able to successfully login

Scenario: Login with Invalid credentials
Given User has opened Application URL
And Navigated to the login Page
When User enters invalid email address "****************"
And Enters invalid password "*************"
And User clicks on login button
Then User should not be able to successfully login
And Get a prompt of message

Scenario: Login with valid email address and invalid password
Given User has opened Application URL
And Navigated to the login Page
When User enters valid email address "****************"
And Enters invalid password "*************"
And User clicks on login button
Then User should not be able to successfully login
And Get a prompt of message

Scenario: Login with invalid email address and valid password
Given User has opened Application URL
And Navigated to the login Page
When User enters invalid email address "****************"
And Enters valid password "*************"
And User clicks on login button
Then User should not be able to successfully login
And Get a prompt of message


Scenario: Login with without entering credentials
Given User has opened Application URL
And Navigated to the login Page
When User do not enter valid email address 
And User do not enters password 
And User clicks on login button
Then User should enter the credentials


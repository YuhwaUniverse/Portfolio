
Feature: Sign up for Starbucks homepage
         As a user, i want to sign up for the Starbucks homepage (https://www.starbucks.com/)  
         so that i can access its services 

     Scenario Outline: Successful sign up with valid credentials    
         Given I am on the Starbucks homepage
         When I click on the "Join now" button
         And I enter First name in the first name field
         And I enter Last name in the last name field
         And I enter "<valid_email>" in the email field
         And I enter "<valid_password>" in the password field
         And I click on the check box to agree to recieve email from Starbucks  
         And I click on the check box to agree to the Terms of Use
         And I click on the "Create Account" button
         Then I should be directed to the menu page displying various products icons with a successful Sign Up

         # Assertion step to check that all email requirements are satisfied
         And all email conditions should be satisfied
         | condition                                        | satisfied |
         | contains one @ symbol                            | Y         |
         | contains one domain                              | Y         |
         | contains at least one dot (.) in a domain        | Y         |
              
         # Assertion step to check that all password requirements are satisfied
         And all password conditions should be satisfied

         | condition                      | satisfied |
         | at least 8 characters          | Y         |
         | at most 25 characters          | Y         |
         | at least one number            | Y         |
         | at least one capital letter    | Y         |
         | at least one lowercase letter  | Y         |
         | at least one special character | Y         |  

         Examples:
         | valid_email                         | valid_password |       
         | testuser123@gmail.com               | TestUser123#   | 
         | testuser456@yahoo.com               | Testuser45^!   |
         | testuser789@icloud.com              | Test@User78*   |
         | testuser.789@icloud.com             | $TestUser7*#   |
         | testuser789@sub.domain.com          | TESTUSEr**#    |
         | test_user789@sub.domain.com         | 8testUser**#   |
         | test_user789@gmail.com.domain.com   | 8testUser**#   |
     

     Scenario Outline: Sign up with an invalid email address   
         Given I am on the Starbucks home page
         When I click on the "Join now" button
         And I enter First name in the first name field
         And I enter Last name in the last name field
         And I enter "<invalid_email>" as my email address
         Then I should see the "<error_message>" under the email field
          
         Examples:
         | invalid_email                   | error_message                        |
         |                                 | Please enter a valid email address.  |                          
         | testuser123gmail.com            | Please enter a valid email address.  |                         
         | testuser123                     | Please enter a valid email address.  |                         
         | testuser123@                    | Please enter a valid email address.  |
         | @gmail.com                      | Please enter a valid email address.  |                                 
         | testuser123@examplecom          | Please enter a valid email address.  |
         | testuser123@gmail..com          | Please enter a valid email address.  |                         
         | testuser123@.com                | Please enter a valid email address.  |                        
         | testuser123@exa!*mple.com       | Please enter a valid email address.  |                         
         | testuser123@gmail.com.          | Please enter a valid email address.  |                        
               
      
     Scenario Outline: Sign up with an invalid password
         Given I am on the Starbucks home page
         When I click on the "Join now" button
         And I enter First name in the first name field
         And I enter Last name in the last name field
         And I enter "<valid_email>" in the email address field
         And I enter "<invalid_password>" in the password field 
         Then I should see the "<checklist>" of requirements to create a valid password under the password field
      
         | condition                       | status  |
         | at least 8 characters           | <char8> |
         | at most 25 characters           | <char25>|
         | at least one number             | <num>   |
         | at least one capital letter     | <cap>   |
         | at least one lowercase letter   | <low>   |
         | at least one special character  | <spec>  |
   
         # Assertion step to check that all password requirements are not satisfied
         And the test should pass only at least one of the password conditions is not met

         # Assertion step to check that a checklist is displayed under the password field only if the test passes
         And the test should pass only if the "<checklist>" is met 

         Examples:
         | email                 | invalid_password    | char8 | char25 | num | cap | low | spec | checklist |
         | testuser123@gmail.com | ABCde               | N     | Y      | N   | Y   | Y   | N    |    Y      |
         | testuser123@gmail.com | 123$&*A!@#          | Y     | Y      | Y   | N   | N   | Y    |    Y      |
         | testuser123@gmail.com | Abc12345            | Y     | Y      | Y   | Y   | Y   | N    |    Y      |
         | testuser123@gmail.com | abcdefghijklmnopq   | Y     | N      | Y   | N   | Y   | N    |    Y      |
         | testuser123@gmail.com | abcdefgh            | Y     | Y      | N   | N   | Y   | N    |    Y      |
         | testuser123@gmail.com | 12345678            | Y     | Y      | Y   | N   | N   | N    |    Y      |
         | testuser123@gmail.com | Abcdefgh            | Y     | Y      | N   | Y   | Y   | N    |    Y      |
         | testuser123@gmail.com |                     | N     | Y      | N   | N   | N   | N    |    Y      |


     Scenario Outline: Sign up with an existing email address
         Given I am on the Starbucks home page
         When I click on the "Join now" button
         And I enter First name in the name field
         And I enter Last name in the name field
         And I enter "<valid_email>" in the email field
         And I enter "<valid_password>" in the password field
         And I click on the check box to agree to recieve email from Starbucks  
         And I click on the check box to agree to the Terms of Use
         And I click on the "Create Account" button
         Then I should see the "<error_message>" under the email field 
       
         Examples:
         | email                     | password           | error_message                   |
         | testuser123@gmail.com     | Testuser123#       | Email address is not available. | 
               
  
     Scenario Outline: Sign up with invalid first name 
         Given I am on the Starbucks homepage
         When I click on the "Join now" button
         And I enter unvalid "<first_name>" in the first name field
         And I enter valid Last name in the last name field
         And I enter valid email in the email field
         And I enter valid password in the password field
         And I click on the check box to agree to recieve email from Starbucks  
         And I click on the check box to agree to the Terms of Use
         And I click on the "Create Account" button
         Then I should see the "<error_message>" under the first name field 

         | condition                                | error_message
         | no numbers                               | First/Last name cannot have special characters or numerals |
         | no special characters                    | First/Last name cannot have special characters or numerals |
         | no other characters that are not english | First/Last name cannot have special characters or numerals |

         Examples:
         | first_name     | error message                                                    |        
         | 123            | First/Last name cannot have special characters or numerals       |  
         | $%^            | First/Last name cannot have special characters or numerals       | 
         | 234$%^         | First/Last name cannot have special characters or numerals       | 
         | Teo123         | First/Last name cannot have special characters or numerals       | 
         | Teo$%^         | First/Last name cannot have special characters or numerals       | 
         | はい           | First/Last name cannot have special characters or numerals       | 
         | 이름           | First/Last name cannot have special characters or numerals       | 
         | 이름 name      | First/Last name cannot have special characters or numerals       | 


     Scenario Outline: Sign up with invalid last name 
         Given I am on the Starbucks homepage
         When I click on the "Join now" button
         And I enter First name in the first name field
         And I enter "<last_name>" in the last name field
         And I enter valid "email" in the email field
         And I enter valid "password" in the password field
         And I click on the check box to agree to recieve email from Starbucks  
         And I click on the check box to agree to the Terms of Use
         And I click on the "Create Account" button
         Then I should see the "<error_message>" under the last name field 
         
         | condition                                | error_message
         | no numbers                               | First/Last name cannot have special characters or numerals |
         | no special characters                    | First/Last name cannot have special characters or numerals |
         | no other characters that are not english | First/Last name cannot have special characters or numerals |

        Examples:
         | last_name      | error_message                                                  |        
         | 123            | First/Last name cannot have special characters or numerals     |  
         | $%^            | First/Last name cannot have special characters or numerals     | 
         | 234$%^         | First/Last name cannot have special characters or numerals     | 
         | name123        | First/Last name cannot have special characters or numerals     | 
         | Name$%^        | First/Last name cannot have special characters or numerals     | 
         | 성             | First/Last name cannot have special characters or numerals     |
         | 성 name        | First/Last name cannot have special characters or numerals     |
         

     Scenario Outline: Sign up with empty first name 
         Given I am on the Starbucks homepage
         When I click on the "Join now" button
         And I leave the "<first_name>" field empty
         Then I should see the "<error_message>" indicating that the first name field should be filled

        Examples:
        | first_name   | error_message             |        
        |              | Enter your first name     |  


     Scenario Outline: Sign up with empty last name 
        Given I am on the Starbucks homepage
         When I click on the "Join now" button
         And I enter valid First name in the name field
         And I leave the "<last_name>" field empty
         Then I should see the "<error_message>" indicating that the last name field should be filled

        Examples:
        | last_name    | error_message             |        
        |              | Enter your last name      |  


     Scenario Outline: Sign up without giving consent to the Terms of Use   
         Given I am on the Starbucks home page
         When I click on the "Join now" button
         And I enter valid First name in the name field
         And I enter valid Last name in the name field
         And I enter valid "<email>" in the email field
         And I enter valid "<password>" in the password field
         And I click on the check box to agree to recieve email from Starbucks  
         And I skip to click on the check box to agree to the Terms of Use
         And I click on the "Create Account" button
         Then I should see the "<error_message>" asking for consent to the Terms of Use under the button 

         Examples:
         | email                     | password           | error_message                    |
         | testuser123@gmail.com     | Testuser123#       | Please agree to the Terms of Use | 

     
     Scenario Outline: Sign up without giving consent to recieve emails from Starbucks  
         Given I am on the Starbucks homepage
         When I click on the "Join now" button
         And I enter First name in the name field
         And I enter Last name in the name field
         And I enter valid "<email>" in the email field
         And I enter valid "<password>" in the password field
         And I click on the check box to agree to recieve email from Starbucks  
         And I click on the check box to agree to the Terms of Use
         And I click on the "Create Account" button
         Then I should be directed to the Menu page displying various products icons with a successful Sign Up

         Examples:
         | email                    | password          |        
         | testuser123@gmail.com    | Testuser123#      |  


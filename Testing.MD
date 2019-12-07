# Testing

For this project I could use mixed testing that means. I test the project manually and runs the test automatically locally
and in the cloud as well as you can see below.

## Manual Testing:

For Manual testing me and some of my friend and acquaintances tested the web application.

- Testing devices:
    - Mobile:
        - Google Pixel 5
        - iPhone SE
    - Tablet:
        - iPad
    - PC and notebooks with HD resolution

### User stories

#### Accounts

- 

#### Feed

- 

#### Products

- 

#### Cart

- 

#### Checkout

- 

#### Blog

- 

#### Search

-

## Automated Testing;

### Locally

In the python console I run the "python manage.py test" command

- Coverage:
    - Install "pip install coverage"
    - Coverage check "coverage run --source='.' manage.py test"
    - Run Report with "coverage report"
    - "coverage html" -> Creates htmlcov report folder locally
    - ![Coverage screenshot]()

### Cloud

- Automated testing with Travis CI [link](https://travis-ci.org/)

I use Travis which is a CI (Continuous Integration) service used to test software in the cloud. After a commit the 
travis jobs runs to test on the pipeline. It will run when I do merge from DEv branch to QA branch. It helps to me to get
fast feedback about the tests. 

## Stripe details:

In order to test Stripe payment we can use the below given card details to test the payment.

- Card Numbers:
    - Numbers:
        - 4242 4242 4242 4242
    - Brand:
        - Visa
    - CVC:
        - Any 3 digits
    - Date:
        - Any future date
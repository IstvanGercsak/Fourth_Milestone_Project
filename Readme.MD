# Fourth Milestone Project 
[![Build Status](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop.svg?branch=QA_branch)](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop)

# Description

# Branches
- QA branch for testing and developing
- Master branch for working stable production environment

# Application hosts
- Application and Database
    - Heroku and PostgreSQL
- Data store
    - Amazon S3 Bucket [link](https://aws.amazon.com/s3/)


# Databases

- Upload database schema:
    - Change url in env.py and type the "migrate" and "makemigrations" command to upgrade db schema

- Local
    - sqlite3
- Remote DB for QA and PROD
    - PostgreSQL 

# Features

- With use of the admin user we can add new product
    - Picture
- The user can add product in the cart
- User can login
- User can make payment
    - Only after login
- User can give review
    - Only after login
- Store everything in AWS
    - Static folder
    - Pictures
- Branches
- Test and test Coverage
- Database sqlite for local and PostgreSQL on Heroku
- Travis CI running on DEV environment

# AWS
- Set up:
    - S3:
        - Create S3 Bucket to storing data (bucket-for-milestone-project)
        - Properties/Static website hosting
    - IAM:
        - Create a group about who can access our site
- I set up two buckets/policies/groups/user:
    - QA bucket (milestone-bucket-qa)
    - Master bucket (milestone-bucket-master)

- CORS Config:
<CORSConfiguration>
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>

- Bucket policy:
{
    "Version":"2012-10-17",
    "Statement":[{
      "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["/*"
      ]
    }
  ]
}

- After changes in the static files:
    - Run "collectstatic". It will upload the static files
    - If the QA is ok, we can run the "collectstatic" for the prod.

# Security
- Django authentication
- Secret keys and confidential data:
    - Locally:
        - env.py file
    - Online:
        - Storing as environmental variables (Travis CI and Heroku)

# Test
- Note that for historical reasons .travis.yml needs to be present on all active branches of your project.
- Automated testing with Travis CI [link](https://travis-ci.org/)
- run test locally:
    - python manage.py test
- Coverage:
    - Install "pip install coverage"
    - Coverage check "coverage run --source='.' manage.py test"
    - Run Report with "coverage report"
    - "coverage html" -> Creates htmlcov report folder 
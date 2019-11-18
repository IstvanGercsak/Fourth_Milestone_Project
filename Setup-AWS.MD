# Setup AWS

#### I.

- Set up:
    - S3:
        - Create S3 Bucket to storing data (bucket-for-milestone-project)
            - One for the QA_branch and one for the master branch
    - IAM:
        - Create policies/groups/user about who can access our site
            - QA bucket (milestone-bucket-qa)
            - Master bucket (milestone-bucket-master)

#### II.
I configured the CORS config and bucket policy as below:
- CORS Config:
```
<CORSConfiguration>
    <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

- Bucket policy:

```
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
```
#### III.
- Set details and secret keys in the setting.py file and in the environmental variables in order to upload and reach the aws buckets.

#### IV.
- After changes in the static files:
    - Run "collectstatic". It will upload the static files
    - If the QA is ok, we can run the "collectstatic" for the prod.
    - Configure Procfile: python manage.py collectstatic --noinput --noreload;
        - Collect static after every deploy
        - The server will run only once instead of twice
# Setup AWS

In order to store static web files and media files(custom css, js, images) I use AWS. 
With this it is easier to store these files online in separate container.

#### I. Steps to set up AWS account and container

- Set up:
    - S3:
        - Create 2 S3 Bucket to storing data (bucket-for-milestone-project)
            - milestone-bucket-master
                - S3 bucket for master branch
            - milestone-bucket-qa
                - S3 bucket for QA branch
    - IAM:
        - Create policies/groups/user about who can access our site
            - QA bucket (milestone-bucket-qa)
            - Master bucket (milestone-bucket-master)

#### II. Configure buckets
I configured the CORS config and bucket policy as below:
- CORS Config:
```xml
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

```json
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
#### III. Set up bucket in my environments
- Set details and secret keys in the setting.py file and in the environmental variables in order to upload and reach the aws buckets.

#### IV. Usage of the buckets
- After changes in the static files:
    - In general: Run "collectstatic" command. It will upload the static files:
    ````bash
    python manage.py colletcstatic
    ````
    - If the QA branch is finished, we can run the "collectstatic" for the prod.
    - Configure Procfile: "python manage.py collectstatic --noinput --noreload;"
        - Collect static after every deploy
        - The server will run only once instead of twice
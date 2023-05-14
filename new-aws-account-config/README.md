## Initial setup as root user
* Go to menu in the top-right section of the screen, click `Account`
  * Activate `IAM User and Role Access to Billing Information` -> `Activate IAM Access`
  * Set up `Alternate Contacts`
  * Turn off `Configure Security Challenge Questions`

* Go to menu in the top-right section of the screen, click `Security credentials`
  * `Multi-factor authentication (MFA)` -> `Assign MFA device`
    Add 2 at least 2 MFA devices.

* Go to menu in the top-right section of the screen, click `Billing Dashboard`
  * Go to `Billing preferences`. Set:
    - [x] `Receive PDF Invoice By Email`
    - [x] `Receive Free Tier Usage Alerts`
    - [x] `Receive Billing Alerts`
    - [ ] `Disable credit sharing`

* Enable [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html)

* Set up a budget.

* Add the following SCP to the root of the organisation.
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": "arn:aws:iam::*:root"
        }
      }
    }
  ]
}
```

* Enable AWS Compute Optimizer
```
aws compute-optimizer update-enrollment-status --status Active --include-member-accounts
```

* Create IAM admin user.

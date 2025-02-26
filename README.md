# AWS Resource Tagging Automation 🚀

This project automates the tagging of AWS resources (**EC2, EBS Volumes, Snapshots, and S3 Buckets**) to help with **cost optimization** and **billing analysis**.

## **🔹 Features**
✔ Automatically tags **EC2 instances** with:
   - `Owner: CloudOps`
   - `Environment: Production`
   - `CostCenter: Finance`
   
✔ Adds **StorageType** tags for:
   - **EBS Volumes**
   - **EBS Snapshots**
   
✔ Adds **Project & RetentionPolicy** tags for:
   - **S3 Buckets**

✔ Runs automatically **every 6 hours** using **EventBridge**.

---

## **🛠 Setup & Deployment**
### **1️⃣ Create IAM Role & Permissions**
1. Go to **AWS IAM Console** → Click **Roles** → **Create Role**.
2. Choose **AWS Lambda** as the trusted entity.
3. Attach the following permissions (JSON format in `iam_policy.json`).

### **2️⃣ Deploy Lambda Function**
1. Open **AWS Lambda Console** → Create a function.
2. Choose **Python 3.9+** runtime.
3. Upload the `lambda_function.py` file.
4. Assign the IAM role created earlier.
5. **Save & Deploy**.

### **3️⃣ Automate with EventBridge**
1. Open **AWS EventBridge Console** → Create **Rule**.
2. Set **Schedule: Every 6 hours**.
3. Choose **AWS Lambda** as target → Select the function.
4. **Create Rule**.

---

## **📜 IAM Policy (`iam_policy.json`)**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:CreateTags",
                "ec2:DescribeVolumes",
                "ec2:DescribeSnapshots",
                "s3:GetBucketTagging",
                "s3:PutBucketTagging"
            ],
            "Resource": "*"
        }
    ]
}

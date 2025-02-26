import boto3

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

# Define tags
TAGS = [
    {"Key": "Owner", "Value": "CloudOps"},
    {"Key": "Environment", "Value": "Production"},
    {"Key": "CostCenter", "Value": "Finance"},
    {"Key": "StorageType", "Value": "Optimized"},
    {"Key": "Project", "Value": "AWS Cost Optimization"},
    {"Key": "RetentionPolicy", "Value": "30Days"}
]

def tag_ec2_instances():
    instances = ec2.describe_instances()
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2.create_tags(Resources=[instance_id], Tags=TAGS[:3])  # Apply first 3 tags
            print(f"Tagged EC2 Instance: {instance_id}")

def tag_ebs_volumes():
    volumes = ec2.describe_volumes()
    
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        ec2.create_tags(Resources=[volume_id], Tags=[TAGS[3]])  # Apply StorageType tag
        print(f"Tagged EBS Volume: {volume_id}")

def tag_ebs_snapshots():
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])
    
    for snapshot in snapshots['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        ec2.create_tags(Resources=[snapshot_id], Tags=[TAGS[3]])  # Apply StorageType tag
        print(f"Tagged EBS Snapshot: {snapshot_id}")

def tag_s3_buckets():
    buckets = s3.list_buckets()
    
    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={'TagSet': TAGS[4:]}  # Apply last 2 tags
        )
        print(f"Tagged S3 Bucket: {bucket_name}")

def lambda_handler(event, context):
    tag_ec2_instances()
    tag_ebs_volumes()
    tag_ebs_snapshots()
    tag_s3_buckets()
    return {"message": "AWS resources tagged successfully!"}

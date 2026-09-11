def calculate_cost(
    ec2_hours,
    s3_storage,
    ebs_storage,
    data_transfer,
    ec2_instances
):
    # Sample pricing for our learning project
    EC2_RATE = 5.00
    S3_RATE = 0.50
    EBS_RATE = 1.00
    DATA_TRANSFER_RATE = 2.00

    ec2_cost = ec2_hours * EC2_RATE
    s3_cost = s3_storage * S3_RATE
    ebs_cost = ebs_storage * EBS_RATE
    data_transfer_cost = data_transfer * DATA_TRANSFER_RATE

    total_cost = (
        ec2_cost
        + s3_cost
        + ebs_cost
        + data_transfer_cost
    )

    return {
        "ec2": ec2_cost,
        "s3": s3_cost,
        "ebs": ebs_cost,
        "data_transfer": data_transfer_cost,
        "total": total_cost
    }
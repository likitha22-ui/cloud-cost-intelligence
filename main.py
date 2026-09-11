from src.cost_calculator import calculate_cost


print("========================================")
print("      CLOUD COST ANALYZER")
print("========================================")

print("\nEnter Cloud Usage Details")

ec2_hours = float(input("EC2 usage hours: "))
s3_storage = float(input("S3 storage in GB: "))
ebs_storage = float(input("EBS storage in GB: "))
data_transfer = float(input("Data transfer in GB: "))
ec2_instances = int(input("Number of EC2 instances: "))

cost = calculate_cost(
    ec2_hours,
    s3_storage,
    ebs_storage,
    data_transfer,
    ec2_instances
)

print("\n========================================")
print("             COST SUMMARY")
print("========================================")

print(f"EC2 Cost          : ₹{cost['ec2']:.2f}")
print(f"S3 Cost           : ₹{cost['s3']:.2f}")
print(f"EBS Cost          : ₹{cost['ebs']:.2f}")
print(f"Data Transfer     : ₹{cost['data_transfer']:.2f}")

print("----------------------------------------")

print(f"TOTAL COST        : ₹{cost['total']:.2f}")

print("========================================")
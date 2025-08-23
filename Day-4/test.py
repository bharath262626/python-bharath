import sys

type = sys.argv[1]

if type == "t2.micro":
    print("you can print ec2 instance")
elif type == "t2.medium":
    print("you can print ec2 instance 4 dollars per day")
elif type == "t2.xlarge":
    print("you can print ec2 instance 8 dollars per day")
else:
    print("t2.micro not available can't print")
        
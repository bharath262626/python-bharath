my_file = ["ec2", "ec2-1", "ec22", "ec2-3", "ec2-4"]

for vms in my_file:
    if vms == "ec22":
        break
    print(vms)
        

for vm2 in my_file:
    if vm2 == "ec22":
        continue
    print(vm2)
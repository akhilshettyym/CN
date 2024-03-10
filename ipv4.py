def classify_and_identify_ipv4(ip_address):
    octets = ip_address.split(".")
    
    if len(octets)!=4:
        return "Invalid ipv4 address"
        
    first_octet = int(octets[0])
    
    if 1<= first_octet <= 126:
        classification = "class A"
        network_id = octets[0]
        host_id = '.'.join(octets[1:])
        
    elif 127<= first_octet <= 191:
        classification = "class B"
        network_id = '.'.join(octets[:2])
        host_id = '.'.join(octets[2:])
    
    elif 192<= first_octet <= 223:
        classification = "class C"
        network_id = '.'.join(octets[:3])
        host_id = octets[3]
        
    elif 224<= first_octet <= 239:
        classification = "class D"
        network_id = "N/A"
        host_id = "N/A"
        
    elif 240<= first_octet <= 255:
        classification = "class E"
        network_id = "N/A"
        host_id = "N/A"
        
    else:
        return "Invaid ipv4 address"
        
    return f"classification: {classification} \n Network id :{network_id}\n  Host id: {host_id}"
    
user_input = input("Enter the IPV4 address :")
result = classify_and_identify_ipv4(user_input) 
print(f"The ipv4 address of {user_input} details are :\n{result}")
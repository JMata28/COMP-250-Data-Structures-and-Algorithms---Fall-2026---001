device = {
    "hostname": "lab-ws-07",
    "os": "Ubuntu 22.04",
    "open_ports": [22, 80, 443],
    "risk_score": 12
}

print(f"Host: {device["hostname"]} running {device["os"]}")
print(f"Fields stored: {len(device)}")
print(device.keys())

owner_name = input("Owner name: ")
device["owner"] = owner_name
print(f"Fields stored: {len(device)}")

new_port = int(input("Port to add: "))
device["open_ports"].append(new_port)
print(f"{device['open_ports']}")

number_of_ports = len(device["open_ports"])-3
device["risk_score"] += (number_of_ports*5)

#Complete the rest of the exercise on your own


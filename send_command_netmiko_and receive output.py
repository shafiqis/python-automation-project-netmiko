from netmiko import Netmiko
import os

csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.96.132',
    'username': 'admin',
    'password': 'strong_password'
}

try:
    net_connect = Netmiko(**csr)
    print("Connected successfully")

    # Use a file for commands
    config_file = 'config.txt'
    if os.path.exists(config_file):
        config = net_connect.send_config_from_file(config_file=config_file)
    else:
        # Fallback to direct command list
        commands = [
            'int lo1001',
            'ip address 11.1.1.10 255.255.255.0',
            'no shut'
        ]
        config = net_connect.send_config_set(commands)

    print(config)
    print(net_connect.send_command("show ip int brief"))
    net_connect.disconnect()
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

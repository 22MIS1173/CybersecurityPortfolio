import ipaddress

def main():
    num_required = int(input("Enter the number of devices or subnets required: "))
    starting_ip = input("Enter the starting IP address : ")

    x = bin(num_required)[2:]
    print(f"Binary representation of {num_required}: {x}")

    num_zero_bits = len(x)
    num_one_bits = 32 - num_zero_bits
    binary_mask = '1' * num_one_bits + '0' * num_zero_bits

    new_subnet_mask = '.'.join([binary_mask[i:i + 8] for i in range(0, 32, 8)])
    decimal_subnet_mask = '.'.join(str(int(binary_mask[i:i+8], 2)) for i in range(0, 32, 8))
    print(f"Subnet Mask: {decimal_subnet_mask}")

    cidr_notation = f"/{num_one_bits}"
    print(f"CIDR Notation: {cidr_notation}")

    flat_mask = new_subnet_mask.replace('.', '')
    last_one_index = flat_mask.rfind('1')
    position_in_octet = last_one_index % 8
    bit_weights = [128, 64, 32, 16, 8, 4, 2, 1]
    subnet_generator = bit_weights[position_in_octet]
    print(f"Subnet generator: {subnet_generator}")

    octets = new_subnet_mask.split('.')
    octet_position = 0
    for i in range(3, -1, -1):
        if '0' in octets[i]:
            octet_position = i + 1
            break
    print(f"Octet position: {octet_position}")

    print("\nAll Possible Network Ranges:")
    network = ipaddress.IPv4Network(f"{starting_ip}{cidr_notation}", strict=False)
    subnet_size = 2 ** num_zero_bits
    current_ip = int(network.network_address)

    num_subnets = 256 // subnet_generator
    for i in range(num_subnets):
        net_start = ipaddress.IPv4Address(current_ip)
        net_end = ipaddress.IPv4Address(current_ip + subnet_size - 1)
        print(f"{net_start} - {net_end}")
        current_ip += subnet_size

if __name__ == "__main__":
    main()

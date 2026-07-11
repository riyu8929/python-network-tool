import argparse
import ipaddress


def summarize_cidr(cidr: str) -> dict:
    network = ipaddress.ip_network(cidr, strict=False)
    host_count = network.num_addresses - 2
    usable_range = None
    if host_count > 0:
        usable_range = f"{network.network_address + 1} - {network.broadcast_address - 1}"
    else:
        usable_range = "No usable hosts"

    return {
        "cidr": str(network),
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "subnet_mask": str(network.netmask),
        "host_count": host_count,
        "usable_range": usable_range,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Show subnet information for CIDR notation")
    parser.add_argument("cidr", nargs="+", help="CIDR notation like 192.168.1.0/24")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    for cidr in args.cidr:
        try:
            info = summarize_cidr(cidr)
        except ValueError as exc:
            print(f"Invalid CIDR: {cidr} ({exc})")
            continue

        print(f"CIDR: {info['cidr']}")
        print(f"Network address: {info['network_address']}")
        print(f"Broadcast address: {info['broadcast_address']}")
        print(f"Subnet mask: {info['subnet_mask']}")
        print(f"Host count: {info['host_count']}")
        print(f"Usable range: {info['usable_range']}")
        print()


if __name__ == "__main__":
    main()

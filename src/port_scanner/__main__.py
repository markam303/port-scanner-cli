"""Port Scanner CLI."""

import argparse
import sys
import time

from port_scanner.scanner import (
    DEFAULT_END_PORT,
    DEFAULT_NUM_THREADS,
    DEFAULT_START_PORT,
    scan_ports,
)


def print_results(results: list) -> None:
    """Print scan results in table format."""
    print(f"{'Port':<10} {'Status':<10} {'Service':<20} {'Banner'}")
    print("-" * 70)
    for result in results:
        banner = result["banner"] if result["banner"] else ""
        print(f"{result['port']:<10} {result['status']:<10} {result['service']:<20} {banner}")


def main() -> int:
    """Main entry point for the port scanner."""
    parser = argparse.ArgumentParser(description="Professional TCP Port Scanner")
    parser.add_argument(
        "host",
        help="Target host to scan",
    )
    parser.add_argument(
        "-s",
        "--start-port",
        type=int,
        default=DEFAULT_START_PORT,
        help=f"Start port (default: {DEFAULT_START_PORT})",
    )
    parser.add_argument(
        "-e",
        "--end-port",
        type=int,
        default=DEFAULT_END_PORT,
        help=f"End port (default: {DEFAULT_END_PORT})",
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=DEFAULT_NUM_THREADS,
        help=f"Number of threads (default: {DEFAULT_NUM_THREADS})",
    )

    args = parser.parse_args()

    if args.start_port > args.end_port:
        print("Error: start-port must be less than or equal to end-port")
        return 1

    print(f"Scanning {args.host} ports {args.start_port}-{args.end_port}...")
    start_time = time.time()

    results = scan_ports(
        host=args.host,
        start_port=args.start_port,
        end_port=args.end_port,
        num_threads=args.threads,
    )

    elapsed = time.time() - start_time

    if results:
        print_results(results)
    else:
        print("No open ports found.")

    print(f"\nScan completed in {elapsed:.2f} seconds")
    return 0


if __name__ == "__main__":
    sys.exit(main())

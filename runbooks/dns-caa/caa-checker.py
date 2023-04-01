#!/usr/bin/env python3

import sys
import dns.resolver as rs


def main():
    domain = sys.argv[1]

    while domain:
        try:
            print(f"domain: {domain}")
            response = rs.resolve(domain, "CAA")

            for r, _ in response.rrset.items.items():
                print(f"\t{r}")
        except rs.NoAnswer:
            pass

        domain = ".".join(domain.split(".")[1:])

    return 0


if __name__ == "__main__":
    sys.exit(main())

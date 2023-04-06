#!/usr/bin/env python3

import io
import os
import subprocess
import sys
import urllib.request
import zipfile


def check_version(file, expected_version):
    try:
        line = subprocess.check_output([file, "version"], text=True)
        version = line.split("\n", maxsplit=1)[0]
        return f"Terraform v{expected_version}" == version
    except Exception:
        return False


def execute_terraform(candidates, version):
    for c in candidates:
        if check_version(c, version):
            os.execvp(c, sys.argv[1:])


def download_terraform(version, store):
    url = f"https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip"
    print(f"Downloading {url}")

    with zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url).read())) as f:
        os.makedirs(f"{store}/{version}", exist_ok=True)
        f.extract("terraform", f"{store}/{version}")
        os.chmod(f"{store}/{version}/terraform", 0o0755)


def main():
    version = sys.argv[1].removeprefix("--version=")

    store = f"{os.environ['TMPDIR']}/terraform-bin"
    binaries = ["terraform", f"{store}/{version}/terraform"]

    execute_terraform(binaries, version)
    download_terraform(version, store)
    execute_terraform(binaries, version)

    return 1


if __name__ == "__main__":
    sys.exit(main())

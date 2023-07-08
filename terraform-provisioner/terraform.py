#!/usr/bin/env python3

import hashlib
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


def execute_terraform(store, version):
    binary = f"{store}/{version}/terraform"

    if check_version(binary, version):
        os.execvp(binary, sys.argv[1:])


def download_terraform(store, version, expected_checksum=None):
    url = f"https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip"
    print(f"Downloading {url}")
    data = io.BytesIO(urllib.request.urlopen(url).read())

    if expected_checksum:
        checksum = hashlib.sha256(data.read()).hexdigest()
        data.seek(0)

    with zipfile.ZipFile(data) as f:
        if expected_checksum and expected_checksum != checksum:
            print(f"Incorrect checksum: {expected_checksum} != {checksum}")
            return

        f.extract("terraform", f"{store}/{version}")
        os.chmod(f"{store}/{version}/terraform", 0o0755)


def main():
    store = f"{os.environ.get('TMPDIR', '/tmp')}/terraform-bin"
    expected_checksum = os.environ.get('TERRAFORM_CHECKSUM', None)
    version = os.environ.get('TERRAFORM_VERSION', '1.3.9')
    os.makedirs(store, exist_ok=True)

    execute_terraform(store, version)
    download_terraform(store, version, expected_checksum)
    execute_terraform(store, version)
    print("Failed to execute terraform binary!")

    return 1


if __name__ == "__main__":
    sys.exit(main())

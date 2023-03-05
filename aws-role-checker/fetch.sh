#!/bin/bash

set -euo pipefail
aws iam list-roles | jq . >roles.json

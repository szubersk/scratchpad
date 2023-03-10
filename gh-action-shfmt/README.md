tag = curl -sSLf -H 'Accept:application/json' https://github.com/mvdan/sh/releases/latest | jq -r '.tag_name'

url=tag/binary_tag_linux_amd64
curl -LO https://github.com/mvdan/sh/releases/download/v3.6.0/shfmt_v3.6.0_linux_amd64

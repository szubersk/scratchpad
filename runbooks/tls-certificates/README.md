# TLS certificates generation

## Self-signed certificate
TODO

## Certificate Authorities

### Generate CA key
openssl genrsa -out ca.key 4096

### Generate CA certificate
openssl req -new -nodes -days 3650 -sha256 -x509 -key ./ca.key -out ./ca.pem -config ./ca.conf -subj '/CN=My Certificate Authority'

## Server certificate
openssl genrsa -out server.key 4096
openssl req -new -nodes -key ./server.key -out ./server.csr -config ./server.conf -subj '/CN=My Server'
openssl x509 -req -sha256 -days 365 -CA ca.pem -CAkey ca.key -CAcreateserial -copy\_extensions copyall -in server.csr -out server.pem

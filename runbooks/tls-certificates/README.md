# TLS certificates generation

## Self-signed certificate
```bash
openssl req -new -newkey rsa:4096 -nodes -x509 -sha256 -days 365 -keyout ss.key -out ss.pem -subj '/CN=SelfSigned' -addext 'subjectAltName = DNS.1:selfsigned.example.com'
```

## CA certificate
```bash
openssl req -new -newkey rsa:4096 -nodes -x509 -sha256 -addext 'authorityKeyIdentifier = keyid,issuer' -addext 'basicConstraints = critical,CA:true' -addext 'keyUsage = critical,keyCertSign,cRLSign' -addext 'subjectKeyIdentifier = hash' -days 3650 -keyout ca.key -out ca.pem -subj '/CN=MyCaAuthority'
```

## Server certificate
```bash
openssl req -new -newkey rsa:4096 -nodes -x509 -sha256 -addext 'basicConstraints = CA:false' -addext 'extendedKeyUsage = serverAuth' -addext 'keyUsage = digitalSignature,nonRepudiation,keyEncipherment,dataEncipherment' -addext 'subjectKeyIdentifier = hash' -CA ca.pem -CAkey ca.key -days 365 -keyout server.key -out server.pem -subj '/CN=MyServer' -addext 'subjectAltName = DNS.1:mydnsname.example.com, URI:myuri'
```

## Client certificate
```bash
openssl req -new -newkey rsa:4096 -nodes -x509 -sha256 -addext 'basicConstraints = CA:false' -addext 'extendedKeyUsage = clientAuth' -addext 'keyUsage = digitalSignature,nonRepudiation,keyEncipherment,dataEncipherment' -addext 'subjectKeyIdentifier = hash' -CA ca.pem -CAkey ca.key -days 365 -keyout client.key -out client.pem -subj '/CN=MyClient' -addext 'subjectAltName = DNS.1:mydnsname.example.com, URI:myuri'
```

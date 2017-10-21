# python-spectrum-change-channel

Python 3 Tool for changing the channel on your Spectrum (TWC/Brighthouse/Charter) Set-Top-Box remotely.

## Prerequisites

Must have Spectrum TV service and STB.

## Install

`pip install requests_oauthlib`

## Usage

```
python3.6 changeChannel.py <username> <password> <channel> <stb-mac-address>

Example:

python3.6 changeChannel.py johnsmith 123456789 82 1B2C3D4E5F0A

Get Mac Addresses for your STB:
python3.6 getMacAddresses <username> <password>
```

## Development

### Contributions

Contributions are welcome.

## Disclaimer
Not affiliated with Spectrum. Use at your own risk.
# DNS update
This is just a short python script/systemd timer that I wrote to 
automate updating DNS records to point to my servers. It costs too much 
to pay for static IPs, so I have to be thrifty! This requires a dnsimple 
account.

## Setup
Simply copy `.dnsimple.example` to `.dnsimple` and fill it out. Fill in 
your domain name in `dns-update.py`, and project path in 
`dns-update.service`. Copy the service/timer files to 
`/etc/systemd/system/` and then run:
```
pip install -r requirements.txt
sudo systemctl enable dns-update.timer
sudo systemctl start dns-update.timer
```

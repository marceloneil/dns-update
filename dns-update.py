from urllib import request
from dnsimple import DNSimple

dns = DNSimple()
ip = request.urlopen('https://ifconfig.co/ip').read().decode('utf-8').rstrip()
data = {'content': ip}
domain = 'example.com'  # Change this!

for item in dns.records(domain):
    if item['record']['record_type'] == 'A':
        if item['record']['content'] != ip:
            old_ip = item['record']['content']
            id = item['record']['id']
            dns.update_record(domain, id, data)
            print('Updated', old_ip, 'to', ip)

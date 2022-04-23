import cmd
from crypt import methods
from flask import Flask
from librouteros import connect
import paramiko
import time

app = Flask(__name__)

@app.route('/configure', methods=['POST'])
def configure():

    hostname = '192.168.1.1'
    username = 'admin'
    password = 'admin123'

    #get router info using librouteros
    api = connect(host=hostname, username=username, password=password)
    identityInfo = api(cmd="/system/identity/print")

    identity = identityInfo[0]['name']

    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(hostname=hostname, username=username, password=password, allow_agent=False, look_for_keys=False)

    list_config = [
        'user add name=daniel, password=tes123, group=read',
        'interface vlan add name=vlan99 vlan-id=99 interface=ether2',
        'ip address add address=11.1.1.1/32 interface=vlan99'
    ]

    for config in list_config:
        conn.exec_command(config)
        time.sleep(2)

if __name__ == '__main__':
    app.run(host='127.0.1.1', debug=True)
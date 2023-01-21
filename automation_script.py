import paramiko, getpass, time

devices = {'R1': {'ip': '172.16.0.1'},
            'R2':{'ip': '172.16.0.2'}}

username = input('username: ')
password = getpass.getpass('password: ')

commands = ['show version\n', 'show ip int br | exc unass\n']

max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

for device in devices.keys():
    outputFilename = device + '_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(5)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    with open(outputFilename, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(5)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output)
    new_connection.close()
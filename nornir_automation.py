from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

commands = ['interface loopback 0 ', 'ip add 1.1.1.1 255.255.255.255', 'no shutdown']

def send_task(task):
    task.run(
        task=netmiko_send_config,
        config_commands=commands,
    )
result=nr.run(task=send_task)
print_result(result)

command_result = nr.run(
    task=netmiko_send_command,
    command_string  ="show ip interface brief | exclude unassigned"
)
print_result(command_result)
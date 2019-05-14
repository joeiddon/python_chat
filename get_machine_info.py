import subprocess

commands = [
	'netstat -aon',
	'ipconfig'
	]

print('kill processes with `tasklill /pid pid_number /f`')
print('=' * 80)

for cmd in commands:
	print(cmd)
	print('-' * len(cmd))
	print(subprocess.check_output(cmd.split()).decode('utf-8'))
	print('=' * 80)
	
input()
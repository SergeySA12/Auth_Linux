import subprocess

def chech_output(comand, text):
    try:
        output = subprocess.check_output(comand, shell=True).decode()
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False
command = "rm --help"
text = "forse"
result = chech_output(command, text)
print(result)
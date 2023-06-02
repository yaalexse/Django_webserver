import subprocess
import os

def cc(language,content):
    title = 'exampe_title'
    print(title)
    print('the code was in cc and the title is empty')
    print(content)
    os.mkdir(title)
    os.chdir(title)
    code_creator(title + '.' + language,content)
    if language == 'ino':
        result = ino_code_compilator(title + '.' + language)
    elif language == 'c':
        result = c_code_compilator(title + '.' + language)
    os.remove(title + '.' + language)
    os.chdir('..')
    os.rmdir(title)
    return result

def code_creator(name,content):
    with open(name, 'w') as file:
        file.write(content)

def ino_code_compilator(name):
    c1 = 'arduino-cli compile --fqbn arduino:samd:mkr1000 '+name
    #print(c1)
    result=subprocess.run(c1, shell=True, capture_output=True, text=True)
    #print("Command Output:")
    #print(result.stdout)
    #print("Command error:")
    #print(result.stderr)
    #print("return code:")
    #print(result.returncode)
    return result

def c_code_compilator(name):
    c1 = 'gcc '+name
    #print(c1)
    result=subprocess.run(c1, shell=True, capture_output=True, text=True)
    #print("Command Output:")
    #print(result.stdout)
    #print("Command error:")
    #print(result.stderr)
    #print("return code:")
    #print(result.returncode)
    return result


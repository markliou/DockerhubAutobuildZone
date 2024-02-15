import subprocess

subprocess.run('docker pull markliou/dind')
subprocess.check_call('docker run -d --rm --name tst markliou/dind')
subprocess.run('docker stop tst')

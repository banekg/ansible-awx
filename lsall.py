import subprocess
import os

output_stream = os.popen('ls -al')
outcome = output_stream.read()
print(outcome)

with open("proba.txt", "w") as text_file:
    text_file.write(outcome)

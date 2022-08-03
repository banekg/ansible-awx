import subprocess
import os
import numpy as np

output_stream = os.popen('ls -al')
outcome = output_stream.read()
print(outcome)

a = np.arange(15).reshape(3, 5)

with open("proba.txt", "w+") as text_file:
    text_file.write(str(a))
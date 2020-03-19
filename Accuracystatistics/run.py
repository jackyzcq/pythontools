import os
cmd='HTKTools/HResults -I src.mlf  /dev/null rec.mlf'
val = os.system(cmd)
print val

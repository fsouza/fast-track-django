import os
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

import sys
sys.path.insert(0, diretorio_atual)
sys.stdout.write("Hello world.\n")
sys.exit(0)

import re
pattern = re.compile("produtos/(\d+)$")
match = pattern.search("http://loja.giran.com.br/produtos/289")
print match.groups()[0] # 289

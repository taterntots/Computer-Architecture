#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) == 2:
  cpu = CPU()
  cpu.load(sys.argv[1])
  cpu.run()

else:
  sys.exit('you done effed up, boi')
#!/usr/bin/env python

import re
import sys

filename = sys.argv[1]
output_dir = sys.argv[2]

fragments = {}
active_fragments = set([])

for line in open(filename, 'r'):
  if m := re.match(r".*--\s+vv\s+([^<]*)", line):
    active_fragments.add(m[1].strip())
    continue
  if m := re.match(r".*--\s+\^\^\s+([^<]*)", line):
    active_fragments.remove(m[1].strip())
    continue
  for fragment in active_fragments:
   fragments[fragment] = fragments.get(fragment, '') + line

for fragment, value in fragments.items():
  file = open(f"{output_dir}/{fragment}.xml", 'w')
  file.write('<screen format="linespecific">' + value.strip() + "</screen>")

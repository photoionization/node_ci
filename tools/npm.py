#!/usr/bin/env python3
# Copyright 2020 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Prints the path of every file in the NPM modules and its dependencies.

 The script should be run with the module names:
 > python ./tools/npm.py mod1 mod2 mod3 ....

 It checks if the module is available locally in the 'node_modules'
 directory, otherwise it runs 'npm install'.

 It prints to the stdout the path of every file in the module directory.

 It fails if 'npm' is not available in PATH.
"""

import os
import subprocess
import sys
import json

def print_mod_contents(mod):
  """Walk the module directory and prints to stdout the path of each file."""
  cwd = os.getcwd()
  for root, _, files in os.walk(os.path.join("node_modules", mod)):
    for f in files:
      print(f'"{os.path.join(cwd, os.path.join(root, f))}",')

def check_npm():
  """Checks if NPM is available in PATH."""
  for path in os.environ["PATH"].split(os.pathsep):
    npm = os.path.join(path, "npm")
    if os.path.isfile(npm) and os.access(npm, os.X_OK):
      return
  print("Error: NPM not found in PATH.")
  print("Please install NPM.")
  exit(1)

def pkg_file_path(mod):
  """Returns the path of 'package.json' for a module."""
  return os.path.join("node_modules", os.path.join(mod, "package.json"))

def mod_is_installed(mod):
  """Checks if a 'package.json' exists for a module."""
  return os.path.isfile(pkg_file_path(mod))

def install_mod(mod):
  """Runs 'npm install' for a module."""
  devnull = open(os.devnull, 'wb')
  subprocess.check_call(["npm", "install", mod], stdout=devnull)

def get_mod_deps(mod):
  """Reads the list of dependencies of a module from its 'package.json'."""
  try:
    pkg = json.load(open(pkg_file_path(mod)))
    return map(lambda mod : mod.split("@")[0], pkg['dependencies'].keys())
  except KeyError: # No 'depenencies' key, so no dependency.
    return []

def print_modules(modules):
  """Prints to stdout the files of the modules and its dependencies."""
  done = []
  print("[")
  for mod in modules:
    if mod in done:
      continue
    if not mod_is_installed(mod):
      install_mod(mod)
    modules.extend(get_mod_deps(mod))
    done.append(mod)
    print_mod_contents(mod)
  print("]")

if __name__ == '__main__':
  check_npm()
  print_modules(sys.argv[1:])

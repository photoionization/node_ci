#!/usr/bin/env python3
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import optparse
import os
import subprocess

DEPS = {
  'base/trace_event/common': 'origin/main',
  'node' : 'origin',
  'third_party/abseil-cpp': 'origin/main',
  'third_party/depot_tools': 'origin/main',
  'third_party/fp16/src': 'origin/master',
  'third_party/googletest/src': 'origin/main',
  'third_party/icu': 'origin/main',
  'third_party/jinja2': 'origin/main',
  'third_party/markupsafe': 'origin/main',
  'third_party/zlib': 'origin/main',
  'v8' : 'origin/main',
}

BUILD_DEPS = {
  'build': 'origin/main',
  'buildtools': 'origin/main',
  'buildtools/clang_format/script': 'origin/main',
  'third_party/libc++/src': 'origin/main',
  'third_party/libc++abi/src': 'origin/main',
  'third_party/libunwind/src': 'origin/main',
  'tools/clang': 'origin/main',
}

def update_deps(root, deps_dict):
  for dep in deps_dict:
    path = os.path.join(root, dep)
    target = deps_dict[dep]
    if '/' not in target:
      # No branch specified. Let's get the latest branch from target remote.
      command = [
        'git', 'ls-remote',
        '--heads',
        '--sort', '-committerdate',
        target,
      ]
    else:
      # Branch specified.
      command = ['git', 'rev-parse', target]

    new_hash = subprocess.check_output(command, cwd=path).strip().decode('utf-8').split('\t')[0]
    old_hash = subprocess.check_output(
      ['gclient', 'getdep', '-r', dep]).strip()
    git_desc = subprocess.check_output(
      ['git', 'log', '--pretty=format:[%h] %s', '-n1', new_hash], cwd=path).strip()
    if new_hash == old_hash:
      print('%s is up-to-date at\n  %s' % (dep, git_desc))
      continue

    subprocess.check_call(
      ['gclient', 'setdep', '-r', '%s@%s' % (dep, new_hash)])
    print('updated %s to\n  %s' % (dep, git_desc))

def main(update_build):
  # Fetch from upstream
  subprocess.check_output(['gclient', 'fetch'])
  # Get gclient root
  root = os.path.join(
            subprocess.check_output(['gclient', 'root']).strip().decode('utf-8'),
            "node-ci")
  update_deps(root, DEPS)
  if update_build:
    update_deps(root, BUILD_DEPS)

if __name__ == '__main__':
  option_parser = optparse.OptionParser()
  option_parser.add_option(
      '', '--update-build',
      action='store_true', dest='update_build', default=False,
      help='Update DEPS for build/ + buildtools/')
  options, args = option_parser.parse_args()
  main(options.update_build)

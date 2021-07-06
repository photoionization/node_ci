#!/usr/bin/env python
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess

DEPS = {
  'node-ci/base/trace_event/common': 'origin/main',
  'node-ci/build': 'origin/main',
  'node-ci/buildtools': 'origin/main',
  'node-ci/buildtools/clang_format/script': 'origin/main',
  'node-ci/buildtools/third_party/libc++/trunk': 'origin/main',
  'node-ci/buildtools/third_party/libc++abi/trunk': 'origin/main',
  'node-ci/buildtools/third_party/libunwind/trunk': 'origin/main',
  'node-ci/node' : 'origin',
  'node-ci/third_party/depot_tools': 'origin/main',
  'node-ci/third_party/googletest/src': 'origin/master',
  'node-ci/third_party/icu': 'origin/master',
  'node-ci/third_party/jinja2': 'origin/main',
  'node-ci/third_party/markupsafe': 'origin/main',
  'node-ci/third_party/zlib': 'origin/main',
  'node-ci/tools/clang': 'origin/main',
  'node-ci/v8' : 'origin/main',
}

def main():
  # Fetch from upstream
  subprocess.check_output(['gclient', 'fetch'])
  # Get gclient root
  root = subprocess.check_output(['gclient', 'root']).strip()
  for dep in DEPS:
    path = os.path.join(root, dep)
    target = DEPS[dep]
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

    new_hash = subprocess.check_output(command, cwd=path).strip().split('\t')[0]
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

if __name__ == '__main__':
  main()

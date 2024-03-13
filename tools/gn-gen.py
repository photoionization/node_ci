#!/usr/bin/env python3
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import os
import subprocess
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ToBool(option):
  return 'true' if option else 'false'

def BuildUpstreamNode():
  with open(os.path.join(ROOT_DIR, 'build/config/gclient_args.gni'), 'r') as f:
    return 'build_upstream_node = true' in f.read()

def GenerateBuildFiles(options):
  gn_args = []
  # Only one sanitizer is enabled.
  assert(options.asan + options.tsan + options.ubsan + options.ubsan_vptr <= 1)

  if BuildUpstreamNode():
    gn_args.append('node_v8_path="//node/deps/v8"')

  if options.asan or options.tsan or options.ubsan or options.ubsan_vptr:
    options.shared = False
    options.debug = False
    options.sysroot = True
    gn_args.append('v8_enable_test_features=true')

  if options.sysroot:
    gn_args.append('use_sysroot=true')
    gn_args.append('use_custom_libcxx=true')

  if options.target_os:
    gn_args.append('target_os="' + options.target_os + '"')

  if options.target_cpu:
    gn_args.append('target_cpu="' + options.target_cpu + '"')

  if options.asan:
    gn_args.append('is_lsan=true')
    gn_args.append('is_asan=true')

  if options.tsan:
    gn_args.append('is_tsan=true')

  if options.ubsan:
    gn_args.append('is_ubsan=true')
    gn_args.append('is_ubsan_no_recover=true')

  if options.ubsan_vptr:
    gn_args.append('is_ubsan_vptr=true')
    gn_args.append('is_ubsan_no_recover=true')

  gn_args.append('icu_use_data_file = false')
  gn_args.append('is_debug=%s' % ToBool(options.debug))
  gn_args.append('symbol_level=%s' % (1 if options.debug else 0))
  gn_args.append('is_component_build=%s' % ToBool(options.shared))
  gn_args.append('node_use_node_code_cache=%s' % ToBool(not options.no_cache))

  flattened_args = ' '.join(gn_args)
  args = ['gn', 'gen', options.out_dir, '-q', '--args=' + flattened_args]
  print('\n'.join(gn_args))
  subprocess.check_call(args)

def ParseOptions(args):
  parser = argparse.ArgumentParser(
      description='Generate GN build configurations')
  parser.add_argument('out_dir', help='build directory')
  parser.add_argument('--asan', help='build with address sanitizer',
                      action='store_true', default=False)
  parser.add_argument('--tsan', help='build with thread sanitizer',
                      action='store_true', default=False)
  parser.add_argument('--ubsan', help='build with undefined-behavior sanitizer',
                      action='store_true', default=False)
  parser.add_argument('--ubsan-vptr',
                      help='build with undefined-behavior (vptr) sanitizer',
                      action='store_true', default=False)
  parser.add_argument('--shared', help='shared library build',
                      action='store_true', default=False)
  parser.add_argument('--sysroot', help='use bundled sysroot',
                      action='store_true', default=False)
  parser.add_argument('--debug', help='debug build',
                      action='store_true', default=False)
  parser.add_argument('--no-cache', help='do not use Node.js code cache',
                      action='store_true', default=False)
  parser.add_argument('--target_os', help='set target OS', default='')
  parser.add_argument('--target_cpu', help='set target CPU', default='')
  return parser.parse_args(args)

if __name__ == '__main__':
  options = ParseOptions(sys.argv[1:])
  GenerateBuildFiles(options)

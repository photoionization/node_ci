# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

gclient_gn_args_file = 'node-ci/build/config/gclient_args.gni'
gclient_gn_args = [
  'checkout_google_benchmark',
  'checkout_fuchsia_for_arm64_host'
]

vars = {
  'checkout_google_benchmark' : False,
  'checkout_fuchsia_for_arm64_host' : False,

  'abseil_revision': '3f6f1caf8d47704b0771d11570d76ac75b279adc',
  'abseil_url': 'https://chromium.googlesource.com/chromium/src/third_party/abseil-cpp.git',

  'build_revision': 'fef3fe31e60ceb77027560ef56e986960463f54b',
  'build_url': 'https://chromium.googlesource.com/chromium/src/build.git',

  'buildtools_revision': '5d2ccbf93c7d956a9aff1d0acd21155e6b515ceb',
  'buildtools_url': 'https://chromium.googlesource.com/chromium/src/buildtools.git',

  'buildtools_clang_format_revision': 'f97059df7f8b205064625cdb5f97b56668a125ef',
  'buildtools_clang_format_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/clang/tools/clang-format.git',

  'buildtools_libcxx_revision': 'f8279b01085b800724f5c5629dc365b9f040dc53',
  'buildtools_libcxx_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libcxx.git',

  'buildtools_libcxxabi_revision': 'f2cb09f94e39caed554c0ea453741edbc24a38a4',
  'buildtools_libcxxabi_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libcxxabi.git',

  'buildtools_libunwind_revision': '129773dde556dfd5dfc7df0eb3c0b970c56029f6',
  'buildtools_libunwind_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libunwind.git',

  'clang_revision': '096dcd2735dd589d85a4ad8bead644869df9eb0e',
  'clang_url': 'https://chromium.googlesource.com/chromium/src/tools/clang.git',

  'depot_tools_revision': '4786a41fb5aa74d356d2fc3e30545d59db5c0bf3',
  'depot_tools_url': 'https://chromium.googlesource.com/chromium/tools/depot_tools.git',

  'fuchsia_sdk_revision': 'f8df9ff79b878d1998970cc04a197061069e48ce',
  'fuchsia_sdk_url': 'https://chromium.googlesource.com/chromium/src/third_party/fuchsia-sdk.git',

  # GN CIPD package version.
  'gn_version': 'git_revision:e9e83d9095d3234adf68f3e2866f25daf766d5c7',

  # ninja CIPD package version.
  # https://chrome-infra-packages.appspot.com/p/infra/3pp/tools/ninja
  'ninja_version': 'version:2@1.11.1.chromium.6',

  'googletest_revision': 'cb455a71fb23303e37ce8ee5b1cde6a2c18f66a5',
  'googletest_url': 'https://chromium.googlesource.com/external/github.com/google/googletest.git',

  'icu_revision': 'a2961dc659b4ae847a9c6120718cc2517ee57d9e',
  'icu_url': 'https://chromium.googlesource.com/chromium/deps/icu.git',

  'jinja2_revision': '264c07d7e64f2874434a3b8039e101ddf1b01e7e',
  'jinja2_url': 'https://chromium.googlesource.com/chromium/src/third_party/jinja2.git',

  'markupsafe_revision': '13f4e8c9e206567eeb13bf585406ddc574005748',
  'markupsafe_url': 'https://chromium.googlesource.com/chromium/src/third_party/markupsafe.git',

  'node_revision': '3afca81d29013accaa098051e1d38f86a829ba99',
  'node_url': 'https://chromium.googlesource.com/external/github.com/v8/node.git',

  'trace_common_revision' : '147f65333c38ddd1ebf554e89965c243c8ce50b3',
  'trace_common_url': 'https://chromium.googlesource.com/chromium/src/base/trace_event/common.git',

  'v8_revision': 'f4d61dfb362c1cbe85d6b74e512c4d619bbd2d38',
  'v8_url': 'https://chromium.googlesource.com/v8/v8.git',

  'zlib_revision': '14dd4c4455602c9b71a1a89b5cafd1f4030d2e3f',
  'zlib_url': 'https://chromium.googlesource.com/chromium/src/third_party/zlib.git',

  'reclient_version': 're_client_version:0.105.0.d6a0caf-gomaip',
}

deps = {
  'node-ci/base/trace_event/common': Var('trace_common_url') + '@' + Var('trace_common_revision'),
  'node-ci/build': Var('build_url') + '@' + Var('build_revision'),
  'node-ci/buildtools': Var('buildtools_url') + '@' + Var('buildtools_revision'),
  'node-ci/buildtools/clang_format/script': Var('buildtools_clang_format_url') + '@' + Var('buildtools_clang_format_revision'),
  'node-ci/buildtools/third_party/libc++/trunk': Var('buildtools_libcxx_url') + '@' + Var('buildtools_libcxx_revision'),
  'node-ci/buildtools/third_party/libc++abi/trunk': Var('buildtools_libcxxabi_url') + '@' + Var('buildtools_libcxxabi_revision'),
  'node-ci/buildtools/third_party/libunwind/trunk': Var('buildtools_libunwind_url') + '@' + Var('buildtools_libunwind_revision'),
  'node-ci/node': Var('node_url') + '@' + Var('node_revision'),
  'node-ci/third_party/abseil-cpp': Var('abseil_url') + '@' + Var('abseil_revision'),
  'node-ci/third_party/depot_tools': Var('depot_tools_url') + '@' + Var('depot_tools_revision'),
  'node-ci/third_party/fuchsia-sdk': {
    'url': Var('fuchsia_sdk_url') + '@' + Var('fuchsia_sdk_revision'),
    'condition': 'checkout_fuchsia',
  },
  'node-ci/third_party/googletest/src': Var('googletest_url') + '@' + Var('googletest_revision'),
  'node-ci/third_party/icu': Var('icu_url') + '@' + Var('icu_revision'),
  'node-ci/third_party/jinja2': Var('jinja2_url') + '@' + Var('jinja2_revision'),
  'node-ci/third_party/markupsafe': Var('markupsafe_url') + '@' + Var('markupsafe_revision'),
  'node-ci/third_party/zlib': Var('zlib_url') + '@' + Var('zlib_revision'),
  'node-ci/tools/clang': Var('clang_url') + '@' + Var('clang_revision'),
  'node-ci/v8': Var('v8_url') + '@' +  Var('v8_revision'),
  'node-ci/buildtools/linux64': {
    'packages': [
      {
        'package': 'gn/gn/linux-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "linux"',
  },
  'node-ci/buildtools/mac': {
    'packages': [
      {
        'package': 'gn/gn/mac-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "mac"',
  },
  'node-ci/buildtools/win': {
    'packages': [
      {
        'package': 'gn/gn/windows-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "win"',
  },
  'node-ci/buildtools/reclient': {
    'packages': [
      {
        'package': 'infra/rbe/client/${{platform}}',
        'version': Var('reclient_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "linux" or host_os == "win"',
  },
  'node-ci/third_party/ninja': {
    'packages': [
      {
        'package': 'infra/3pp/tools/ninja/${{platform}}',
        'version': Var('ninja_version'),
      }
    ],
    'dep_type': 'cipd',
  },
}

hooks = [
  {
    'name': 'generate_node_filelist',
    'pattern': 'node-ci/node',
    'action': ['python3', 'node-ci/tools/generate_node_files_json.py'],
  },
  {
    # Update the Windows toolchain if necessary.
    'name': 'win_toolchain',
    'pattern': '.',
    'condition': 'checkout_win',
    'action': ['python3', 'node-ci/build/vs_toolchain.py', 'update'],
  },
  {
    # Update the Mac toolchain if necessary.
    'name': 'mac_toolchain',
    'pattern': '.',
    'condition': 'checkout_mac',
    'action': ['python3', 'node-ci/build/mac_toolchain.py'],
  },
  {
    'name': 'clang',
    'pattern': '.',
    'action': ['python3', 'node-ci/tools/clang/scripts/update.py'],
  },
  {
    # Update LASTCHANGE.
    'name': 'lastchange',
    'pattern': '.',
    'action': ['python3', 'node-ci/build/util/lastchange.py',
               '-o', 'node-ci/build/util/LASTCHANGE'],
  },
  {
    'name': 'sysroot_x64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_x64',
    'action': ['python3',
               'node-ci/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x64'],
  },
  {
    'name': 'fuchsia_sdk',
    'pattern': '.',
    'condition': 'checkout_fuchsia',
    'action': [
      'python3',
      'node-ci/build/fuchsia/update_sdk.py',
    ],
  },
]

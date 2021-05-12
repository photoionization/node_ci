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

  'abseil_cpp_revision': '66b870c3b1cbbb7f85b31cc9a8a785329f5ebcb8',
  'abseil_cpp_url': 'https://chromium.googlesource.com/chromium/src/third_party/abseil-cpp.git',

  'build_revision': '32281a3e42d30495248ea4c89aa6de41371a1001',
  'build_url': 'https://chromium.googlesource.com/chromium/src/build.git',

  'buildtools_revision': 'e72cd4587a1b833ecf559e4524b69a359cc87697',
  'buildtools_url': 'https://chromium.googlesource.com/chromium/src/buildtools.git',

  'buildtools_clang_format_revision': 'bb994c6f067340c1135eb43eed84f4b33cfa7397',
  'buildtools_clang_format_url': 'https://chromium.googlesource.com/chromium/llvm-project/cfe/tools/clang-format.git',

  'buildtools_libcxx_revision': '8fa87946779682841e21e2da977eccfb6cb3bded',
  'buildtools_libcxx_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libcxx.git',

  'buildtools_libcxxabi_revision': 'a136a3b8e91029a499ca04f94ad89143eaf5fac4',
  'buildtools_libcxxabi_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libcxxabi.git',

  'buildtools_libunwind_revision': '08f35c8514a74817103121def05351186830d4b7',
  'buildtools_libunwind_url': 'https://chromium.googlesource.com/external/github.com/llvm/llvm-project/libunwind.git',

  'clang_revision': 'e76c8f17cf2833813d671674cd89f01f3a21e851',
  'clang_url': 'https://chromium.googlesource.com/chromium/src/tools/clang.git',

  'depot_tools_revision': 'cb17bc602880062ea728a78449fb87d778791dc2',
  'depot_tools_url': 'https://chromium.googlesource.com/chromium/tools/depot_tools.git',

  'fuchsia_sdk_revision': 'f8df9ff79b878d1998970cc04a197061069e48ce',
  'fuchsia_sdk_url': 'https://chromium.googlesource.com/chromium/src/third_party/fuchsia-sdk.git',

  # GN CIPD package version.
  'gn_version': 'git_revision:39a87c0b36310bdf06b692c098f199a0d97fc810',

  'googletest_revision': 'f5e592d8ee5ffb1d9af5be7f715ce3576b8bf9c4',
  'googletest_url': 'https://chromium.googlesource.com/external/github.com/google/googletest.git',

  'icu_revision': 'f022e298b4f4a782486bb6d5ce6589c998b51fe2',
  'icu_url': 'https://chromium.googlesource.com/chromium/deps/icu.git',

  'jinja2_revision': '11b6b3e5971d760bd2d310f77643f55a818a6d25',
  'jinja2_url': 'https://chromium.googlesource.com/chromium/src/third_party/jinja2.git',

  'markupsafe_revision': '0944e71f4b2cb9a871bcbe353f95e889b64a611a',
  'markupsafe_url': 'https://chromium.googlesource.com/chromium/src/third_party/markupsafe.git',

  'node_revision': 'b0b5fec12870e21b9e7718489c108d034cbcf712',
  'node_url': 'https://chromium.googlesource.com/external/github.com/v8/node.git',

  'trace_common_revision' : 'd5bb24e5d9802c8c917fcaa4375d5239a586c168',
  'trace_common_url': 'https://chromium.googlesource.com/chromium/src/base/trace_event/common.git',

  'v8_revision': '4f51af6de8b463007f1e9aab925dcc6d6fd9fb5e',
  'v8_url': 'https://chromium.googlesource.com/v8/v8.git',

  'zlib_revision': '09490503d0f201b81e03f5ca0ab8ba8ee76d4a8e',
  'zlib_url': 'https://chromium.googlesource.com/chromium/src/third_party/zlib.git',
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
  'node-ci/third_party/abseil-cpp': Var('abseil_cpp_url') + '@' + Var('abseil_cpp_revision'),
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
}

hooks = [
  {
    'name': 'generate_node_filelist',
    'pattern': 'node-ci/node',
    'action': ['python', 'node-ci/tools/generate_node_files_json.py'],
  },
  {
    # Update the Windows toolchain if necessary.
    'name': 'win_toolchain',
    'pattern': '.',
    'condition': 'checkout_win',
    'action': ['python', 'node-ci/build/vs_toolchain.py', 'update'],
  },
  {
    # Update the Mac toolchain if necessary.
    'name': 'mac_toolchain',
    'pattern': '.',
    'condition': 'checkout_mac',
    'action': ['python', 'node-ci/build/mac_toolchain.py'],
  },
  {
    'name': 'clang',
    'pattern': '.',
    'action': ['python', 'node-ci/tools/clang/scripts/update.py'],
  },
  {
    # Update LASTCHANGE.
    'name': 'lastchange',
    'pattern': '.',
    'action': ['python', 'node-ci/build/util/lastchange.py',
               '-o', 'node-ci/build/util/LASTCHANGE'],
  },
  {
    'name': 'sysroot_x64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_x64',
    'action': ['python',
               'node-ci/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x64'],
  },
  {
    'name': 'fuchsia_sdk',
    'pattern': '.',
    'condition': 'checkout_fuchsia',
    'action': [
      'python',
      'node-ci/build/fuchsia/update_sdk.py',
    ],
  },
]

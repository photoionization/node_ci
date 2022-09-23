#!/usr/bin/env python3
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys

# Assert python3.
assert sys.version_info.major >= 3

basedir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(basedir, 'node', 'tools'))
import test

sys.exit(test.Main())

#!/usr/bin/env python
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys
basedir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(basedir, 'node', 'tools'))
import test
sys.exit(test.Main())

#!/usr/bin/env python3

import pdb
import time
import sys
from enum import Enum, auto
import subprocess
from typing import Tuple
import unittest
import logging

from jumpstart import Installs
from jumpstart.install_map import install

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


INSTALL_SUBSET = {
    # Installs.chrome,
    # Installs.docker,
    # Installs.i3,
    # Installs.i3_gaps,
}


class TestInstallScripts(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        print(f"{self._testMethodName} -> " f"{time.time() - self.start_time:.2f}[s]")

    # # TODO test missing scripts
    # def test_coverage(self):
    #     self.assertEqual(0, 0, 'TODO')


# Add install tests!


def _make_install_test(key):
    def _wrapped_fcn(self):
        returncode, stdout = install(key)
        self.assertEqual(0, returncode, msg=stdout)

    return _wrapped_fcn


for key in Installs:
    if INSTALL_SUBSET and key not in INSTALL_SUBSET:
        print(f"Skipping {key.name}")
    else:
        setattr(TestInstallScripts, f"test_install_{key.name}", _make_install_test(key))

if __name__ == "__main__":
    # print("STarted the stess")
    # sys.stdout.write("SYS STarted the stess")
    unittest.main()

#
# Copyright (C) 2019, Tomohiro NAKAMURA <quickness.net@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, unicode_literals

import os
import subprocess
import sys

_PY2 = sys.version_info[0] <= 2
_PY35 = sys.version_info[0:2] == tuple([3.5])
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_black(monkeypatch):
    if _PY2 or _PY35:
        # black only support py3.6 and more.
        return

    monkeypatch.chdir(_ROOT)
    stderr = subprocess.run(
        [sys.executable, "-m", "black", ".", "--check"], stderr=subprocess.PIPE
    ).stderr
    assert "reformatted" not in str(stderr), "Please run `./venv/bin/python3 -m black .`."

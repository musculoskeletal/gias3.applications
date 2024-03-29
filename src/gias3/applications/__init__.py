"""
GIAS, a library for Geometry, Image Analysis, and Statistics.
Copyright (C) 2014 Ju Zhang
    
This file is part of GIAS. (https://bitbucket.org/jangle/gias)

    GIAS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GIAS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GIAS.  If not, see <http://www.gnu.org/licenses/>..
"""
import os
import logging

log = logging.getLogger(__name__)

if 'ETS_TOOLKIT' not in os.environ:
    os.environ['ETS_TOOLKIT'] = 'qt4'
elif os.environ['ETS_TOOLKIT'] != 'qt4':
    log.warning("'ETS_TOOLKIT' environment variable does not match the version required for this module ('qt4')")

__version__ = "3.0.2"

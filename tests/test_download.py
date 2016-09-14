"""
Tests for the download module of GLDAS.
"""
import os
from datetime import datetime
import tempfile
import glob

from smap_io.download import get_last_formatted_dir_in_dir
from smap_io.download import get_first_formatted_dir_in_dir
from smap_io.download import get_last_folder
from smap_io.download import get_first_folder
from smap_io.download import folder_get_first_last
from smap_io.download import main


def test_get_last_dir_in_dir():
    path = os.path.join(os.path.dirname(__file__),
                        'test_data', 'SPL3SMP')
    last_dir = get_last_formatted_dir_in_dir(path, "{:%Y.%m.%d}")
    assert last_dir == '2015.04.02'


def test_get_first_dir_in_dir():
    path = os.path.join(os.path.dirname(__file__),
                        'test_data', 'SPL3SMP')
    last_dir = get_first_formatted_dir_in_dir(path, "{:%Y.%m.%d}")
    assert last_dir == '2015.04.01'


def test_get_last_folder():
    path = os.path.join(os.path.dirname(__file__),
                        'test_data', 'SPL3SMP')
    last = get_last_folder(path, ['{:%Y.%m.%d}'])
    last_should = os.path.join(path, "2015.04.02")
    assert last == last_should


def test_get_first_folder():
    path = os.path.join(os.path.dirname(__file__),
                        'test_data', 'SPL3SMP')
    last = get_first_folder(path, ['{:%Y.%m.%d}'])
    last_should = os.path.join(path, "2015.04.01")
    assert last == last_should


def test_get_start_end():
    path = os.path.join(os.path.dirname(__file__),
                        'test_data', 'SPL3SMP')
    start, end = folder_get_first_last(path)
    start_should = datetime(2015, 4, 1)
    end_should = datetime(2015, 4, 2)
    assert end == end_should
    assert start == start_should


def test_download_SPL3SMP_ftp():

    rootpath = tempfile.mkdtemp()
    startdate = "2015-05-01"
    enddate = "2015-05-03"

    args = [rootpath, '-s', startdate, '-e', enddate]
    main(args)
    folders = glob.glob(os.path.join(rootpath, '*'))
    assert len(folders) == 3
    for folder in folders:
        files = glob.glob(os.path.join(rootpath, folder, '*'))
        assert len(files) == 3

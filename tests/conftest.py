import datetime

import pytest


@pytest.fixture(scope='session')
def ltx_doc_fixture():
    from utils import THESIS_DIR_TOPLEVEL
    return {'title': 'Thesis-latex',
     'author': 'Prajay T. Shah',
     'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
     'filename': 'Thesis-ltx',
     'directory': THESIS_DIR_TOPLEVEL}
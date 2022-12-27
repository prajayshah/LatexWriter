import datetime
import os

from pylatex import Section, Command
from pylatex.section import Chapter, Subsection
from pylatex.utils import italic, NoEscape

from utils import THESIS_DIR_TOPLEVEL, read_contents, MyLtxDocument, convert_docx_to_


def ch_am1(doc: MyLtxDocument):

    # chapter = doc.add_chapter('A1: Imaging+: An integrated analysis tool-suite in Python for multi-modal neuroscience data')

    # add results - from tex input
    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim1/aim1-full.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    return doc


def ch_am2(doc: MyLtxDocument):

    # chapter = doc.add_chapter('A2: ')

    # add results - from tex input
    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim2/aim2-full.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    return doc


def ch_am3(doc: MyLtxDocument):

    # add results - from tex input
    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim3/aim3-full.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    return doc


def ch_general_discussion(doc: MyLtxDocument):

    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/4_Discussion/Discussion_full.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    return doc


def ch_general_introduction(doc: MyLtxDocument):

    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.tex'
    assert os.path.exists(input_path), f'File not found: {input_path}'
    doc.add_input(tex_path=NoEscape(input_path))

    return doc


def assemble_texdoc(doc: MyLtxDocument=None):
    """
    Assemble the full tex document in order with all the chapters.

    :param doc: the initialized tex doc
    """
    if doc is None:
        doc: MyLtxDocument = MyLtxDocument(**{'title': NoEscape('The profile of neuronal excitability in epilepsy and seizure'),
                                                 'author': 'Prajay T. Shah',
                                                 'date': NoEscape(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                                 'filename': NoEscape('Thesis-ltx'),
                                                 'directory': THESIS_DIR_TOPLEVEL})

    doc = ch_general_introduction(doc)
    doc = ch_am1(doc)
    doc = ch_am2(doc)
    doc = ch_am3(doc)
    doc = ch_general_discussion(doc)
    doc.append(Command('printbibliography'))
    doc.save_ltx_tex()
    doc.save_ltx_pdf()


# %%
# run the program using Ctrl-R in PyCharm or calling ThesisWriter.main() from the console or `python ThesisWriter.py` from the command line
if __name__ == '__main__':
    # convert_docx_to_(extension='.tex', directory='/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/')
    assemble_texdoc()


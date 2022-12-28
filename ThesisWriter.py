import datetime
import os

from pylatex import Section, Command
from pylatex.section import Chapter, Subsection
from pylatex.utils import italic, NoEscape

from utils import THESIS_DIR_TOPLEVEL, read_contents, MyLtxDocument, convert_docx_to_, _open_preview

PDF_PATH = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/Thesis-ltx.pdf'

def ch_am1(doc: MyLtxDocument):
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim1/aim1-full.tex')

    return doc


def ch_am2(doc: MyLtxDocument):
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim2/aim2-full.tex')

    return doc


def ch_am3(doc: MyLtxDocument):
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim3/aim3-full.tex')

    return doc


def ch_general_discussion(doc: MyLtxDocument):
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/4_Discussion/Discussion_full.tex')

    return doc


def ch_general_introduction(doc: MyLtxDocument):
    inputs = ['/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.tex',
              '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.tex',
              '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.tex',
              '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.tex']

    doc.add_input(*inputs)

    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.tex'
    # doc.add_input(tex_path=NoEscape(input_path))
    #
    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.tex'
    # doc.add_input(tex_path=NoEscape(input_path))
    #
    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.tex'
    # doc.add_input(tex_path=NoEscape(input_path))
    #
    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.tex'
    # doc.add_input(tex_path=NoEscape(input_path))

    return doc


def assemble_texdoc(doc: MyLtxDocument = None):
    """
    Assemble the full tex document in order with all the chapters.

    :param doc: the initialized tex doc
    """
    if doc is None:
        doc: MyLtxDocument = MyLtxDocument(
            **{'title': NoEscape('The profile of neuronal excitability in epilepsy and seizure'),
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
    _open_preview(doc.export_path + '.pdf')


# %%
# run the program using Ctrl-R in PyCharm or calling ThesisWriter.main() from the console or `python ThesisWriter.py` from the command line
if __name__ == '__main__':
    # convert_docx_to_(extension='.tex', directory='/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/')
    convert_docx_to_(extension='.tex',
                     docx_files=[
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.docx',
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.tex',
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.tex',
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.tex',
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim1/aim1-full.docx',
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim2/aim2-full.docx',
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim3/aim3-full.docx',
                         '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/4_Discussion/Discussion_full.docx',
                     ])
    assemble_texdoc()


# _open_preview(PDF_PATH)

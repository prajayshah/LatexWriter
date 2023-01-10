import datetime
import os

from pylatex.utils import NoEscape

from LatexWriter import MyLtxDocument, convert_docx_to_, _open_preview

GRAPHICS_PATH = '/Users/prajayshah/Library/CloudStorage/GoogleDrive-packer.laboratorium@gmail.com/.shortcut-targets-by-id/1xIVr07-1SShbPSgo6UMogmKC8rz8FIe2/Packer Lab/Manuscripts/Alloptical focal 4ap seziure/Figures/2022-12-21 (current)/PNGs/'
PDF_PATH = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/Thesis-ltx.pdf'
DOC_DIR = '/Users/prajayshah/Library/CloudStorage/GoogleDrive-packer.laboratorium@gmail.com/.shortcut-targets-by-id/1xIVr07-1SShbPSgo6UMogmKC8rz8FIe2/Packer Lab/Manuscripts/Alloptical focal 4ap seziure/Manuscript'
TOP_DIR = '/Users/prajayshah/Library/CloudStorage/GoogleDrive-packer.laboratorium@gmail.com/.shortcut-targets-by-id/1xIVr07-1SShbPSgo6UMogmKC8rz8FIe2/Packer Lab/Manuscripts/Alloptical focal 4ap seziure/'
FIGURESDOC_DIR = '/Users/prajayshah/Library/CloudStorage/GoogleDrive-packer.laboratorium@gmail.com/.shortcut-targets-by-id/1xIVr07-1SShbPSgo6UMogmKC8rz8FIe2/Packer Lab/Manuscripts/Alloptical focal 4ap seziure/Figures/tex/'



def assemble_figsandlegends():
    """
    Assemble a tex document and PDF with figures and figure legends converted from a docx document.
    """
    doc: MyLtxDocument = MyLtxDocument(
        **{'filename': NoEscape('Figures and Legends'),
           'directory': DOC_DIR,
           'document_class': 'article',
           'document_options': '11pt',
           'graphics_dir': GRAPHICS_PATH})
    doc.add_Figure_Env()
    doc.set_default_font_sf()
    doc.add_input(FIGURESDOC_DIR+'figureandlegends.docx')
    doc.save_ltx_tex()
    doc.save_ltx_pdf()
    _open_preview(doc.export_path + '.pdf')


# %%
# run the program using Ctrl-R in PyCharm or calling ThesisWriter.main() from the console or `python ThesisWriter.py` from the command line
if __name__ == '__main__':
    assemble_figsandlegends()


# %%

convert_docx_to_(extension='.tex', docx_files=[FIGURESDOC_DIR+'figureandlegends.docx'])

# _open_preview(PDF_PATH)
# convert_docx_to_(extension='.tex', directory='/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/')
# convert_docx_to_(extension='.tex', docx_files=[
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.tex',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.tex',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.tex',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim1/aim1-full.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim2/aim2-full.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim3/aim3-full.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/4_Discussion/Discussion_full.docx',
#                  ])

# use pytest and test create_latex_doc

from LatexWriter import MyLtxDocument

def test_create_latex_doc(ltx_doc_fixture):
    MyLtxDocument(**ltx_doc_fixture)

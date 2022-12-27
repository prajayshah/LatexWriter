# use pytest and test create_latex_doc


from utils import LatexDoc


def test_create_latex_doc(ltx_doc_fixture):
    LatexDoc(**ltx_doc_fixture)

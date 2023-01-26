# utility functions
import datetime
import os
import pypandoc

from typing import List, Union
from pylatex import Document, Section, Subsection, Command, NoEscape, Package
from pylatex.section import Chapter
from pylatex.utils import italic

THESIS_DIR_TOPLEVEL = "/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing"
GRAPHICS_DIR = "/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/_figure-items/export"
EXCLUDE_DIRS = ('9_Archive', 'presentations', '_figure-items', '_archive')


def convert_docx_to_(extension: str, exclude: Union[tuple, List] = EXCLUDE_DIRS,
                     docx_files: list = None, directory: str = THESIS_DIR_TOPLEVEL):
    """
    Convert all .docx files in a directory to the desired extension files using pypandoc

    :param extension: extension of the new file type
    :param docx_files: list of docx files
    :return: None
    """
    docx_files = _get_docx_list(directory=directory, exclude=exclude) if not docx_files else docx_files
    print('\nTo convert ... ')
    [print("\t", doc) for doc in docx_files]
    # get list of all .docx files in directory
    for filename in docx_files:
        if '~$' in filename: pass
        else:
            filepath = os.path.join(directory, filename)
            _convert_to_(filepath=filepath, extension=extension)

    # convert_docx_to_(docx_files, extension=extension, directory=directory)


def _get_docx_list(directory: str, exclude: Union[tuple, List] = EXCLUDE_DIRS) -> list:
    """
    Get all .docx files in a directory

    :param directory: path to directory containing .docx files
    :param exclude: list of directory paths to exclude from search and conversion
    :return: None
    """

    # get list of all .docx files in directory recursively
    docx_files = []
    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file.endswith(".docx"):
                path = os.path.join(root, file)
                # print(path)
                docx_files.append(path)
    return docx_files


def _convert_to_(filepath, extension):
    # output = pypandoc.convert_file(filepath, 'plain')
    output = pypandoc.convert_file(filepath, 'plain')
    with open(filepath[:-5] + extension, 'w') as f:
        f.write(output)
    print(f'Converted: {filepath}')


def read_contents(filename: str, directory: str = THESIS_DIR_TOPLEVEL) -> str:
    """
    Read the contents of a file in a directory

    :param filename: name of file to read
    :param directory: path to directory containing file
    :return: contents of file as string
    """

    if directory in filename:
        filepath = filename
    else:
        filepath = os.path.join(directory, filename)

    assert os.path.exists(filepath), f'File not found: {filepath}'

    with open(filepath, 'r') as f:
        content = f.read()
    return content


def open_preview(*args):
    """
    Open 1 or more files using Preview on Mac.

    :param filepath: path to file
    :return: None
    """
    import subprocess
    for filepath in args:
        assert os.path.exists(filepath), f'File not found: {filepath}'
        subprocess.run(['open', '-a', 'Preview', filepath])


def open_texstudio(*args):
    """
    Open 1 or more files using texstudio on Mac.

    :param filepath: path to .tex file
    :return: None
    """
    import subprocess
    for filepath in args:
        assert os.path.exists(filepath), f'File not found: {filepath}'
        subprocess.run(['open', '-a', 'texstudio', filepath])


class MyLtxDocument(Document):
    def __init__(self, document_class=NoEscape("ut-thesis"),
                 document_options=['normalmargins', '12pt'], filename: str = 'Thesis-ltx',
                 directory: str = THESIS_DIR_TOPLEVEL, graphics_dir: str = GRAPHICS_DIR):

        super().__init__(documentclass=document_class, document_options=document_options)

        # "colorlinks=true, citecolor=black, urlcolor=blue"
        self.packages.append(Package('hyperref', options=NoEscape('colorlinks=true, citecolor=black, urlcolor=blue, linkcolor=black')))
        self.packages.append(Package('caption'))
        self.packages.append(Package('setspace'))
        self.packages.append(Package('amsmath'))
        self.packages.append(Package('enumitem'))
        self.packages.append(Package('acronym', options=('printonlyused', 'nohyperlinks')))

        self.add_graphics(root_path=graphics_dir)
        # self.preamble.append(Command('addbibresource', NoEscape('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/My Library.bib')))

        # self.append(Command('pagenumbering', options='roman'))

        self.__save_dir = directory
        self.__filename = filename


    @property
    def save_dir(self):
        return self.__save_dir

    @save_dir.setter
    def save_dir(self, directory: str):
        self.__save_dir = directory

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def export_path(self):
        "path for the exported file"
        return os.path.join(self.save_dir, self.filename)

    def startThesis(self, title: str = 'Thesis-latex', author: str = 'Prajay T. Shah',
                 date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), acknowledgements=''):
        self.preamble.append(Command('title', title))
        self.preamble.append(Command('author', author))
        self.preamble.append(Command('date', date))
        self.preamble.append(Command('degree', 'Doctor of Philosophy'))
        self.preamble.append(Command('department', 'Biomedical Engineering'))
        self.preamble.append(Command('gradyear', '2022'))
        # self.preamble.append(Command('doublespacing'))
        self.append(NoEscape(r'\maketitle'))
        self.add_acknowledgements(acknowledgements)
        self.append(Command('tableofcontents'))
        self.append(Command('newpage'))
        self.append(Command('listoffigures'))
        # self.append(Command('listoftables'))
        self.add_list_of_eqations()

    def add_list_of_eqations(self):
        "from https://tex.stackexchange.com/questions/173102/table-of-equations-like-list-of-figures"
        self.packages.append(Package('tocloft'))
        self.preamble.append(NoEscape(r"\newcommand{\listequationsname}{List of Equations}"))
        self.preamble.append(NoEscape(r"\newlistof{myequations}{equ}{\listequationsname}"))
        self.preamble.append(NoEscape(r"\newcommand{\myequations}[1]{%"))
        self.preamble.append(NoEscape(r"\addcontentsline{equ}{myequations}{\protect\numberline{\theequation}#1}\par}"))
        self.preamble.append(NoEscape(r"\setlength{\cftmyequationsnumwidth}{2.5em}% Width of equation number in List of Equations"))

        self.append(Command('newpage'))
        self.append(Command('listofmyequations'))

    def add_Figure_Env(self):
        """
        New figure environment to use for placing figures. Use `\begin{figurehere}` to start figure in the tex doc.

        latex commands being added in this function:

        \makeatletter
        \newenvironment{figurehere}
        {\def\@captype{figure}}
        {}
        \makeatletter

        """
        self.preamble.append(Command(NoEscape(r"makeatletter")))
        self.preamble.append(Command(NoEscape(r"newenvironment{figurehere}")))
        self.preamble.append(NoEscape(r"{\def\@captype{figure}}"))
        self.preamble.append(NoEscape(r"{}"))
        self.preamble.append(Command(NoEscape(r"makeatletter")))

    def set_margins(self, margin='2in'):
        self.packages.append(Package('geometry', options=('a4paper', fr'margin={margin}')))

    def set_default_font_sf(self, font_type: str = 'helvet'):

        self.packages.append(Package(NoEscape(font_type), options=('scaled')))
        self.packages.append(Package('fontenc', options=('T1')))
        self.preamble.append(Command(NoEscape(r"renewcommand\familydefault{\sfdefault}")))

    def print_tex(self):
        tex = self.dumps()
        print(tex)

    def save_ltx_pdf(self, filename: str = None, directory: str = None):
        """
        Save current latex document as a pdf

        :param filename: filename of latex document
        :param directory: directory to save pdf in
        :return: None
        """

        if filename is not None: self.filename = filename
        if directory is not None: self.save_dir = directory

        # save document
        self.print_tex()
        print(f'\nCompiling latex pdf ...', end='\r')
        self.generate_pdf(self.export_path)
        print(f'\n\t\__ Saved compiled latex pdf to: {self.export_path}.pdf')

    def save_ltx_tex(self):
        """
        Save current latex document as a tex file.

        :return: None
        """
        print(f'\nSaving compiled latex tex to: {self.export_path}.tex ...', end='\r')
        self.generate_tex(self.export_path)
        print(f'\nSaved compiled latex tex to: {self.export_path}.tex')

    def add_pdf_file(self, file, pages=None):
        """include pages from a pdf file.
        Uses the pdfpages latex package.

        Example of how to use `pages` argument to specify pages to customize:
        \includepdf[pages={1}]{myfile.pdf} % to include just first page of the file
        \includepdf[pages={1,3,5}]{myfile.pdf} % would include pages 1, 3, and 5 of the file
        To include the entire file, you specify pages={-}, where {-} is a range without the endpoints specified which default to the first and last pages, respectively

        source: https://stackoverflow.com/questions/2739159/inserting-a-pdf-file-in-latex
        """
        pgs = r'pages=-' if pages is None else ('pages={' + NoEscape(fr'{pages}') + '}')
        self.packages.append(Package('pdfpages'))
        self.append(Command(NoEscape('includepdf'), arguments=NoEscape(file), options=NoEscape(pgs)))

    def add_chapter(self, title: str):
        """
        Add a chapter to the latex document

        :param title: title of chapter
        :return: None
        """
        chapter = Chapter(title)

        self.append(chapter)
        return chapter

    # add section to latex document
    def add_section(self, chapter: Chapter, title: str, content: str):
        """
        Add a section to the latex document under the specified chapter
        :param chapter: chapter to add section to
        :param title: title of section
        :param content: content of section
        :return:
        """
        section = Section(title)
        section.append(content)
        chapter.append(section)
        return section, chapter

    # add subsection to latex document
    def add_subsection_from_txt(self, section: Section, title: str, content: str):
        """
        Add a subsection to the latex document under the specified section
        :param section: section to add subsection to
        :param title: title of subsection
        :param content: content of subsection
        :return:
        """
        subsection = Subsection(title)
        subsection.append(content)
        section.append(subsection)
        return subsection, section

    # add input statement
    def add_input(self, *args):
        # alternate way of reading and then appending the contents in the .tex file directly:
        # latex_document = tex_path
        # with open(latex_document) as file:
        #     tex = file.read()
        # self.append(NoEscape(tex))
        #####
        for tex_path in args:
            assert type(tex_path) == str, f'Input path must be a string, not {type(tex_path)}'
            assert os.path.exists(tex_path), f'File not found: {tex_path}'
            if tex_path[-4:] != '.tex' and tex_path[-5:] == '.docx':
                convert_docx_to_(extension='.tex', docx_files=[tex_path])
                tex_path = tex_path[:-5] + '.tex'
            assert tex_path[-4:] == '.tex', f'Input file is not a .tex file'
            self.append(Command('input', NoEscape(tex_path)))

    # add include statement
    def add_include(self, *args):
        # alternate way of reading and then appending the contents in the .tex file directly:
        # latex_document = tex_path
        # with open(latex_document) as file:
        #     tex = file.read()
        # self.append(NoEscape(tex))
        #####
        for tex_path in args:
            assert type(tex_path) == str, f'include path must be a string, not {type(tex_path)}'
            assert os.path.exists(tex_path), f'File not found: {tex_path}'
            if tex_path[-4:] != '.tex' and tex_path[-5:] == '.docx':
                convert_docx_to_(extension='.tex', docx_files=[tex_path])
                tex_path = tex_path[:-5] + '.tex'
            assert tex_path[-4:] == '.tex', f'include file is not a .tex file'
            self.append(Command('include', NoEscape(tex_path)))

    def add_graphics(self, root_path):
        self.packages.append(Package('graphicx'))
        self.preamble.append(Command('graphicspath', NoEscape(' {%s/} ' % root_path)))

    # add .bib references document
    def add_bib(self, bib_path):
        # NATBIB:
        self.packages.append(Package('natbib', options='round, comma'))
        self.preamble.append(Command('bibliographystyle', 'plainnat'))
        self.append(Command(NoEscape('addcontentsline{toc}{chapter}{Bibliography}')))
        self.append(Command('bibliography', NoEscape(bib_path)))
        "\addcontentsline{toc}{chapter}{Bibliography}"
        # # BIBLATEX
        # self.packages.append(Package('biblatex', options=(
        #     # NoEscape('backend=biber'),
        #     # NoEscape('style=authoryear'),
        #     # NoEscape('sorting=nyt')
        # )))
        # self.preamble.append(Command('addbibresource', bib_path))
        # self.append(Command('printbibliography'))

    def add_acknowledgements(self, file):
        self.add_input(file)


    def command(self, command: str, *args, **kwargs):
        """
        Add a command to the latex document

        :param command: command to add
        :param args: arguments to command
        :param kwargs: options to command
        :return: None
        """
        self.append(Command(command, *args, **kwargs))


if __name__ == '__main__':
    newdoc = MyLtxDocument()

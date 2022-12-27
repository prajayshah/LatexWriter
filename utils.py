# utility functions
import datetime
import os
import pypandoc

from typing import List, Union
from pylatex import Document, Section, Subsection, Command, NoEscape, Package
from pylatex.section import Chapter
from pylatex.utils import italic

THESIS_DIR_TOPLEVEL = "/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing"
EXCLUDE_DIRS = ('9_Archive', 'presentations', '_figure-items', '_archive')


def convert_docx_to_(directory: str, extension: str, exclude: Union[tuple, List] = EXCLUDE_DIRS,
                        docx_files=None):
    """
    Convert all .docx files in a directory to the desired extension files using pypandoc

    :param extension: extension of the new file type
    :param docx_files: list of docx files
    :return: None
    """
    docx_files = _get_docx_list(directory=directory, exclude= exclude) if not docx_files else docx_files
    # get list of all .docx files in directory
    for filename in docx_files:
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


class MyLtxDocument(Document):
    def __init__(self, title: str = 'Thesis-latex', author: str = 'Prajay T. Shah',
                 date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), documentclass=NoEscape("ut-thesis"),
                 document_options=['normalmargins', '12pt', 'onehalfspacing'],
                 filename: str = 'Thesis-ltx', directory: str = THESIS_DIR_TOPLEVEL):

        # self.doc = Document(documentclass=NoEscape('ut-thesis'))

        super().__init__(documentclass=documentclass, document_options=document_options)

        self.packages.append(Package('biblatex', options=NoEscape('backend=biber')))
        self.packages.append(Package('hyperref', options=NoEscape('colorlinks')))

        self.preamble.append(Command('title', title))
        self.preamble.append(Command('author', author))
        self.preamble.append(Command('date', date))
        self.preamble.append(Command('degree', 'Doctor of Philosophy'))
        self.preamble.append(Command('department', 'Biomedical Engineering'))
        self.preamble.append(Command('gradyear', '2022'))
        self.preamble.append(Command('doublespacing'))
        # self.preamble.append(Command('addbibresource', NoEscape('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/My Library.bib')))

        self.add_bib(bib_path=NoEscape('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/My Library.bib'))

        self.append(NoEscape(r'\maketitle'))

        self.add_pre_content_matter()
        self.append(Command('tableofcontents'))
        self.append(Command('listoffigures'))
        self.append(Command('listoftables'))
        self.__save_dir = directory
        self.__filename = filename

        # print(self.dumps())

        # self.generate_pdf(os.path.join(self.save_dir, self.filename))

        # self.save_ltx_pdf()

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


    def fill_document(self):
        """Add a section, a subsection and some text to the document."""
        with self.create(Section('A section')):
            self.append('Some regular text and some ')
            self.append(italic('italic text. '))

            with self.create(Subsection('A subsection')):
                self.append('Also some crazy characters: $&#{}')


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
        tex = self.dumps()
        print(tex)
        print(f'\nSaving rendered latex pdf to: {os.path.join(self.save_dir, self.filename)}.pdf ...', end='\r')
        self.generate_pdf(os.path.join(self.save_dir, self.filename))
        print(f'\nSaved rendered latex pdf to: {os.path.join(self.save_dir, self.filename)}.pdf')


    def save_ltx_tex(self):
        """
        Save current latex document as a tex file

        :return: None
        """
        print(f'\nSaving rendered latex tex to: {os.path.join(self.save_dir, self.filename)}.tex ...', end='\r')
        self.generate_tex(os.path.join(self.save_dir, self.filename))
        print(f'\nSaved rendered latex tex to: {os.path.join(self.save_dir, self.filename)}.tex')


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
    def add_input(self, tex_path):
        # alternate way of reading and then appending the text in .tex file directly:
        # latex_document = tex_path
        # with open(latex_document) as file:
        #     tex = file.read()
        # self.append(NoEscape(tex))
        #####

        self.append(Command('input', tex_path))

    # add .bib references document
    def add_bib(self, bib_path):
        # self.preamble.append(Command('usepackage', arguments='biblatex', options=NoEscape('backend=biber')))
        self.preamble.append(Command('addbibresource', bib_path))

    def add_pre_content_matter(self):
        self.append(Command('begin', 'dedication'))
        self.append(NoEscape("To everyone who has a passion for science."))
        self.append(Command('end', 'dedication'))
        self.append(Command('begin', 'acknowledgements'))
        self.append(NoEscape("Thanks Mom and Dad and Preet."))
        self.append(Command('end', 'acknowledgements'))

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


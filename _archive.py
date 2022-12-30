# ARCHIVE


# # create a latex document with a title page
# def create_latex_doc(title: str = 'Thesis-latex', author: str = 'Prajay T. Shah', date: str = '2022-12-xx', filename: str = 'Thesis-ltx', directory: str = THESIS_DIR_TOPLEVEL):
#     """
#     Create a latex document with a title page
#
#     """
#
#     # create a latex document
#     doc = Document()
#
#     # add title page
#     doc.preamble.append(Command('title', title))
#     doc.preamble.append(Command('author', author))
#     doc.preamble.append(Command('date', date))
#     doc.append(NoEscape(r'\maketitle'))
#
#     # save document
#     print(f'Saving rendered latex pdf to: {directory}')
#     doc.generate_pdf(os.path.join(directory, filename))

# %%

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



# %%
chapter = doc.add_chapter('A1: Imaging+: An integrated analysis tool-suite in Python for multi-modal neuroscience data')

# add introduction chapter
# content = read_contents('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3 Results/ch-aim1/aim1-intro.txt')
content = 'hot content for introduction'
_ = doc.add_section(chapter=chapter, title='Introduction', content=content)

# add results - introduction chapter
# content = read_contents('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3 Results/ch-aim1/aim1-results.txt')
content = 'hot content for results'
_ = doc.add_section(chapter=chapter, title='Results', content=content)

# add discussion - discussion chapter
# content = read_contents('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3 Results/ch-aim1/aim1-discussion.txt')
content = 'hot content for discussion'
_ = doc.add_section(chapter=chapter, title='Discussion', content=content)


# %%
def fill_document(self):
    """Add a section, a subsection and some text to the document."""

    self.append(Chapter('a new chapter'))

    # self.append(Command('chapter', arguments=('a new chapter')))

    # self.dumps()

    with self.create(Section('A section')):
        self.append('Some regular text and some ')
        self.append(italic('italic text. '))

        with self.create(Subsection('A subsection')):
            self.append('Also some crazy characters: $&#{}')


    with self.create(Chapter('A second new chapter')):
        self.append('some text under A new chapter')


# %%
class LatexDoc(Document):
    """A class to create a full latex doc"""

    def __init__(self, title: str = 'Thesis-latex', author: str = 'Prajay T. Shah',
                 date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 filename: str = 'Thesis-ltx', directory: str = THESIS_DIR_TOPLEVEL):
        """
        :param title: title of document
        :param author: author of document
        :param date: date of document
        :param filename: filename of document
        :param directory: directory to save document in
        :return: latex doc instance
        """
        # create a latex document
        super().__init__()

        print(f'Creating latex document...'
              f'\n\ttitle: {title}'
              f'\n\tauthor: {author}'
              f'\n\tdate: {date}'
              f'\n\tfilename: {filename}'
              f'\n\tdirectory: {directory}')

        # add title page
        self.preamble.append(Command('title', title))
        self.preamble.append(Command('author', author))
        self.preamble.append(Command('date', date))
        self.append(NoEscape(r'\maketitle'))

        self.__save_dir = directory
        self.__filename = filename

        self.save_ltx_pdf()

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
        print(f'Saving rendered latex pdf to: {os.path.join(self.save_dir, self.filename)}')
        self.generate_pdf(os.path.join(self.save_dir, self.filename))

    def save_ltx_tex(self):
        """
        Save current latex document as a tex file

        :return: None
        """
        print(f'Saving rendered latex tex to: {os.path.join(self.save_dir, self.filename)}')
        self.generate_tex(os.path.join(self.save_dir, self.filename))

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


# %%
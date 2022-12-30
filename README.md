*Are you thinking about writing your thesis in word and copy/paste-ing it into Overleaf to build a Latex document?*

**STOP!**

**Use ThesisWriter.**

This repo is designed to enable a hybrid option for writing your content in word, and then directly running a few lines in Python to create a full Latex document (utilizes the ```pylatex``` package).
This is useful for those who are not familiar with Latex, but want to use it to create a thesis document. 

**Procedure:**
- Convert .docx files to a plain-text .tex files. Note: The conversion process uses a plain text intermediate which does not retain any formatting or styling information. 
- Assemble the latex document using the package functions. 
- Create a compiled Latex document as .tex and .pdf output
- Open the .pdf document in preview on Mac

**WARNING:** the overall procedure requires you to write latex commands directly in the word doc for the following (since the docx to tex conversion outputs plain-text):
- specifying chapters, sections, subsections, etc.
- specifying the figures and tables, along with their in-text references 
- specifying special symbols and characters (e.g. $\alpha$)
- in-text citations to articles, books etc. (e.g. \cite{[citation-key]})
- in-text acronyms and the corresponding acronym list (which needs to be added as a separate section, following the TeX acronym package conventions)

*Note:*
For generating in-text citations that follow the correct citation key directly from a reference database, install and use the Zotero citation style CSL file provided in this repo (custom-better-bibtex-citekeys.csl) 
The nice thing about this procedure is that you can write content as usual in word with a Zotero citation style that you like and then when you are ready to compile the overall document, convert the citation style to `Better BibTex Citekeys [custom]`, and you're good to go.



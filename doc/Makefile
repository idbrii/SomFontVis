#FILE=presentation
EPS_FILES=$(wildcard diagrams/*.eps)
FILE=report

all: $(FILE).pdf

clean:
	$(RM) *.aux
	$(RM) *.bbl
	$(RM) *.blg
	$(RM) *.idx
	$(RM) *.ilg
	$(RM) *.ind
	$(RM) *.lof
	$(RM) *.log
	$(RM) *.lot
	$(RM) *.toc
	$(RM) $(FILE).pdf
	$(RM) $(FILE).dvi

TOTIDY=*.aux *.log *.nav *.out *.snm *.toc *~ *.bbl *.blg *.dvi
tidy:
	$(RM) $(TOTIDY)

# TODO: Make these into generic targets

fixeps: 
	for a in $(EPS_FILES); do epstopdf $$a; done

$(FILE).bbl: ref.bib
	pdflatex $(FILE)
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)

$(FILE).pdf: $(FILE).tex diagrams/*.png $(FILE).bbl
	pdflatex $<

letter.pdf: letter.tex
	pdflatex $<

#$(FILE).dvi: $(FILE).tex *.tex
#	texi2dvi -l latex $(FILE).tex

evince:
	while :; do make $(PDF) && evince $(FILE).pdf || read; done

open: $(FILE).pdf
	open $(FILE).pdf

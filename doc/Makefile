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

$(FILE).pdf: $(FILE).dvi
	dvipdf $^

$(FILE).dvi: $(FILE).tex *.tex
	texi2dvi -l latex $(FILE).tex

xpdf:
	while :; do make $(PDF) && xpdf $(FILE).pdf || read; done

open: $(FILE).pdf
	open $(FILE).pdf

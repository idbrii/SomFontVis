CC = env python
FLAGS = -t
SRCS= $(wildcard *.py)
OUTFILE=__init__.py
MAIN=$(OUTFILE)

.PHONY:	all doctest clean

init:	$(SRCS)
	-rm $(OUTFILE)
	$(CC) $(FLAGS) -uc "import os; print '__all__ = [', [reduce(lambda x,y: (y[-2:]=='py' and x+y[:-3]+'\", \"') or x, filter( (lambda x: x.find('$(OUTFILE)')==-1), os.listdir('.') ), '\"')][0][:-3], ']'" | cat | tee $(OUTFILE)

all:	init doctest $(SRCS)


# run doctest for every py file except main
doctest:	$(SRCS)
	for file in $(filter-out $(MAIN), $(SRCS)); do $(CC) $$file; done

clean:
	-rm $(OUTFILE)
	-rm *.pyc

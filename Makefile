CC = env python
FLAGS = -tt
MAIN = main.py
SRCS= $(wildcard *.py)

.PHONY:	all run doctest clean

all:	tags run

tags:	$(SRCS)
	-ctags -R .

run:	make.lib
	$(CC) $(FLAGS) $(MAIN)

# run doctest for every py file except main
doctest:	$(SRCS)
	for file in $(filter-out $(MAIN), $(SRCS)); do $(CC) $$file; done

# Don't know how to get make do dependents recursively, so fake it for now.
make.lib:	lib/*.py
	make -C lib init
	touch make.lib

clean:
	-rm *.pyc
	-rm tags
	-rm make.lib
	make -C lib clean

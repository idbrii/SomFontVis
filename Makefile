CC = env python
FLAGS = -tt
MAIN = main.py
SRCS= $(wildcard *.py)

.PHONY:	all init run doctest clean

all:	tags run

tags:	$(SRCS)
	-ctags -R .

init:
	mkdir weight

run:	init make.lib.stamp make.Generated.stamp
	$(CC) $(FLAGS) $(MAIN)

# run doctest for every py file except main
doctest:	$(SRCS)
	for file in $(filter-out $(MAIN), $(SRCS)); do $(CC) $$file; done

# Don't know how to get make do dependents recursively, so fake it for now.
make.%.stamp:	% %/*.py
	make -C $< init
	touch $@

clean:
	-rm *.pyc
	-rm tags
	-rm make.*.stamp
	-rm -rf weight/
	make -C lib clean
	make -C Generated clean

.PHONY: solution

solution: solution.md
	
%.txt: %.py
	python $< > $@

%.md: %.py
	publish $< md

%.tex: %.py
	publish $< tex
	
%.docx: %.py
	publish $< docx
	
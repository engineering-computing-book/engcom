.PHONY: solution
	
title = Solution for Problem DN
author = Rico A. R. Picone

solution: solution.md # Default document(s) to make
	
%.txt: %.py
	python $< > $@

%.md: %.py
	publish $< md --title "$(title)" --author "$(author)"

%.tex: %.py
	publish $< tex --title "$(title)" --author "$(author)"
	
%.docx: %.py
	publish $< docx --title "$(title)" --author "$(author)"

%.pdf: %.py
	publish $< pdf --title "$(title)" --author "$(author)"
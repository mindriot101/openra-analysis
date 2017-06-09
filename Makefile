all: exploration.html new_ideas.html

%.html: %.ipynb
	./venv/bin/jupyter nbconvert --execute $<

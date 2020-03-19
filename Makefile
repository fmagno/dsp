# -- Setup ----------------------------#

.PHONY: install
install:
	python setup.py install && \
	rm -rf dist/ build/ dsp.egg-info/
	# mkdir -p vendor && \
	# git clone https://github.com/pavel-demin/red-pitaya-notes.git vendor/red-pitaya-notes


.PHONY: uninstall
uninstall:
	pip uninstall -y dsp


.PHONY: clean
clean:
	rm -rf dist/ build/ dsp.egg-info* && \
	find . \( -name __pycache__ \
		-o -name "*.pyc" \
		-o -name .eggs \
\) -exec rm -rf {} +\
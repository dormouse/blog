# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = DormouseBlog
SOURCEDIR     = source
BUILDDIR      = build
GITHUB_DIR=~/project/dormouse.github.io

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

git:
	@echo
	@echo "Rsync starting..."
	rsync -a $(BUILDDIR)/html/ ~/project/dormouse.github.io --exclude ".*"
	cd $(GITHUB_DIR) && git pull && git add -A && git commit -m 'update' && git push origin $(GITHUB_PAGES_BRANCH)
	@echo
	@echo "Rsync finished."

.PHONY: help git Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

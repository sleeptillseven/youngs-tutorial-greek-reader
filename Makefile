# A Self-Documenting Makefile: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# the version is hold in the file .version

.PHONY: test help
.DEFAULT_GOAL := help

build-html:	## build HTML files from sources
	@echo "building HTML docs..."
	@python3 scripts/generate-static.py > docs/index.html
	@echo "🍺 done"

check-encoding:	## verify encoding of text
	@echo "running encoding checker..."
	@validate-text text-validator.toml text/tutorial-greek-reader.txt 2>&1 | grep -v TOKEN_REGEXES

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

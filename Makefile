PRJ_NAME="Play Bench"
AUTHOR="Meteormin \(miniyu97@gmail.com\)"
PRJ_BASE=$(shell pwd)
PRJ_DESC=$(PRJ_NAME) Deployment and Development Makefile.\n Author: $(AUTHOR)

.DEFAULT: help
.SILENT:;

##help: helps (default)
.PHONY: help
help: Makefile
	echo ""
	echo " $(PRJ_DESC)"
	echo ""
	echo " Usage:"
	echo ""
	echo "	make {command}"
	echo ""
	echo " Commands:"
	echo ""
	sed -n 's/^##/	/p' $< | column -t -s ':' |  sed -e 's/^/ /'
	echo ""


##setup: setup report with openai (MCP)
.PHONY: setup
setup:
	./scripts/setup.sh

##build: build all
.PHONY: build
build:
	./scripts/build.sh

##run algo={fib} n={number}: run main
.PHONY: run
run:
	./main $(algo) $(n)
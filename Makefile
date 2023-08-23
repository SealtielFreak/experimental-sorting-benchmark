# Makefile for automating tests with pyperf

SCRIPTS := $(wildcard bench_*.py)
STATS_FILES := $(patsubst bench_%.py, stats_bench_%.json, $(SCRIPTS))

.PHONY: all clean

all: $(STATS_FILES)

bench_%.json: bench_%.py
	python $< -o $@
	pyperf stats $@
	mv $@ $@_$(shell date +'%Y%m%d_%H%M%S')

clean:
	rm -f stats_*.json_*

run: $(STATS_FILES)

run_single: bench_name = $(filter-out $@,$(MAKECMDGOALS))
run_single: bench_$(bench_name).json

%:
	@:

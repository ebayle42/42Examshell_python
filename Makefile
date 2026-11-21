all:
	@bash exam.sh

test:
	@bash .resources/tools/selftest.sh

clean:
	@rm -rf rendu

fclean: clean
	@rm -rf trace

.PHONY: all test clean fclean

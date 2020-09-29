build:
	@docker build -t python .

test:
	@make build
	@docker run --rm python python setup.py test

hello:
	@docker run --rm python hello

hello2:
	@docker run --rm python hello2

goodbye:
	@docker run --rm python goodbye

goodbye2:
	@docker run --rm python goodbye2

build:	#	выполнит poetry publish
	poetry build

publish:	#	выполнит poetry publish
	poetry publish --dry-run

package-install:	#	которая выполнит python3 -m pip install
	python3 -m pip install --user dist/*.whl


install:	#	Установка поетри
	poetry install

brain-games:	#	Запуск игры
	poetry run brain-games

make lint:  #запуск flake8
	poetry run flake8 brain_games
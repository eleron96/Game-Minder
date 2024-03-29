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

brain-even: # запуск игры четное не четное
	poetry run brain_even

brain-calc: # запуск игры калькулятора
	poetry run brain_calc

brain-gcd: # запуск игры калькулятора
	poetry run brain_gcd

brain-progression:  # запуск игры геометрическая прогрессия
	poetry run brain_progression

brain-prime:  # запуск игры геометрическая прогрессия
	poetry run brain_prime

git:
	poetry install
	poetry version patch
	poetry build
	python3 -m pip install --user dist/*.whl
	poetry publish --dry-run --username ' ' --password ' '

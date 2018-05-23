from bottle import route, run, request, redirect, template

from repo import ToyRepo

MIN_PRICE = 0
MAX_PRICE = 100000
MIN_AGE = 0
MAX_AGE = 100

repo = ToyRepo()


@route('/')
@route('/add')
def add_form():
    return template('static/add.html')


@route('/select')
def select_form():
    return template('static/select.html')


@route('/add', method='POST')
def add():
    name, price, min_age, max_age = get_add_params()
    if name:
        repo.put(name, price, min_age, max_age)
    return redirect('/add')


@route('/result')
def result():
    min_price, max_price, min_age, max_age = get_select_params()
    toys = repo.get_where(min_price, max_price, min_age, max_age)
    toys_tbody = ''
    for id, name, price, min_age, max_age in toys:
        toys_tbody += '''
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}-{}</td>
        </tr>\n
        '''.format(id, name, price, min_age, max_age)
    return template('static/result.html', toys_tbody=toys_tbody)


def clamp(x, minimum, maximum, default=0):
    x = int(x) if x else default
    return minimum if x < minimum else maximum if x > maximum else x


def get_add_params():
    name = request.forms.get('name')
    price = clamp(request.forms.get('price'), MIN_PRICE, MAX_PRICE, MIN_PRICE)
    min_age = clamp(request.forms.get('minAge'), MIN_AGE, MAX_AGE, MIN_AGE)
    max_age = clamp(request.forms.get('maxAge'), MIN_AGE, MAX_AGE, MAX_AGE)
    return name, price, min_age, max_age


def get_select_params():
    min_price = clamp(request.params.get('minPrice'), MIN_PRICE, MAX_PRICE, MIN_PRICE)
    max_price = clamp(request.params.get('maxPrice'), MIN_PRICE, MAX_PRICE, MAX_PRICE)
    min_age = clamp(request.params.get('minAge'), MIN_AGE, MAX_AGE, MIN_AGE)
    max_age = clamp(request.params.get('maxAge'), MIN_AGE, MAX_AGE, MAX_AGE)
    return min_price, max_price, min_age, max_age


def load_sample_data():
    repo.put('Plush Cat', 50, 10, MAX_AGE)
    repo.put('Lego Set', 500, 8, 80)
    repo.put('RC Truck', 5000, 15, MAX_AGE)
    repo.put('Plastic Doll', 250, 2, 10)


def main():
    load_sample_data()
    run(host='localhost', port=8080)


if __name__ == '__main__':
    main()

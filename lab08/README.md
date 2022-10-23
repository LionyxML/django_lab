# graphqlpratice

Clone this repo and inside its folder:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata ingredients
python manage.py createsuperuser
ptyhon manage.py runserver
```

Add new users and posts on `http://localhost:8000/admin`.

Use the GraphiQL interface to make a query: `http://localhost:8000/graphql`.

Examples:

```
query {
  allIngredients {
    id
    name
  }
}

```

```
query {
  categoryByName(name: "Dairy") {
    id
    name
    ingredients {
      id
      name
    }
  }
}

```

```
query {
  allIngredients {
    id
    name
    category {
      id
      name
    }
  }
}
```

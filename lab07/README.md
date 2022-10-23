# graphqlpratice

Clone this repo and inside its folder:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd graphqlpratice
python manage.py migrate
python manage.py createsuperuser
```

Add new users and posts on `http://localhost:8000/admin`.

Use the GraphiQL interface to make a query: `http://localhost:8000/graphql`.

Example:

```
{
  authors {
    name
    posts {
      title
      body
    }
  }
}

```

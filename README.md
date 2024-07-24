# Blog-GraphQL
Create Blog App with GraphQL

## Install GraphQL
- Install Graphene-Django

```bash
pip install graphene-django
```
- Add graphene_django to INSTALLED_APPS in settings.py

```python
INSTALLED_APPS = [
    ...
    'graphene_django',
]
```
- Add Graphene Schema in settings.py

```python
GRAPHENE = {
    'SCHEMA': 'blog.schema.schema'
}
```


## Install pre-commit

- Install Required Tools

```bash
pip install isort black flake8 pre-commit
```

- Create a Pre-Commit Configuration File
    - Create or update a file named .pre-commit-config.yaml in the root of your project:
    ```yaml
    repos:
        - repo: https://github.com/pre-commit/pre-commit-hooks
            rev: v4.6.0
            hooks:
            - id: trailing-whitespace
            - id: end-of-file-fixer
            - id: check-added-large-files


        - repo: https://github.com/PyCQA/isort
            rev: 5.13.2
            hooks:
            - id: isort


        - repo: https://github.com/psf/black
            rev: 24.4.2
            hooks:
            - id: black


        - repo: https://github.com/pycqa/flake8
            rev: 7.1.0
            hooks:
            - id: flake8


        - repo: local
            hooks:
            - id: django-check
                name: Run Django Check
                entry: python manage.py check
                language: system
                pass_filenames: false
                types: [python]
    ```

- Configure flake8
    - Create or update a setup.cfg file in the root of your project:
    ```cfg
    [flake8]
    max-line-length = 99
    exclude = **/migrations/*,venv
    extend-ignore = E203, W503

    [isort]
    profile=black
    ```

- Set up Pre-Commit
```bash
pre-commit install
```

- Update all pre-commit hooks
```bash
pre-commit autoupdate
```

- Running Pre-Commit Manually
```bash
pre-commit run --all-files
```


### Create Author in GraphQL Server by using GraphiQL
- Create Author
```graphql
mutation{
  createAuthor(name:"fares"){
    author{
      id,
      name
    }
  }
}
```
- Query All Authors
```graphql
query{
  allAuthors{
    id,
    name
  }
}
```
- Update Post
```graphql
mutation{
  updatePost(id:1, title:"updated",content:"anyupdate"){
    post{
      id
      title
    }
  }
}
```
- Retrieve Author by ID
```graphql
query{
  autherById(id:1){
    name
  }
}
```

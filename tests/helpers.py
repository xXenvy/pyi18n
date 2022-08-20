test_path: str = 'tests/locales/'
empty_locales: str = 'tests/empty_locales/'
bigger_files_path: str = 'tests/bigger_locales/'
custom_loader_path: str = 'examples/locales/'

locale_content: dict = {
    "pl": {
        "hello": {
            "world": "Witaj świecie!",
            "hello_user": "Witaj {user}!",
            "hello_full_name_age": "Witaj {name} {surname}! Ty masz {age} lat."
        },
        "common": {
            "hello": "Witaj",
            "center": "Centrum",
            "world": "Świat",
            "developer": "Programista",
            "age": "Wiek"
        },
        "announcement": {
            "hello": "Witaj!",
            "hello_user": "Witaj {user}!",
            "hello_full_name_age": "Witaj {name} {surname}! Ty masz {age} lat."
        },
        "date": {
            "today": "Dziś jest {date}",
            "tomorrow": "Jutro jest {date}",
            "yesterday": "Wczoraj był {date}"
        }
    },
    "en": {
        "hello": {
            "world": "Hello world!",
            "hello_user": "Hello {user}!",
            "hello_full_name_age": "Hello {name} {surname}! You are {age} years old."
        },
        "common": {
            "hello": "Hello",
            "center": "Center",
            "world": "World",
            "developer": "Developer",
            "age": "Age"
        },
        "announcement": {
            "hello": "Hello {user}!",
            "hello_user": "Hello {user}!",
            "hello_full_name_age": "Hello {name} {surname}! You are {age} years old."
        },
        "date": {
            "today": "Today is {date}",
            "tomorrow": "Tomorrow is {date}",
            "yesterday": "Yesterday is {date}"
        }
    }
}

bigger_locales: dict = {
    "en": {
        "hello": {
            "world": "Hello world!",
            "hello_user": "Hello {user}!",
            "hello_full_name_age": "Hello {name} {surname}! You are {age} years old."
        },
        "labels": {
            "todos": {
                "empty": "You have no todos.",
                "one": "You have 1 todo.",
                "many": "You have {count} todos.",
                "add": "Add a todo.",
                "delete": "Delete todo.",
                "delete_confirm": "Are you sure you want to delete this todo?"
            },
            "products": {
                "empty": "You have no products.",
                "one": "You have 1 product.",
                "many": "You have {count} products.",
                "add": "Add a product.",
                "delete": "Delete product.",
                "delete_confirm": "Are you sure you want to delete this product?"
            },
            "users": {
                "empty": "You have no users.",
                "one": "You have 1 user.",
                "many": "You have {count} users.",
                "add": "Add a user.",
                "delete": "Delete user.",
                "delete_confirm": "Are you sure you want to delete this user?",
                "username": "Username",
                "full_name": "Full name",
                "age": "Age",
                "password": "Password",
                "password_confirm": "Password confirm",
                "email": "Email",
                "phone": "Phone",
                "address": "Address",
                "description": "Description",
                "created_at": "Created at",
                "updated_at": "Updated at"
            }
        },
        "messages": {
            "todos": {
                "added": "Todo added.",
                "deleted": "Todo deleted.",
                "not_found": "Todo not found.",
                "updated": "Todo updated."
            },
            "products": {
                "added": "Product added.",
                "deleted": "Product deleted.",
                "not_found": "Product not found.",
                "updated": "Product updated."
            },
            "users": {
                "added": "User added.",
                "deleted": "User deleted.",
                "not_found": "User not found.",
                "updated": "User updated."
            }
        }
    }
}


from contextlib import contextmanager
import pytest

@contextmanager
def not_raises(exc):
    try:
        yield
    except exc:
        raise pytest.fail("DID RAISE {0}".format(exc))
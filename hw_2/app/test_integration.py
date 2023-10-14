import pytest

from fastapi.testclient import TestClient
from . import main

client = TestClient(main.app)


@pytest.mark.parametrize(
    "id, excepted_status",
    [
        (-1, 200),
        (2, 404),
        (3, 404),
        (4, 200),
    ],
)
def test_add_book(create_test_db, id, excepted_status):
    get_response = client.post(
        f"/books",
        json={
            "id": id,
            "title": "new title",
            "author": "new author",
            "description": "new description",
        },
    )
    assert get_response.status_code == excepted_status


@pytest.mark.parametrize(
    "id, excepted_status",
    [
        (-1, 404),
        (0, 200),
        (1, 200),
        (100, 404),
    ],
)
def test_get_book(create_test_db, id, excepted_status):
    get_response = client.get(f"/books/{id}")
    assert get_response.status_code == excepted_status


@pytest.mark.parametrize(
    "id, excepted_status",
    [
        (0, 200),
        (1, 200),
        (100, 404),
    ],
)
def test_update_book(create_test_db, id, excepted_status):
    get_response = client.put(
        f"/books/{id}",
        json={
            "id": id,
            "title": "new title",
            "author": "new author",
            "description": "new description",
        },
    )
    assert get_response.status_code == excepted_status


@pytest.mark.parametrize(
    "id, excepted_status",
    [
        (2, 200),
        (-10, 404),
        (100, 404),
    ],
)
def test_delete_book(create_test_db, id, excepted_status):
    get_response = client.delete(f"/books/{id}")
    assert get_response.status_code == excepted_status

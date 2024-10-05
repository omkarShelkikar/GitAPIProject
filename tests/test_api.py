import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    post = response.json()
    assert post['id'] == 1
    assert post['title'] is not None

def test_create_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert response.json()['title'] == new_post['title']

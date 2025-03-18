import requests

url = "https://jsonplaceholder.typicode.com/"

## check pagination


def test_pagination():
    page = 1
    while True:
        response  = requests.get(f"{url}/todos",params={"_page": page, "_limit": 10})
        response.status_code == 200
        results = response.json()
        if not results:
            print("No more data found, stopping pagination page found are",page)
            break
        assert len((results)) <=10
        assert all('id' in result and 'title' in result for result in results)
        page +=1


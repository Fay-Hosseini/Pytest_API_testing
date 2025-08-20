import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class API_crud:
    def get_posts(self, post_id):
        return requests.get(f"{BASE_URL}/posts/{post_id}")

    def get_all_posts(self):
        return requests.get(f"{BASE_URL}/posts")

    def create_posts(self,title,body,user_id):
        new_post = {"title": title, "body": body, "user_id": user_id}
        return requests.post(f"{BASE_URL}/posts", json=new_post)

    def update_posts(self, post_id, title, body, user_id ):
        updated_post = {"id":post_id, "title":title, "body": body, "user_id": user_id}
        return requests.put(f"{BASE_URL}/posts/{post_id}", json= updated_post)

    def delete_posts(self,post_id):
        return requests.delete(f"{BASE_URL}/posts/{post_id}")
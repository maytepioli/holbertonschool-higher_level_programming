import requests
import csv

def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    answer = requests.get(url)

    if answer.status_code == 200:
        posts = answer.json()
        for i in posts:
            print(i["title"])

def fetch_and_save_posts():
    list_dic = []
    url = 'https://jsonplaceholder.typicode.com/posts'
    answer = requests.get(url)
    if answer.status_code == 200:
        posts = answer.json()
        for i in posts:
           dic = {'id': i['id'], 'title': i['title'], 'body': i['body']}
           list_dic.append(dic)
    with open('posts.csv', 'w') as file:
        write = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        write.writeheader()
        write.writerows(list_dic)

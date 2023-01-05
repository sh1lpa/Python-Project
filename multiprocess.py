# from multiprocessing import Pool
# import os 

# def spawn():

#     print("spawned !! ")

# def main():
#     for i in range(5):
#         p = multiprocessing.Process(target=spawn)
#         p.start()
#         print(p.pid)

# def task(num):
#     print(num +2)
# def main():
#     p = Pool(processes=20)
#     data = p.map(task, [0, 1, 2, 3, 4])
#     p.close()

from multiprocessing import Pool
import bs4 as bs
import random    
import requests
import string

def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    return ''.join('http://'+ starting + '.com')

def handle_local_links(url, link):
    return ''.join(url+link) if link.startswith('/') else url

def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode('ascii')) for link in links]

        return links
    except TypeError as e:
        print(e)
        print('Got a TypeError.\nProbably got a None to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('we did not find anything useful returning empty list')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got none, so returning empty list')
        return []
    except Exception as e:
        # print(e)
        print(str(e))
        return []

def main():
    how_many = 10
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('urls.txt','w') as f:
        f.write(str(data))
if __name__ == '__main__':
    main()
        


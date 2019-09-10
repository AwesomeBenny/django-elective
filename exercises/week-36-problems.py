import urllib.request
import re

def fibonacci_sequence(num):
    fibonacci_list = [1, 1]
    for i in range(2, num+1):
        result = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(result)
    return fibonacci_list

def count_html_tags(website, tag):
    file = urllib.request.urlopen(website)
    data = file.read().decode('utf-8')
    return data.count(tag)

def find_count_tags(website):
    dic = {}
    file = urllib.request.urlopen(website)
    data = file.read().decode('utf-8')
    for match in re.findall('</[A-Za-z0-9=".? -]*>', data):
        key = match[2:(len(match)-1)]
        if dic.get(key): dic[key] += 1
        else: dic[key] = 1
    return dic

if __name__ == "__main__":
    print(fibonacci_sequence(9))
    print(count_html_tags("https://kea.dk/", "</div>"))
    print(find_count_tags("https://kea.dk/"))
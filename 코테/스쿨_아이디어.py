import re


def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'[.]+[.]+[.]', '.', new_id)
    new_id = re.sub(r'[.]+[.]', '.', new_id)
    new_id = new_id.strip('.')

    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id

    return answer

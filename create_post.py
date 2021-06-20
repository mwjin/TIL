#!/usr/bin/env python3
import json

from pathlib import Path


def load_json(json_path: Path) -> dict:
    json_data = dict()

    if json_path.exists():
        with json_path.open() as json_f:
            json_data = json.load(json_f)

    return json_data


def print_contents(cursor: dict):
    print('===== Table of Categories =====')
    print('.')
    print('..')
    for category in cursor:
        if category != '_posts':
            print(f'- {category}')


def print_order(list_: list):
    for i, item in enumerate(list_):
        print(f'{i + 1}. {item}')


def print_err(msg: str):
    print(f'[ERROR] {msg}')


def count_contents(cursor: dict) -> int:
    cnt = len(cursor)
    posts = cursor.get('_posts')

    if posts:
        cnt -= 1  # Do not count '_posts'
        cnt += len(posts)  # Count the number of posts instead

    return cnt


def choose_directory(cursor: dict) -> str:
    while True:
        directory = input('Choose the directory (Enter "q" to quit): ')
        if (directory in cursor) \
           or directory == '.' \
           or directory == '..' \
           or directory == 'q':
            return directory
        print_err(f'The directory "{directory}" does not exists.')


def choose_mode(only_file: True) -> str:
    valid_mode = {'f', 'q'} if only_file else {'f', 'd', 'q'}
    while True:
        mode = input('Choose the mode (file(f), quit(q)): ') if only_file else\
               input('Choose the mode (file(f), directory(d), quit(q)): ')
        if mode in valid_mode:
            return mode
        print_err(f'The mode "{mode}" is invalid.')


def choose_index(list_) -> int:
    if list_:
        while True:
            try:
                index = int(input(f'Choose the index (1 ~ f{len(list_) + 1}: '))
                if 1 <= index <= len(list_) + 1:
                    return index
                else:
                    print_err(f'Your index "{index}" is out of the valid '
                              f'range.')
            except ValueError:
                print_err(f'The index "{index}" is invalid. '
                          f'It may be not a number')

    return 1


def make_filename(title: str) -> str:
    filename = '_'.join(title.lower().split())
    return filename


def get_title(file_path: str) -> str:
    title = ''
    with file_path.open() as f:
        for line in f:
            if line.startswith('title'):
                title = line.strip().split(': ')[1]
                break
    return title


def get_parent_title(curr_path: list) -> (str, str):
    parent_title = ''
    grand_title = ''
    
    if len(curr_path) > 1:  # Ignore 'posts' directory
        parent_dir_path = Path('/'.join(curr_path))
        parent_filename = curr_path[-1]
        parent_file_path = parent_dir_path / f'{parent_filename}.md'
        parent_title = get_title(parent_file_path)

        if len(curr_path) > 2:
            grand_dir_path = parent_dir_path.parent
            grand_filename = curr_path[-2]
            grand_file_path = grand_dir_path / f'{grand_filename}.md'
            grand_title = get_title(grand_file_path)

    return (parent_title, grand_title)


def create_file(curr_path: list, nav_order: int,
                create_dir: bool = False) -> str:
    title = input('Enter the file title: ')
    parent_title, grand_title = get_parent_title(curr_path)
    filename = make_filename(title)
    file_dir_path = Path('/'.join(curr_path))

    if create_dir:
        file_dir_path = file_dir_path / filename
        file_dir_path.mkdir()

    file_path = file_dir_path / f'{filename}.md'

    with file_path.open('w') as post_f:
        print('---', file=post_f)
        print('layout: default', file=post_f)
        print(f'title: {title}', file=post_f)
        if parent_title:
            print(f'parent: {parent_title}', file=post_f)
        if grand_title:
            print(f'grand_parent: {grand_title}', file=post_f)
        print(f'nav_order: {nav_order}', file=post_f)
        if create_dir:
            print('has_children: true', file=post_f)
            print(f'permalink: /{str(file_dir_path)}', file=post_f)
        print('---', file=post_f)
        print(f'# {title}', file=post_f)

    return filename


def cli(cursor: dict, curr_path: list):
    cursor_stack = [cursor]
    only_file = False

    while True:
        print(f'Current location: /{"/".join(curr_path)}')
        content_cnt = count_contents(cursor)
        print(f'Current No. Contents: {content_cnt}')
        print_contents(cursor)

        if len(curr_path) == 3:
            only_file = True
        directory = choose_directory(cursor)

        if directory == '.':
            mode = choose_mode(only_file)
            if mode == 'f':
                if cursor.get('_posts') is None:
                    cursor['_posts'] = []
                posts = cursor['_posts']

                if posts:
                    print('===== Current posts =====')
                    print_order(posts)

                filename = create_file(curr_path, content_cnt + 1)
                cursor['_posts'].append(filename)
            elif mode == 'd':
                dirs = list(filter(lambda x: x != '_posts', cursor.keys()))

                if dirs:
                    print('===== Current directories =====')
                    print_order(dirs)

                dirname = create_file(curr_path, content_cnt + 1, True)
                cursor[dirname] = {}
        elif directory == '..':
            if len(curr_path) == 1:
                print_err('Current location is the root.')
            else:
                cursor_stack.pop()
                curr_path.pop()
                cursor = cursor_stack[-1]
        elif directory == 'q':
            break
        else:
            cursor = cursor.get(directory)
            cursor_stack.append(cursor)
            curr_path.append(directory)
        print()


def main():
    json_path = Path('posts.json')
    json_data = load_json(json_path)
    cursor = json_data['posts']  # 'posts' is a root directory.
    curr_path = ['posts']

    try:
        cli(cursor, curr_path)
    except:
        print_err('Some error has occurred.')
        raise
    finally:
        with json_path.open('w') as json_f:
            json.dump(json_data, json_f, indent=2)


if __name__ == '__main__':
    main()

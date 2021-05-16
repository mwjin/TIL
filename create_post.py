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


def count_contents(cursor: dict) -> int:
    cnt = len(cursor)
    posts = cursor.get('_posts')

    if posts:
        cnt -= 1
        cnt += len(posts)

    return cnt


def choose_directory(cursor: dict) -> str:
    while True:
        directory = input('Choose the directory (Enter "q" to quit): ')
        if (directory in cursor) \
           or directory == '.' \
           or directory == '..' \
           or directory == 'q':
            return directory
        print(f'The directory "{directory}" does not exists.')


def choose_mode() -> str:
    valid_mode = {'f', 'd', 'q'}
    while True:
        mode = input('Choose the mode (file(f), directory(d), quit(q)): ')
        if mode in valid_mode:
            return mode
        print(f'The mode "{mode}" is invalid.')


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


def get_parent_title(curr_path: list) -> str:
    parent_title = ''
    if curr_path:
        parent_dir_path = Path('/'.join(curr_path))
        parent_filename = curr_path[-1]
        parent_file_path = parent_dir_path / f'{parent_filename}.md'
        parent_title = get_title(parent_file_path)
    return parent_title


def create_file(curr_path: list, nav_order: int, create_dir: bool = False) -> str:
    title = input('Enter the file title: ')
    parent_title = get_parent_title(curr_path)
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
        print(f'nav_order: {nav_order}', file=post_f)
        if create_dir:
            print('has_children: true', file=post_f)
            print(f'permalink: /{str(file_dir_path)}', file=post_f)
        print('---', file=post_f)
        print(f'# {title}', file=post_f)

    return filename


def cli(cursor: dict):
    cursor_stack = [cursor]
    curr_path = []

    while True:
        print(f'Current location: /{"/".join(curr_path)}')
        content_cnt = count_contents(cursor)
        print(f'Current No. Contents: {content_cnt}')
        print_contents(cursor)

        directory = choose_directory(cursor)
        if directory == '.':
            mode = choose_mode()
            if mode == 'f':
                filename = create_file(curr_path, content_cnt + 1)
                if cursor.get('_posts') is None:
                    cursor['_posts'] = []
                cursor['_posts'].append(filename)
            elif mode == 'd':
                dirname = create_file(curr_path, content_cnt + 1, True)
                cursor[dirname] = {}
        elif directory == '..':
            if len(curr_path) == 0:
                print('Current location is the root.')
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

    try:
        cli(json_data)
    except:
        print('Some error has occured.')
        raise
    finally:
        with json_path.open('w') as json_f:
            json.dump(json_data, json_f)


if __name__ == '__main__':
    main()

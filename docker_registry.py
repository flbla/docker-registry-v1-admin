# @Author: flbla
# @Date:   2018-08-17T13:31:22+02:00
# @Filename: docker_registry.py
# @Last modified by:   flbla
# @Last modified time: 2018-08-17T13:41:17+02:00

#!/usr/bin/python3

import argparse
import requests
from requests.auth import HTTPBasicAuth
import json
import sys
import re
import logging
import logging.handlers

def list_repositories(url):
    '''
    List all repositories in server
    '''
    repositories = []
    response = requests.get(url + "/v1/search").json()['results']
    for repository in response:
        repositories.append((repository['name']))
    return repositories

def search_repositories(url, search):
    '''
    Search repositories in server
    '''
    repositories = []
    response = requests.get(url + "/v1/search?q=" + search).json()['results']
    for repository in response:
        repositories.append(repository['name'])
    return repositories

def list_tags(url, repository):
    '''
    List all tags in repo
    '''
    response = requests.get(url + "/v1/repositories/" + repository  + "/tags").json()
    return response

def delete_tag(url, tag, repository):
    '''
    Delete tag
    '''
    response = requests.delete(url + "/v1/repositories/" + repository  + "/tags/" + tag).text
    return response

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''Manage Docker Registry V1;''')
    parser.add_argument('manage', metavar='delete/list/tag/search', nargs=1, choices=['delete', 'tag', 'list', 'search'], help='What do you want to do?')
    parser.add_argument('-u', metavar='url', nargs=1, help='Docker registry URL', required=True)
    parser.add_argument('-t', metavar='tag', help='tag you want to delete')
    parser.add_argument('-r', metavar='repository', nargs=1, help='repository you want to list tag')
    parser.add_argument('-s', metavar='search', nargs=1, help='repository you want to search')
    args = parser.parse_args()
    MANAGE = (vars(args))['manage'][0]
    try:
        TAG = (vars(args))['t']
    except:
        TAG = None
    try:
        URL = (vars(args))['u'][0]
    except:
        TAG = None
    try:
        REPO = (vars(args))['r'][0]
    except:
        REPO = None
    try:
        SEARCH = (vars(args))['s'][0]
    except:
        SEARCH = None

    if MANAGE == "list":
        for repo in list_repositories(URL):
            print(repo)
    elif MANAGE == "tag":
        for name, tag in list_tags(URL, REPO).items():
            print(name + " : " + tag)
    elif MANAGE == "search":
        for repo in search_repositories(URL, SEARCH):
            print(repo)
    elif MANAGE == "delete":
        print(delete_tag(URL, TAG, REPO))

if __name__ == '__main__':
    main()

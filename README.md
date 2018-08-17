# docker-registry-v1-admin

- List repositories
  - docker_registry.py list -u http://localhost:5000
- List tags of a repository
  - docker_registry.py tag -u http://localhost:5000 -r repository_name
- Search a repository
  - docker_registry.py search -u http://localhost:5000 -s search_repo
- Delete a tag
  - docker_registry.py delete -u http://localhost:5000 -r repository_name -t tag_to_delete

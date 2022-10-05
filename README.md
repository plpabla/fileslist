# FilesList project
Create a web app (Django based) to which you can add files location with extra info about their belonging

# Use stories 
## Authentication and Authorization
- [ ] As an user I want to be able to login/logout from each page
- [ ] As an user I want to see if I'm logged in


## Basic functionality 
- [ ] As a logged user I want to see my lists
- [ ] As a logged user I want to see documents on the list I have access
- [ ] As a logged user I want to add a new document in the list
- [ ] As a logged user I want to update a document (next revision)
- [ ] As a logged user I want to see only latest revisions, but have access to older ones
- [ ] As a logged user I want to filter specific document type

## "Document" fields
- Name / description
- File path / link
- Revision: A,B,C
- Latest revision flag
- Document type, e.g. G0, G1, ...
- Tags (0 or more), e.g. C, C++, PHP, Python
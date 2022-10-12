# FilesList project
Create a web app (Django based) to which you can add files location with extra info about their belonging

# Use stories 

## Authentication and Authorization
- [ ] As an user I want to be able to login/logout from each page
- [ ] As an user I want to see if I'm logged in


## Basic functionality 

### Documents
- [ ] As a logged user I want to create a new document entry
- [ ] As a logged user I want to edit existing document
- [ ] As a logged user I want to update a document (add next revision to existing one)
- [ ] As a logged user I want to see by default only latest revisions
- [ ] As a logged user I can see document revision history
- [ ] As a logged user I want to filter specific document type
- [ ] As a logged user I want to filter specific tags

### Lists
- [ ] As a logged user I want to see my lists
- [ ] As a logged user I want to see documents on the list I have access
- [ ] As a logged user I want to add a new document into the list
- [ ] As a logged user I want to add an existing document into the list

### Exporting
- [ ] As a logged user I want to export given list to csv format
- [ ] As a logged user I can define to export only latest revisions
- [ ] As a logged user I can define to export all revisions
- [ ] As a logged user I can define to export only documents with given doc. type
- [ ] As a logged user I can define to export only documents with given doc. types (multiple selection)
- [ ] As a logged user I can define to export only documents with given tags (multiple selection)

## "Document" fields
- Name / description
- File path / link
- Revision: A,B,C
- Latest revision flag
- Document type, e.g. G0, G1, ...
- Tags (0 or more), e.g. C, C++, PHP, Python
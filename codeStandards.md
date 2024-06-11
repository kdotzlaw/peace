# Coding Standards

## File System Structure

## Frontend
- Elements that are in focus/being displayed will have the 'focused' class, while hidden elements will have the 'unfocused' class
- All classes are done in camel case
- All react components are capitalized

### React Practices

### HTML Practices

### CSS Practices

## Backend

### Flask Practices
- All API endpoints should go into `app.py`
- All API endpoints should be organized by functionality (ie all endpoints relating to Logins should be next to each other)
- All API endpoints should use **camelCase** where applicable
- All API endpoints should be prefaced by **preconditions**, **postconditions**, and a **description of the method**
- All comments outside a method should be done using `''' '''`. Comments inside an endpoint can use `#` if they are single lined
### Python Practices
- All database methods go into `db.py`
- Database methods should be organized by functionality (ie all Volunteer methods should be next to each other)
- All database methods should be prefaced by **preconditions** (input), **postconditions** (output), and a **description of the method**
- All database function names should be in **camelCase**
- All Python MySQL queries need to be **prepared statements** to ensure security. A valid  query is: `cursor.execute("SELECT * FROM <tableName> WHERE <colName> = ?", username)`
- All comments outside of a method should be done using `''' '''`. Comments inside a method can use `#` if they are single lined

### MySQL Practices
- All comments outside a method should be done using `/* */`. Comments inside a method can use `//` if they are single lined
- All MySQL keywords should be capitalized
- Table names should all be **lowercase** (ie volunteers, jobs), column names should all be prefaced by the first letter of their table (ie vMember)
- Multi-word column names should be camelCase (ie vChurchBackground)
- All MySQL files should be in `/sql` but should not be used for any reason, as the database is already built and hosted elsewhere

### Testing Practices
- Database testing will be done with **unittest**
- API testing will be done using **flask_unittest**
- Database and API test methods need to be in seperate classes, but can be in the same file
- Unit tests should only test **one** component/method
- All tests should be prefaced with **pass conditions** and a **description of what is being tested**
- Tests should include **negative testing** (ie tests that ensure incorrect input fails correctly)
- Unit tests should be **ordered by compontent** (ie all Volunteer tests should be next to each other in test suite)


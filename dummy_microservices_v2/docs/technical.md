## Overview

This document outlines the technical architecture for an AI-based IDE built Python and Typescript. The system follows a modular microservices architecture. 

Application is for displaying current possition of ISS. It shows latitiude nad longtitied along country name over which ISS is at the moment. If it is over the cee or ocen appropriate infor should be displayed intead of country.

Application requires authorisation. User must register and then log in to access information about ISS position.

For getting ISS position applition use  'http://api.open-notify.org/iss-now.json'. For getting country name based on geocoordinates application use 'https://nominatim.openstreetmap.org/reverse'.

## Busines logic:
    - User logs in to frontend app, request is send to beckend app. Backend app to authorise user send request to authorisation app
    - Authorisation app send response to backend app, backend app send response to frontend app.- If user is authorised to access resources api response will be dsiplayed.

## Technology Stack

- **Backend Framework**: FastApi
- **Frontend Framework**: React
- **Database**: SqLite
- **Backend Language**: Python
- **Frontend Language**: Typescript
- **Authentication**: Django, Django OAuth Toolkit, JWT + OAuth2

## Core Modules

### 1. Frontend app located in frontend folder
    - Use html and css located in template folder to generate React template
### 2. Backend app located in backend folder
### 3. Authorisation app located in oauth folder

## Code generation:
- Code should be OOP with SOLID principles
- Business logic should be separated from controllers and placed in service classes
- There should be only one class per file
- SqLite database should be generated based on data model and save in project folder
- Docker files with nginx vhosts must be generated for every microservice
- All classes and functions must be documentated
- All classes and functions must be covered with unit test
- After every promp request and response should be logged to docs/prompt file
- Readme.md file in main directory should be created along Readme.md files in backend, frontend and oath folders
- After evey new prompt all Readme.md files should be updated accordingly

## Future Considerations

1. **Developer Experience**
   - Interactive documentation
   - API playground
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
- **Authentication**: Django OAuth Toolkit, JWT + OAuth2

## Core Modules

## Core Modules

### 1. Frontend app located in frontend folder
    - Use template located in template folder
### 2. Backend app located in backend folder
### 3. Authorisation app located in oauth folder

## Future Considerations

1. **Developer Experience**
   - Interactive documentation
   - API playground
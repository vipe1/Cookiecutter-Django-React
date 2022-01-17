# Change Log
## v 0.4.0
**Added**
- Implemented user authentication with JWT*

**Used Djoser and djangorestframework Simple JWT*

## v 0.3.1
**Changed**
- Restructurized URLs in `backend/config/urls.py`
- Changed default api path from `api/` to `api/v1/`

**Removed**
- Removed users example*

**I've decided that it's useless feature and thus removed it*

## v 0.3.0
**Added**
- Added DRF
- Added optional users example*
- Created User Serializer
- Configured CORS for Frontend
- Moved whole CSS to `frontend/src/App.css`

**Changed**
- Splitted Apps in config for more clear and tidy look
- Changed Frontend port for local development from 80 to 3000**
- Moved local development part of README to LOCAL_DEVELOPMENT.MD

**Users list view on Backend and users list display on Frontend*\
***Frontend container should now refresh on every change when saved*

## v 0.2.1
**Added**
- Added environmental generating hook

**Changed**
- Changed local docker-compose file volumes naming

## v 0.2
**Added**
- Implemented custom user model for Django
- Added simple environmental variables for Postgres and Django

**Changed**
- Changed database to PostgreSQL 14.1

## v 0.1 (Initial version)
- **Created base for the project.**
- **Generated simple Django and React projects without any content**
- **Created Dockerfiles and docker-compose config files**

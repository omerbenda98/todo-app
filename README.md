# Flask Todo App

A simple todo application built with Flask that helps track tasks and test system connectivity.

## Features

- Add, delete, and toggle tasks
- Monitor app status
- Check database connectivity

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/omerbenda98/todo-app.git
   cd todo-app
   ```

## Running with Docker Compose

1. **Start the application:**

   ```sh
   docker-compose up -d
   ```

   This command will:

   - Build the application container
   - Start the Nginx reverse proxy
   - Initialize the MySQL database
   - Set up required networks and volumes

2. **Open your browser and navigate to:**

   - [http://localhost](http://localhost)
   - [http://127.0.0.1](http://127.0.0.1)

3. **To stop the application:**

   ```sh
   docker-compose down
   ```

4. **To remove all data including the database volume:**
   ```sh
   docker-compose down -v
   ```

## Container Structure

- **Nginx:** Reverse proxy handling requests on port 80
- **App:** Flask application serving the todo functionality
- **Database:** MySQL 8.0 for data persistence

## Rebuilding the Application

To rebuild the application after making changes:

```sh
docker-compose up -d --build
```

# Task Manager Web Application using Django

The Task Manager Web Application is a full-stack web project developed using the Django framework. It allows users to efficiently manage their daily tasks, organize activities, and keep track of completed items. Users can add, edit, and delete tasks, set specific dates and times for each task, and mark tasks as completed.

## Key Features

- **User Authentication:** Implemented user registration and login system using Django's built-in authentication module to provide secure access to the application.
- **Task Management:** Users can add new tasks with details such as activity, date, time, and description, facilitating efficient task organization.
- **Real-Time Validation:** Incorporated real-time validation to ensure users input valid dates, times, and activity details, reducing input errors.
- **Search Functionality:** Implemented a search feature that enables users to quickly find specific tasks based on keywords.
- **Completed Task List:** Provided an additional feature to move completed tasks to a separate "Done List," enhancing task completion tracking.
- **Rate Us:** Integrated a "Rate Us" functionality, allowing users to provide feedback and ratings for the application.

## Technologies Used

- **Django Framework:** Utilized Django to build the backend and handle server-side logic.
- **HTML, CSS, JavaScript:** Designed and developed the frontend user interface for an interactive and responsive user experience.
- **SQLite:** Used SQLite database to store user data and task information securely.

## Installation and Usage

1. Clone the repository to your local machine.

```
git clone https://github.com/your-username/task-manager.git
```

2. Navigate to the project directory.

```
cd task-manager
```

3. Install the django.

```
pip install django
```

4. Set up the database by running migrations.

```
python manage.py migrate
```

5. Create a superuser to access the Django admin panel (optional).

```
python manage.py createsuperuser
```

6. Run the development server.

```
python manage.py runserver
```

7. Access the application in your web browser at `http://localhost:8000/`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments

Special thanks to the Django community for providing excellent documentation and resources.

Happy task managing!

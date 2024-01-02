# CSCK542 Team Assignment

This is a NodeJS API solution that uses the “mysql2” and “express” packages. The API solution has 5 API calls that call the following stored procedures:

- AssignCoursesToTeacher(teacherIdParam, courseIdParam)
- EnrollInCourse(courseIdParam, userIdParam)
- ListAvailableCourses()
- PassFailStudent(enrolmentIdParam, markParam, teacherIdParam)
- ToggleCourseAvailability(courseIdParam, courseavailableParam, userIdParam)

## Project Structure

```
CSCK542 Team Assignment
├── app
|   ├── src
│       ├── index.js
│       ├── api
│       │   ├── AssignCoursesToTeacher.js
│       │   ├── EnrollInCourse.js
│       │   ├── ListAvailableCourses.js
│       │   ├── PassFailStudent.js
│       │   └── ToggleCourseAvailability.js
│       ├── database
│       │   └── db.js
│       └── routes
│           └── api.js
|   ├── package.json
├── database
|   ├── mydb_courses.sql
|   ├── mydb_enrolements.sql
|   ├── mydb_procedures.sql
|   ├── mydb_roles.sql
|   └── mydb_users.sql
└── README.md
```

## How to clone the repo
1) Browse to your repo folder
2) type the following command
```console
git clone https://github.com/Bowside/CSCK542_TeamAssignment.git
```

## How to Setup the database
1) Open MySQL workbench,
2) Connect to a local server,
3) Create schema called "mydb" and select charaset "utf8",
4) Once the schema is created, select "mydb" schema, right click and select "Set as Default Schema",
5) Under main menu bar, select "Server" and under the pull down menu, select "Data Import",
6) In “Data Import”, select “Import from dump project folder” and navigate to the \database folder in the repo,
7) Click on “Load folder content” button,
8) Click “Start import” button and you should have the database the in your “Schemas” list. If you don’t see the database, try refreshing the database connection.

## API Setup

1. Open the commond prompt window and locate the app folder,
2. Run `npm install` to install the dependencies,
3. Ensure 0 vulnerabilities observed,
4. Create a `.env` file in the root directory and add your MySQL database credentials:

```
#Environment Configuration
PORT = your_port

#DB Configuration
DB_HOST = your_sqlserver
DB_USER = your_sqlusername
DB_PASSWORD = your_sqlpassword
DB_NAME = your_sqldatabase
DB_PORT =3306

```

4. Run `npm run start` to start the server

## API Endpoints

- `POST /api/assignCoursesToTeacher`: Assigns a course to a teacher. The request body should be a JSON object with the properties `teacherId`, `courseId` and `userId`.

- `POST /api/enrollInCourse`: Enrolls a user in a course. The request body should be a JSON object with the properties `courseId` and `userId`.

- `GET /api/listAvailableCourses`: Lists all available courses.

- `POST /api/passFailStudent`: Passes or fails a student. The request body should be a JSON object with the properties `enrolmentId`, `mark`, and `teacherId`.

- `POST /api/toggleCourseAvailability`: Toggles the availability of a course. The request body should be a JSON object with the properties `courseId`, `courseavailable`, and `userId`.

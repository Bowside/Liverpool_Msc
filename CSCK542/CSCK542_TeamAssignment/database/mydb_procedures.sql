-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Dec 11, 2023 at 11:57 AM
-- Server version: 8.1.0
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--

DELIMITER $$
--
-- Procedures
--
CREATE PROCEDURE `AssignCoursesToTeacher` (IN `teacherIdParam` INT, IN `courseIdParam` INT, IN `userIdParam` INT)   BEGIN
    DECLARE `userRole` VARCHAR(45);
    SET `userRole` = (SELECT roles.Role
                    FROM users
                    LEFT JOIN roles ON users.RoleID = roles.RoleID
                    WHERE users.UserID = UserIdParam);
    SET `teacherRole` = (SELECT roles.Role
                    FROM users
                    LEFT JOIN roles ON users.RoleID = roles.RoleID
                    WHERE users.UserID = teacherIdParam);

    IF `userRole` = 'Admin' and `teacherRole` = 'Teacher'
    THEN
        -- Update the TeacherID for the specified courses
        UPDATE courses
        SET TeacherID = `teacherIdParam`
        WHERE CourseID = `courseIdParam`;

        SELECT 'Courses assigned to teacher successfully.' AS Message;
    ELSE
        SELECT 'You do not have the necessary privileges to perform this operation, or you are not assigning a teacher.' AS Message;
    END IF;
END$$

CREATE PROCEDURE `EnrollInCourse` (IN `courseIdParam` INT, IN `userIdParam` INT)   BEGIN
    DECLARE `userRole` VARCHAR(45);
    SET `userRole` = (SELECT roles.Role
                      FROM users
                      LEFT JOIN roles ON users.RoleID = roles.RoleID
                      WHERE users.UserID = UserIdParam);

    IF `userRole` = 'Student' THEN
        -- Check if the student is not already enrolled in the course
        IF NOT EXISTS (SELECT 1 FROM enrolments WHERE CourseID = `courseIdParam` AND UserID = `userIdParam`) THEN
            -- Enroll the student in the course
            INSERT INTO enrolments (CourseID, UserID) VALUES (`courseIdParam`, `userIdParam`);
            SELECT 'Enrollment successful.' AS Message;
        ELSE
            SELECT 'You are already enrolled in this course.' AS Message;
        END IF;
    ELSE
        SELECT 'You do not have the necessary privileges to perform this operation.' AS Message;
    END IF;
END$$

CREATE PROCEDURE `ListAvailableCourses` ()   BEGIN
    -- Select available courses with teacher's name
    SELECT c.Title AS CourseTitle
    , u.Name AS TeacherName
    FROM courses c
    LEFT JOIN users u 
    ON c.TeacherID = u.UserID
    WHERE c.isAvailable = 1;
END$$

CREATE PROCEDURE `PassFailStudent` (IN `enrolmentIdParam` INT, IN `markParam` INT, IN `teacherIdParam` INT)   BEGIN
    DECLARE `userRole` VARCHAR(45);
    SET `userRole` = (SELECT roles.Role
                    FROM users
                    LEFT JOIN roles ON users.RoleID = roles.RoleID
                    WHERE users.UserID = teacherIdParam);

    IF `userRole` = 'Teacher' THEN
        -- Update the student's mark
        UPDATE enrolments
        SET Mark = `markParam`
        WHERE EnrolmentID = `enrolmentIdParam`;

        SELECT 'Student mark updated successfully.' AS Message;
    ELSE
        SELECT 'You do not have the necessary privileges to perform this operation.' AS Message;
    END IF;
END$$

CREATE PROCEDURE `ToggleCourseAvailability` (IN `courseIdParam` INT, IN `courseavailableParam` INT, IN `userIdParam` INT)   BEGIN
    DECLARE `userRole` VARCHAR(45);
    -- Get the role of the user executing the procedure
    set `userRole` = (SELECT roles.Role
                   	 FROM users
                   	 LEFT JOIN roles 
                   	 ON users.RoleID = roles.RoleID
                     WHERE users.UserID = UserIdParam);
    
    -- Check if the user has admin privileges
    IF `userRole` = 'Admin' 
    THEN
        -- Update the course availability
        UPDATE courses
        SET isAvailable = courseavailableParam
        WHERE CourseID = courseIdParam;
        
        SELECT CONCAT('Course availability updated successfully for CourseID ', courseIdParam) AS Message;
    ELSE
        SELECT 'You do not have the necessary privileges to perform this operation.' AS Message;
    END IF;
END$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

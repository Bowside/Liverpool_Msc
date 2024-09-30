-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Nov 27, 2023 at 05:03 PM
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
-- Database: `college_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_id` int NOT NULL,
  `course_code` varchar(10) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `course_desc` varchar(255) NOT NULL,
  `inserttimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `insertedby_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `courseassignment`
--

CREATE TABLE `courseassignment` (
  `courseassignment_id` int NOT NULL,
  `teacher_id` int NOT NULL,
  `course_id` int NOT NULL,
  `year` int NOT NULL,
  `semester` varchar(10) NOT NULL,
  `inserttimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `insertedby_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `role_id` int NOT NULL,
  `role` varchar(25) NOT NULL,
  `inserttimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `studentgrade`
--

CREATE TABLE `studentgrade` (
  `grade_id` int NOT NULL,
  `student_id` int NOT NULL,
  `courseassignment_id` int NOT NULL,
  `grade` varchar(10) NOT NULL,
  `inserttimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `insertedby_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `inserttimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `userrole`
--

CREATE TABLE `userrole` (
  `user_id` int NOT NULL,
  `role_id` int NOT NULL,
  `inserttimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`),
  ADD UNIQUE KEY `ncuidx_course_bk` (`course_code`) USING BTREE;

--
-- Indexes for table `courseassignment`
--
ALTER TABLE `courseassignment`
  ADD PRIMARY KEY (`courseassignment_id`),
  ADD UNIQUE KEY `ncuidx_courseassignment_bk` (`course_id`,`year`,`semester`) USING BTREE,
  ADD KEY `fk_teacher` (`teacher_id`),
  ADD KEY `fk_course` (`course_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`role_id`),
  ADD UNIQUE KEY `ncuidx_role_bk` (`role`) USING BTREE;

--
-- Indexes for table `studentgrade`
--
ALTER TABLE `studentgrade`
  ADD PRIMARY KEY (`grade_id`),
  ADD UNIQUE KEY `ncuidx_studentgrade_bk` (`student_id`,`courseassignment_id`),
  ADD KEY `fk_student` (`student_id`),
  ADD KEY `fk_courseassignment` (`courseassignment_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `ncuidx_user_bk` (`email`);

--
-- Indexes for table `userrole`
--
ALTER TABLE `userrole`
  ADD PRIMARY KEY (`user_id`,`role_id`),
  ADD KEY `fk_role` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `courseassignment`
--
ALTER TABLE `courseassignment`
  MODIFY `courseassignment_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `role_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `studentgrade`
--
ALTER TABLE `studentgrade`
  MODIFY `grade_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `courseassignment`
--
ALTER TABLE `courseassignment`
  ADD CONSTRAINT `fk_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`) ON UPDATE RESTRICT,
  ADD CONSTRAINT `fk_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `user` (`user_id`) ON UPDATE RESTRICT;

--
-- Constraints for table `studentgrade`
--
ALTER TABLE `studentgrade`
  ADD CONSTRAINT `fk_courseassignment` FOREIGN KEY (`courseassignment_id`) REFERENCES `courseassignment` (`courseassignment_id`) ON UPDATE RESTRICT,
  ADD CONSTRAINT `fk_student` FOREIGN KEY (`student_id`) REFERENCES `user` (`user_id`) ON UPDATE RESTRICT;

--
-- Constraints for table `userrole`
--
ALTER TABLE `userrole`
  ADD CONSTRAINT `fk_role` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`) ON UPDATE RESTRICT,
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

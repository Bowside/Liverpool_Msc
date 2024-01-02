const express = require('express');
const router = express.Router();

const assignCoursesToTeacher = require('../api/AssignCoursesToTeacher');
const enrollInCourse = require('../api/EnrollInCourse');
const listAvailableCourses = require('../api/ListAvailableCourses');
const passFailStudent = require('../api/PassFailStudent');
const toggleCourseAvailability = require('../api/ToggleCourseAvailability');

// Common handler function
const handleRequest = async (handler, params, res) => {
  try {
    const result = await handler(...params);
    res.json(result);
  } catch (err) {
    res.status(500).json(err);
    console.error(err);
  }
};

router.post('/assignCoursesToTeacher', (req, res) => {
  handleRequest(assignCoursesToTeacher, [req.query.teacherId, req.query.courseId, req.query.userId], res);
});

router.post('/enrollInCourse', (req, res) => {
  handleRequest(enrollInCourse, [req.query.courseId, req.query.userId], res);
});

router.get('/listAvailableCourses', (req, res) => {
  handleRequest(listAvailableCourses, [], res);
});

router.post('/passFailStudent', (req, res) => {
  handleRequest(passFailStudent, [req.query.enrolmentId, req.query.mark, req.query.teacherId], res);
});

router.post('/toggleCourseAvailability', (req, res) => {
  handleRequest(toggleCourseAvailability, [req.query.courseId, req.query.courseavailable, req.query.userId], res);
});

module.exports = router;
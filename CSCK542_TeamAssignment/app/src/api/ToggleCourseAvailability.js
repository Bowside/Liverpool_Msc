const db = require('../database/db');

module.exports = async function toggleCourseAvailability(courseId, courseavailable, userId) {

    result = await db.query('CALL ToggleCourseAvailability(?, ?, ?)', [courseId, courseavailable, userId])
    //return only the query response
    return result[0];
};
const db = require('../database/db.js');

module.exports = async function assignCoursesToTeacher(teacherId, courseId, userId) {

    result = await db.query('CALL AssignCoursesToTeacher(?, ?, ?)', [teacherId, courseId, userId])
    //return only the query response
    return result[0];
};
const db = require('../database/db.js');

module.exports = async function EnrollInCourse(courseId, userId) {

    result = await db.query('CALL EnrollInCourse(?, ?)', [courseId, userId]);
    //return only the query response
    return result[0];

};
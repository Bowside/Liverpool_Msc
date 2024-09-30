const db = require('../database/db.js');

module.exports = async function listAvailableCourses() {
    
    result = await db.query('CALL ListAvailableCourses()')
    //return only the query response
    return result[0];
};

const db = require('../database/db');

module.exports =  async function passFailStudent(enrolmentId, mark, teacherId) {
    
    result = await db.query('CALL PassFailStudent(?, ?, ?)', [enrolmentId, mark, teacherId])
    //return only the query response
    return result[0];
};
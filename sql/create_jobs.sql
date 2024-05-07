CREATE TABLE jobs(
	jID INT NOT NULL AUTO_INCREMENT,
	vID INT,
	jName VARCHAR(255) NOT NULL,
	jMinistry VARCHAR(255) NOT NULL, /*can be comma seperated list*/
	jDesc VARCHAR(1024), /*streamlined duties+description*/
	jRecurring BOOLEAN, 
	jFrequency VARCHAR (255), /*like 1x per week*/
	jDate DATETIME, /*specific date, for one time events*/
	jLocation VARCHAR(255),
	jSkills VARCHAR (1024), /*as a comma seperated list*/
	jLocked BOOLEAN, /*is this locked for specific church members, yes or no*/
	jLockedCriteria VARCHAR(255), /* if locked, why?*/
	jFilled BOOLEAN,
	jActive BOOLEAN, /*if not active, job is considered archived*/
	jVName VARCHAR(255), /*Volunteer Name*/
	PRIMARY KEY(jID)
);

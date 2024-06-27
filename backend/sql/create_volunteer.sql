CREATE TABLE volunteers(
	vID INT NOT NULL AUTO_INCREMENT,
	vFName VARCHAR(255) NOT NULL,
	vLName VARCHAR(255) NOT NULL,
	vEmail VARCHAR(255) NOT NULL UNIQUE,
	vPhone VARCHAR(50),
	vBirthday DATE,
	vMarriageStatus ENUM ('single', 'engaged', 'married'),
	vPartner VARCHAR(255),
	vAnniversary DATE,
	vChurchBackground VARCHAR(1024),
	vDateBaptism DATE,
	vDateConfirmation DATE,
	vListChildren VARCHAR(255),
	vHistory VARCHAR(1024),
	vSkills VARCHAR (1024),
	vInterests VARCHAR (1024),
	vGifts VARCHAR (1024),
	vHobbies VARCHAR (1024),
	PRIMARY KEY (vID),
	CONSTRAINT vFullname UNIQUE(vFName,vLName)
);


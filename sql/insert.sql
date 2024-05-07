INSERT INTO volunteers VALUES('Bob','Bobbington','bob@bobbington.com','',STR_TO_DATE('1990, 8, 10','%M, %D, %y'),'married','Sally E Bobbington','',STR_TO_DATE('2010,10,10','%m,%d,%Y'),NULL,'','','');
/
INSERT INTO volunteers VALUES('Sally','Bobbington','sally@bobbington.com','',TO_DATE('10/17/1990','MM/DD/YY'),'married','Bob B Bobbington',TO_DATE('10/10/2010','MM/DD/YY'),NULL,'','','');
/
INSERT INTO jobs VALUES(1, 'Greeter','Fellowship','Greet the People','yes','1x per week', NULL, 'Church','Friendly, Sociable','no','','yes','yes','Bob Bobbington');
/
INSERT INTO jobs VALUES(0, 'Usher','Fellowship','Usher the people','yes','1x per week', NULL, 'Church','Friendly, Sociable','yes','Active Church Member','no','yes','');

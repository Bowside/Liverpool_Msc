DELETE FROM `studentgrade`;
DELETE FROM `courseassignment`;
DELETE FROM `userrole`;
DELETE FROM `role`;
DELETE FROM `course`;
DELETE FROM `user`;

-- #############
-- # U S E R S #
-- #############

-- Disable Identity Insert for user table
-- SET IDENTITY_INSERT `user` ON;

-- Insert admin users
INSERT INTO `user` (`user_id`, `username`, `email`, `name`, `surname`, `password`, `inserttimestamp`) VALUES
  (1, 'gandalf', 'gandalf@wizards.org', 'Gandalf', 'The Grey', 'youshallnotpass', CURRENT_TIMESTAMP),
  (2, 'sauron', 'sauron@wizards.org', 'Sauron', 'Dark Lord', 'oneringtoRuleThemAll', CURRENT_TIMESTAMP);

-- Insert teachers
INSERT INTO `user` (`user_id`, `username`, `email`, `name`, `surname`, `password`, `inserttimestamp`) VALUES
  (3, 'elrond', 'elrond@rivendell.edu', 'Elrond', 'Half-elven', 'r1v3nd3llC0unc1l', CURRENT_TIMESTAMP),
  (4, 'legolas', 'legolas@lothlorien.edu', 'Legolas', 'Greenleaf', 'b0wAnd4rr0w', CURRENT_TIMESTAMP),
  (5, 'glorfindel', 'glorfindel@rivendell.edu', 'Glorfindel', 'Goldenflower', '3lvenL1ght', CURRENT_TIMESTAMP),
  (6, 'celeborn', 'celeborn@lothlorien.edu', 'Celeborn', 'Lord of Lothlorien', 'L0thl0r13nRul3s', CURRENT_TIMESTAMP),
  (7, 'thranduil', 'thranduil@mirkwood.edu', 'Thranduil', 'Elvenking', 'M1rkwwdR3alm', CURRENT_TIMESTAMP),
  (8, 'galadriel', 'galadriel@lothlorien.edu', 'Galadriel', 'Lady of Lothlorien', 'L0thl0r13nQu33n', CURRENT_TIMESTAMP),
  (9, 'haldir', 'haldir@lothlorien.edu', 'Haldir', 'Marchwarden', 'Gu@rd1@n0fL0thl0r13n', CURRENT_TIMESTAMP);

-- Insert students
INSERT INTO `user` (`user_id`, `username`, `email`, `name`, `surname`, `password`, `inserttimestamp`) VALUES
  (10, 'frodo', 'frodo@fellowship.org', 'Frodo', 'Baggins', 'R1ngB3ar3r', CURRENT_TIMESTAMP),
  (11, 'samwise', 'samwise@fellowship.org', 'Samwise', 'Gamgee', 'P0tato3s', CURRENT_TIMESTAMP),
  (12, 'aragorn', 'aragorn@fellowship.org', 'Aragorn', 'Elessar', 'Str1d3r', CURRENT_TIMESTAMP),
  (13, 'legolas', 'legolas@fellowship.org', 'Legolas', 'Greenleaf', '3lvenArr0w', CURRENT_TIMESTAMP),
  (14, 'gimli', 'gimli@fellowship.org', 'Gimli', 'Son of Gloin', '4x3And4H@lf', CURRENT_TIMESTAMP),
  (15, 'boromir', 'boromir@fellowship.org', 'Boromir', 'Son of Denethor', 'G0nd0rG0nds', CURRENT_TIMESTAMP),
  (16, 'merry', 'merry@fellowship.org', 'Meriadoc', 'Brandybuck', 'P1p3w33d', CURRENT_TIMESTAMP),
  (17, 'pippin', 'pippin@fellowship.org', 'Peregrin', 'Took', 'T00kishAdventur3', CURRENT_TIMESTAMP),
  (18, 'faramir', 'faramir@gondor.edu', 'Faramir', 'Son of Denethor', 'St3w@rd0fG0nd0r', CURRENT_TIMESTAMP),
  (19, 'eowyn', 'eowyn@rohan.edu', 'Eowyn', 'Shieldmaiden', 'D3f13r0fR0h@n', CURRENT_TIMESTAMP),
  (20, 'bilbo', 'bilbo@bagend.edu', 'Bilbo', 'Baggins', 'El3v3nT1ngs', CURRENT_TIMESTAMP),
  (21, 'arwen', 'arwen@rivendell.edu', 'Arwen', 'Undomiel', 'L0v3InM1ddl3Earth', CURRENT_TIMESTAMP),
  (22, 'gollum', 'gollum@caves.org', 'Gollum', 'Smeagol', 'Pr3c1ous', CURRENT_TIMESTAMP),
  (23, 'radagast', 'radagast@wizard.org', 'Radagast', 'The Brown', 'B1rdWh1sp3r3r', CURRENT_TIMESTAMP),
  (24, 'gimli2', 'gimli2@fellowship.org', 'Gimli', 'Son of Gloin', 'Ax3AndB3@rd', CURRENT_TIMESTAMP),
  (25, 'rosie', 'rosie@hobbiton.org', 'Rosie', 'Cotton', 'G@rd3nQu33n', CURRENT_TIMESTAMP),
  (26, 'glorfindel2', 'glorfindel2@rivendell.edu', 'Glorfindel', 'Goldenflower', '3lvenH0rs3L0rd', CURRENT_TIMESTAMP),
  (27, 'haldir2', 'haldir2@lothlorien.edu', 'Haldir', 'Marchwarden', 'Guard1an0fG0ld3nW00d', CURRENT_TIMESTAMP),
  (28, 'thorin', 'thorin@erebor.edu', 'Thorin', 'Oakenshield', 'H0bbitFr13nd', CURRENT_TIMESTAMP),
  (29, 'bifur', 'bifur@erebor.edu', 'Bifur', 'Dwarf', '3r3b0rB3ard', CURRENT_TIMESTAMP);


-- Disable Identity Insert for user table
-- SET IDENTITY_INSERT `user` OFF;

-- #############
-- # R O L E S #
-- #############
-- Enable Identity Insert for role table
-- SET IDENTITY_INSERT `role` ON;

-- Insert roles
INSERT INTO `role` (`role_id`, `role`, `inserttimestamp`) VALUES 
  (1, 'Admin', CURRENT_TIMESTAMP),
  (2, 'Teacher', CURRENT_TIMESTAMP),
  (3, 'Student', CURRENT_TIMESTAMP);

-- Disable Identity Insert for role table
-- SET IDENTITY_INSERT `role` OFF;

-- Assign roles to admin users
INSERT INTO `userrole` (`user_id`, `role_id`, `inserttimestamp`) VALUES
  (1, 1, CURRENT_TIMESTAMP), -- Admin1
  (2, 1, CURRENT_TIMESTAMP); -- Admin2
  
-- Assign roles to teachers
INSERT INTO `userrole` (`user_id`, `role_id`, `inserttimestamp`) VALUES
  (3, 2, CURRENT_TIMESTAMP), -- Teacher1
  (4, 2, CURRENT_TIMESTAMP), -- Teacher2
  (5, 2, CURRENT_TIMESTAMP), -- Teacher3
  (6, 2, CURRENT_TIMESTAMP), -- Teacher4
  (7, 2, CURRENT_TIMESTAMP), -- Teacher5
  (8, 2, CURRENT_TIMESTAMP), -- Teacher6
  (9, 2, CURRENT_TIMESTAMP); -- Teacher7
  
 -- Assign roles to students
INSERT INTO `userrole` (`user_id`, `role_id`, `inserttimestamp`) VALUES
  (10, 3, CURRENT_TIMESTAMP), -- Frodo
  (11, 3, CURRENT_TIMESTAMP), -- Samwise
  (12, 3, CURRENT_TIMESTAMP), -- Aragorn
  (13, 3, CURRENT_TIMESTAMP), -- Legolas
  (14, 3, CURRENT_TIMESTAMP), -- Gimli
  (15, 3, CURRENT_TIMESTAMP), -- Boromir
  (16, 3, CURRENT_TIMESTAMP), -- Merry
  (17, 3, CURRENT_TIMESTAMP), -- Pippin
  (18, 3, CURRENT_TIMESTAMP), -- Faramir
  (19, 3, CURRENT_TIMESTAMP), -- Eowyn
  (20, 3, CURRENT_TIMESTAMP), -- Bilbo
  (21, 3, CURRENT_TIMESTAMP), -- Arwen
  (22, 3, CURRENT_TIMESTAMP), -- Gollum
  (23, 3, CURRENT_TIMESTAMP), -- Radagast
  (24, 3, CURRENT_TIMESTAMP), -- Gimli2
  (25, 3, CURRENT_TIMESTAMP), -- Rosie
  (26, 3, CURRENT_TIMESTAMP), -- Glorfindel2
  (27, 3, CURRENT_TIMESTAMP), -- Haldir2
  (28, 3, CURRENT_TIMESTAMP), -- Thorin
  (29, 3, CURRENT_TIMESTAMP); -- Bifur

-- #################
-- # C O U R S E S #
-- #################

-- Enable Identity Insert for course table
-- SET IDENTITY_INSERT `course` ON;

-- Insert courses
INSERT INTO `course` (`course_id`, `course_code`, `course_name`, `course_desc`, `insertedby_id`, `inserttimestamp`) VALUES
  (1, 'HP101', 'Introduction to Potions', 'Basic principles of potion-making', 1, CURRENT_TIMESTAMP),
  (2, 'HP201', 'Advanced Charms', 'Mastery of charm spells', 1, CURRENT_TIMESTAMP),
  (3, 'HP301', 'Defense Against the Dark Arts', 'Protection from dark creatures and spells', 1, CURRENT_TIMESTAMP),
  (4, 'HP401', 'Transfiguration', 'Changing the form or appearance of an object', 1, CURRENT_TIMESTAMP),
  (5, 'HP501', 'Herbology', 'Study of magical plants and their uses', 1, CURRENT_TIMESTAMP),
  (6, 'HP601', 'Magical Creatures', 'Understanding and handling magical creatures', 1, CURRENT_TIMESTAMP),
  (7, 'HP701', 'Divination', 'Predicting the future through various magical methods', 1, CURRENT_TIMESTAMP),
  (8, 'HP801', 'Ancient Runes', 'Study of magical runic symbols', 1, CURRENT_TIMESTAMP),
  (9, 'HP901', 'Alchemy', 'Magical science of transmuting substances', 1, CURRENT_TIMESTAMP),
  (10, 'HP1001', 'History of Magic', 'Chronicles magical events throughout history', 1, CURRENT_TIMESTAMP);

-- Disable Identity Insert for course table
-- SET IDENTITY_INSERT `course` OFF;

-- Insert course assignments for teachers
INSERT INTO `courseassignment` (`courseassignment_id`, `teacher_id`, `course_id`, `year`, `semester`, `insertedby_id`, `inserttimestamp`) VALUES
  (1, 3, 1, 2023, 'Spring', 1, CURRENT_TIMESTAMP), -- Elrond teaching Introduction to Potions
  (2, 4, 2, 2023, 'Spring', 1, CURRENT_TIMESTAMP), -- Legolas teaching Advanced Charms
  (3, 5, 3, 2023, 'Spring', 1, CURRENT_TIMESTAMP), -- Glorfindel teaching Defense Against the Dark Arts
  (4, 6, 4, 2023, 'Spring', 1, CURRENT_TIMESTAMP), -- Celeborn teaching Transfiguration
  (5, 7, 5, 2023, 'Spring', 1, CURRENT_TIMESTAMP), -- Thranduil teaching Herbology
  (6, 8, 6, 2023, 'Spring', 1, CURRENT_TIMESTAMP), -- Galadriel teaching Magical Creatures
  (7, 9, 7, 2023, 'Spring', 1, CURRENT_TIMESTAMP); -- Haldir teaching Divination
  
-- ###############
-- # G R A D E S #
-- ###############
  
-- Insert grades for students
INSERT INTO `studentgrade` (`student_id`, `courseassignment_id`, `grade`, `insertedby_id`, `inserttimestamp`) VALUES
  (10, 1, 'A', 3, CURRENT_TIMESTAMP),   -- Frodo's grade for Introduction to Potions (Assigned by Elrond)
  (11, 2, 'B', 4, CURRENT_TIMESTAMP),   -- Samwise's grade for Advanced Charms (Assigned by Legolas)
  (12, 3, 'A-', 5, CURRENT_TIMESTAMP),  -- Aragorn's grade for Defense Against the Dark Arts (Assigned by Glorfindel)
  (13, 4, 'B+', 6, CURRENT_TIMESTAMP),  -- Legolas's grade for Transfiguration (Assigned by Celeborn)
  (14, 5, 'A', 7, CURRENT_TIMESTAMP),   -- Gimli's grade for Herbology (Assigned by Thranduil)
  (15, 6, 'C', 8, CURRENT_TIMESTAMP),   -- Boromir's grade for Magical Creatures (Assigned by Galadriel)
  (16, 7, 'B-', 9, CURRENT_TIMESTAMP),  -- Merry's grade for Divination (Assigned by Haldir)
  (17, 1, 'A', 3, CURRENT_TIMESTAMP),   -- Pippin's grade for Ancient Runes (Assigned by Elrond)
  (18, 2, 'A', 4, CURRENT_TIMESTAMP),   -- Faramir's grade for Alchemy (Assigned by Legolas)
  (19, 3, 'B', 5, CURRENT_TIMESTAMP),  -- Eowyn's grade for History of Magic (Assigned by Glorfindel)
  (20, 4, 'C+', 6, CURRENT_TIMESTAMP),  -- Bilbo's grade for Introduction to Potions (Assigned by Celeborn)
  (21, 5, 'A', 7, CURRENT_TIMESTAMP),   -- Arwen's grade for Advanced Charms (Assigned by Thranduil)
  (22, 6, 'A-', 8, CURRENT_TIMESTAMP),  -- Gollum's grade for Defense Against the Dark Arts (Assigned by Galadriel)
  (23, 7, 'B', 9, CURRENT_TIMESTAMP),   -- Radagast's grade for Transfiguration (Assigned by Haldir)
  (24, 1, 'B+', 3, CURRENT_TIMESTAMP),  -- Gimli2's grade for Herbology (Assigned by Elrond)
  (25, 2, 'A', 4, CURRENT_TIMESTAMP),   -- Rosie's grade for Magical Creatures (Assigned by Legolas)
  (26, 3, 'C-', 5, CURRENT_TIMESTAMP),  -- Glorfindel2's grade for Divination (Assigned by Glorfindel)
  (27, 4, 'B', 6, CURRENT_TIMESTAMP),   -- Haldir2's grade for Ancient Runes (Assigned by Celeborn)
  (28, 5, 'A', 7, CURRENT_TIMESTAMP),   -- Thorin's grade for Alchemy (Assigned by Thranduil)
  (29, 6, 'A-', 8, CURRENT_TIMESTAMP); -- Bifur's grade for History of Magic (Assigned by Galadriel)
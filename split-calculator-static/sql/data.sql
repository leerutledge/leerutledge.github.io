INSERT INTO users (username,fullname,email,admin,password,earnings)
VALUES
	('leerutledge', 'Lee Rutledge', 'leektproductions@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('ahmedowda', 'Ahmed Owda', 'aowdamusic@gmail.com', 1, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('spencerlee', 'Spencer Lee', 'spencerleellc@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('sabumabanda', 'Sabum Abanda', 'sabangvision@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('jamesvincent', 'James Vincent', 'liftoffbeatz@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('kevinstephens', 'Kevin Stephens', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('pierrecornilliat', 'Pierre Cornilliat', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('tazjayecarpenter', 'Tazjaye Carpenter', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('briannagandara', 'Brianna Gandara', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('andrewmesadieu', 'Andrew Mesadieu', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('garyking', 'Gary King', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('ammarmohamed', 'Ammar Mohamed', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00),
	('christopherterrell', 'Christopher Terrell', '???@gmail.com', 0, 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',0.00);

INSERT INTO artists (name,owner)
VALUES
	('Kakuyon','leerutledge'),
	('Shotta Spence','spencerlee'),
	('Spencer Lee','spencerlee'),
	('SaBang','sabumabanda'),
	('LiftOFF','jamesvincent'),
	('kevth.wz','kevinstephens'),
	('Seph Pierre','pierrecornilliat'),
	('TJ Lavish','tazjayecarpenter'),
	('Veni Love','briannagandara'),
	('Benny Francs','andrewmesadieu'),
	('G. King','garyking'),
	('Ammar Mo','ammarmohamed'),
	('RELLA','christopherterrell');

INSERT INTO projects (projectid,releasedate,title,coverart)
VALUES
	(1, '23 August, 2019', 'Castling : Sky', 'skytestcolor.jpg'),
	(2, '30 July, 2019', 'Washed Away', 'skytestcolor.jpg'),
	(3, '25 October, 2018', 'Rich', 'RICH-K.jpg'),
	(4, '2 June, 2018', 'Super Blue Blood', 'sbb-f1.jpg'),
	(5, '10 April, 2018', 'I Understand', 'i-understand.jpg'),
	(6, '14 March, 2018', 'Maria', 'mariamac-vodka.jpg'),
	(7, '26 February, 2018', 'Mirage', 'img007.jpg'),
	(8, '18 February, 2018', 'Celebration', 'cele2Y.jpg'),
	(9, '9 February, 2018', 'Funny', 'fvnny2.jpg'),
	(10, '27 November, 2017', 'Conscience', 'CONSCIENCE_COVER1.jpg'),
	(11, '28 October, 2017', 'Fire', 'fye7.jpg'),
	(12, '6 January, 2017', 'Now Go And Flourish', 'nowgo-front.jpg');

INSERT INTO tracks (
	trackid,projectid,title,tracknumber,upc,isrc,
	owner0,ownership0,owner1,ownership1,owner2,ownership2,owner3,ownership3,owner4,ownership4
)
VALUES
	(1,1,'Early Morning Sun',1,5054526289024,'GBKPL1961564','kevinstephens',0.25,'leerutledge',0.25,'spencerlee',0.25,'sabumabanda',0.25,'',0.00),
	(2,1,'Lavish By Nature',2,5054526289024,'QM24S1915718','tazjayecarpenter',0.00,'leerutledge',0.00,'jamesvincent',0.00,'',0.00,'',0.00),
	(3,1,'Hypnosis',3,5054526289024,'GBKPL1961562','kevinstephens',0.00,'briannagandara',0.00,'leerutledge',0.00,'',0.00,'',0.00),
	(4,1,'Washed Away',4,5054526289024,'GBKPL1957887','leerutledge',0.00,'spencerlee',0.00,'',0.00,'',0.00,'',0.00),
	(5,1,'Miss Starry',5,5054526289024,'GBKPL1961563','leerutledge',0.00,'andrewmesadieu',0.00,'',0.00,'',0.00,'',0.00),
	(6,1,'Genevieve',6,5054526289024,'GBKPL1961565','leerutledge',0.00,'sabumabanda',0.00,'',0.00,'',0.00,'',0.00),
	(7,2,'Washed Away',1,5054526539419,'GBKPL1957887','leerutledge',0.00,'spencerlee',0.00,'',0.00,'',0.00,'',0.00),
	(8,3,'Rich',1,193436034081,'QM24S1837076','leerutledge',0.75,'jamesvincent',0.25,'',0.00,'',0.00,'',0.00),
	(9,4,'Super Blue Blood',1,843357150369,'QM24S1813413','leerutledge',0.00,'',0.00,'',0.00,'',0.00,'',0.00),
	(10,5,'I Understand',1,843357131719,'QM24S1806666','leerutledge',0.00,'garyking',0.00,'',0.00,'',0.00,'',0.00),
	(11,6,'Maria',1,843357118864,'QM24S1803144','leerutledge',0.00,'ammarmohamed',0.00,'',0.00,'',0.00,'',0.00),
	(12,7,'Mirage',1,843357113753,'QM24S1801935','leerutledge',0.00,'pierrecornilliat',0.00,'',0.00,'',0.00,'',0.00),
	(13,8,'Celebration',1,843357112374,'QM24S1801189','leerutledge',0.00,'christopherterrell',0.00,'pierrecornilliat',0.00,'',0.00,'',0.00),
	(14,9,'Funny',1,843357110097,'QM24S1800705','leerutledge',0.00,'',0.00,'',0.00,'',0.00,'',0.00),
	(15,10,'Conscience',1,800739236349,'CAENV1747800','leerutledge',0.00,'spencerlee',0.00,'',0.00,'',0.00,'',0.00),
	(16,11,'Fire',1,0885014833376,'SEYOK1772983','leerutledge',0.00,'ammarmohamed',0.00,'',0.00,'',0.00,'',0.00),
	(17,12,'Sugar',1,193436064231,'SEYOK1670909','leerutledge',0.00,'kevinstephens',0.00,'',0.00,'',0.00,'',0.00),
	(18,12,'Troubled Water',2,193436064231,'SEYOK1670910','leerutledge',0.00,'sabumabanda',0.00,'pierrecornilliat',0.00,'jamesvincent',0.00,'',0.00),
	(19,12,'Leverage',3,193436064231,'SEYOK1670911','leerutledge',0.00,'',0.00,'',0.00,'',0.00,'',0.00),
	(20,12,'Nirvana',4,193436064231,'SEYOK1670912','leerutledge',0.00,'ammarmohamed',0.00,'',0.00,'',0.00,'',0.00),
	(21,12,'Trough / Crest... (Interlude)',5,193436064231,'SEYOK1670913','leerutledge',0.00,'spencerlee',0.00,'sabumabanda',0.00,'pierrecornilliat',0.00,'',0.00),
	(22,12,'Molt',6,193436064231,'SEYOK1670914','leerutledge',0.00,'',0.00,'',0.00,'',0.00,'',0.00),
	(23,12,'Sunny Soon',7,193436064231,'SEYOK1670915','leerutledge',0.00,'spencerlee',0.00,'',0.00,'',0.00,'',0.00),
	(24,12,'I See Ya',8,193436064231,'SEYOK1670916','leerutledge',0.00,'',0.00,'',0.00,'',0.00,'',0.00),
	(25,12,'Perfect',9,193436064231,'SEYOK1670917','leerutledge',0.00,'jamesvincent',0.00,'',0.00,'',0.00,'',0.00),
	(26,12,'Ethereal',10,193436064231,'SEYOK1670919','leerutledge',0.00,'',0.00,'',0.00,'',0.00,'',0.00);

INSERT INTO earnings (trackid,payperiodstart,amount)
VALUES
	(1,'Jul',0.00),
	(2,'Jul',0.00),
	(3,'Jul',0.00),
	(4,'Jul',0.00),
	(5,'Jul',0.00),
	(6,'Jul',0.00),
	(7,'Jul',0.00),
	(8,'Jul',0.00),
	(9,'Jul',0.00),
	(10,'Jul',0.00),
	(11,'Jul',0.00),
	(12,'Jul',0.00),
	(13,'Jul',0.00),
	(14,'Jul',0.00),
	(15,'Jul',0.00),
	(16,'Jul',0.00),
	(17,'Jul',0.00),
	(18,'Jul',0.00),
	(19,'Jul',0.00),
	(20,'Jul',0.00),
	(21,'Jul',0.00),
	(22,'Jul',0.00),
	(23,'Jul',0.00),
	(24,'Jul',0.00),
	(25,'Jul',0.00),
	(26,'Jul',0.00),
	(1,'Aug',0.99),
	(2,'Aug',0.99),
	(3,'Aug',0.99),
	(4,'Aug',0.99),
	(5,'Aug',0.99),
	(6,'Aug',0.99),
	(7,'Aug',0.99),
	(8,'Aug',0.99),
	(9,'Aug',0.99),
	(10,'Aug',0.99),
	(11,'Aug',0.99),
	(12,'Aug',0.99),
	(13,'Aug',0.99),
	(14,'Aug',0.99),
	(15,'Aug',0.99),
	(16,'Aug',0.99),
	(17,'Aug',0.99),
	(18,'Aug',0.99),
	(19,'Aug',0.99),
	(20,'Aug',0.99),
	(21,'Aug',0.99),
	(22,'Aug',0.99),
	(23,'Aug',0.99),
	(24,'Aug',0.99),
	(25,'Aug',0.99),
	(26,'Aug',0.99);

-- MAY NOT NEED THIS, BOOL MAYBE KEPT IN REACT TO PERSIST SELECTED STATE AND HAVE THAT EFFECT WHAT  EARNINGS ARE DISPLAYED
INSERT INTO payperiods (payperiodstart,selected)
VALUES
	('Jun',0),
	('Jul',0),
	('Aug',1),
	('Sep',0);

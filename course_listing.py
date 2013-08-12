from collections import namedtuple

Course = namedtuple('Course','dept course_num title adv_vers')

courses = []

intro_honors = Course('COMS',1007,'Honors Intro to CS', None)
intro_basic = Course('COMS',1004,'Intro to CS and Prog in Java',intro_honors)
dsa_honors = Course('COMS',3137,'Honors Data Structures', None)
dsa_basic = Course('COMS',3134,'Data Structures in Java', dsa_honors)
stat_adv = Course('SIEO',3600,'Prob and Stats',None)
stat_basic = Course('SIEO',4150,'Prob and Stats',stat_adv)

courses.append(intro_basic)
courses.append(dsa_basic)
courses.append(Course('COMS',3157,'Advanced Programming',None))
courses.append(Course('COMS',3203,'Discrete Math',None))
courses.append(Course('COMS',3251,'Computational Linear Algebra',None))
courses.append(Course('COMS',3261,'CS Theory',None))
courses.append(Course('CSEE',3827,'Fundamentals of Computer Systems',None))
courses.append(stat_basic)

adv_courses = set()

aml_advanced = Course('COMS',6772,'Adv Machine Learning', None)
aml_basic = Course('COMS',4772,'Adv Machine Learning', aml_advanced)

adv_courses.add(aml_basic)
adv_courses.add(aml_advanced)
adv_courses.add(Course('CSOR',4231,'Analysis of Algorithms, I',None))
adv_courses.add(Course('COMS',4236,'Intro to Computational Complexity',None))
adv_courses.add(Course('COMS',4241,'Numerical Algorithms and Complexity',None))
adv_courses.add(Course('COMS',4203,'Graph Theory',None))
adv_courses.add(Course('COMS',4205,'Combinatorial Theory',None))
adv_courses.add(Course('COMS',4252,'Intro to Computational Learning Theory',None))
adv_courses.add(Course('COMS',4261,'Intro to Cryptography',None))
adv_courses.add(Course('COMS',4281,'Intro to Quantum Computing',None))
adv_courses.add(Course('COMS',4444,'Prog and Problem Solving',None))
adv_courses.add(Course('COMS',4771,'Machine Learning',None))
adv_courses.add(Course('COMS',4995,'Math Foundations of Machine Learning',None))
adv_courses.add(Course('COMS',6232,'Analysis of Algorithms II',None))
adv_courses.add(Course('COMS',6261,'Advanced Cryptography',None))
adv_courses.add(Course('COMS',6717,'Information Theory',None))
adv_courses.add(Course('COMS',6998,'Approximation Algorithms',None))
adv_courses.add(Course('COMS',3902,'Undergraduate Thesis',None))
adv_courses.add(Course('COMS',3998,'Projects in CS',None))
adv_courses.add(Course('COMS',4901,'Projects in CS',None))
adv_courses.add(Course('COMS',6901,'Projects in CS',None))

adv_courses.add(Course('COMS',4115,'Prog Languages and Translators',None))
adv_courses.add(Course('COMS',4118,'Operating Systems',None))
adv_courses.add(Course('CSEE',4119,'Computer Networks',None))

adv_courses.add(Course('COMS',4995,'Special projects in CS I',None))
adv_courses.add(Course('COMS',4996,'Special projects in CS II',None))

adv_courses.add(Course('CSEE',4824,'Computer Architecture',None))
adv_courses.add(Course('EECS',4340,'Computer Hardware Design',None))
adv_courses.add(Course('CSEE',4823,'Advanced Logic Design',None))
adv_courses.add(Course('CSEE',4840,'Embedded Systems',None))
adv_courses.add(Course('COMS',4130,'Parallel Programming',None))
adv_courses.add(Course('CSEE',6824,'Parallel Computer Architecture',None))
adv_courses.add(Course('CSEE',6847,'Distributed Embedded Systems',None))
adv_courses.add(Course('COMS',6861,'CAD of Digital Systems',None))
adv_courses.add(Course('CSEE',6868,'System-on-Chip Platforms',None))

adv_courses.add(Course('COMS',4701,'Artificial Intelligence',None))
adv_courses.add(Course('COMS',4705,'Natural Language Processing',None))
adv_courses.add(Course('COMS',4706,'Spoken Language Processing',None))
adv_courses.add(Course('COMS',4731,'Computer Vision',None))
adv_courses.add(Course('COMS',4733,'Computational Aspects of Robotics',None))
adv_courses.add(Course('COMS',4165,'Computational Techniques in Pixel Processing',None))
adv_courses.add(Course('COMS',4252,'Intro to Computational Learning Theory',None))
adv_courses.add(Course('COMS',6998,'Topics in CS I',None))
adv_courses.add(Course('COMS',6999,'Topics in CS II',None))
adv_courses.add(Course('COMS',4111,'Introduction to Databases',None))
adv_courses.add(Course('COMS',4160,'Computer Graphics',None))
adv_courses.add(Course('COMS',4170,'User Interface Design',None))
adv_courses.add(Course('COMS',4999,'Computing and the Humanities',None))

adv_courses.add(Course('COMS',4167,'Computer Animation',None))
adv_courses.add(Course('COMS',4162,'Advanced Computer Graphics',None))
adv_courses.add(Course('COMS',4172,'3D User Interfaces and Augmented Reality',None))
adv_courses.add(Course('COMS',4735,'Visual Interfaces to Computers',None))
adv_courses.add(Course('COMS',4995,'Special Topics in CS (Video Game Technology and Design)',None))

adv_courses.add(Course('ECBM',4060,'Introduction to Genomic Information',None))

adv_courses.add(Course('COMS',4117,'Compilers and Interpreters',None))
adv_courses.add(Course('COMS',4112,'Database System Implementation',None))
adv_courses.add(Course('CSEE',4140,'Networking Laboratory',None))
adv_courses.add(Course('COMS',4156,'Advanced Software Engineering',None))
adv_courses.add(Course('COMS',4180,'Network Security',None))
adv_courses.add(Course('COMS',4187,'Security Architecture and Engineering',None))
adv_courses.add(Course('COMS',4460,'Principles of Innovation and Entrepreneurship',None))
adv_courses.add(Course('COMS',4560,'Introduction to Computer Applications in Health Care and Biomedicine',None))

adv_courses.add(Course('COMS',4725,'Knowledge Representation and Reasoning',None))

bio_adv = Course('COMS',6737,'Biometrics',None)
bio_basic = Course('COMS',4737,'Biometrics',bio_adv)

adv_courses.add(Course('COMS',4737,'Biometrics',None))
adv_courses.add(Course('CBMF',4761,'Computational Genomics',None))
adv_courses.add(Course('COMS',6121,'Reliable Software',None))

adv_courses.add(Course('COMS',4910,'Curricular Practical Training',None))
adv_courses.add(Course('COMS',6732,'Computational Imaging',None))

adv_courses.add(bio_basic)
adv_courses.add(bio_adv)

adv_courses.add(Course('COMS',6900,'Tutorial in CS',None))
adv_courses.add(Course('COMS',6902,'Thesis',None))
class Mentor(object):

	def __init__(self, gender, course_code, student_id, interests, preferences=[]):
		self.gender = gender
		self.course_code = course_code
		self.student_id = student_id
		self.interests = interests
		self.preferences = []

	def __str__(self):
		return f"Mentor: {self.student_id}"

	def get_gender(self):
		return self.gender

	def get_course_code(self):
		return self.course_code

	def get_student_id(self):
		return self.student_id

	def get_interests(self):
		return self.interests


	def calc_pair_score(self, mentee, gender_score, course_code_score, interest_score):
		pairing_score = 0

		if self.gender == mentee.get_gender():
			pairing_score += gender_score

		if self.course_code == mentee.get_course_code():
			pairing_score += course_code_score

		for interest in self.interests:
			if interest in mentee.get_interests():
				pairing_score += interest_score

		return(mentee, pairing_score)



	def set_preferences(self, menteeList, gender_weight, course_code_weight, interest_weight):
		gender_score = 1.5 * gender_weight
		course_code_score = 1.5 * course_code_weight
		interest_score = 1 * interest_weight

		for mentee in menteeList:
			pairing = self.calc_pair_score(mentee, gender_score, course_code_score, interest_score)
			self.preferences.append(pairing)

		#sort preferences list
		self.preferences.sort(key=lambda x: x[1], reverse=True)

		#unpack preference tuples
		for i, mentee in enumerate(self.preferences):
			self.preferences[i] = mentee[0]



	def print_preferences(self):
		for s in self.preferences:
			print(s)
		print("\n")







class Mentee(object):

	def __init__(self, gender, course_code, student_id, interests, preferences=[]):
		self.gender = gender
		self.course_code = course_code
		self.student_id = student_id
		self.interests = interests
		self.preferences = []

	def __str__(self):
		return f"Mentee: {self.student_id}"

	def get_gender(self):
		return self.gender

	def get_course_code(self):
		return self.course_code

	def get_student_id(self):
		return self.student_id

	def get_interests(self):
		return self.interests


	def calc_pair_score(self, mentor, gender_score, course_code_score, interest_score):
		pairing_score = 0

		if self.gender == mentor.get_gender():
			pairing_score += gender_score

		if self.course_code == mentor.get_course_code():
			pairing_score += course_code_score

		for interest in self.interests:
			if interest in mentor.get_interests():
				pairing_score += interest_score

		return(mentor, pairing_score)


	def set_preferences(self, mentorList, gender_weight, course_code_weight, interest_weight):
		gender_score = 1.5 * gender_weight
		course_code_score = 1.5 * course_code_weight
		interest_score = 1 * interest_weight

		for mentor in mentorList:
			pairing = self.calc_pair_score(mentor, gender_score, course_code_score, interest_score)
			self.preferences.append(pairing)


		#sort preferences list
		self.preferences.sort(key=lambda x: x[1], reverse=True)

		#unpack preference tuples
		for i, mentee in enumerate(self.preferences):
			self.preferences[i] = mentee[0]


	def print_preferences(self):
		for s in self.preferences:
			print(s)
		print("\n")



def main():
	mentor1 = Mentor("male", "CASE", 1, ["sailing", "skiing", "gaming"])
	# mentor1 = Mentor("other", "nothing", 1, ["boo", "boo", "boo"])
	mentor2 = Mentor("female", "POPD", 2, ["eating", "skiing", "shoes"])
	mentor3 = Mentor("male", "CASE", 3, ["football", "programming", "pints"])
	mentor4 = Mentor("male", "CASE", 4, ["tennis", "basketball", "pints"])

	mentorList = [mentor1, mentor2, mentor3, mentor4]

	mentee1 = Mentee("male", "CASE", 1, ["sailing", "skiing", "gaming"])
	mentee2 = Mentee("female", "POPD", 2, ["eating", "skiing", "shoes"])
	mentee3 = Mentee("male", "CASE", 3, ["football", "programming", "pints"])
	mentee4 = Mentee("male", "CASE", 4, ["tennis", "basketball", "pints"])

	menteeList = [mentee1, mentee2, mentee3, mentee4]

	# mentor1.set_preferences(menteeList, 1, 1, 1)

	# mentor1.print_preferences()

	for mentee in menteeList:
		mentee.set_preferences(mentorList, 1, 1, 1)
		print("Mentee:")
		print(mentee)
		print("preferences:")
		mentee.print_preferences()


if __name__ == '__main__':
	main()
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

	def calc_pair_score(self, mentee, gender_weight, course_code_weight, interest_weight):
		gender_score = 1.5 * gender_weight
		course_code_score = 1.5 * course_code_weight
		interest_score = 1 * interest_weight

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
		for mentee in menteeList:
			pairing = self.calc_pair_score(mentee, gender_weight, course_code_weight, interest_weight)
			self.preferences.append(pairing)

		print(self.preferences)
		#sort preferences
		#unpack preference tuples







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



def main():
	mentor1 = Mentor("other", "nothing", 1, ["boo", "boo", "boo"])
	mentor2 = Mentor("female", "POPD", 2, ["eating", "skiing", "shoes"])
	mentor3 = Mentor("male", "CASE", 3, ["football", "programming", "pints"])
	mentor4 = Mentor("male", "CASE", 4, ["tennis", "basketball", "pints"])

	mentorList = [mentor1, mentor2, mentor3, mentor4]


if __name__ == '__main__':
	main()
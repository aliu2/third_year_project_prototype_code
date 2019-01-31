class Mentor(object):

	def __init__(self, gender, course_code, student_id, interests):
		self.gender = gender
		self.course_code = course_code
		self.student_id = student_id
		self.interests = interests

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



class Mentee(object):

	def __init__(self, gender, course_code, student_id, interests):
		self.gender = gender
		self.course_code = course_code
		self.student_id = student_id
		self.interests = interests

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
	pass


if __name__ == '__main__':
	main()
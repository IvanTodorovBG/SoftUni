from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def test_init_with_empty_course(self):
        student = Student("Test")
        self.assertEqual("Test", student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_course(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        self.assertEqual("Test", student.name)
        self.assertEqual({"TestCourse": ["TestNote1"]}, student.courses)

    def test_enroll_if_course_name_already_in_courses(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        result = student.enroll("TestCourse", ["TestNote2", "TestNote3"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"TestCourse": ["TestNote1", "TestNote2", "TestNote3"]}, student.courses)

    def test_enroll_if_course_name_and_notes_added(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        result = student.enroll("Test", ["TestNote2", "TestNote3"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"TestCourse": ["TestNote1"], "Test": ["TestNote2", "TestNote3"]}, student.courses)

    def test_enroll_if_course_name_and_notes_added_test(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        result = student.enroll("Test", ["TestNote2", "TestNote3"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"TestCourse": ["TestNote1"], "Test": ["TestNote2", "TestNote3"]}, student.courses)

    def test_enroll_if_course_not_exist(self):
        student = Student("Test")
        result = student.enroll("Test", ["n1, n2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Test": []}, student.courses)

    def test_add_notes_course_not_found_raise(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        with self.assertRaises(Exception) as ex:
            student.add_notes("Test", ["TestNote2", "TestNote3"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_updated_notes_in_course_name(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        result = student.add_notes("TestCourse", "TestNote2")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"TestCourse": ["TestNote1", "TestNote2"]}, student.courses)

    def test_leave_course_course_not_found_raise(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        with self.assertRaises(Exception) as ex:
            student.leave_course("Test")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_remove_course_from_courses(self):
        student = Student("Test", {"TestCourse": ["TestNote1"]})
        result = student.leave_course("TestCourse")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, student.courses)


if __name__ == "__main__":
    main()

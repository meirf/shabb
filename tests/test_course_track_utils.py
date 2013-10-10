#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from matching_utils.track_utils import is_fulfilled
from matching_utils.course_utils import get_convert_to_course
from cs_course_pool.course_listing import Course
from track_requirements.course_structures import CourseReq


class TestTrackUtils(unittest.TestCase):

    def setUp(self):
        self.req_a = CourseReq("4901", ["COMS"], "Projects in CS", True, 2)
        self.intro_honors = Course('COMS', 1007, 'Honors Intro to CS', None)
        self.req_b = CourseReq("6232", ["COMS"], "Analysis of Algorithms II")
        self.ana_algo_II = Course('COMS', 6232, 'Analysis of Algorithms II', None)

    def test_single_fulfillment_return_correct_type(self):
        self.assertIsInstance(is_fulfilled(self.intro_honors, self.req_a) , int)

    def test_single_fulfillment_result_non_match(self):
        self.assertFalse(is_fulfilled(self.intro_honors, self.req_a))

    def test_single_fulfillment_result_match(self):
        self.assertTrue(is_fulfilled(self.ana_algo_II, self.req_b))


class TestCourseUtil(unittest.TestCase):

    def setUp(self):
        self.course_from_input = "COMS1004IntrotoCSandProginJava"

    def test_get_convert_to_course(self):
        self.assertIsInstance(get_convert_to_course(self.course_from_input), Course)

    def test_course_fields(self):
        crs = get_convert_to_course(self.course_from_input)
        self.assertEqual(crs.dept, 'COMS')
        self.assertEqual(crs.course_num, '1004')
        self.assertEqual(crs.title, 'IntrotoCSandProginJava')
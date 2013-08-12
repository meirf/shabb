#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from course_listing import courses, adv_courses
from course_structures import CourseReq, TrackSubsection
from course_rules import found_sec_A_courses, found_sec_B_courses
from url_manipulation.url_decode import get_url_param_mappings

class CourseTest(unittest.TestCase):

    def test_course_import(self):
        self.failUnless(len(courses) > 0 and len(adv_courses) > 0)


class TestGeneralCourseReq(unittest.TestCase):

    def test_course_req_creation(self):
        self.failUnless(CourseReq('41', ['COMS']))


class TestTrackSubsection(unittest.TestCase):

    def test_track_subsection(self):
        self.failUnless(TrackSubsection(5))


class TestTrackFull(unittest.TestCase):

    def test_foundations_class_size(self):
        self.failUnless(len(found_sec_A_courses) == 3
                        and len(found_sec_B_courses) == 16)

class TestUrlDecode(unittest.TestCase):

    x = "GET /taken?content=hey!!&a=xyz HTTP/1.1 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language: en-US,en;q=0.8 Host: shobbus.appspot.com Referer: http://shobbus.appspot.com/ User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36 X-Appengine-City: santa clara X-Appengine-Citylatlong: 37.354108,-121.955236 X-Appengine-Country: US X-Appengine-Region: ca"
    def test_url_decode_2_params(self):
        self.failUnless(
            get_url_param_mappings(self.x)=={'content':'hey!!','a':'xyz'}
        )
        
    y = "GET /taken?content=hey HTTP/1.1 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language: en-US,en;q=0.8 Host: shobbus.appspot.com Referer: http://shobbus.appspot.com/ User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36 X-Appengine-City: santa clara X-Appengine-Citylatlong: 37.354108,-121.955236 X-Appengine-Country: US X-Appengine-Region: ca"
    def test_url_decode_1_params(self):
        self.failUnless(
            get_url_param_mappings(self.y)=={'content':'hey'}
        )

    z = "GET /taken? HTTP/1.1 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language: en-US,en;q=0.8 Host: shobbus.appspot.com Referer: http://shobbus.appspot.com/ User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36 X-Appengine-City: santa clara X-Appengine-Citylatlong: 37.354108,-121.955236 X-Appengine-Country: US X-Appengine-Region: ca"
    def test_url_decode_0_params(self):
        self.failUnless(
            get_url_param_mappings(self.z)=={}
        )




def main():
    unittest.main()


if __name__ == '__main__':
    main()
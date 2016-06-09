from junit_xml import TestSuite, TestCase

test_cases1 = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
test_cases2 = [TestCase('Test2', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
test_cases3 = [TestCase('Test3', 'some.class.name', 'abc', 'I am stdout!', 'I am stderr!')]

ts1 = TestSuite("my test suite", test_cases1)
ts2 = TestSuite("my test suite", test_cases2)
ts3 = TestSuite("my test suite", test_cases3)
# pretty printing is on by default but can be disabled using prettyprint=False
print(TestSuite.to_xml_string([ts1]))
print(TestSuite.to_xml_string([ts2]))
print(TestSuite.to_xml_string([ts3]))
# you can also write the XML to a file and not pretty print it
#print(TestSuite.to_xml_string([ts]))
with open('output1.xml', 'w') as f1:
    TestSuite.to_file(f1, [ts1], prettyprint=False)
with open('output2.xml', 'w') as f2:
    TestSuite.to_file(f2, [ts2], prettyprint=False)
##
#with open('output3.xml', 'w') as f3:
#    TestSuite.to_file(f3, [ts3], prettyprint=False)

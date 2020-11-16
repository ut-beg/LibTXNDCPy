import unittest
from NDCRockCoreSample import NDCRockCoreSample

sampleTypeDesc = "Slabbed Core"
formationName = "Eagle Ford"
formationAge = "Permian"

class Test_test_NDCRockCoreSample(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_test_NDCRockCoreSample, self).__init__(*args, **kwargs)

        self.rcs = NDCRockCoreSample()

        self.rcs.sampleTypeDesc = sampleTypeDesc
        self.rcs.formationName = formationName
        self.rcs.formationAge = formationAge

    def test_sampleTypeDesc(self):
        self.failIfEqual(self.rcs.sampleTypeDesc, None, "Sample type should not be null")
        self.failIf((self.rcs.sampleTypeDesc != sampleTypeDesc), "Sample type value is not correct.")

    def test_formationName(self):
        self.failIfEqual(self.rcs.formationName, None, "Formation name should not be null")
        self.failIf((self.rcs.formationName != formationName), "Formation name value is not correct.")

    def test_formationAge(self):
        self.failIfEqual(self.rcs.formationAge, None, "Formation age should not be null")
        self.failIf((self.rcs.formationAge != formationAge), "Formation age value is not correct")

if __name__ == '__main__':
    unittest.main()

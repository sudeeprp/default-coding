import unittest
import scripts.mdcontentcheck as mdchecker

class MDContentCheckTester(unittest.TestCase):
    def test_extract_links_and_words(self):
        md_content = \
        '''
        Hi there this is a link [linked](link.md)
        and this is not (not a link).
        Good luck.
        '''
        links = mdchecker.find_md_links(md_content)
        self.assertTrue('link.md' in links)

    def test_misspellings(self):
        GOOD_SPELL = ['initialize', 'initiate']
        BAD_SPELL = ['innnovate']
        misses = mdchecker.find_misspellings(GOOD_SPELL + BAD_SPELL)
        self.assertTrue(BAD_SPELL[0] in misses and GOOD_SPELL[0] not in misses,
                        msg="Mistakes reported: " + str(misses))

    def test_missinglinks(self):
        PRESENT_FILES = ['test/test_samples/present1.md', 'test/test_samples/present2.md']
        MISSING_FILES = ['missing.md']
        missinglinks = mdchecker.find_missinglinks(PRESENT_FILES + MISSING_FILES)
        self.assertTrue(MISSING_FILES[0] in missinglinks and PRESENT_FILES[0] not in missinglinks,
                        msg="Missing links reported: " + str(missinglinks))


if __name__ == '__main__':
    unittest.main()

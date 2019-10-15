import unittest
import scripts.mdcontentcheck as md_checks


class MarkDownsFunctionalTest(unittest.TestCase):
    def assertOnMistakes(self, filename, mistaken_wordlist, message):
        self.assertFalse(mistaken_wordlist,
                         msg=filename + ': ' + message + ': ' + str(mistaken_wordlist))

    def test_markdowns_spellings_and_links(self):
        md_filelist = md_checks.find_md_files()
        self.assertTrue(md_filelist, msg='No markdown files found')
        for md_filename in md_filelist:
            with open(md_filename) as f:
                md_content = f.read()
            md_extract = md_checks.md_to_links_and_words(md_content)
            self.assertOnMistakes(md_filename, md_checks.find_missinglinks(md_extract['links']),
                                  'Links without files')
            misspellings = md_checks.find_misspellings(md_extract['words'])
            self.assertOnMistakes(md_filename, misspellings,
                                  'Spelling mistakes')


if __name__ == '__main__':
    unittest.main()

import unittest
import scripts.mdcontentcheck as md_checks


def showMistakes(filename, mistaken_list, message):
    if mistaken_list:
        print(filename + ': ' + message + ': ' + str(mistaken_list))


def all_mds_are_spelt_well(md_filelist):
    spelt_well = True
    print("Checking spellings...")
    for md_filename in md_filelist:
        with open(md_filename) as f:
            md_content = f.read()
        md_words = md_checks.remove_nonwords(md_content)
        misspellings = md_checks.find_misspellings(md_words)
        spelt_well &= not misspellings
        showMistakes(md_filename, misspellings, '\n Spelling mistakes')
    print("Done")
    return spelt_well


def all_links_in_mds_are_accessible(md_filelist):
    print("Checking links...", end='')
    for md_filename in md_filelist:
        with open(md_filename) as f:
            md_content = f.read()
        md_links = md_checks.find_md_links(md_content)
        missinglinks = md_checks.find_missinglinks(md_links)
        showMistakes(md_filename, missinglinks, '\n Inaccessible links: ')
    print("Done")
    return not missinglinks


class MarkDownsFunctionalTest(unittest.TestCase):
    def test_markdowns_spellings_and_links(self):
        md_filelist = md_checks.find_md_files()
        self.assertTrue(md_filelist, msg='No markdown files found')
        self.assertTrue(all_mds_are_spelt_well(md_filelist))
        self.assertTrue(all_links_in_mds_are_accessible(md_filelist))


if __name__ == '__main__':
    unittest.main()

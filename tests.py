import unittest
import unittest.mock
import pathlib as pl

from data_handling_utils import get_input

expected_output1 ="""{"sample-sheet-path": "test_folder_1/SampleSheet1.csv", "fastq-names": "[{"file1": "Survey_Covid24/1_S1_R1_001.fastq.gz", "file2": "Survey_Covid24/1_S1_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/2_S2_R1_001.fastq.gz", "file2": "Survey_Covid24/2_S2_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/3_S3_R1_001.fastq.gz", "file2": "Survey_Covid24/3_S3_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/4_S4_R1_001.fastq.gz", "file2": "Survey_Covid24/4_S4_R2_001.fas
tq.gz"}, {"file1": "Survey_Covid24/5_S5_R1_001.fastq.gz", "file2": "Survey_Covid24/5_S5_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/6_S6_R1_001.fastq.gz", "file2": "Survey_Covid24/6_S6_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/7_S7_R1_001.fastq.gz", "file2": "Survey_Covid24/7_S7_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/8
_S8_R1_001.fastq.gz", "file2": "Survey_Covid24/8_S8_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/9_S9_R1_001.fastq.gz", "file2": "Survey_Covid24/9_S9_R2_001.fastq.gz"
}, {"file1": "Survey_Covid24/10_S10_R1_001.fastq.gz", "file2": "Survey_Covid24/10_S10_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/11_S11_R1_001.fastq.gz", "file2":
"Survey_Covid24/11_S11_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/12_S12_R1_001.fastq.gz", "file2": "Survey_Covid24/12_S12_R2_001.fastq.gz"}, {"file1": "Survey_Covi
d24/13_S13_R1_001.fastq.gz", "file2": "Survey_Covid24/13_S13_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/14_S14_R1_001.fastq.gz", "file2": "Survey_Covid24/14_S14_R2_0
01.fastq.gz"}, {"file1": "Survey_Covid24/15_S15_R1_001.fastq.gz", "file2": "Survey_Covid24/15_S15_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/16_S16_R1_001.fastq.gz"
, "file2": "Survey_Covid24/16_S16_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/17_S17_R1_001.fastq.gz", "file2": "Survey_Covid24/17_S17_R2_001.fastq.gz"}, {"file1":
"Survey_Covid24/18_S18_R1_001.fastq.gz", "file2": "Survey_Covid24/18_S18_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/19_S19_R1_001.fastq.gz", "file2": "Survey_Covid2
4/19_S19_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/20_S20_R1_001.fastq.gz", "file2": "Survey_Covid24/20_S20_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/21_S21_R1_0
01.fastq.gz", "file2": "Survey_Covid24/21_S21_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/22_S22_R1_001.fastq.gz", "file2": "Survey_Covid24/22_S22_R2_001.fastq.gz"},
 {"file1": "Survey_Covid24/23_S23_R1_001.fastq.gz", "file2": "Survey_Covid24/23_S23_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/24_S24_R1_001.fastq.gz", "file2": "
Survey_Covid24/24_S24_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/25_S25_R1_001.fastq.gz", "file2": "Survey_Covid24/25_S25_R2_001.fastq.gz"}, {"file1": "Survey_Covid2
4/26_S26_R1_001.fastq.gz", "file2": "Survey_Covid24/26_S26_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/27_S27_R1_001.fastq.gz", "file2": "Survey_Covid24/27_S27_R2_001
.fastq.gz"}, {"file1": "Survey_Covid24/28_S28_R1_001.fastq.gz", "file2": "Survey_Covid24/28_S28_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/29_S29_R1_001.fastq.gz",
"file2": "Survey_Covid24/29_S29_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/30_S30_R1_001.fastq.gz", "file2": "Survey_Covid24/30_S30_R2_001.fastq.gz"}]"}"""

expected_output2 = """{"sample-sheet-path": "test_folder_2/SampleSheet2.csv", "fastq-names": "[{"file1": "14_S1_R1_001.fastq.gz", "file2": "14_S1_R2_001.fastq.gz"}, {"file1": "44_S2_R1_001.fastq.gz", "file2": "44_S2_R2_001.fastq.gz"}, {"file1": "67_S3_R1_001.fastq.gz", "file2": "67_S3_R2_001.fastq.gz"}, {"file1": "68_S4_R1_001.fastq.gz", "file2": "68_S4_R2_001.fastq.gz"}, {"file1": "72_S5_R1_001.fastq.gz", "file2": "72_S5_R2_001.fastq.gz"}, {"file1": "76_S6_R1_001.fastq.gz", "file2": "76_S6_R2_001.fastq.gz"}, {"file1": "87_S7_R1_001.fastq.gz", "file2": "87_S7_R2_001.fastq.gz"}, {"file1": "88_S8_R1_001.fastq.gz", "file2": "88_S8_R2_001.fastq.gz"}, {"file1": "61_S9_R1_001.fastq.gz", "file2": "61_S9_R2_001.fastq.gz"}]"}"""

# class TestDataHandling(unittest.TestCase):
    # maxDiff = None
    # @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    # def assert_stdout(self, input_dir, output_path, samples_filename, expected_output, mock_stdout):
    #     build_fastq_names(input_dir, output_path, samples_filename)
    #     output = json.loads(mock_stdout.getvalue())
    #     print(mock_stdout.getvalue())
    #     ex_output = json.loads(expected_output)
    #     self.assertEqual(output, ex_output)

    # def test_data_handling(self):
        # self.assert_stdout('test_folder_2', 'test_folder_2/output/', 'samples.csv', expected_output2)
    
        # self.assert_stdout('test_folder_1', 'test_folder_1/output/', 'samples.csv', expected_output1)


class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class ActualTest(TestCaseBase):

    def execute_program(self, args):
        get_input(args)

    def test(self):
        self.execute_program(["", 'test_folder_1', 'test_folder_1/output', 'samples.csv'])
        path = pl.Path("test_folder_1/output/samples.csv")
        self.assertIsFile(path)
        self.execute_program(["", 'test_folder_2', 'test_folder_2/output', 'samples.csv'])
        path = pl.Path("test_folder_2/output/samples.csv")
        self.assertIsFile(path)
        self.execute_program(["", "test_folder_3", "test_folder_3/output", "samples.csv", "SampleSheet3.csv"])
        path = pl.Path("test_folder_3/output/samples.csv")
        self.assertIsFile(path)


        
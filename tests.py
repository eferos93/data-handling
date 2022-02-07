from distutils.command.build import build
import io
import unittest
import unittest.mock

from data_handling_utils import build_fastq_names

expected_output1 ="""{"sample-sheet-path": "test_folder_1/SampleSheet.csv", "fastq-names": "[{"file1": "Survey_Covid24/1_S1_R1_001.fastq.gz", "f
ile2": "Survey_Covid24/1_S1_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/2_S2_R1_001.fastq.gz", "file2": "Survey_Covid24/2_S2_R2_001.fastq.gz"}, {"file1": "Survey_Co
vid24/3_S3_R1_001.fastq.gz", "file2": "Survey_Covid24/3_S3_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/4_S4_R1_001.fastq.gz", "file2": "Survey_Covid24/4_S4_R2_001.fas
tq.gz"}, {"file1": "Survey_Covid24/5_S5_R1_001.fastq.gz", "file2": "Survey_Covid24/5_S5_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/6_S6_R1_001.fastq.gz", "file2":
 "Survey_Covid24/6_S6_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/7_S7_R1_001.fastq.gz", "file2": "Survey_Covid24/7_S7_R2_001.fastq.gz"}, {"file1": "Survey_Covid24/8
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

expected_output2 = """{"sample-sheet-path": "test_folder_2/SampleSheet.csv", "fastq-names": "[{"file1": "14_S1_R1_001.fastq.gz", "file2": "14_S
1_R2_001.fastq.gz"}, {"file1": "44_S2_R1_001.fastq.gz", "file2": "44_S2_R2_001.fastq.gz"}, {"file1": "67_S3_R1_001.fastq.gz", "file2": "67_S3_R2_001.fastq.gz"}, {
"file1": "68_S4_R1_001.fastq.gz", "file2": "68_S4_R2_001.fastq.gz"}, {"file1": "72_S5_R1_001.fastq.gz", "file2": "72_S5_R2_001.fastq.gz"}, {"file1": "76_S6_R1_0
01.fastq.gz", "file2": "76_S6_R2_001.fastq.gz"}, {"file1": "87_S7_R1_001.fastq.gz", "file2": "87_S7_R2_001.fastq.gz"}, {"file1": "88_S8_R1_001.fastq.gz", "file2
": "88_S8_R2_001.fastq.gz"}, {"file1": "61_S9_R1_001.fastq.gz", "file2": "61_S9_R2_001.fastq.gz"}]"}"""

class TestDataHandling(unittest.TestCase):
    maxDiff = None
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, input_dir, output_path, samples_filename, expected_output, mock_stdout):
        build_fastq_names(input_dir, output_path, samples_filename)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_data_handling(self):
        self.assert_stdout('test_folder_1', 'test_folder_1/output/', 'samples.csv', expected_output1)
        self.assert_stdout('test_folder_2', 'test_folder_2/output/', 'samples.csv', expected_output2)
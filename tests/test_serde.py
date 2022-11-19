import pytest
from pathlib import Path
import hexdump

# Test serialization / deserialization

@pytest.mark.parametrize('case_dir', list((Path('tests') / 'cases').iterdir()))
def test_parse(case_dir: Path, snapshot):
    case_file = case_dir.joinpath(case_dir.name)  # tests/cases/<TESTCASE_NAME>/<TESTCASE_NAME>
    s = case_file.with_suffix('.txt').read_text()
    d = hexdump.restore(s)
    print(d)

    from context import parse_resp
    

    # Snapshot the return value.
    snapshot.snapshot_dir = case_dir
    snapshot.assert_match(d, case_file.with_suffix('.bin'))

    output = parse_resp(d)
    snapshot.assert_match(repr(output), case_file.with_suffix('.out'))


def test_command_serialization(snapshot):
    snapshot.snapshot_dir = Path('tests') / 'commands'
    from context import Commands

    case_file = snapshot.snapshot_dir / 'on'
    #d = hexdump.restore(case_file.with_suffix('.txt').read_text())
    d = Commands.build_request(mac="04FA83FFFFFF", seq=57, cmd_data=Commands.on)
    snapshot.assert_match(hexdump.hexdump(d, result='return'), case_file.with_suffix('.txt'))
    snapshot.assert_match(d, case_file.with_suffix('.bin'))

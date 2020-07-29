from snyk.models import Issue
from snyk.models import IssueSet
from snyk.models import Vulnerability

from snyk_test.cli import main


def test_main(mocker):
    mocker.patch('snyk_test.Package.Package.run_assesment',
                 return_value=IssueSet(ok=False,
                                       packageManager='pip',
                                       dependencyCount=27,
                                       issues=Issue(
                                           vulnerabilities=[
                                               Vulnerability(
                                                   id='SNYK-PYTHON-CHANNELSREDIS-574718',
                                                   url='https://snyk.io/vuln/SNYK-PYTHON-CHANNELSREDIS-574718',
                                                   title='Denial of Service (DoS)',
                                                   description='## Overview\n[channels-redis]('
                                                               'https://www.pypi.org/project/channels-redis) is '
                                                               'a Redis-backed ASGI channel layer '
                                                               'implementation\n\nAffected versions of this '
                                                               'package are vulnerable to Denial of Service ('
                                                               'DoS) due to incorrect expiration '
                                                               'mechanisms.\n\n## Details\n\nDenial of Service '
                                                               '(DoS) describes a family of attacks, '
                                                               'all aimed at making a system inaccessible to '
                                                               'its intended and legitimate users.\n\nUnlike '
                                                               'other vulnerabilities, DoS attacks usually do '
                                                               'not aim at breaching security. Rather, '
                                                               'they are focused on making websites and '
                                                               'services unavailable to genuine users resulting '
                                                               'in downtime.\n\nOne popular Denial of Service '
                                                               'vulnerability is DDoS (a Distributed Denial of '
                                                               'Service), an attack that attempts to clog '
                                                               'network pipes to the system by generating a '
                                                               'large volume of traffic from many '
                                                               'machines.\n\nWhen it comes to open source '
                                                               'libraries, DoS vulnerabilities allow attackers '
                                                               'to trigger such a crash or crippling of the '
                                                               'service by using a flaw either in the '
                                                               'application code or from the use of open source '
                                                               'libraries.\n\nTwo common types of DoS '
                                                               'vulnerabilities:\n\n* High CPU/Memory '
                                                               'Consumption- An attacker sending crafted '
                                                               'requests that could cause the system to take a '
                                                               'disproportionate amount of time to process. For '
                                                               'example, '
                                                               '[commons-fileupload:commons-fileupload]('
                                                               'SNYK-JAVA-COMMONSFILEUPLOAD-30082).\n\n* Crash '
                                                               '- An attacker sending crafted requests that '
                                                               'could cause the system to crash. For Example,  '
                                                               '[npm `ws` package](npm:ws:20171108)\n\n## '
                                                               'Remediation\nUpgrade `channels-redis` to '
                                                               'version 3.0.0 or higher.\n## References\n- ['
                                                               'GitHub Commit]('
                                                               'https://github.com/django/channels_redis/commit'
                                                               '/c13b3453f976e23a617fc55f9748609c1692c8f0)\n- ['
                                                               'GitHub Issue]('
                                                               'https://github.com/django/channels_redis/issues'
                                                               '/182)\n- [GitHub PR]('
                                                               'https://github.com/django/channels_redis/pull'
                                                               '/184)\n',
                                                   upgradePath=[],
                                                   package='channels-redis',
                                                   version='2.4.2',
                                                   severity='medium',
                                                   exploitMaturity='no-known-exploit',
                                                   isUpgradable=False,
                                                   isPatchable=False,
                                                   identifiers={
                                                       'CVE': [],
                                                       'CWE': [
                                                           'CWE-400']},
                                                   semver={
                                                       'vulnerable': [
                                                           '[0,3.0.0)']},
                                                   fromPackages=[],
                                                   language='python',
                                                   packageManager='pip',
                                                   publicationTime='2020-07-16T13:58:02.513987Z',
                                                   disclosureTime='2020-06-28T14:12:54Z',
                                                   credit=[
                                                       'astutejoe'],
                                                   CVSSv3='CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L',
                                                   cvssScore=5.3,
                                                   ignored=[],
                                                   patched=[])],
                                           licenses=[])))

    testargs = ["snyk-test", "channels-redis@2.4.2"]
    mocker.patch('sys.argv', testargs)
    assert main(argv=testargs) == 0

    testargs = ["snyk-test", "channels-redis@2.4.2", "--json"]
    mocker.patch('sys.argv', testargs)
    assert main(argv=testargs) == 0

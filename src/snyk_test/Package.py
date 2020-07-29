from snyk import SnykClient

from snyk_test.utils import get_default_token_path
from snyk_test.utils import get_org_id
from snyk_test.utils import get_token


class Package:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.vulnerabilities = []
        self.license_issues = []

    def run_assesment(self):
        snyk_token_path = get_default_token_path()
        snyk_token = get_token(snyk_token_path)
        org_id = get_org_id(snyk_token_path)

        client = SnykClient(snyk_token)
        org_client = client.organizations.get(org_id)

        print("Testing package %s@%s" % (self.name, self.version))
        print("=====================")

        snyk_result = org_client.test_python(self.name, self.version)

        vulnerabilities_output = snyk_result.issues.vulnerabilities
        license_issues_output = snyk_result.issues.licenses

        severity_order = ['critical', 'high', 'medium', 'low']

        if vulnerabilities_output is not None:
            for v in vulnerabilities_output:
                formatted_vulnerability = {
                    'id': v.id,
                    'title': v.title,
                    'url': v.url,
                    'package': v.package,
                    'version': v.version,
                    'identifiers': v.identifiers['CVE'],
                    'severity': v.severity,
                    'language': v.language,
                    'package_manager': v.packageManager,
                    'is_upgradable': v.isUpgradable,
                    'is_patchable': v.isPatchable
                }

                self.vulnerabilities.append(formatted_vulnerability)
            self.vulnerabilities = sorted(self.vulnerabilities, key=lambda k: severity_order.index(k['severity']))

        if license_issues_output is not None:
            for i in license_issues_output:
                formatted_license_issue = {
                    'id': i.id,
                    'title': i.title,
                    'url': i.url,
                    'package': i.package,
                    'version': i.version,
                    'severity': i.severity,
                    'is_ignored': i.isIgnored,
                    'is_patched': i.isPatched,
                    'language': i.language,
                    'priority_score': i.priorityScore,
                    'package_manager': i.packageManager
                }

                self.license_issues.append(formatted_license_issue)
            self.license_issues = sorted(self.license_issues, key=lambda k: severity_order.index(k['severity']))

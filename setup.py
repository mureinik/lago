import os
from setuptools import setup

setup(
    name='lago',
    version=os.environ['LAGO_VERSION'],
    description=(
        'Deploy and tear down environments of several virtual machines'
    ),
    license='GNU GPLv2+',
    author='Dima Kuznetsov',
    author_email='dkuznets@redhat.com',
    url='redhat.com',
    package_dir={
        'lago': 'lib/lago',
        'lago_template_repo': 'lib/lago_template_repo',
        'ovirtlago': 'contrib/ovirt/lib/ovirtlago'
    },
    packages=[
        'lago',
        'lago.plugins',
        'lago_template_repo',
        'ovirtlago',
    ],
    package_data={
        'lago': [
            '*.xml',
            '*.log.conf',
        ],
    },
    provides=['lago', 'ovirtlago'],
    entry_points={
        'console_scripts': [
            'lagocli=lago.cmd:main',
            'lago=lago.cmd:main',
        ],
        'lago.plugins.cli': [
            'cleanup=lago.cmd:do_cleanup',
            'collect=lago.cmd:do_collect',
            'console=lago.cmd:do_console',
            'copy-from-vm=lago.cmd:do_copy_from_vm',
            'copy-to-vm=lago.cmd:do_copy_to_vm',
            'init=lago.cmd:do_init',
            'ovirt=ovirtlago.cmd:OvirtCLI',
            'revert=lago.cmd:do_revert',
            'shell=lago.cmd:do_shell',
            'snapshot=lago.cmd:do_snapshot',
            'start=lago.cmd:do_start',
            'status=lago.cmd:do_status',
            'stop=lago.cmd:do_stop',
            'template-repo=lago_template_repo:TemplateRepoCLI',
        ],
    },
)

from setuptools import setup

setup(
    name='jenkins-job-builder-active-choice',
    version='0.0.4',
    description='Jenkins Job Builder Active Choice Parameter builder',
    url='https://github.com/bgaifullin/jenkins-job-builder-active-choice',
    author='Bulat Gaifullin',
    author_email='gaifullinbf@gmail.com',
    license='MIT license',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'jenkins-job-builder<2.0.0'],
    entry_points={
        'jenkins_jobs.parameters': [
            'separator = jenkins_jobs_active_choice.separator:separator_parameter',
            'cascade-choice = jenkins_jobs_active_choice.active_choice:cascade_choice_parameter',
            'validating = jenkins_jobs_active_choice.validating:validating_parameter',
            'autocomplete = jenkins_jobs_active_choice.autocomplete:autocomplete_parameter'
        ]
    },
    packages=['jenkins_jobs_active_choice'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])

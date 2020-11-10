from invoke import task

# Install Requirements
@task
def install(c):
	print('Dependencies are installed')
	c.run('pip install -r requirements.txt')

# Cleaning
@task
def clean(c):
	print('Cleaning')
	c.run('find . -name \'*.pyc\' -delete')

# Run Tests
@task
def test(c):
	print('Tests are running..')
	c.run('pytest -v')

# Run Execution
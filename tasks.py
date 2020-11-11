from invoke import task

#Create Virtualenv
@task
def create(c):
	print('Creating new virtual environment')
	c.run('python3.8 -m venv selva_urbana')
	c.run('source selva_urbana/bin/activate')

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
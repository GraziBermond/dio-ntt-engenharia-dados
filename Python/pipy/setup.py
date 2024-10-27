from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="criar_conta",
    version="0.0.1",
    author="GraziBermond",
    author_email="grabermond@gmal.com",
    description="Criar conta de usuario",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GraziBermond/dio-ntt-engenharia-dados/blob/main/Python/Desafio03_Sistema_Bancario_CadastroUsuario.py"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
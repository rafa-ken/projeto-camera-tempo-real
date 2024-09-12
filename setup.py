from setuptools import setup, find_packages

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="camera-tempo-real",  # Substitua pelo nome do seu pacote
    version="0.1.0",
    author="Rafae Ken Reis Miyamoto, Vinicius Leal Silva",
    author_email="rafaelkrm@al.insper.edu.br, viniciusls2@al.insper.edu.br",
    description="Pacote para capturar imagens da câmera em tempo real",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafa-ken/projeto-camera-tempo-real",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'projeto-camera-tempo-real=projeto-camera-tempo-real.main:main',
        ],
    },
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines()
    ],
)
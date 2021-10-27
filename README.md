# PyDRS - Sirius Power Supplies communication.

![Linting and Static](https://github.com/lnls-sirius/pydrs/actions/workflows/lint.yml/badge.svg)
![Latest tag](https://img.shields.io/github/tag/lnls-sirius/pydrs.svg?style=flat)
[![Latest release](https://img.shields.io/github/release/lnls-sirius/pydrs.svg?style=flat)](https://github.com/lnls-sirius/pydrs/releases)
[![PyPI version fury.io](https://badge.fury.io/py/pydrs.svg)](https://pypi.python.org/pypi/pydrs/)
[![Read the Docs](https://readthedocs.org/projects/spack/badge/?version=latest)](https://lnls-sirius.github.io/pydrs/)

## What is PyDRS?

**PyDRS** is a Python package based on the Basic Small Messages Protocol [**BSMP**](https://github.com/lnls-sirius/libbsmp). It is used to communicate with and command Sirius Current Power Supplies and its peripherals ran by Digital Regulation System (**DRS**).

Development packages are listed at [requirements-dev.txt](requirements_dev.txt) and runtime dependencies at [requirements.txt](requirements.txt).
## Prerequisites

 * [python==3.6](https://www.python.org/downloads/release/python-3612/)  
* pyserial==3.5  
* numpy  

**Disclaimer:** Although pydrs is tested up to [**Python 3.10.0**](https://www.python.org/downloads/release/python-3100/) version you may check whether other apps you want to use with it may run Python 3.10 version.
Also should be the case that any of these applications may require Microsoft C++ build tools  [**visualcppbuildtools**](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools). 


## Dev Utility scripts

```sh
sh ./scripts/clean.sh
```
## Installation Guide

### **User level:**  
User-level version must be installed from the [**PyPI**](https://pypi.org/project/pydrs/) repository, using the 'pip install pydrs' command, which will install PyDRS onto the current Python path version.  
  
### **Optional: - Conda**  
 
Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux.

It can be used to create a specific environment where PyDRS module can be installed.
Use [**miniconda**](https://docs.conda.io/en/latest/miniconda.html#miniconda) for a free minimal installer for conda **or**
 [**anaconda**](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) for a full version for Conda.

```command
conda create --name pydrs python=3.6
conda activate pydrs
```

```command
pip install -U pydrs
```

### **Developer level:**  

For a developer level firstly clone the project repository from [**GitHub**](https://github.com/lnls-sirius/pydrs) to **your_local_folder** via git command: 

```command
 git clone https://github.com/lnls-sirius/pydrs.git
``` 

![image](https://user-images.githubusercontent.com/19196344/139123128-3b70e4de-9bf3-4164-9e39-a3f8c2e64806.png)


Proceed to the **pydrs** folder and then you can use pip command by **two means** at your **choice**:    

![image](https://user-images.githubusercontent.com/19196344/139126431-eae06bcd-81f9-4746-b8c5-2115f0637bab.png)


**1**. Just copying the repository locally. (Local changes on the project won't take effect on current pydrs installation).

É possível instalar o módulo python a partir do código fonte clonado. Usando o comando `pip install .` na raiz do repositório o módulo será instalado normalmente, ou seja, os arquivos clonados serão copiados para a pasta `site-packages` do python ativo.

```command
pip install .
```

![image](https://user-images.githubusercontent.com/19196344/139126660-0ce7cb62-8abe-492c-8596-1e581a061530.png)



**2**. Copying the repository locally with the update feature. (Local changes will immediately take effect on pydrs current installation). 

O uso da flag `-e` na instalação local é recomendada para situações em que o código está em desenvolvimento e é desejado utilizar as alterações imediatamente. A instalação com o comando `pip install -e .` cria uma espécie de link com a pasta do repositório, dessa forma, não será necessário reinstalar o pacote sempre que uma mudança ocorrer no repositório local.

```command
pip install -e .
```
![image](https://user-images.githubusercontent.com/19196344/139126876-150791c2-9a94-4e75-b91c-28ace5002699.png)



## Usage

When all installation is done, python or ipython instance can be called.

![14](https://user-images.githubusercontent.com/19196344/138935751-d90dc9b9-1409-4dc4-98bd-66f480dcd489.png)


Import pydrs

![image](https://user-images.githubusercontent.com/19196344/139112617-2629340e-fac9-4002-8456-1e3b079cd837.png)


Create *drs* object.

![image](https://user-images.githubusercontent.com/19196344/139116187-fc58c909-9b4f-46fe-91ca-d80796f3256d.png)


Establish the connection.

![image](https://user-images.githubusercontent.com/19196344/139116355-790b9f0e-8536-4203-9276-b3e592329661.png)


Set the device address to communicate.

![image](https://user-images.githubusercontent.com/19196344/139116450-1b083db1-b257-40ca-868c-350b9af193e4.png)


Use BSMP commands to control the device.

![image](https://user-images.githubusercontent.com/19196344/139116593-7fcbd965-85e4-460e-a912-91782a21d412.png)



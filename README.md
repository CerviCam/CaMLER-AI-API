# CerviCam - AI API
The source codes of all CerviCam AI models. The core is built by PyTorch and Flask. PyTorch is used to run our AI model in high-performance by allocating the processing to the GPU as the main cores/computation and Flask is a light-framework with a job to enable the AI model to be accessible to public through URI. 

## **Table of Contents**
- [Prerequisites](#prerequisites)
- [File structure](#file-structure)
- [Setup](#setup)
- [Activate/Deactivate Local Environment](#activate/deactivate-local-environment)
- [Add and Install Packages](#add-and-install-packages)
- [Usage](#usage)
- [Troubleshootings](#Troubleshootings)
- [Acknowledgements](#acknowledgements)

## **File structure**
```
AI-API
├── api                             
│   ├── helper.py                   <- Global functions
│   ├── urls.py                     <- All endpoints and handler for every endpoint
│   └── views.py                    <- Endpoint handlers
│
├── instance                             
│   ├── app.py                      <- A function to run the application
│   ├── setting.py                  <- Env variables
│   └── wsgi.py                     <- If you want to use wsgi-like tool to run the server, such as gunicorn
│
├── Dockerfile                      <- Use this when you want to create an image by Docker
├── manage.py                       <- All available commands to configure/run the application
├── .env                            <- Local variables
├── env                             <- Local environment, where all installed packages will be stored
├── requirements.txt                <- All required packages are defined in here
```

## **Prerequisites***
As requirements, you need to install all these following packages/tools:
- **Git** - Use any version as you like, will use this tool for managing the source codes.
- **Python v3.7.7** - To run a server. The version doesn't have to be exact, try with your python if something goes wrong then try this version as a last option.
## **Setup**
You must setup the environment before going anywhere. Here are simple steps you can follow:
1. Create **env** folder to store all required packages from requirements.txt.
    ```bash
    python -m venv env
    ```
2. Create **.env** file in the root of project to set environment variables. Here is the format:
    ```
    DEBUG=
    AI_API_HOST=
    AI_API_PORT=
    ```
    e.g:
    ```
    DEBUG=1
    AI_API_HOST=localhost
    AI_API_PORT=2020
    ``` 
    
    More detail about the **environment variables**:
    | Variable          | Optional    | Value                                                                             |
    |-------------------|-------------|-----------------------------------------------------------------------------------|
    | DEBUG             | Yes         | Either **0** or **1**. The default is **1**, means True                           |
    | AI_API_HOST       | Yes         | The default is **localhost**                                                      |
    | AI_API_PORT       | Yes         | The default is **2020**                                                           |

### **Notable**
You can use global environment to install/store required packages, but we don't recommend that since it can affect another application to run that also uses the global environment. Isolated environment will prevent you to have false environment, so it would be better if we stick to the local environment.

## **Activate/Deactivate Local Environment**
Before you can use all available commands on [usage](#usage), you need to activate a local environment first by calling this command in the root of repository:
- Windows:
    ```bash
    env\Scripts\activate
    ```
- Unix:
    ```bash
    source env/bin/activate
    ```

And if you need to close it, then run as easy as run terminated signal:
- Windows/Unix:
    ```bash
    [CTRL + C]
    ```

or you can close it in gracefully way:
- Windows/Unix:
    ```bash
    deactivate
    ```

## **Add and Install Packages**
Activate your local environment from [this section](#activate/deactivate-local-environment) before add or install packages.
- Install all required packages from requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```
- Add new package
    1. Add new package and the version of it on the requirements.txt. e.g:
        ```bash
        Flask==1.1.2
        ```
    2. Finally, install all packages after you add it to the requirements.txt
       ```bash
       pip install -r requirements.txt
       ```

### **Notable**
1. **Prefer to edit requirements.txt and then install** rather than install manually and then copy all new installed packages to requirements.txt.

    In simple words, don't do this:
    ```bash
    pip install Flask
    pip freeze > requirements.txt
    ```
    Putting all installed package (including a package dependencies) into requirements.txt is chaos, because it also will add you-dont-know packages to requirements.txt. If you do that then when your requirements.txt is getting bigger you will find out that it's hardly to manage. Just don't do that.
2. **Always provide a version of the package on requirements.txt** to avoid a failing system due the incompatible of different version of same package. If you don't provide it, the pip will install to the lastest one, that's why it can give you a different version than others.

## **Usage**
Ensure you already activated your local environment in [here](#activate/deactivate-local-environment), something will go wrong if the environment hasn't  set up properly when you use one of these commands.

- Run application in development
    ```bash
    python manage.py server
    ```

- Run application in production
    ```bash
    gunicorn instance.wsgi:app
    ```

## **Troubleshootings**
Write down in here if you have common solved problem need to be shared among developers.

## **Acknowledgements**
- CerviCam
- IMERI
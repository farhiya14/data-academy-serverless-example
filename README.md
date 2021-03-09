# data-academy-serverless-example
A repository to demonstrate a simple serverless repo for the data academy.

### Pre-requisites

1. Install [Node.js](https://nodejs.org/en/). Check that it has installed by running `node -v`.

    > `Node.js` is a free, open-sourced, cross-platform JavaScript run-time environment that lets developers write command line tools and server-side scripts outside of a browser.

    If you're running your project in a development container, skip this step and run the following commands on the terminal:

    ```sh
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt install node
    sudo apt install npm
    ```

1. In your repository, Check if `npm` is installed by running `npm -v`.

   > `npm` (originally short for `Node Package Manager`) is a package manager for the JavaScript programming language. We need this so that we can install the `serverless` package, along with other potentially useful packages.

1. Run `npm init` to initialise `npm` in your project.

1. Run `npm install serverless`. This will install the `serverless` package for us.

    > The Serverless Framework is a free and open-source web framework written using Node.js. Serverless was the first framework developed for building applications on AWS Lambda. A Serverless app can simply be a couple of lambda functions to accomplish some tasks, or an entire back-end composed of hundreds of lambda functions and other AWS services.

### Setting up serverless

1. Run `npx serverless` or `npx sls` as a short-hand.
1. Select `AWS Python`.
1. Give the service a name.
1. Select `n` for allowing monitoring services.
1. Select `n` for setting AWS credentials.

This will generate a new directory, containing an `.npmignore`, `handler.py` and `serverless.yml` file. However, this repository is structured slightly differently by removing `.npmignore` and moving `serverless.yml` to the top-level directory. This is so you can define multiple services for a project. You can see this with the two example service directories that have been setup inside the `src` folder.

- The `handler.py` file is the entry point for your service.
- The `serverless.yml` file is used to define the infrastructure of your service(s).

Imagine each service is just a regular Python application which lives inside AWS Lambda. Inside each of our example service directories, you can define as many Python files as you want, as long as you specify where the starting point of your service is. You can also define a `requirements.txt` for each service too.

### How to define a Lambda as infrastructure

If we look at this snippet from `serverless.yml`:

```yml
functions:
  example-service-1:
    handler: src/example-service-1/handler.start
```

This tells us that we have defined a `Lambda` function with the name `example-service-1`. It will have a runtime of `Python 3.8`. The `handler` defines the entry point of the `Lambda`, so in our case it will be `src/example-service-1/handler.start`.

### Deploying your application

Assuming you can access AWS through the CLI, you can deploy your application to AWS using the following command:

```sh
sls deploy
```

This command will deploy your entire service via `CloudFormation`. Run this command when you have made infrastructure changes (i.e., you edited `serverless.yml`).

### Current problems and workarounds

Serverless Framework does not currently provide support for AWS SSO. When running the deploy command, it will look for the file `~/.aws/credentials` which stores the credentials of your AWS profile to be able to access AWS services through the CLI. An example file may look like this:

```
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

AWS SSO does not require this file, and so the deploy command will fail to work by default. In order to counteract this, someone created a useful `npm` package called [aws-sso-credentials-getter](https://github.com/PredictMobile/aws-sso-credentials-getter/) that will generate temporary credentials for us when we run `aws sso login`.

To install locally, run `npm install aws-sso-credentials-getter`.

When installed, we can run the following commands to now get the deploy to work for us:

```sh
$ aws sso login --profile [name-of-profile]   # make sure we are logged in first
$ npx ssocred [name-of-profile]               # generate temporary local credentials
$ sls deploy --aws-profile [name-of-profile]  # deploy serverless application to AWS
```

When running `ssocred` on Windows, if you get an error akin to `no such file or directory, open 'C:\Users\user\.aws\credentials'`, run `touch ~/.aws/credentials`.

### Example output

If `sls deploy` succeeded, you should see the following output in your terminal:

```
Serverless: Stack update finished...
Service Information
service: data-academy-serverless-example
stage: dev
region: eu-west-1
stack: data-academy-serverless-example-dev
resources: 9
api keys:
  None
endpoints:
  None
functions:
  example-service-1: data-academy-serverless-example-dev-example-service-1
  example-service-2: data-academy-serverless-example-dev-example-service-2
layers:
  None
```

### Tearing down a serverless application

To remove anything you have deployed with serverless, run `sls remove --aws-profile [name-of-profile]`.

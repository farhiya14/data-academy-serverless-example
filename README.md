# data-academy-serverless-example
A repository to demonstrate a simple serverless repo for the data academy.

### Pre-requisites

1. Install [Node.js](https://nodejs.org/en/). Check that it has installed by running `node -v`.

    > `Node.js` is a free, open-sourced, cross-platform JavaScript run-time environment that lets developers write command line tools and server-side scripts outside of a browser.

1. In your repository, Check if `npm` is installed by running `npm -v`. Run `npm init`.

   > `npm` (originally short for `Node Package Manager`) is a package manager for the JavaScript programming language. We need this so that we can install the `serverless` package, along with other potentially useful packages.

1. Run `npm install serverless`. This will install the `serverless` package for us.

    > The Serverless Framework is a free and open-source web framework written using Node.js. Serverless was the first framework developed for building applications on AWS Lambda. A Serverless app can simply be a couple of lambda functions to accomplish some tasks, or an entire back-end composed of hundreds of lambda functions and other AWS services.

### Setting up serverless

1. Run `serverless` or `sls` as a short-hand.
1. Select `AWS Python`.
1. Give the service a name.
1. Select `n` for allowing monitoring services.

This will generate a new directory, containing an `.npmignore`, `handler.py` and `serverless.yml` file. However, this repository is structured slightly differently by removing `.npmignore` and moving `serverless.yml` to the top-level directory. This is so you can define multiple services for a project. You can see this with the two example service directories that have been setup.

- The `.npmignore` file is used to keep stuff out of your package, like `.gitignore`.
- The `handler.py` file is the entry point for your service.
- The `serverless.yml` file is used to define the infrastructure of your service(s).

Imagine each service is just a regular Python application which lives inside AWS Lambda. Inside each of our example service directories, you can define as many Python files as you want, as long as you specify where the starting point of your service is. You can also define a `requirements.txt` for each service too.

### How to define a Lambda as infrastructure

If we look at this snippet from `serverless.yml`:

```yml
functions:
  example-service-1:
    runtime: python3.8
    handler: handler.start
    module: example-service-1
```

This tells us that we have defined a `Lambda` with the name `example-service-1`. It will have a runtime of `Python 3.8`. The `handler` defines the entry point of the `Lambda`, which is denoted as `module_name.function_name`, so in our case it will be `handler.start`.

### Deploying your application

Assuming you can access AWS through the CLI, you can deploy your application to AWS using the following commands:

```sh
sls package
```

This command will package your entire infrastructure into the `.serverless` directory by default and make it ready for deployment.

```sh
sls deploy
```

This command will deploy your entire service via `CloudFormation`. Run this command when you have made infrastructure changes (i.e., you edited `serverless.yml`).

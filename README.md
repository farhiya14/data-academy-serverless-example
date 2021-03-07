# data-academy-serverless-example
A repository to demonstrate a simple serverless repo for the data academy.

### Pre-requisites

1. Install [Node.js](https://nodejs.org/en/). Check that it has installed by running `node -v`.

    > `Node.js` is a free, open-sourced, cross-platform JavaScript run-time environment that lets developers write command line tools and server-side scripts outside of a browser.

1. In your repository, Check if `npm` is installed by running `npm -v`. Run `npm init`.

   > `npm` (originally short for `Node Package Manager`) is a package manager for the JavaScript programming language. We need this so that we can install the `serverless` package, along with other potentially useful packages.


1. Run `serverless`.

    > The Serverless Framework is a free and open-source web framework written using Node.js. Serverless was the first framework developed for building applications on AWS Lambda. A Serverless app can simply be a couple of lambda functions to accomplish some tasks, or an entire back-end composed of hundreds of lambda functions and other AWS services.

1. Select `AWS Python`.
1. Give the project a name.
1. Select `n` for allowing monitoring services.

This will generate a new directory, containing an `.npmignore`, `handler.py` and `serverless.yml` file.

- The `.npmignore` file is used to keep stuff out of your package, like `.gitignore`.
- The `handler.py` file is the entry point for your application.
- The `serverless.yml` file is used to define the infrastructure of your application.

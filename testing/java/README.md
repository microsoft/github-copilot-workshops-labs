# GitHub copilot testing lab

This repository contains a collection of challenges to improve your skills with GitHub Copilot regarding testing and related topics.

## Pre-requisites

- [Visual Studio Code](https://code.visualstudio.com/) or any other editor that supports GitHub Copilot.
- [GitHub Copilot](https://copilot.github.com/) extensions installed.
- Java 17 or higher
- Maven 
- [Jmeter](https://jmeter.apache.org/download_jmeter.cgi)
- Access to SonarQube (or a local instance running with Docker)

## Getting started

1. Clone this repository. 
2. Open the project in Visual Studio Code or your favorite editor.

## Challenges

### Understand the API

    This challenge is about understanding the API that you are going to test. You will need to document the API and understand the endpoints, request and response payloads, and the expected behavior of the API. Create also examples of curl commands to interact with the API.

    The output should be a markdown file with the API documentation.

### Create unit tests

In this challenge, you will create unit tests for the API. You will need to create unit tests for the the repository, service, and controller layers.

**Repository tests**

    It is your first test, I will provide some tips: 

    - Use predefined commands.
    - Add context to the ask, in this case, the repository class.

    Expected result: a new test class named `EmployeeRepositoryTest`.

**Service tests**

    Do not forget that this is a unit test, so you should mock the repository layer.

    Expected result: a new test class named `EmployeeServiceTest`.

**Controller tests**

    No more tips here. You should be able to create the test class by yourself.. with the help of GitHub Copilot, of course.

    Expected result: a new test class named `EmployeeControllerTest`.


**Bonus**

    Create a new operation in the API, such as find employees by email and all the tests in every layer in a single shot.

    Tips: Use multi edit feature and provide all the necessary classes.

### Customize instructions

    How can you customize the instructions to generate tests automatically? Use [GitHub Copilot custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)

    Validate that you only get tests implementations only when asked for new features.

### Improve test coverage and quality

    In this challenge, you will improve the test coverage and quality of the tests. You will ask GitHub Copilot to recommend improvements to the test coverage and how you can check current coverage locally.

    Also, integrate your IDE with SonarQube and improve your code quality with the help of GitHub Copilot.

    NOTE: You will need to have a SonarQube instance running to complete this challenge. 
    For the shake of simplicity, you can use a local instance running with Docker. Instructions:

    - Install sonarqube extension
    - Run sonarqube server
    ```bash
    docker run --name sonarqube-custom -p 9000:9000 sonarqube:10.6-community
    ```	
    - Configure extension to point to http://localhost:9000 and create a token
    - Create project in sonarqube, get a new token and run analysis
    ```bash
    SONAR_TOKEN=sqp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    mvn clean verify sonar:sonar \
    -Dsonar.projectKey=demo \
    -Dsonar.projectName='demo' \
    -Dsonar.host.url=http://localhost:9000 \
    -Dsonar.token=$SONAR_TOKEN
    ```

### Performance testing

    Implement performance tests for the API. You will need to create a JMeter test plan to test the performance of the API. The test plan should include the following:
    - A sequence of calls: create, update, read and delete.
    - Extract the id from the create call and use it in the update, read, and delete calls.
    - Use assertions to validate the response of the calls.

    Remember that you need to have [Jmeter](https://jmeter.apache.org/download_jmeter.cgi) installed to complete this challenge.

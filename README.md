# API Testing
### ⚙️🛠 Automated API Testing using Python Language 🛠⚙️

📢 This repository contains an API testing project for Second Hand using Python, requests, PyTest. The tests are designed to cover various scenarios on the Second Hand (https://secondhand.binaracademy.org).

## Table of Contents

- [Introduction](#introduction)
- [Scope](#scope)
- [Features](#features)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Test Cases](#test-cases)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Test automation is the process of using software tools and frameworks to automate test execution, compare actual outcomes to expected outcomes, and generate test reports. This helps to increase efficiency, accuracy, and repeatability of testing processes, as well as reducing the time and costs associated with manual testing. <br><br>In here we are going to Second Hand Endpoint (https://secondhand.binaracademy.org). This project focuses on API automating tests for the Second Hand API Endpoint using python.

## Scope

The project covers the following areas of the Swag Labs website:

- Authentication (POST Registration, POST Login)
- Categories (GET List Categories, GET Category by id)
- Offers (POST Offers, GET List Offers, PUT Update Offer)
- Products (POST Product, GET List Product, GET List Product by id, PUT Update Product, DELETE Product)
- Profiles (PUT Update Profile, GET Profile)

## Features

- Uses Selenium for interacting with web elements and performing automated actions.
- Organizes test scenarios using TestNG testing framework.
- Includes a wide range of test cases covering login, checkout product functionality, and more.
- Provides easy-to-understand bug reports and test outcomes.


## Tools and Technologies Used

This test automation project for Swag Labs utilizes a variety of tools and technologies to streamline the testing process and ensure efficient and accurate results.

- **Java**: The primary programming language used for writing the test automation code.

- **Selenium**: A popular open-source framework for automating web browser interactions and testing.

- **TestNG**: A popular and most widely used testing framework for Selenium automation.

- **ChromeDriver**: The WebDriver implementation for Google Chrome, enabling Selenium to automate Chrome browser actions.

- **Maven**: A build and dependency management tool that simplifies project setup and maintenance.

- **IntelliJ IDE**:  An integrated development environment (IDE) written in Java for developing computer software written in Java, Kotlin, Groovy, and other JVM-based languages.

- **Qase**:  A modern test management platform for manual & automated QA testing & reporting that helps your team deliver a higher quality product, faster.

These technologies are combined to create an effective testing framework that automates test cases, performs comparisons between expected and actual outcomes, and generates detailed test reports.


## Test Cases

The test cases are written in third-party platform using [Qase](https://qase.io/). Each test case covers various aspects of the Swag Labs website, ensuring comprehensive coverage.

## Installation

Ensure that you have the following tools and technologies installed on your machine:

- [Java](https://www.java.com/en/download/)
- [Maven](https://maven.apache.org/install.html)
- [IntelliJ IDE](https://www.jetbrains.com/idea/download/)
- [Selenium](https://www.selenium.dev/downloads/)
- [Chrome driver](https://chromedriver.chromium.org)
  <br><br>Note: Make sure to download the relavent Chrome driver version for your chrome browser match, and put it into project directory.

## Usage

1. Open the project in IntelliJ or your preferred IDE.
2. Navigate to the `src/test/java/testng` directory.
3. Locate the test files `testng.xml`.
4. Run the test by `Right click > Run` to execute the automated test scenarios.

## Contributing

Contributions to this project are welcome! If you identify any issues or wish to enhance the existing test suite, please feel free to create pull requests.




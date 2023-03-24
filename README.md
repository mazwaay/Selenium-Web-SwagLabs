# Hi, I'm Mazway 👋

I will create a simple automation test using Selenium Python, Pytest  and Unittest, for reporting, I will use Allure Report on the [Swag Labs Website](https://www.saucedemo.com/).

## Installation

- clone this project
- install required.txt

## Scenario Test

 - **1. Login using standard user**
	- **Test Step**
	   >1. Open the website
	   >2. Input username as standard_user
	   >3. Input password as secret_sauce
	   >4. Click button login
	  - **Expected : Successfully logged in and redirects to the product page.**
   

- **2. Login using locked user**
	- **Test Step**
	   >1. Open the website
	   >2. Input username as locked_out_user
	   >3. Input password as secret_sauce
	   >4. Click button login
      - **Expected : Will display an error message "Epic sadface: Sorry, this user has been locked out."**

- **3. Login using problem user**
	- **Test Step**
	   >1. Open the website
	   >2. Input username as problem_user
	   >3. Input password as secret_sauce
	   >4. Click button login
	  - **Expected : Successfully logged in but an inappropriate image is displayed.**

 4. **4. Login using performance user**
	- Test Step
	   >1. Open the website
	   >2. Input username as performance_glitch_user
	   >3. Input password as secret_sauce
	   >4. Click button login
	  - **Expected : Login is successful but it takes a longer time.**

## Screen Record
<img width="300" src="https://user-images.githubusercontent.com/42727156/227218971-49909bea-ae57-4c44-b7f7-d68aab03a8c8.mp4" />
  

## Reporting

for reporting [Allure Report](https://swaglabs.netlify.app/#), check this.




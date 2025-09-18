# Developers Hackathon 👩‍💻👨🏾‍💻
Welcome to the Developers Hackathon. The challenge is to develop a software described in the "Challenge" section using the most modern development tools:  GitHub Repos for code and GitHub Actions for automation, GitHub Codespaces as development environment and obtaining assistance from GitHub Copilot.

## Codespace Environment 💻
**Installed Software:** SQL Server 2019, .NET Core, Python, Node.js, JavaScript, TypeScript, C++, Java, C#, F#,  PHP, Go, Ruby, Conda  
**VS Code Extensions:** GitHub Copilot, C#, SQL Server 2019

**SQL Server Connection**: Server: localhost,1433 - Username: sa - Password: Passw0rd  
**Connection string:**  Server=localhost,1433;User Id=sa;Password=Passw0rd;Database=[yourDbName];MultipleActiveResultSets=true;Encrypt=False

## Start the Hackathon 🏁
1) Click on 'Code' -> 'Select Codespaces tab' -> 'New with options...' 
2) Select the branch corresponding to your team (i.e. team1)
3) Select the 8 core machine size 
4) Start the Codespace and Happy coding 😊

# Challenge 1: Retail Store App 🌐

The main challenge is to develop an application that allows a store operator to manage customer data, product data, and purchase orders. The application should be a Web Application that stores data in an Azure SQL Database and is hosted on an Azure App Service. The application should be user-friendly and allow the store operator to view, update, and delete data as required.

Functional requirements for the application:

1. User Interface:
   - The system is a WebApplication and should have an intuitive, user-friendly interface.
2. Customer Management:
   - The system should allow store operators to add new customers with id, name, surname, address, birth date and email.
   - The system should allow store operators to view, update, and delete customer data.
   - The system should validate customer data input (e.g., check the format of email addresses).
3. Product Management:
   - The system should allow store operators to create new products with id, name, description and price.
   - The system should allow store operators to view, update, and delete products.
   - The system should allow store operators to search products based on various parameters like id and product name.
4. Order Management:
   - The system should allow store operators to create a purchase order, with order number, customer and product.
   - The system should allow store operators to view, update, and delete purchase orders.
   - The system should allow store operators to search purchase orders based on various parameters like customer name and order number.
5. Reporting:
   - The system should allow store operators to export data in various formats (e.g., PDF, Excel).

💡Make sure the database structure is initialized by the app when it runs. For the connection string use the name "DatabaseConnectionString". The same name will be used by the Operation teams for configure the Connection String in the App Service and accessible trough an [environment variable](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#configure-connection-strings). For local development you can create your own database by leveraging SQL Server configured within the Codespace.

# Challenge 2: Application Testing 🧪
The application must have unit tests for the main functionalities.

# Challenge 3: CI/CD 🚀
The application must be build and deployed with GitHub Actions.

💡To connect to Azure use the GitHub Action secret named AZURE_CREDENTIALS already configured for you. Sync with the operation team for the target Azure resources.  
💡A skeleton of the GitHub Action has been created [.github/workflows/build-deploy-app.yml](.github/workflows/build-deploy-app.yml). Do not modify the trigger. Complete it with your code and make sure to launch it for your branch.


# Challenge 4: Documentation 📝
The application must have a DOCS.md file with a description of the application, a sequence diagram for the database schema and instructions on how to build, test, and deploy the application.

# GitHub Copilot assistance 🤖
Given the hackathon challenges, try to ask to GitHub Copilot for help, following some suggestions for build a .NET Web Application:
<table>
	<tr><th>Requirements</th><th>Ask to GitHub Copilot…</th></tr>
	<tr>
		<td>The system is a WebApplication and should have an intuitive, user-friendly interface.</td>
		<td>Generate a .NET web application</td></tr>
	<tr>
		<td>Customer Management: <br>
		- The system should allow store operators to add new customers with id, name, surname, address, birth date and email. <br>
		- The system should allow store operators to view, update, and delete customer data. <br>
		- The system should validate customer data input (e.g., check the format of email addresses). <br>
		</td>
		<td>
		1. Generate a model named Customer with Id, Name, Surname, Address, BirthDate and Email <br>
		2. Add NuGet packages for Entity Framework  <br>
		3. Generate Razor Pages for Create, Read, Update, and Delete by using scaffold tool for model Customer  <br>
		4. Add EF Initial database schema  <br>
		</td>
	</tr>
	<tr>
		<td>Product Management: <br>
		- The system should allow store operators to create new products with id, name, description and price. <br>
		- The system should allow store operators to view, update, and delete products. <br>
		- The system should allow store operators to search products based on various parameters like id and product name. <br>
		</td>
		<td>
		1. Generate a model named Product with Id, Name, Description and Price.<br>
		2. Generate Razor Pages for Create, Read, Update, and Delete by using scaffold tool for model Product <br>
		3. Add EF migration for Product <br>
		4. Add search to Products page that allows to search by Id and Name <br>
		</td>
	</tr>
	<tr>
		<td>Order Management: <br>
		- The system should allow store operators to create a purchase order, with order number, customer and product. <br>
		- The system should allow store operators to view, update, and delete purchase orders. <br>
		- The system should allow store operators to search purchase orders based on various parameters like customer name and order number. <br>
		</td>
		<td>
		1. Generate a model named PurchaseOrder with Id, PurchaseDate, Customer and Products.<br>
		2. Generate Razor Pages for Create, Read, Update, and Delete by using scaffold tool for model PurchaseOrder <br>
		3. Add EF migration for PurchaseOrder <br>
		4. Add search to PurchaseOrders page that allows to search by Id, PurchaseDate and Customer <br>
		</td>
	</tr>
	<tr>
		<td>
		Reporting: <br>
		- The system should allow store operators to export data in various formats (e.g., PDF, Excel). 
		</td>
		<td>
		1. Export customer in excel and pdf<br>
		2. Export purchase order in excel and pdf
		</td>
	</tr>
	 <tr>
		<td>
		    GitHub Actions
		</td>
		<td>
		1. Generate a GitHub Action that: build a .NET Application, deploys it in Azure App Service with Azure Credentials
		</td>
	</tr>
</table>

💡Those are just some examples about how interact with Copilot, depending on how you decide to approach the challenges you will need to change the prompt accordingly or submit new ones.

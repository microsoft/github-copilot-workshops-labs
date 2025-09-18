# Operations Hackathon 👩‍💻👨🏾‍💻
Welcome to the Operations Hackathon. The challenge is to deploy an infrastructure described in the "Challenge" section using the most modern development tools: GitHub Repos for code and GitHub Actions for automation, GitHub Codespaces as development environment and obtaining assistance from GitHub Copilot.

## Codespace Environment 💻
**Installed Software:** Terraform, Azure CLI  
**VS Code Extensions:** GitHub Copilot, Terraform, Azure

## Start the Hackathon 🏁
1) Click on 'Code' -> 'Select Codespaces tab' -> 'New with options...' 
2) Select the branch corresponding to your team (i.e. team1)
3) Select the 8 core machine size 
4) Start the Codespace and Happy coding 😊

### Terraform Development 
The Login to Azure has already been configured with the following environment variables (required by the Terraform CLI) accessible in the GitHub Codespace: ARM_CLIENT_ID, ARM_CLIENT_SECRET, ARM_TENANT_ID, ARM_SUBSCRIPTION_ID.
For more details visit the [Terraform documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret#configuring-the-service-principal-in-terraform).

In this way you can execute the Terraform commands:
```
terraform init, validate, plan, apply
```
💡The resources deployment must happen in an Azure resource group already created for your team and accessible with the configured credentials. The name of the resource group is: 'rg-hackathon-team-N' (replace N with wour team number). A storage account for the terraform state has already provisioned for use, the name of this storage account is 'sahacktfstateN' (replace N with your team number).

# Challenge 1: Application Infrastructure 🌐

The infrustructure must be created by IaaC in Azure by using Terraform and a storage account for the state. The resources must be deployed in an existing resource group.

The reference architecture for the Azure Infrastructure is composed of:
1. **Azure App Service**: This is a fully managed platform for building, deploying, and scaling web apps. You can use it to host the web application.  
2. **Azure SQL Database**: This is a fully managed relational database with built-in intelligence for high performance. You can use it to store the data collected from the app. The database would hold tables for customers and their respective prescription data. 
3. **[OPTIONAL] - Virtual Netowrk and Private Endpoint**: The AppService must reach the the Azure SQL Database over a private network
4. **[OPTIONAL] - Azure Front Door**: The application muste be exposed for security and delivery purpose by an Azure Front Door

💡Configure a Connection String named "DatabaseConnectionString" that will be used by the Application for access the database in the App Service.

# Challenge 2: CI/CD 🚀
The infrastructure must be deployed with the GitHub Actions. 

💡To connect to Azure, credentials are already configured for you as GitHub Actions secrets with those names: ARM_CLIENT_ID, ARM_CLIENT_SECRET, ARM_TENANT_ID, ARM_SUBSCRIPTION_ID. You can expose it as environment variables for the action.  
💡A skeleton of the GitHub Action has been created [.github/workflows/deploy-infrastructure.yml](.github/workflows/deploy-infrastructure.yml). Don not modify the trigger. Complete it with your code and make sure to launch it for your branch.

# GitHub Copilot sample prompts 🤖
Given the infrastructure requirments, try to ask to GitHub Copilot for help, following some suggestions:
<table>
	<tr><th>Requirements</th><th>Ask to GitHub Copilot…</th></tr>
	<tr>
		<td>The infrustructure must be created by IaaC in Azure  and a storage account must be used for the state.</td>
		<td>Generate Terraform file with azure provider and state on storage account</td>
  </tr>
	<tr>
		<td>
      		The resources must be deployed in existing resource group.
		</td>
		<td>
		  Reference an existing resource group
		</td>
	</tr>
	<tr>
		<td>Azure App Service Resource
		</td>
		<td>
		1. Generate code for Azure App Service for .NET App  <br>
		2. Configure a Log Analytics Workspace Based Application Insights for the App Service
		</td>
	</tr>
	<tr>
		<td>
		Azure SQL Database Resource
		</td>
		<td>
		1. Generate code for Azure SQL Database  <br>
		2. Add connection string to Azure SQL as Configuration to the App Service
		</td>
	</tr>
  <tr>
		<td>
		Virtual Netowrk and Private Endpoint
		</td>
		<td>
		1. Add a virtual network <br>
    		2. Connect the App Service to the Azure SQL Database through the virtual network <br>
		3. Add Private DNS Zone for SQL Server to existing VNET <br>
		4. Add record to Private DNS Zone for SQL Server Private Endpdoint IP
		</td>
	</tr>
   <tr>
		<td>
		Azure Front Door
		</td>
		<td>
		1. Add an Azure Front Door that exposes the Azure App Service
		</td>
	</tr>
	 <tr>
		<td>
		    GitHub Actions
		</td>
		<td>
		1. Generate a GitHub Action that deploys the Terraform in Azure
		</td>
	</tr>
</table>

💡Those are just some examples about how interact with Copilot, depending on how you decide to approach the challenges you will need to change the prompt accordingly or submit new ones.

**link for video**: https://drive.google.com/file/d/10CadLofsPsqF91X_xmDtuyDoHBO1QWIS/view?usp=sharing

**AWS Serverless Calculator **
This project is a cloud-based serverless calculator built using AWS services. It performs basic arithmetic operations (+, -, *, /, ^) and logs the results in Amazon DynamoDB. The application is hosted using AWS Amplify, with a backend powered by AWS Lambda and API Gateway.

**Features**
✅ Perform addition, subtraction, multiplication, division, and exponentiation.
✅ Fully serverless architecture for scalability and cost-efficiency.
✅ REST API using AWS API Gateway to connect frontend and backend.
✅ DynamoDB storage for tracking input values and results.
✅ CI/CD pipeline with AWS Amplify and GitHub for automated deployments.
✅ Secure access management using AWS IAM roles.

**Technologies Used**
Frontend: HTML, CSS, JavaScript, AWS Amplify
Backend: AWS Lambda (Python), API Gateway
Database: Amazon DynamoDB
Security: AWS IAM (Role-based Access Control)
Deployment & CI/CD: AWS Amplify, GitHub

**Architecture**
1️⃣ User inputs numbers and operation on the frontend.
2️⃣ API Gateway sends the request to AWS Lambda.
3️⃣ Lambda function processes the calculation.
4️⃣ The result is stored in DynamoDB and returned to the frontend.
5️⃣ AWS Amplify ensures continuous deployment from GitHub.

**How to Run the Project**
1. Setup Frontend (AWS Amplify)
Clone the repository from GitHub.
Deploy the frontend using AWS Amplify.
Connect GitHub for CI/CD integration.
2. Backend Configuration (AWS Lambda & API Gateway)
Create a Lambda function in AWS to handle calculations.
Set up an API Gateway to expose the Lambda function.
Use DynamoDB to store calculation logs.
3. Security & Permissions
Configure IAM roles for Lambda, API Gateway, and DynamoDB.

**API Endpoints**
Method : POST	Endpoint:/calculate	Description:Processes a calculation request
		
**Request Body Example:**

json
Copy
Edit
{
  "base": 5,
  "operation": "+",
  "exponent": 3
}
**Response Example:**

json
Copy
Edit
{
  "result": 8
}

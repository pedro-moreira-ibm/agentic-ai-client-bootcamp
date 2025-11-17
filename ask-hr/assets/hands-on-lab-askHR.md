
# 🧑‍💼 AskHR: Automate HR tasks with Agentic AI

## Table of Contents

- [Use Case description](#use-case-description)
- [Architecture](#architecture)
- [Instructions](#instructions)
  - [Open Agent Builder](#open-agent-builder)
  - [Create HR Agent](#create-hr-agent)
  - [Test HR Agent in preview](#test-hr-agent-in-preview)
  - [Test HR Agent in AI Chat](#test-hr-agent-ai-chat)

## Use Case Description

This use case targets developing and deploying an AskHR agent leveraging IBM watsonx Orchestrate, as depicted in the provided architecture diagram. This agent will empower employees to interact with HR systems and access information efficiently through conversational AI. 

In this lab we will build an HR agent in watsonx Orchestrate, leveraging tools and external knowledge to connect to a simulated Human Capital Management System. This agent retrieves relevant information from documents to answer user queries and  allows users to view and manage their profiles.

## Architecture

<img width="1000" alt="image" src="arch_diagm.png">


## Instructions

### Open Agent Builder

- Log in to IBM Cloud (cloud.ibm.com). Navigate to top left hamburger menu, then to Resource List. Open the AI/Machine Learning section. You should see a **watsonx Orchestrate** service, click to open.

  <img width="1000" alt="image" src="/environment-setup/assets/cloud-resource-list.png">

- Click the "Launch watsonx Orchestrate" button.

   <img width="1000" alt="image" src="/environment-setup/assets/cloud-wxo.png">

- Welcome to watsonx Orchestrate. Open the hamburger menu, click on the down arrow next to **Build**.  Then click on **Agent Builder**:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_1_v2.png">

### Create HR Agent
1. Click on **Create agent +**:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_2_v2.png">

1. Select **Create from scratch**, give your agent a name, e.g. `HR Agent`, and fill in the **Description** as shown below: 

   ```
   You are an agent who handles employee HR queries.  You provide short and crisp responses, keeping the output to 200 words or less.  You can help users check their profile data, retrieve latest time off balance, update title or address, and request time off. You can also answer general questions about company benefits.
   ```  
   Click on **Create**:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_3_v2.png">
<!--   
1. Click on the down arrow against **Model**. Select Model "llama-3-405b-instruct"

   <img width="1000" alt="image" src="hands-on-lab-assets/step_4_v2.png">
-->   
1. Select **Default** in **Agent style** section.

   <img width="1000" alt="image" src="hands-on-lab-assets/step_5_v3.png">
  
1. Scroll down the screen to the **Knowledge** section.
   Click on **Choose knowledge**.
   
   <img width="1000" alt="image" src="hands-on-lab-assets/step_6_v3.png">
  
1. Select **Upload files**.
   Click on **Next**.
   
   <img width="1000" alt="image" src="hands-on-lab-assets/step_7_v3.png">
     
1. Download the [Employee Benefits.pdf](/ask-hr/assets/Employee-Benefits.pdf) onto your system, then upload the file here. You can download the pdf by clicking on [Employee Benefits.pdf](/ask-hr/assets/Employee-Benefits.pdf) and then click on download icon in opened page as shown in image below.
      <img width="1000" alt="image" src="hands-on-lab-assets/step_7.1_v3.png">

      
   Once you upload the file, Click on **Next**.

   <img width="1000" alt="image" src="hands-on-lab-assets/step_8_v3.png">

1. Add the name "Employee Benefits" to the file. Also, copy the following description into the **Description** section and then click on **Save**:

   ```
   This knowledge base addresses the company's employee benefits, including parental leaves, pet policy, flexible work arrangements, and student loan repayment.
   ```
   
   <div align="center">
     <img width="1024" height="474" alt="image" src="https://github.com/user-attachments/assets/ad58437b-d055-416a-83a2-4c84517550f7" />
   </div>

1. Scroll down to the **Toolset** section. Click on **Add tool +**:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_9_v3.png">

1. Select **Add from OpenAPI file**:
   
   <div align="center">
     <img width="1467" height="999" alt="image" src="https://github.com/user-attachments/assets/3044aae4-0d1c-4de5-8b1c-08c9bb68b487" />
   </div>

1. Select **Import from file**:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_11_v3.png">

1. Drag and drop or click to upload the [hr.yaml](/ask-hr/assets/hr.yaml) file, then click on **Next**:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_12_v3.png">    

1. Select all the operations and click on **Done**:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_13_v3.png">

   In a real environment, these tools would equip your agent to connect with your enterprise applications (Salesforce, SAP, etc.).

1. Scroll down to the **Behavior** section. Insert the instructions below into the **Instructions** field:

   ```
   Use your knowledge base to answer general questions about employee benefits. 

   Use the tools to get or update user specific information.

   When user asks to show profile data or check time off balance or update title/address or request time off for the very first time,  first ask the user for their name,  then invoke the tool and then use the same name in the whole session without asking for the name again.

   When the user requests time off, convert the dates to YYYY-MM-DD format, e.g. 5/22/2025 should be converted to 2025-05-22 before passing the date to the post_request_time_off tool.
   ```
1. Turn on the toggle button for **Chat with documents**. Select **None** in **Citations show in webchat**. Turn on the toggle button for **Show agent**. Click on **Deploy** in the top right corner to deploy your agent:

   <img width="1000" alt="image" src="hands-on-lab-assets/step_14_v3.png">

### Test HR Agent in Preview
Test your agent in the preview chat on the right side by asking the following questions and validating the responses.  They should look similar to what is shown in the screenshots below:

```
What is the pet policy? 
```
<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13.png">

Ask the agent for your profile data. 

```
Show me my profile data.
```

When asked for your name, you should choose a name of one of the company's employees (e.g. "Victoria Baker"). Find the employees list by downloading the [Users_Data](/ask-hr/assets/users_data.xlsx) file.

After that, ask the agent to update your job title.

```
I'd like to update my title. 
```
<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_2.png">

Try the command below and update your address.
```
Update my address
```
After that, you can ask what is your time off balance.
```
What is my time off balance?
```
<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_3.png">

Request the time off by sending the message below:
```
Request time off
```

<div align="center">
  <img width="1550" height="1186" alt="image" src="https://github.com/user-attachments/assets/cca08ba8-68c2-4e9f-9555-31961ab9f08f" />
</div>

Please note that your start and end date may differ from the image presented above.

Check again your profile data to see all the changes you made.
```
Show my profile data.
```

<div align="center">
  <img width="1524" height="724" alt="image" src="https://github.com/user-attachments/assets/8705a4dc-a798-490d-a402-191b9964aaa6" />
</div>


### Adjust the Instructions of the Agent and keep exploring

Let's make some small adjustments on the Instructions of the Agent. More precisely, let's try to better organize the profile data, and instruct the agent to present the data in a table for easier readability.

1. Scroll down to the **Behavior** section (Section 1 in the image below). Insert the new instructions into the **Instructions** field:

   ```
   Use your knowledge base to answer general questions about employee benefits.

   Use the tools to get or update user specific information.

   When user asks to show profile data or check time off balance or update title/address or request time off for the very first time,  first ask the user for         their name,  then invoke the tool and then use the same name in the whole session without asking for the name again.
   
   When the user requests time off, convert the dates to YYYY-MM-DD format, e.g. 5/22/2025 should be converted to 2025-05-22 before passing the date to the           post_request_time_off tool.
   
   When user asks to see, change or update data, present the final information in a table for an easier readability and before that table, write something            similar to “This is the information associated to your current profile.”.
   ```

   <img width="1000" alt="image" src="hands-on-lab-assets/step_14_v3.png">

Refresh the Preview chat to make sure the new instructions are loaded.

<div align="center">
  <img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/06f252b0-991a-4021-8ec1-5eb7184c506c" />
</div>

<p>Ask the agent for your profile data. 

```
Show me my profile data.
```


You should now see the data in a nice and clean table.

<div align="center">
  <img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/0c52d30b-8880-461b-a153-01e05686f20a" />
</div>

Once again, request time off and after define a start and end date. Feel free to use the example below.

```
Request time off
```
```
Start date is 2025-12-01 and end date is 2025-12-06
```

When the agent answers, click on "Show Reasoning" and confirm that the agent is chosing the right tool to solve the task.

<div align="center">
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/fe958154-251d-46b3-9857-088ccfc82fa7" />
</div>

Let's make a completely different question and again analyze the reasoning of the agent.

```
Does my company organize team building activities
```
<div align="center">
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/9a3ab2f0-0dd6-40d7-8003-475d90668924" />
</div>

The agent recognized that to solve this task, it would not require one of the tools we previously tested. Instead, it found the answer on the "Employee-Benefits.pdf".

Feel free to scroll up in the chat and/or repeat any prompts we already tested, and explore the reasoning behind the agent's answers.

### Test HR Agent AI Chat


After completing your tests and once you’re ready to make the agent available to employees, click on "Deploy".

<div align="center">
  <img width="1905" height="956" alt="image" src="https://github.com/user-attachments/assets/4bb19e44-79ca-4b19-a6f6-ebaaeab9e207" />
</div>


# Congratulations 🎉 You’ve reached the end of the workshop! 
If you have any questions, please reach out to the instructors.


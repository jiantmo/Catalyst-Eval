from thinkingbox.common import Judge, TestContext
from thinkingbox.tools.judgeagent import JudgeAgent

"""!
scenario: fno
"""

#1.read
def test_read_CustTable(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Find the credit limit for a customer account on the CustTable page

        # Data
        {
          "company": "USMF",
          "AccountNum": "US-001"
        }
    """

    # Verify the response contains the credit limit information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the credit limit information for customer account 'US-001'?",
    )


#2.create
def test_create_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new customer record in the USMF company on the 'All customers' menu item in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "DE-006",
          "Name": "Sample Test Customer",
          "Type": "Organization",
          "CustomerGroup": "30",
          "Currency": "USD",
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the customer with account 'DE-006' and name 'Sample Test Customer' created successfully in company 'USMF'?",
    )


#3.update
def test_update_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Use MCP tools to complete this task:

        Update the credit limit of an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "DE-006",
          "CreditLimit": 50000
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the credit limit for customer DE-006 was updated to 50000?",
    )


#4.read
def test_read_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Find the credit limit for an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "DE-006"
        }
    """

    # Verify the response contains the correct credit limit
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message state the correct credit limit for customer DE-006?",
    )


#5.read
def test_read2_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Find the Phone (Telephone) number for an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "DE-001"
        }
    """

    # Verify the response contains the phone number information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the phone (telephone) number information for customer account 'DE-001'?",
    )


#6.delete
def test_delete_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "DE-006"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the customer DE-006 was deleted successfully?",
    )


#7.create
def test_create_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new product record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product type": "Item",
          "Product subtype": "Product",
          "Product number": "Z0001",
          "Product name": "Electronic widgets",
          "Retail category": "Laptops",
          "Description": "<Generated description>"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the product Z0001 : Electronic widgets was created successfully?",
    )


#8.update
def test_update_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the description of an existing product record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "Z0005",
          "Description": "High-performance electronic widget for retail customers."
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the description for product Z0005 was updated successfully?",
    )


#9.read
def test_read_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing product record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "Z0005"
        }
    """

    # Verify the response contains the product details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for product Z0005?",
    )


#10.delete
def test_delete_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing product record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "Z0005"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the product Z0005 was deleted successfully?",
    )


#11.create
def test_create_SalesTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new sales order record with two order lines in the USMF company in Dynamics 365 Finance and Operations.
        # Data
        {
          "dataAreaId": "USMF",
          "SalesOrderHeader": {
            "CustomerAccount": "US-001",
            "OrderDate": "2025-07-06",
            "CurrencyCode": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "OrderedQuantity": 10,
                "SalesPrice": 25.00,
                "SiteId": "1",
                "WarehouseId": "11"
              },
              {
                "ItemNumber": "M0003",
                "OrderedQuantity": 5,
                "SalesPrice": 40.00,
                "SiteId": "1",
                "WarehouseId": "11"
              }
            ]
          }
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the sales order was created successfully for customer account 'US-001' with two order lines (M0001 and M0003)?",
    )


#12.create
def test_create_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new purchase order record for a given vendor using default values where applicable.

        # Data
        {
          "company": "USSI",
          "VendorID": "US_SI_000009"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the purchase order for vendor US_SI_000009 was created successfully?",
    )


#13.update
def test_update_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Add a new line to an existing purchase order in the USSI company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USSI",
          "Purchse order": "00000254",
          "Vendor account": "000009",
          "Line": {
            "ProductName": "Electronic widgets",
            "ProcurementCategory": "Computers",
            "Quantity": 5,
            "UnitPrice": 150
          }
        }
    """

    # Verify the response confirms the line addition
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that a new line qith product name of Electronic widgets was added to purchase order 00000254 successfully?",
    )


#14.read
def test_read_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing purchase order in the USSI company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USSI",
          "PurchaseOrderNumber": "00000254"
        }
    """

    # Verify the response contains the purchase order details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for purchase order 00000254?",
    )


#15.delete
def test_delete_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing purchase order from the USSI company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USSI",
          "PurchaseOrderNumber": "00000254"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the purchase order 00000254 was deleted successfully?",
    )


#16.create
def test_create_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new worker record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FirstName": "Sophia",
          "LastName": "Doe",
          "EmploymentStartDate": "2025-07-16",
          "EmploymentType": "Warehouse",
          "WorkerType": "Employee",
          "EmploymentCategory": "Intern"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the worker record for Sophia Doe was created successfully?",
    )


#17.update
def test_update_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Add a contact information to the following worker in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FirstName": "Sophia",
          "LastName": "Doe",
          "Description": "Work",
          "Type": "Phone",
          "PrimaryPhone": "223-488-06-98"
        }
    """

    # Verify the response confirms the phone number addition
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the phone number 223-488-06-98 was added to worker Sophia Doe successfully?",
    )


#18.read
def test_read_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing worker record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "PersonnelNumber": "000895"
        }
    """

    # Verify the response contains the worker details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for worker with personnel number 000895?",
    )


#19.delete
def test_delete_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing worker record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "PersonnelNumber": "000895"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the worker with personnel number 000895 was deleted successfully?",
    )


#20.create
def test_create_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new bank account record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF CAN",
          "Name": "CAN currency account",
          "BankGroup": "BankUSA",
          "Routing number": "12345",
          "MainAccount": "110110"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the bank account 'USMF CAN' was created successfully?",
    )


#21.update
def test_update_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the name of an existing bank account in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF MXC",
          "Name": "Updated MXC currency account"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the bank account 'USMF MXC' name was updated to 'Updated MXC currency account' successfully?",
    )


#22.read
def test_read_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing bank account record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF MXC"
        }
    """

    # Verify the response contains the bank account details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for bank account 'USMF MXC'?",
    )


#23.delete
def test_delete_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing bank account record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF MXC"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the bank account 'USMF MXC' was deleted successfully?",
    )


#24.create
def test_create_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new data source in Data Management Framework in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "SourceName": "test_source5"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the data source 'test_source5' was created successfully?",
    )


#25.update
def test_update_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the description of an existing data source in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "SourceName": "test_source5",
          "Description": "This is test5"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the description for data source 'test_source5' was updated successfully?",
    )


#26.read
def test_read_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing data source in data management from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "SourceName": "test_source5"
        }
    """

    # Verify the response contains the data source details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for data source 'test_source5'?",
    )


#27.delete
def test_delete_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing data source from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "SourceName": "test_source5"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the data source 'test_source5' was deleted successfully?",
    )


#28.create
def test_create_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense report for a business trip with specified expenses and payment methods.

        # Data
        {
          "company": "USMF",
          "reportTitle": "testing_expense5",
          "expenses": [
            {
              "Expense Category": "Car rental",
              "amount": 110,
              "currency": "USD",
              "Payment Method": "Credit card"
            }
          ]
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the expense report 'testing_expense5' was created successfully?",
    )


#29.update
def test_update_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Add a new expense item to an existing expense report in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "reportTitle": "testing_expense5",
          "expenses": [
            {
              "Expense Category": "Conference",
              "amount": 150,
              "currency": "USD",
              "Payment Method": "Credit card"
            }
          ]
        }
    """

    # Verify the response confirms the addition
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the new expense item was added to expense report 'testing_expense5' successfully?",
    )


#30.read
def test_read_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve all the details of an existing expense report from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Expense report number": "000037"
        }
    """

    # Verify the response contains the expense report details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide all the details for expense report number 000037?",
    )


#31.delete
def test_delete_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing expense report from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "reportTitle": "testing_expense5"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the expense report 'testing_expense5' was deleted successfully?",
    )


#32.create
def test_create_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new warehouse in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "mcp-test5",
          "Site": 1,
          "Type": "Default"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the warehouse 'mcp-test5' was created successfully?",
    )


#33.update
def test_update_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Assign a quarantine warehouse to an existing warehouse in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "mcp-test5",
          "QuarantineWarehouse": 18
        }
    """

    # Verify the response confirms the assignment
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the quarantine warehouse 18 was assigned to warehouse 'mcp-test5' successfully?",
    )


#34.read
def test_read_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing warehouse from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "mcp-test5"
        }
    """

    # Verify the response contains the warehouse details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for warehouse 'mcp-test5'?",
    )


#35.delete
def test_delete_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing warehouse record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "mcp-test5"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the warehouse 'mcp-test5' was deleted successfully?",
    )


#36.create
def test_create_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new language record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "LanguageID": "test_language",
          "Description": "New language"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the language 'test_language' was created successfully?",
    )


#37.update
def test_update_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the description of an existing language record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "LanguageID": "test_language",
          "Description": "Test Language Updated"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the description for language 'test_language' was updated to 'Test Language Updated' successfully?",
    )


#38.read
def test_read_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the details of an existing language record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Language code": "test_language"
        }
    """

    # Verify the response contains the language details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for language 'test_language'?",
    )


#39.delete
def test_delete_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing language record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "LanguageID": "test_language"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the language 'test_language' was deleted successfully?",
    )


#40.create
def test_create_HcmApplicantListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new candidate record in the USMF company in Dynamics 365 Finance and Operations using the Candidates form.

        # Data
        {
          "company": "USMF",
          "FirstName": "John",
          "LastName": "Smith",
          "Email": "john.smith@example.com",
          "Phone": "555-6789",
          "ResumeAttachment": "Resume_JohnSmith.pdf"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the candidate John Smith was created successfully?",
    )


#41.update
def test_update_HcmApplicantListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the contact details of an existing candidate record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FirstName": "John",
          "LastName": "Smith",
          "Phone": "555-9999"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the phone number for candidate John Smith was updated to 555-9999 successfully?",
    )


#42.read
def test_read_HcmApplicantListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the details of an existing candidate record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Applicant": "000056"
        }
    """

    # Verify the response contains the candidate details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for candidate with Applicant ID '000056'?",
    )


#43.delete
def test_delete_HcmApplicantListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing candidate record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FirstName": "John",
          "LastName": "Smith"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the candidate John Smith was deleted successfully?",
    )


#44.create
def test_create_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new currency exchange rate in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "AMD",
          "ToCurrency": "AFN",
          "ConversionFactor": 10
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the currency exchange rate from AMD to AFN was created successfully?",
    )


#45.update
def test_update_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the valid from date between AMD and AFN for a given date in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "AMD",
          "ToCurrency": "AFN",
          "FromDate": "7/11/2025"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the valid from date for the exchange rate from AMD to AFN was updated to 7/11/2025 successfully?",
    )


#46.read
def test_read_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the exchange rate for a specific entry in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "EUR",
          "ToCurrency": "JPY"
        }
    """

    # Verify the response contains the exchange rate details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the exchange rate details for EUR to JPY?",
    )


#47.delete
def test_delete_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing currency exchange rate between AMD and AFN in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "AMD",
          "ToCurrency": "AFN"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the currency exchange rate from AMD to AFN was deleted successfully?",
    )


#48.create
def test_create_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new unit conversion rule from Celsius to Fahrenheit in the USMF company in Dynamics 365 Finance and Operations using the advanced formula layout.

        # Data
        {
          "company": "USMF",
          "FromUnit": "°C",
          "ToUnit": "°F",
          "Rounding": "To nearest",
          "FormulaLayout": "Advanced",
          "ConversionFormula": {
            "Multiplier1": 1.0,
            "Numerator1": 9,
            "Denominator1": 5,
            "Addend1": 0.0,
            "Addend2": 32.0
          },
          "Definition": "1 °C = (9/5) * °C + 32 °F"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the unit conversion rule from °C to °F was created successfully?",
    )


#49.update
def test_update_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the conversion formula for the Celsius to Fahrenheit rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromUnit": "°C",
          "ToUnit": "°F",
          "Rounding": "To nearest",
          "FormulaLayout": "Advanced",
          "ConversionFormula": {
            "Multiplier1": 1.0,
            "Numerator1": 9,
            "Denominator1": 5,
            "Addend1": 0.0,
            "Addend2": 33.0
          },
          "Definition": "1 °C = (9/5) * °C + 33 °F"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the unit conversion formula from °C to °F was updated with Addend2 changed to 33.0 successfully?",
    )


#50.read
def test_read_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the unit conversion rule from t to lb in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromUnit": "t",
          "ToUnit": "lb"
        }
    """

    # Verify the response contains the unit conversion details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the unit conversion rule details from t to lb?",
    )


#51.delete
def test_delete_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete the unit conversion rule from Celsius to Fahrenheit in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
        #   "FromUnit": "°C",
          "FromUnit": "dz",
        #   "ToUnit": "°F"
          "ToUnit": "ea"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the unit conversion rule from dz to ea was deleted successfully?",
    )


#52.create
def test_create_CustPaym(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new customer payment journal in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Company Name": "USMF",
          "Name": "CustPay",
          "Description": "Payment by customer",
          "Modified by": "test"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the customer payment journal 'CustPay' was created successfully?",
    )


#53.update
def test_update_CustPaym(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Modify an existing customer payment journal in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "USMF",
          "Journal batch number": "00647",
          "Description": "This is my test payment"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the customer payment journal with journal batch number 00647 was modified successfully?",
    )


#54.read
def test_read_CustPaym(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the customer payment journal information in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "USMF",
          "Journal batch number": "00638"
        }
    """

    # Verify the response contains the customer payment information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the customer payment journal information for journal batch number 00638?",
    )


#55.delete
def test_delete_CustPaym(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete a customer payment journal in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Journal batch number": "00647"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the customer payment journal with batch number 00647 was deleted successfully?",
    )


#56.create
def test_create_LedgerJournalTable5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new vendor payment in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "VendPay",
          "Description": "Payment by Vendor",
          "account": "1001"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the vendor payment 'VendPay' was created successfully?",
    )


#57.update
def test_update_LedgerJournalTable5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Modify an existing vendor payment in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Journal batch number": "00647",
          "credit": "100"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the vendor payment with journal batch number 00647 was modified with credit 100 successfully?",
    )


#58.read
def test_read_LedgerJournalTable5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the vendor payment information in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "USMF",
          "Journal batch number": "00469"
        }
    """

    # Verify the response contains the vendor payment information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the vendor payment information for journal batch number 00469?",
    )


#59.delete
def test_delete_LedgerJournalTable5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete a vendor payment information in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "USMF",
          "Journal batch number": "00647"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the vendor payment with journal batch number 00647 was deleted successfully?",
    )


#60.create
def test_create_AssetTable(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new fixed asset record in the USMF company in Dynamics 365 Finance and Operations for a building asset.

        # Data
        {
          "company": "USMF",
          "FixedAssetGroup": "Buildings",
          "Name": "building-test2",
          "Type": "Financial",
          "MajorType": "Own_Build",
          "PropertyType": "Fixed asset",
          "Quantity": 1
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the fixed asset 'building-test2' was created successfully in the USMF company?",
    )


#61.update
def test_update_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Modify an existing fixed asset record in the USMF company in Dynamics 365 Finance and Operations for a building asset.

        # Data
        {
          "company": "USMF",
          "FixedAssetnumber": "BUIL-000012",
          "Unit cost": "100"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the fixed asset BUIL-000012 was modified with unit cost 100 successfully?",
    )


#62.read
def test_read_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the information of an existing fixed asset record in the USMF company in Dynamics 365 Finance and Operations for a building asset.

        # Data
        {
          "company": "USMF",
          "FixedAssetnumber": "BUIL-000001"
        }
    """

    # Verify the response contains the fixed asset information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for fixed asset BUIL-000001?",
    )


#63.delete
def test_delete_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing fixed asset record in the USMF company in Dynamics 365 Finance and Operations for a building asset.

        # Data
        {
          "company": "USMF",
          "FixedAssetnumber": "BUIL-000012"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the fixed asset BUIL-000012 was deleted successfully in the USMF company?",
    )


#64.create
def test_create_BudgetTransactions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new budget register entry in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Budget model": "FY2018",
          "Budget code": "CarryForward"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the budget register entry with budget model FY2018 and budget code CarryForward was created successfully?",
    )


#65.update
def test_update_BudgetTransactions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Modify an existing budget register record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Budget model": "FY2018",
          "Budget code": "CarryForward",
          "Reason code": "AdJ"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the budget register record with budget model FY2018 and budget code CarryForward was modified with reason code AdJ successfully?",
    )


#66.read
def test_read_BudgetTransactions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the information an existing budget register record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Entry number": "USMF000004"
        }
    """

    # Verify the response contains the budget register information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for budget register record with entry number USSI000004?",
    )


#67.delete
def test_delete_BudgetTransactions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing budget register record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Entry number": "USMF000018"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the budget register record with entry number USMF000018 was deleted successfully?",
    )


#68.create
def test_create_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new product in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "114",
          "Item number": "114",
          "Inventory unit": "°C",
          "Purchase unit": "°C",
          "Sales unit": "°C"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the product '114' was created successfully?",
    )


#69.update
def test_update_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing product in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Item number": "114",
          "Product name": "test_product"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the product '114' was updated with product name 'test_product' successfully?",
    )


#70.read
def test_read_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve information of an existing product in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Item number": "4403"
        }
    """

    # Verify the response contains the product information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for product with item number '4403'?",
    )


#71.delete
def test_delete_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing product record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Item number": "114"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the product with item number '114' was deleted successfully?",
    )


#72.create
def test_create_SystemNotificationBlockingActivity(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new high-volume system notification rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "User ID": "ALICIA",
          "Rule ID": 85,
          "High-volume threshold": 50
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the high-volume system notification rule with Rule ID 85 for User ID 'ALICIA' with threshold 50 was created successfully?",
    )


#73.update
def test_update_SystemNotificationBlockingActivity(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing high-volume system notification rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "User ID": " ALICIA ",
          "High-volume threshold": 100,
          "Is blocked": 1
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the high-volume system notification rule for User ID 'ALICIA' was updated with threshold 100 and blocked status successfully?",
    )


#74.read
def test_read_SystemNotificationBlockingActivity(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve information about an existing high-volume system notification rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "User ID": "APRIL"
        }
    """

    # Verify the response contains the notification rule information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the high-volume system notification rule for User ID 'APRIL'?",
    )


#75.delete
def test_delete_SystemNotificationBlockingActivity(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing high-volume system notification rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "User ID": "ALICIA"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the high-volume system notification rule for User ID 'ALICIA' was deleted successfully?",
    )


#76.create
def test_create_SysThrottlingPriorityMappingTable(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new priority mapping in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "authentication type": "User",
          "User ID": "ARNIE",
          "priority": "Low"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the priority mapping for User ID 'ARNIE' with authentication type 'User' and priority 'Low' was created successfully?",
    )


#77.update
def test_update_SysThrottlingPriorityMappingTable(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing priority mapping in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "User ID": "ARNIE",
          "priority": "Medium"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the priority mapping for User ID 'ARNIE' was updated with priority 'Medium' successfully?",
    )


#78.read
def test_read_SysThrottlingPriorityMappingTable(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve information about an existing priority mapping in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "User ID": "BROOKE"
        }
    """

    # Verify the response contains the priority mapping information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the priority mapping for User ID 'BROOKE'?",
    )


#79.delete
def test_delete_SysThrottlingPriorityMappingTable(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing priority mapping in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "User ID": "ARNIE"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the priority mapping for User ID 'ARNIE' was deleted successfully?",
    )


#80.create
def test_create_SIGReasonCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new electronic signature reason in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Reason code": "test_sig",
          "Description": "This is a test signature reason"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the electronic signature reason with reason code 'test_sig' and description 'This is a test signature reason' was created successfully?",
    )


#81.update
def test_update_SIGReasonCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing electronic signature reason in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Reason code": "test_sig",
          "Description": "This is an updated signature reason"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the electronic signature reason with reason code 'test_sig' was updated with description 'This is an updated signature reason' successfully?",
    )


#82.read
def test_read_SIGReasonCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the information of an existing electronic signature reason in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Reason code": "SOX"
        }
    """

    # Verify the response contains the electronic signature reason information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the electronic signature reason with reason code 'SOX'?",
    )


#83.delete
def test_delete_SIGReasonCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing electronic signature reason in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Reason code": "test_sig"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the electronic signature reason with reason code 'test_sig' was deleted successfully?",
    )


#84.create
def test_create_SysEmailRetrySchedule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new retry schedule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "retry delay": 1,
          "measurement": "Days"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the retry schedule with retry delay 1 and measurement 'Days' was created successfully?",
    )


#85.update
def test_update_SysEmailRetrySchedule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing retry schedule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "delay period": 2,
          "retry delay": 1,
          "measurement": "Hours"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the retry schedule was updated with delay period 2, retry delay 1, and measurement 'Hours' successfully?",
    )


#86.read
def test_read_SysEmailRetrySchedule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve information of an existing retry schedule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "delay period": 1
        }
    """

    # Verify the response contains the retry schedule information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the retry schedule with delay period 1?",
    )


#87.delete
def test_delete_SysEmailRetrySchedule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing retry schedule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "delay period": 2
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the retry schedule with delay period 2 was deleted successfully?",
    )


#88.create
def test_create_SysSecSegregationOfDutiesRule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new segregation of duties rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "rule_test1",
          "First duty": "Access employee development workspace",
          "Second duty": "Access benefits workspace",
          "severity": "Low"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the segregation of duties rule 'rule_test1' was created successfully with first duty 'Access employee development workspace' and second duty 'Access benefits workspace'?",
    )


#89.update
def test_update_DutySegregationRule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing segregation of duties rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "rule_test1",
          "severity": "High"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the segregation of duties rule 'rule_test1' was updated with severity 'High' successfully?",
    )


#90.read
def test_read_DutySegregationRule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve an existing segregation of duties rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "new_rule"
        }
    """

    # Verify the response contains the segregation of duties rule information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the segregation of duties rule 'new_rule'?",
    )


#91.delete
def test_delete_DutySegregationRule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing segregation of duties rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "rule_test1"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the segregation of duties rule 'rule_test1' was deleted successfully?",
    )


#92.create
def test_create_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new asset acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "test_method",
          "Description": "This is a test."
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the asset acquisition method 'test_method' was created successfully with description 'This is a test.'?",
    )


#93.update
def test_update_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "test_method",
          "Description": "Updated method"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the acquisition method 'test_method' was updated with description 'Updated method' successfully?",
    )


#94.read
def test_read_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve information of an existing acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "DONATION"
        }
    """

    # Verify the response contains the acquisition method information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the acquisition method 'DONATION'?",
    )


#95.delete
def test_delete_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "test_method"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the acquisition method 'test_method' was deleted successfully?",
    )


#96.create
def test_create_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "test_code",
          "Description": "This is a test asset code."
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the asset activity code 'test_code' was created successfully with description 'This is a test asset code.'?",
    )


#97.update
def test_update_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "test_code",
          "Description": "This is an updated description."
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the asset activity code 'test_code' was updated with description 'This is an updated description.' successfully?",
    )


#98.read
def test_read_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve information on an existing asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "REMODEL"
        }
    """

    # Verify the response contains the asset activity code information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the asset activity code 'REMODEL'?",
    )


#99.delete
def test_delete_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "test_code"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the asset activity code 'test_code' was deleted successfully?",
    )


#100.create
def test_create_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "Medium",
          "Description": "Medium condition"
        }
    """

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the fixed asset condition 'Medium' was created successfully with description 'Medium condition'?",
    )


#101.update
def test_update_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "Medium",
          "Description": "Updated Medium condition"
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the fixed asset condition 'Medium' was updated with description 'Updated Medium condition' successfully?",
    )


#102.read
def test_read_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve information of an existing fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "POOR"
        }
    """

    # Verify the response contains the fixed asset condition information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the fixed asset condition 'POOR'?",
    )


#103.delete
def test_delete_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Delete an existing fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "Medium"
        }
    """

    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the fixed asset condition 'Medium' was deleted successfully?",
    )

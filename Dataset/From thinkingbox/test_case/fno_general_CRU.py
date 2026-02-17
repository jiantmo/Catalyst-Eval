from thinkingbox.common import Judge, TestContext
from thinkingbox.tools.judgeagent import JudgeAgent
from thinkingbox.tools.fno_test_helper import fno_test_helper

"""!
scenario: fno
"""


# 1.read
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
        validation_question="Is the credit limit for customer account 'US-001' $500,000.0?",
    )


# 2.create
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
        validation_question="Was the customer with account 'DE-006' and name 'Sample Test Customer' created successfully in company 'USMF'?  Use the CustomersV3 OData endpoint to validate the creation.",
    )


# 3.update
def test_update_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Use MCP tools to complete this task:

        Update the credit limit of an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "DE-001",
          "CreditLimit": $50,000.0
        }
    """

    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Is the credit limit for customer DE-001 updated to $50,000.0?  Use the CustomersV3 OData endpoint to validate the update.  Use the CustomersV3 OData endpoint with cross-company=true and filter=(dataAreaId eq 'USMF' and CustomerAccount eq 'DE-001') to find and validate the customer record.",
    )


# 4.read
def test_read_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Find the credit limit expiration date for an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "US-001"
        }
    """
    # Verify the response contains the correct credit limit
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the response say that the customer's credit limit expiration date is December 31, 2019?",
    )


# 5.read
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
        validation_question="Is the phone (telephone) number for customer account 'DE-001' 01234 56789?",
    )


# 6.create
def test_create_EcoResDistinctProductListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the product Z0001 : Electronic widgets was created successfully?  Use the ProductsV2 OData endpoint with cross-company=true and filter=(ProductNumber eq 'Z0001') to validate the creation.",
    )


# 7.update
def test_update_EcoResDistinctProductListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update the description of an existing product record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "0001",
          "Description": "High-performance electronic widget for retail customers."
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the description for product 0001 was updated successfully?  Use the ProductsV2 OData endpoint to validate the update.  Use the ProductNumber and dataAreaId filters to find the product.",
    )


# 8.read
def test_read_EcoResDistinctProductListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Retrieve details of an existing product record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "0002"
        }
    """
    # Verify the response contains the product details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for product 0002?",
    )


# 9.create
def test_create_SalesTableListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Create a new sales order record with two order lines in the USMF company in Dynamics 365 Finance and Operations.  Use the SalesOrderLines array below to specify the order lines.
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
        validation_question="Does the message confirm that the sales order was created successfully for customer account 'US-001' with two order lines (M0001 and M0003)?  Use the SalesOrderHeadersV4 and SalesOrderLinesV3 OData endpoints to validate the creation.  Use the SalesOrderNumber from the response as a filter to find and validate the sales order header and lines.",
    )


# 10.create
def test_create_PurchTableListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Create a new purchase order record for a given vendor using default values where applicable.

        # Data
        {
          "company": "USMF",
          "VendorID": "US-101"
        }
    """
    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the purchase order for vendor US-101 is created successfully?  Use the PurchaseOrderHeadersV2 OData endpoint with dataAreaId and PurchaseOrderNumber as filters to find and validate the purchase order record.")


# 11.update
def test_update_PurchTableListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Add a new line to an existing purchase order in the USSI company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USSI",
          "Purchse order": "00000227",
          "Vendor account": "US_SI_000006",
          "Line": {
            "Item number": "S0012",
            "Quantity": 5,
            "UnitPrice": 150
          }
        }
    """
    # Verify the response confirms the line addition
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that a new line with product name of Hardware: Desktop was added to purchase order 00000227 successfully?  Use the PurchaseOrderLinesV2 OData endpoint with dataAreaId and PurchaseOrderNumber as filters to find and validate the purchase order line record.",
    )


# 12.read
def test_read_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing purchase order in the USSI company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USSI",
          "PurchaseOrderNumber": "00000227"
        }
    """
    # Verify the response contains the purchase order details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the purchase order 00000227 has product name OFFICE AND DESK ACCESSORIES?",
    )


# 13.create
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
        validation_question="Does the message confirm that the worker record for Sophia Doe was created successfully?  Use the Workers OData endpoint with filter FirstName eq 'Sophia' and LastName eq 'Doe' to find and validate the worker record.",
    )


# 14.update
def test_update_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Add a contact information to the following worker in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FirstName": "Sara",
          "LastName": "Davis",
          "Description": "Work",
          "Type": "Phone",
          "PrimaryPhone": "223-488-06-98"
        }
    """
    # Verify the response confirms the phone number addition
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the phone number 223-488-06-98 was added to worker Sara Davis successfully?  Use the WorkerContacts OData endpoint and filter with PersonnelNumber eq '000065' and Locator eq '223-488-06-98' to find and validate the data.",
    )


# 15.read
def test_read_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing worker record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "PersonnelNumber": "000065"
        }
    """
    # Verify the response contains the worker details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Is the worker with personnel number 000065 Sara Davis with a phone number 415 555-5098?",
    )


# 16.create
def test_create_BankAccountTableListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the bank account 'USMF CAN' was created successfully?  Use the BankAccounts OData endpoint with filter BankAccountId eq 'USMF CAN' to validate the creation.",
    )


# 17.update
def test_update_BankAccountTableListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update the name of an existing bank account in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF EUR",
          "Name": "Updated EUR currency account"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the bank account 'USMF EUR' name was updated to 'Updated EUR currency account' successfully?  Use the BankAccounts OData endpoint with filter BankAccountId eq 'USMF EUR' to validate the update.",
    )


# 18.read
def test_read_BankAccountTableListPage(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Retrieve details of an existing bank account record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF EUR"
        }
    """
    # Verify the response contains the bank account details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Is the bank account number for the bank account 'USMF EUR' 23456?",
    )


# 19.create
def test_create_DM_DataManagementWorkspaceMenuItem(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the data source 'test_source5' was created successfully?  There are no OData endpoints to validate this data, so base the validation solely on the agent's response.",
    )


# 20.update
def test_update_DM_DataManagementWorkspaceMenuItem(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update the description of an existing data source in the USMF company in Dynamics 365 Finance and Operations.  Only use the form* tools for this task.

        # Data
        {
          "company": "USMF",
          "SourceName": "EXCEL",
          "Description": "This is test5 - not Excel"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the description for data source 'EXCEL' was updated successfully?  There are no OData endpoints to validate this data, so base the validation solely on the agent's response.",
    )


# 21.read
def test_read_DM_DataManagementWorkspaceMenuItem(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Retrieve details including the Row Delimiter of an existing data source in data management from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "SourceName": "TabSeparated"
        }
    """
    # Verify the response contains the data source details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the row delimiter for data source 'TabSeparated' contain CR & LF?  There are no OData endpoints to validate this data, so base the validation solely on the agent's response.",
    )


# 22.create
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
        validation_question="Does the message confirm that the expense report 'testing_expense5' was created successfully?  Use the ExpMobileReports OData endpoint with filter ReferenceDataAreaId eq 'USMF' and Txt2 eq 'testing_expense5' to validate the creation.  The Txt2 field should match the report title.",
    )


# 23.update
def test_update_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    init:
        fnoproxy:
            ExpMobileReports: { Operation: "Create", Key:{ExpNumber: "@Out"}, Txt2: "Expense update test", LegalEntity_DataArea: "USMF", ReferenceDataAreaId: "USMF", InterCompanyLE: "USMF" }
    query: |
        # Task
        Update expense report "{init[fnoproxy][ExpMobileReports][ExpNumber]}" by adding a new expense.  Once processing has completed, return the ExpenseReportNumber and output in json format.

        # Data
        {
          "company": "USMF",
          "expenses": [
            {
              "Expense Category": "Conference",
              "amount": 150,
              "currency": "USD",
            }
          ]
        }
    """

    expense_report_number = fno_test_helper.parse_response_for_value(x.response, "ExpenseReportNumber")

    # Verify the response confirms the addition
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question=f"Does the message confirm that the new expense item was added to expense report number '{expense_report_number}' successfully?  Use the Expenses OData endpoint with filter LegalEntityDataAreaId eq 'USMF' and ExpenseReportNumber eq {expense_report_number} to validate the addition.",
    )


# 24.read
def test_read_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    init:
        fnoproxy:
            ExpMobileReports: { Operation: "Create", Key:{ExpNumber: "@Out"}, Txt2: "Expense read test", LegalEntity_DataArea: "USMF", ReferenceDataAreaId: "USMF", InterCompanyLE: "USMF" }
    query: |
        Retrieve all the details of existing expense report "{init[fnoproxy][ExpMobileReports][ExpNumber]}".  Once processing has completed, return the ExpenseReportNumber and output in json format.
    """

    expense_report_number = fno_test_helper.parse_response_for_value(x.response, "ExpenseReportNumber")

    # Verify the response contains the expense report details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question=f"Does the message provide all the details for expense report number {expense_report_number}?",
    )



# 25.create
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
        validation_question="Does the message confirm that the warehouse 'mcp-test5' was created successfully?  Use the Warehouses OData endpoint with dataAreaId and WarehouseId as filters to find and validate the warehouse record.",
    )

# 26.update
def test_update_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Assign a quarantine warehouse to an existing warehouse in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "12-802",
          "QuarantineWarehouse": 18
        }
    """
    # Verify the response confirms the assignment
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the quarantine warehouse 12-802 was assigned to quarantine warehouse 18 successfully?  Use the Warehouse OData endpoint with dataAreaId and WarehouseId as filters to find and validate the warehouse record.",
    )


# 27.read
def test_read_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve details of an existing warehouse from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "22"
        }
    """
    # Verify the response contains the warehouse details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide that the associated Quarantine warehouse is 28 and Transit warehouse is 29?",
    )


# 28.create
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
        validation_question="Does the message confirm that the language 'test_language' was created successfully?  Use the LanguageCodes OData endpoint with filter LanguageCodeId to find and validate the language record.",
    )


# 29.update
def test_update_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update the description of an existing language record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "LanguageID": "Spanish",
          "Description": "Hola"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the description for language 'Spanish' was updated to 'Hola' successfully?  Use the LanguageCodes OData endpoint with filter LanguageCodeId to find and validate the language record.",
    )


# 30.read
def test_read_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Retrieve the details of an existing language record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Language code": "Spanish"
        }
    """
    # Verify the response contains the language details
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the details for language 'Spanish'?",
    )

# These tests are disabled because they require Human Resources > Setup > Human resources parameters > Recruitment to be "HR Recruitment".  All demo companies currently have this set to "Recruitment projects", and this field was not added to HRMParametersEntity, so it can't be updated via OData.
# 31.create
# def test_create_HcmApplicantListPage(
#     x: TestContext, judge: Judge, judgeAgent: JudgeAgent
# ):
#     """!
#     query: |
#         # Task
#         Create a new candidate record in the USMF company in Dynamics 365 Finance and Operations using the Candidates form.

#         # Data
#         {
#           "company": "USMF",
#           "FirstName": "John",
#           "LastName": "Smith",
#           "Email": "john.smith@example.com",
#           "Phone": "555-6789",
#           "ResumeAttachment": "Resume_JohnSmith.pdf"
#         }
#     """
#     # Verify the response confirms the creation
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the message confirm that the candidate John Smith was created successfully?",
#     )


# # 32.update
# def test_update_HcmApplicantListPage(
#     x: TestContext, judge: Judge, judgeAgent: JudgeAgent
# ):
#     """!
#     query: |
#         # Task
#         Update the contact details of an existing candidate record in the USMF company in Dynamics 365 Finance and Operations.

#         # Data
#         {
#           "company": "USMF",
#           "FirstName": "John",
#           "LastName": "Emory",
#           "Phone": "555-9999"
#         }
#     """
#     # Verify the response confirms the update
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the message confirm that the phone number for candidate John Emory was updated to 555-9999 successfully?",
#     )


# # 33.read
# def test_read_HcmApplicantListPage(
#     x: TestContext, judge: Judge, judgeAgent: JudgeAgent
# ):
#     """!
#     query: |
#         # Task
#         Retrieve the details of an existing candidate record from the USMF company in Dynamics 365 Finance and Operations.

#         # Data
#         {
#           "company": "USMF",
#           "Applicant": "000026"
#         }
#     """
#     # Verify the response contains the candidate details
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Is the candidate with Applicant ID '000026' has the highest degree Bachelor?",
#     )


# 34.create
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
        validation_question="Does the message confirm that the currency exchange rate from AMD to AFN was created successfully?  Use the ExchangeRates OData endpoint with filter (FromCurrency eq 'AMD' and ToCurrency eq 'AFN') to validate the creation.",
    )


# 35.update
def test_update_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Add a new currency exchange rate between USD and INR for a given date in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "USD",
          "ToCurrency": "INR",
          "FromDate": "11/11/2025"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the valid from date for the exchange rate from USD to INR was updated to 11/11/2025 successfully?  Use the ExchangeRates OData endpoint and filter (FromCurrency eq 'USD' and ToCurrency eq 'INR') to validate the update.",
    )


# 36.read
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
        validation_question="Is the exchange rate between EUR to JPY 98.4?",
    )


# 37.create
def test_create_UnitOfMeasureConversion(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
          "Definition": "1 °F = (9/5) * °C + 32"
        }
    """
    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the unit conversion rule from °C to °F was created successfully?  Use the UnitOfMeasureConversions OData endpoint to validate the creation with filter=(FromUnitSymbol eq '°C' and ToUnitSymbol eq '°F') to validate the creation.",
    )


# 38.update
def test_update_UnitOfMeasureConversion(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update the conversion formula for the "km to m" rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromUnit": "km",
          "ToUnit": "m",
          "Rounding": "Down",
          "Definition": "1 km = 1000 m"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the unit conversion formula from km to m have the Rounding text 'Down'? Use the UnitOfMeasureConversions OData endpoint to validate the creation with filter=(FromUnitSymbol eq 'km' and ToUnitSymbol eq 'm') to validate the update.",
    )


# 39.read
def test_read_UnitOfMeasureConversion(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message provide the unit conversion rule details from t to lb as 1t = 2,200 lb?",
    )


# 40.create
def test_create_LedgerJournalTable_CustPaym(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Create a new customer payment journal in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Company Name": "USMF",
          "Name": "CustPay",
          "Description": "Payment by customer",
          "Modified by": "testUser"
        }
    """
    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the customer payment journal 'CustPay' was created successfully?  Use the CustomerPaymentJournalHeaders OData endpoint with dataAreaId and JournalBatchNumber as filters to find and validate the customer payment journal record.",
    )


# 41.update
def test_update_LedgerJournalTable_CustPaym(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Modify an existing customer payment journal in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "USMF",
          "Journal batch number": "00591",
          "Description": "This is my test payment"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the customer payment journal with journal batch number 00591 was modified successfully?  Use the CustomerPaymentJournals OData endpoint with dataAreaId and JournalBatchNumber as filters to find and validate the customer payment journal record.",
    )


# 42.read
def test_read_LedgerJournalTable_CustPaym(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Retrieve the customer payment journal information in the USMF company in Dynamics 365 Finance and Operations.  Use the form* tools for this task becuase the entity does not return enough of the data.

        # Data
        {
          "Name": "USMF",
          "Journal batch number": "00475"
        }
    """
    # Verify the response contains the customer payment information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the journal batch number 00475 have a description of 'Customer Payment' and modified by ABruer?",
    )


# 43.create
def test_create_LedgerJournalTable5(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Create a new vendor payment in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Name": "VendPay",
          "Description": "Payment by Vendor123",
          "account": "1001"
        }
    """
    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the vendor payment 'VendPay' was created successfully?  Use the VendorPaymentJournalHeaders OData endpoint with dataAreaId and Description as filters to find and validate the vendor payment journal record.",
    )


# 44.update
def test_update_LedgerJournalTable5(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Modify an existing vendor payment in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Journal batch number": "00468",
          "credit": "100"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the vendor payment with journal batch number 00468 was modified with credit 100 successfully?  Use the VendorPaymentJournalHeaders OData endpoint with dataAreaId and JournalBatchNumber as filters to find and validate the vendor payment journal record.",
    )


# 45.read
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
        validation_question="Does the journal batch number 00469 have offset account 'USMF OPER'?",
    )


# 46.create
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
        validation_question="Does the message confirm that the fixed asset 'building-test2' was created successfully in the USMF company?  Use the FixedAssetsV2 OData endpoint with filter (dataAreaId eq 'USMF' and Name eq 'building-test2') to validate the creation.",
    )


# 47.update
def test_update_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Modify an existing fixed asset record in the USMF company in Dynamics 365 Finance and Operations for a building asset.

        # Data
        {
          "company": "USMF",
          "FixedAssetnumber": "BUIL-000007",
          "Unit cost": "100"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Is the fixed asset BUIL-000007 was modified with unit cost 100 successfully?  Use the FixedAssetsV2 OData endpoint with filter (dataAreaId eq 'USMF' and FixedAssetNumber eq 'BUIL-000007') to validate the creation.",
    )


# 48.read
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
        validation_question="Is the major type for fixed asset BUIL-000001 'OWN BUILD'?",
    )


# 49.create
def test_create_BudgetTransactions(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Create a new budget register entry in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the BudgetRegisterEntryHeaderNumber and output in json format.

        # Data
        {
          "company": "USMF",
          "Budget model": "FY2018",
          "Budget code": "CarryForward"
        }
    """

    budget_register_entry_header_number = fno_test_helper.parse_response_for_value(x.response, "BudgetRegisterEntryHeaderNumber")

    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question=f"Does the message confirm that the budget register entry with budget model FY2018 and budget code CarryForward was created successfully?  Use the BudgetRegisterEntryHeaders OData endpoint and filter with dataAreaId eq 'USMF' and EntryNumber eq '{budget_register_entry_header_number}' to find and validate the data.",
    )


# 50.update
def test_update_BudgetTransactions(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Modify an existing budget register record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Entry number": "USMF000004",
          "Budget model": "FY2018",
          "Budget code": "CarryForward",
          "Expense budget total": 1,500,000
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the budget with entry number USMF000004 have the updated expense budget total of 1,500,000?  Use the BudgetRegisterEntryHeaders OData endpoint and filter with dataAreaId eq 'USMF' and EntryNumber eq 'USMF000004' to find and validate the data.",
    )


# 51.read
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
        validation_question="Does the budget with entry number USMF000004 have 40 account entries?",
    )


# 52.create
def test_create_EcoResProductDetailsExtendedGrid(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the product '114' was created successfully?  Use the ReleasedProductsV2 OData endpoint to validate the creation with filter (dataAreaId eq 'USMF' and ItemNumber eq '114') to validate the creation.",
    )


# 53.update
def test_update_EcoResProductDetailsExtendedGrid(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update an existing product in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Item number": "1000",
          "Product name": "test_product"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the product '1000' was updated with product name 'test_product' successfully?  Use the ReleasedProductsV2 OData endpoint to validate the creation with filter (dataAreaId eq 'USMF' and ItemNumber eq '1000') to validate the creation.",
    )


# 54.read
def test_read_EcoResProductDetailsExtendedGrid(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Is the storage dimension group for item number '4403' SiteWH?",
    )


# 55.create
def test_create_SystemNotificationBlockingActivity(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the high-volume system notification rule with Rule ID 85 for User ID 'ALICIA' with threshold 50 was created successfully?  Use the message to validate the creation alone since there is no OData endpoint.",
    )


# #73.update, cannot read or update since there is no data in the system
# def test_update_SystemNotificationBlockingActivity(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Update an existing high-volume system notification rule in the USMF company in Dynamics 365 Finance and Operations.

#         # Data
#         {
#           "User ID": " ALICIA ",
#           "High-volume threshold": 100,
#           "Is blocked": 1
#         }
#     """
#     # Verify the response confirms the update
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the message confirm that the high-volume system notification rule for User ID 'ALICIA' was updated with threshold 100 and blocked status successfully?",
#     )


# #74.read
# def test_read_SystemNotificationBlockingActivity(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Retrieve information about an existing high-volume system notification rule in the USMF company in Dynamics 365 Finance and Operations.

#         # Data
#         {
#           "User ID": "APRIL"
#         }
#     """
#     # Verify the response contains the notification rule information
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the message provide the information for the high-volume system notification rule for User ID 'APRIL'?",
#     )


# 56.create
def test_create_SysThrottlingPriorityMappingTable(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the priority mapping for User ID 'ARNIE' with authentication type 'User' and priority 'Low' was created successfully?  Use the message to validate the creation alone since there is no OData endpoint.",
    )


# 57.update
def test_update_SysThrottlingPriorityMappingTable(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update an existing priority mapping in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Authentication type": "Microsoft Entra ID Application",
          "priority": "Medium"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the priority mapping for User ID 'ARNIE' was updated with priority 'Medium' successfully?  Use the message to validate the creation alone since there is no OData endpoint.",
    )


# 58.read
def test_read_SysThrottlingPriorityMappingTable(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Retrieve information about an existing priority mapping in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Authentication type": "Microsoft Entra ID Application"
        }
    """
    # Verify the response contains the priority mapping information
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message provide the information for the priority mapping for Authentication type 'Microsoft Entra ID Application'?",
    )


# 59.create
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
        validation_question="Does the message confirm that the electronic signature reason with reason code 'test_sig' and description 'This is a test signature reason' was created successfully?  Use the message to validate the creation alone since there is no OData endpoint.",
    )


# 60.update
def test_update_SIGReasonCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing electronic signature reason in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Reason code": "FDA",
          "Description": "This is an updated signature reason"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the electronic signature reason with reason code 'FDA' was updated with description 'This is an updated signature reason' successfully?  Use the message to validate the creation alone since there is no OData endpoint.",
    )


# 61.read
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
        validation_question="Is the description for the reason code 'SOX' 'Approval required for SOX Compliance changes'?",
    )


# 62.create
def test_create_SysEmailRetrySchedule(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the retry schedule with retry delay 1 and measurement 'Days' was created successfully?  Use the message to validate the creation alone since there is no OData endpoint.",
    )


# 63.update
def test_update_SysEmailRetrySchedule(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update an existing retry schedule with daily period "1" in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "retry delay": 1,
          "measurement": "Hours"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the retry schedule was updated with retry delay 1 and measurement 'Hours' successfully?  Use the message to validate the creation alone since there is no OData endpoint.",
    )


# 64.read
def test_read_SysEmailRetrySchedule(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Is the measurement for the retry schedule with delay period 1 in minutes?",
    )


# This form is no longer supported with MCP tools
# 65.create
# def test_create_SysSecSegregationOfDutiesRule(
#     x: TestContext, judge: Judge, judgeAgent: JudgeAgent
# ):
#     """!
#     query: |
#         # Task
#         Create a new segregation of duties rule in the USMF company in Dynamics 365 Finance and Operations.

#         # Data
#         {
#           "Name": "rule_test1",
#           "First duty": "Access employee development workspace",
#           "Second duty": "Access benefits workspace",
#           "severity": "Low"
#         }
#     """
#     # Verify the response confirms the creation
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the message confirm that the segregation of duties rule 'rule_test1' was created successfully with first duty 'Access employee development workspace' and second duty 'Access benefits workspace'?",
#     )


# Cannot have updtae or read since there is no data in the system
# #89.update
# def test_update_DutySegregationRule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Update an existing segregation of duties rule in the USMF company in Dynamics 365 Finance and Operations.

#         # Data
#         {
#           "Name": "rule_test1",
#           "severity": "High"
#         }
#     """
#     # Verify the response confirms the update
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the message confirm that the segregation of duties rule 'rule_test1' was updated with severity 'High' successfully?",
#     )


# #90.read
# def test_read_DutySegregationRule(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Retrieve an existing segregation of duties rule in the USMF company in Dynamics 365 Finance and Operations.

#         # Data
#         {
#           "Name": "new_rule"
#         }
#     """
#     # Verify the response contains the segregation of duties rule information
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the message provide the information for the segregation of duties rule 'new_rule'?",
#     )


# 66.create
def test_create_AssetAcquisitionMethod(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Does the message confirm that the asset acquisition method 'test_method' was created successfully with description 'This is a test.'  Use the AcquisitionMethods OData endpoint to validate the creation with filter (dataAreaId eq 'USMF' and AcquisitionMethod eq 'test_method')?",
    )


# 67.update
def test_update_AssetAcquisitionMethod(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
    """!
    query: |
        # Task
        Update an existing acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "TRADE_IN",
          "Description": "Updated method"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the acquisition method 'TRADE_IN' was updated with description 'Updated method' successfully?  Use the AcquisitionMethods OData endpoint to validate the update with filter (dataAreaId eq 'USMF' and AcquisitionMethod eq 'TRADE_IN')",
    )


# 68.read
def test_read_AssetAcquisitionMethod(
    x: TestContext, judge: Judge, judgeAgent: JudgeAgent
):
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
        validation_question="Is the description for the acquisition method 'DONATION' 'Received through donation'?",
    )


# 69.create
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
        validation_question="Does the message confirm that the asset activity code 'test_code' was created successfully with description 'This is a test asset code.'?  Use the AssetActivityCodes OData endpoint to validate the creation with filter (dataAreaId eq 'USMF' and ActivityCode eq 'test_code') to validate the creation.",
    )


# 70.update
def test_update_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "BUILD",
          "Description": "This is an updated description."
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the asset activity code 'BUILD' was updated with description 'This is an updated description.' successfully?  Use the AssetActivityCodes OData endpoint to validate the creation with filter (dataAreaId eq 'USMF' and ActivityCode eq 'BUILD') to validate the creation.",
    )


# 71.read
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
        validation_question="Is the description for the asset activity code 'REMODEL' 'Company remodeling'?",
    )


# 72.create
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
        validation_question="Does the message confirm that the fixed asset condition 'Medium' was created successfully with description 'Medium condition'?  Use the AssetConditions OData endpoint to validate the creation with filter=(dataAreaId eq 'USMF' and ConditionCode eq 'Medium') to validate the creation.",
    )


# 73.update
def test_update_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Update an existing fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "EXCELLENT",
          "Description": "Updated excellent condition"
        }
    """
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that the fixed asset condition 'EXCELLENT' was updated with description 'Updated excellent condition' successfully?  Use the AssetConditions OData endpoint to validate the creation with filter=(dataAreaId eq 'USMF' and ConditionCode eq 'EXCELLENT') to validate the creation.",
    )


# 74.read
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

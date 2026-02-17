from thinkingbox.common import Judge, TestContext
from thinkingbox.tools.judgeagent import JudgeAgent
from thinkingbox.tools.fno_odataquerytool import fno_odataquerytool, fno_odataquerytool_judge
from thinkingbox.tools.fno_test_helper import fno_test_helper

"""!
scenario: fno
"""

def test_read_CustTable(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Find the credit limit for a customer account on the "All customers" list page

        # Data
        {
          "company": "USMF",
          "AccountNum": "US-001"
        }
    """

    assert judge.text_yesno(x.response, "Does the message say the credit limit for customer account 'US-001' is 500000?")


def test_create_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
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

    fno_odataquerytool_judge.query_and_assert_fields(
        "CustomersV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and CustomerAccount eq 'DE-006')  ",
        {"CustomerAccount": "DE-006"},
    )


def test_update_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            CustomersV3: { Operation: "Create", Key: {"CustomerAccount": "US-123"}, CustomerAccount: "US-123", CustomerGroupId: "30", OrganizationName: "Contoso US-123", SalesCurrencyCode: "USD", dataAreaId: "USMF", CreditLimit: 1000 }
    query: |
        # Task
        Use MCP tools to complete this task:

        Update the credit limit of an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "US-123",
          "CreditLimit": 51234
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "CustomersV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and CustomerAccount eq 'US-123')  ",
        {"CreditLimit": 51234},
    )


def test_convert_Prospect000031_ToCustomerUS200_SetABCCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Using form tools, find the Prospect record and convert it to a customer. On the new customer record, set the ABC code.

        # Data
        {
          "company": "USMF",
          "Prospect Account": "000031",
          "Customer Number": "US-200",
          "ABC Code": "A"
        }

    """

    # Verify via OData that the customer was created with correct fields
    fno_odataquerytool_judge.query_and_assert_fields(
        "CustomersV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and CustomerAccount eq 'US-200')",
        {"CustomerAccount": "US-200", "OrganizationName": "Nutmeg Center", "OrganizationABCCode": "A"},
    )


def test_read_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Find the credit limit for an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "US-018"
        }
    """

    assert judge.text_yesno(x.response, "Does the message say the credit limit for customer account 'US-018' is 350000?")

def test_read2_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Find the Phone (Telephone) number for an existing customer record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "US-025"
        }
    """

    assert judge.text_yesno(x.response, "Does the message say the phone number for customer account 'US-025' is '123-555-0157'?")


# Tests string control using form tools which do not have data source binding 
def test_read3_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            CustomersV3: { Operation: "Create", Key: {"CustomerAccount": "US-420"}, CustomerAccount: "US-420", PrimaryContactPhone: "123-456-7890", CustomerGroupId: "30", OrganizationName: "Contoso US-420", SalesCurrencyCode: "USD", dataAreaId: "USMF", CreditLimit: 1000 }
    query: |
        # Task
        Find the existing customer record using searchstring control from a telephone number from All customers menu item in the USMF company in Dynamics 365 Finance and Operations only using form* tools.

        # Data
        {
          "company": "USMF",
          "PrimaryContactPhone": "123-456-7890"
        }
    """

    assert judge.text_yesno(x.response, "Does the message say the customer account is 'US-420'?")

def test_delete_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            CustomersV3: { Operation: "Create", Key: {"CustomerAccount": "US-1234"}, CustomerAccount: "US-1234", CustomerGroupId: "30", OrganizationName: "Contoso US-1234", SalesCurrencyCode: "USD", CreditLimit: 1000, dataAreaId: "USMF" }
    query: |
        # Task
        Delete an existing customer record "US-1234" in the USMF company in Dynamics 365 Finance and Operations.

    """
    # Verify the customer record is deleted
    fno_odataquerytool_judge.query_and_assert_deleted(
        "CustomersV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and CustomerAccount eq 'US-1234')"
    )


def test_read_CustomersOnCreditHold(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Which customers are currently on credit hold?

        # Data
        {
          "company": "USMF"
        }
        
    """

    assert judge.text_yesno(x.response, "Does the message include 3 customers including US-017, US-041, and US-103?")


def test_read_Top5CustomersByCreditLimit(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Who are our top 5 customers by credit limit?

        # Data
        {
          "company": "USMF"
        }

    """

    assert judge.text_yesno(x.response, """Does the message include these customers?
                1. US-009 (Owl Wholesales) with $1,000,000, 
                2. US-001 (Contoso Retail San Diego) with $500,000,
                3. US-002 (Contoso Retail Los Angeles) with $500,000,
                4. US-013 (Pelican Wholesales) with $500,000, and
                5. US-040 (Contoso Retail USA) with $500,000?                 
                     """)


def test_read_CustomersWithZeroCreditLimit(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Which customers have zero credit limit?

        # Data
        {
          "company": "USMF"
        }

    """

    assert judge.text_yesno(x.response, "Does the message include these customers: DE-001 (Contoso Europe), US-017 (Turtle Wholesales), and US-103 (Rain Projectors)?")



def test_read_MostCommonPaymentTerms(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        What are the top 2 most common payment terms among our customers?

        # Data
        {
          "company": "USMF"
        }

    """

    assert judge.text_yesno(x.response, "Does the message include Net10 and Net45?")


def test_read_CustomersWithCashDiscountTerms(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        List the customers that have cash discount terms available along with their cash discount details.

        # Data
        {
          "company": "USMF"
        }

    """

    assert judge.text_yesno(x.response, """Does the message include these customers and their cash discount details? 
                - US-003: 0.5 percent if paid within 30 days
                - US-004: 1 percent if paid within 7 days
                - US-005: 2 percent if paid within 15 days
                - US-006: 0.5 percent if paid within 30 days
                - US-007: 0.5 percent if paid within 10 days
                - US-008: 1 percent if paid within 7 days
                - US-009: 2 percent if paid within 10 days
        """
    )


def test_read_USDollarNameAndSymbol(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        What is the name and symbol for US Dollar?

    """

    assert judge.text_yesno(x.response, "Does the message say that the symbol for the US Dollar is $?")


def test_read_EuroCurrencyName(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        What is the Euro currency code in the system?

    """

    assert judge.text_yesno(x.response, "Does the message say that the Euro has CurrencyCode EUR?")


def test_read_First5CurrenciesAlphabetically(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        What are the first 5 currencies alphabetically by currency code?

    """

    assert judge.text_yesno(x.response, """Does the message include the following:
                AED (UAE Dirham),
                AFN (Afghani),
                ALL (Lek),
                AMD (Armenian Dram), and
                ANG (Netherlands Antillian Guilder)?
        """)


def test_read_JapaneseYenConfiguration(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Is the Japanese Yen configured?

    """

    assert judge.text_yesno(x.response, "Does the message say that the Japanese Yen (JPY) is configured in the system?")


def test_read_First5Customers(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Who are our first 5 customers alphabetically by customer account number?

        # Data
        {
          "company": "USMF"
        }

    """

    assert judge.text_yesno(x.response, """Does the message correctly identify the first 5 customers:
                DE-001 (Contoso Europe),
                US-001 (Contoso Retail San Diego),
                US-002 (Contoso Retail Los Angeles),
                US-003 (Forest Wholesales), and
                US-004 (Cave Wholesales)?
        """)


def test_read_CustomerDE001(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        What are the details of customer DE-001?

        # Data
        {
          "company": "USMF"
        }

    """

    assert judge.text_yesno(x.response, "Does the message include Organization Name: Contoso Europe?")


def test_read_VendorUSTX001(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        What are the details of vendor US_TX_001?

    """

    assert judge.text_yesno(x.response, "Does the message correctly identify that US_TX_001 is California State Tax Authority?")


def test_read_VendorsInGroup30(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Which vendors are in vendor group 30?

    """
   
    assert judge.text_yesno(x.response, """Does the message correctly identify vendors in group 30?
            These include multiple state tax authorities such as California, Florida, Colorado, Georgia, and Idaho.
        """,
    )


def test_read_VendorUS101(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Does the vendor US-101 have an address on file?

        # Data
        {
          "company": "USMF"
        }

    """

    assert judge.text_yesno(x.response, """Does the message correctly identify vendor US-101 and say that this vendor has address Cindy Road456, Guadaljara, JAL, 44190 MEX ?""")


def test_update_Vendor1001_PaymentMethodAndTaxExempt(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Find the vendor record and update their payment method and add tax exempt number.

        # Data
        {
          "company": "USMF",
          "Vendor Account": "1001",
          "Payment Method": "ELECTRONIC",
          "Tax Exempt Number": "991234"
        }

    """

    # Verify via OData that the fields were updated correctly
    fno_odataquerytool_judge.query_and_assert_fields(
        "VendorsV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and VendorAccountNumber eq '1001')",
        {"DefaultVendorPaymentMethodName": "ELECTRONIC", "TaxExemptNumber": "991234"},
    )


# Adds coverage for the menu item control
def test_create_CustomerContact(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            CustomersV3: { Operation: "Create", Key: {"CustomerAccount": "US-123"}, CustomerAccount: "US-123", CustomerGroupId: "30", OrganizationName: "Contoso US-123", SalesCurrencyCode: "USD", dataAreaId: "USMF", CreditLimit: 1000 }
    query: |
        # Task
        Add a new contact to a customer in the USMF company in Dynamics 365 Finance and Operations using the form* tools.  Once processing has completed, return the ContactPersonId as output in json format.

        # Data
        {
            "dataAreaId": "USMF",
            "Customer Account": "US-123",
            "Contact":
                {
                    "First name": "John",
                    "Middle name": "Arthur",
                    "Last name": "Kartch",
                }
        }
    """

    contact_person_id = fno_test_helper.parse_response_for_value(x.response, "ContactPersonId")

    fno_odataquerytool_judge.query_and_assert_fields(
        f"ContactPersons?cross-company=true&$filter=(dataAreaId eq 'usmf' and ContactPersonId eq '{contact_person_id}')  ",
        {"FirstName": "John", "MiddleName": "Arthur", "LastName": "Kartch"},
    )


def test_create_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
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
          "Description": "Product test description"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "ProductsV2?cross-company=true&$filter=(ProductNumber eq 'Z0001')",
        {"ProductType": "Item", "ProductSubType": "Product", "ProductName": "Electronic widgets", "RetailProductCategoryName": "Laptops", "ProductDescription": "Product test description"},
	)


# Same test as prior but using only form* tools. This adds coverage for combobox control that is not bound to a data source.
def test_create_EcoResDistinctProductListPage_FormTools(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new product record in the USMF company in Dynamics 365 Finance and Operations using only the form* tools.

        # Data
        {
          "company": "USMF",
          "Product type": "Item",
          "Product subtype": "Product",
          "Product number": "Z0002",
          "Product name": "Electronic widgets",
          "Retail category": "Laptops"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "ProductsV2?cross-company=true&$filter=(ProductNumber eq 'Z0002')",
        {"ProductType": "Item", "ProductSubType": "Product", "ProductName": "Electronic widgets", "RetailProductCategoryName": "Laptops"},
	)

    
def test_update_EcoResDistinctProductListPage_ExplicitNavigation(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ProductsV2: { Operation: "Create", Key: {"ProductNumber": "1234567"}, ProductNumber: "1234567"}        
    query: |
        # Task
        Update the description of an existing product record in the USMF company in Dynamics 365 Finance and Operations.  Navigate initially to the 'EcoResDistinctProductListPage' menu item.

        # Data
        {
          "company": "USMF",
          "Product number": "1234567",
          "Description": "High-performance electronic widget for retail customers."
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "ProductsV2?cross-company=true&$filter=(ProductNumber eq '1234567')",
        {"ProductDescription": "High-performance electronic widget for retail customers."},
	)
    

# Same test as prior but without explicit navigation step
def test_update_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ProductsV2: { Operation: "Create", Key: {"ProductNumber": "12345678"}, ProductNumber: "12345678"}        
    query: |
        # Task
        Update the description of an existing product record in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "12345678",
          "Description": "High-performance electronic widget for retail customers."
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "ProductsV2?cross-company=true&$filter=(ProductNumber eq '12345678')",
        {"ProductDescription": "High-performance electronic widget for retail customers."},
	)


def test_read_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Retrieve details of an existing product record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "0027"
        }
    """

    assert judge.text_yesno(x.response, """Does the message provide the details for product 0027?""")


def test_delete_EcoResDistinctProductListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ProductsV2: { Operation: "Create", Key: {"ProductNumber": "123456789"}, ProductNumber: "123456789"}        
    query: |
        # Task
        Delete an existing product record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Product number": "123456789"
        }
    """
    # Verify the product record is deleted
    fno_odataquerytool_judge.query_and_assert_deleted(
        "ProductsV2?cross-company=true&$filter=(ProductNumber eq '123456789')"
    )

def test_create_SalesTableListPageOneLine_ExplicitNavigation(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the find_menu_item tool with companyId "USMF", menuItemFilter "SalesTableListPage", and responseSize "50" to find the SalesTableListPage menu item of type display in USMF company and then create a new sales order record with one order line in Dynamics 365 Finance and Operations.  Once processing has completed, return the SalesOrderNumber as output in json format.
        # Data
        {
          "company": "USMF",
          "SalesOrderHeader": {
            "Customer Account": "US-001",
            "Currency": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "Ordered Quantity": 10,
                "Unit Price": 25.00,
                "Site": "1",
                "Warehouse": "11"
              }            
            ]
          }
        }
    """

    # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"ItemNumber": "M0001", "OrderedSalesQuantity": 10, "SalesPrice": 25, "ShippingSiteId": "1", "ShippingWarehouseId": "11"}
	)

def test_create_SalesTableListPageTwoLines_ExplicitNavigation_ExplicitSave(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the find_menu_item tool with companyId "USMF", menuItemFilter "SalesTableListPage", and responseSize "50" to find the SalesTableListPage menu item of type display in USMF company and then create a new sales order record with two order lines in Dynamics 365 Finance and Operations.  Once both lines are created, save the form.  Once processing has completed, return the SalesOrderNumber as output in json format.
        # Data
        {
          "company": "USMF",
          "SalesOrderHeader": {
            "Customer Account": "US-001",
            "Currency": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "Ordered Quantity": 10,
                "Site": "1",
                "Warehouse": "12",
                "Unit Price": 25.00,
              },
              {
                "ItemNumber": "M0003",
                "Ordered Quantity": 5,
                "Site": "2",
                "Warehouse": "22",
                "Unit Price": 40.00,
              }
            ]
          }
        }
    """

    # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        [{"ItemNumber": "M0001", "OrderedSalesQuantity": 10, "SalesPrice": 25, "ShippingSiteId": "1", "ShippingWarehouseId": "12"},
         {"ItemNumber": "M0003", "OrderedSalesQuantity": 5, "SalesPrice": 40, "ShippingSiteId": "2", "ShippingWarehouseId": "22"}]
	)


def test_create_SalesTableListPageTwoLines_ExplicitNavigation(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the find_menu_item tool with companyId "USMF", menuItemFilter "SalesTableListPage", and responseSize "50" to find the SalesTableListPage menu item of type display in USMF company and then create a new sales order record with two order lines in Dynamics 365 Finance and Operations.  Once processing has completed, return the SalesOrderNumber as output in json format.
        # Data
        {
          "company": "USMF",
          "SalesOrderHeader": {
            "Customer Account": "US-001",
            "Currency": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "Ordered Quantity": 10,
                "Site": "1",
                "Warehouse": "12"
                "Unit Price": 25.00,
            },
              {
                "ItemNumber": "M0003",
                "Ordered Quantity": 5,
                "Site": "2",
                "Warehouse": "22",
                "Unit Price": 40.00,
              }
            ]
          }
        }
    """

    # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        [{"ItemNumber": "M0001", "OrderedSalesQuantity": 10, "SalesPrice": 25, "ShippingSiteId": "1", "ShippingWarehouseId": "12"},
         {"ItemNumber": "M0003", "OrderedSalesQuantity": 5, "SalesPrice": 40, "ShippingSiteId": "2", "ShippingWarehouseId": "22"}]
	)


def test_create_SalesTableListPageOneLine(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new sales order record with one order line in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the SalesOrderNumber and output in json format.
        # Data
        {
          "company": "USMF",
          "SalesOrderHeader": {
            "Customer Account": "US-001",
            "Currency": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "Ordered Quantity": 10,
                "Site": "1",
                "Warehouse": "11"
                "Unit Price": 25.00,
              }            
            ]
          }
        }
    """

    # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"ItemNumber": "M0001", "OrderedSalesQuantity": 10, "SalesPrice": 25, "ShippingSiteId": "1", "ShippingWarehouseId": "11"}
	)


def test_create_SalesTableListPageTwoLines(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new sales order record with two order lines in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the SalesOrderNumber and output in json format.
        # Data
        {
          "company": "USMF",
          "SalesOrderHeader": {
            "Customer Account": "US-001",
            "Currency": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "Ordered Quantity": 10,
                "Site": "1",
                "Warehouse": "12",
                "Unit Price": 25.00,
              },
              {
                "ItemNumber": "M0003",
                "Ordered Quantity": 5,
                "Site": "2",
                "Warehouse": "22",
                "Unit Price": 40.00,
              }
            ]
          }
        }
    """

   # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        [{"ItemNumber": "M0001", "OrderedSalesQuantity": 10, "SalesPrice": 25, "ShippingSiteId": "1", "ShippingWarehouseId": "12"},
         {"ItemNumber": "M0003", "OrderedSalesQuantity": 5, "SalesPrice": 40, "ShippingSiteId": "2", "ShippingWarehouseId": "22"}]
	)


def test_update_SalesOrderHeader_LineAndShippingDate_FormTools(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            SalesOrderHeadersV4: { Operation: "Create", Key:{SalesOrderNumber: "@Out"}, OrderingCustomerAccountNumber: "US-002", CurrencyCode: "USD", dataAreaId: "USMF" }
    query: |
        # Task
        1. Find the existing sales order record "{init[fnoproxy][SalesOrderHeadersV4][SalesOrderNumber]}" from SalesTableListPage in the USMF company in Dynamics 365 Finance and Operations using the form* tools.
        2. Update the "Requested ship date" on the "Sales order header" tab to the day after tomorrow. Today's date is {init[fnoproxy][CurrentDate]}.
        3. Add sales order line as specified in the data section.
        4. Once processing has completed, return the SalesOrderNumber and output in json format.
        
        # Data
        "SalesOrderLines": [
            {
                "ItemNumber": "M0001",
                "Ordered Quantity": 2,
                "Site": "1",
                "Warehouse": "12"
            }
        ]
    """
    
    # Calculate 2 days ahead and skip weekends
    formatted_future_date = fno_test_helper.get_future_datetime_formatted(2)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")

    # Verify the sales record delivery date is updated and lines are added
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-002", "RequestedShippingDate": formatted_future_date}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"ItemNumber": "M0001", "OrderedSalesQuantity": 2, "ShippingSiteId": "1", "ShippingWarehouseId": "12" }
	)


def test_create_SalesOrderHeader_DataTools(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the data_find_entities, data_find_entity_type, and data_create_entity tools to create a new sales order record in the USMF company in Dynamics 365 Finance and Operations.  Use the "SalesOrderHeadersV4" OData entity endpoint to create the sales order.  Once processing has completed, return the SalesOrderNumber and output in json format.
        # Data
        {
          "dataAreaId": "USMF",
          "SalesOrderHeader": {
            "OrderingCustomerAccountNumber": "US-001",
            "CurrencyCode": "USD"
          }
        }
    """

    # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)


def test_create_SalesOrderHeaderOneLine__DataTools_ExplicitEndpoints(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the data_find_entities, data_find_entity_type, and data_create_entity tools to create a new sales order record with one order line in the USMF company in Dynamics 365 Finance and Operations.  Use the "SalesOrderHeadersV4" OData entity endpoint to create the sales order.  
        Use the "SalesOrderLinesV3" OData entity endpoint to create the order line. Once processing has completed, return the SalesOrderNumber and output in json format.

        # Data
        {
          "dataAreaId": "USMF",
          "SalesOrderHeader": {
            "OrderingCustomerAccountNumber": "US-001",
            "CurrencyCode": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "OrderedSalesQuantity": 10,
                "SalesPrice": 25.00,
                "ShippingSiteId": "1",
                "ShippingWarehouseId": "11"
              }            
            ]
          }
        }
    """

    # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"ItemNumber": "M0001", "OrderedSalesQuantity": 10, "SalesPrice": 25, "ShippingSiteId": "1", "ShippingWarehouseId": "11"}
	)


def test_create_SalesOrderHeaderOneLine_DataTools(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the data_find_entities, data_find_entity_type, and data_create_entity tools to create a new sales order record with one order line in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the SalesOrderNumber and output in json format.

        # Data
        {
          "dataAreaId": "USMF",
          "SalesOrderHeader": {
            "OrderingCustomerAccountNumber": "US-001",
            "CurrencyCode": "USD",
            "SalesOrderLines": [
              {
                "ItemNumber": "M0001",
                "OrderedSalesQuantity": 10,
                "SalesPrice": 25.00,
                "ShippingSiteId": "1",
                "ShippingWarehouseId": "11"
              }            
            ]
          }
        }
    """

    # Get the SalesOrderNumber from the response (string or dict)
    sales_order_number = fno_test_helper.parse_response_for_value(x.response, "SalesOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderHeadersV4?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"CurrencyCode": "USD", "OrderingCustomerAccountNumber": "US-001"}
	)
  
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesOrderLinesV3?cross-company=true&$filter=(dataAreaId eq 'usmf' and SalesOrderNumber eq '{sales_order_number}')",
        {"ItemNumber": "M0001", "OrderedSalesQuantity": 10, "SalesPrice": 25, "ShippingSiteId": "1", "ShippingWarehouseId": "11"}
	)


def test_create_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new purchase order record for a given vendor using default values where applicable. Once processing has completed, return the PurchaseOrderNumber and output in json format.

        # Data
        {
          "company": "USSI",
          "Vendor account": "US_SI_000009"
        }
    """

    # Get the PurchaseOrderNumber from the response (string or dict)
    purchase_order_number = fno_test_helper.parse_response_for_value(x.response, "PurchaseOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderHeadersV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"PurchaseOrderNumber": purchase_order_number},
    )


def test_update_PurchTableListPageExplicitNavigation(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            PurchaseOrderHeadersV2: { Operation: "Create", Key:{PurchaseOrderNumber: "@Out"}, OrderVendorAccountNumber: "US_SI_000009", dataAreaId: "USSI" }
    query: |
        Add a new line to purchase order "{init[fnoproxy][PurchaseOrderHeadersV2][PurchaseOrderNumber]}".  Start navigation using the PurchTableListPage menu item in the USSI company in Dynamics 365 Finance and Operations and continue to the details page to add a line.
        Once processing has completed, return the PurchaseOrderNumber and output in json format.

        # Data
        {
          "Line": {
            "Item number": "S0012",
            "Quantity": 5,
            "UnitPrice": 150
          }
        }
            
    """

    # Get the PurchaseOrderNumber from the response (string or dict)
    purchase_order_number = fno_test_helper.parse_response_for_value(x.response, "PurchaseOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderHeadersV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"PurchaseOrderNumber": purchase_order_number},
    )

    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderLinesV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"ItemNumber": "S0012", "LineDescription": "Hardware: Laptop", "OrderedPurchaseQuantity": 5, "PurchasePrice": 150}
	)


def test_update_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            PurchaseOrderHeadersV2: { Operation: "Create", Key:{PurchaseOrderNumber: "@Out"}, OrderVendorAccountNumber: "US_SI_000009", dataAreaId: "USSI" }
    query: |
        Add a new line to purchase order "{init[fnoproxy][PurchaseOrderHeadersV2][PurchaseOrderNumber]}" in the USSI company in Dynamics 365 Finance and Operations.
        Once processing has completed, return the PurchaseOrderNumber and output in json format.

        # Data
        {
          "Line": {
            "Item number": "S0012",
            "Quantity": 5,
            "UnitPrice": 150
          }
        }
            
    """

    # Get the PurchaseOrderNumber from the response (string or dict)
    purchase_order_number = fno_test_helper.parse_response_for_value(x.response, "PurchaseOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderHeadersV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"PurchaseOrderNumber": purchase_order_number},
    )

    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderLinesV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"ItemNumber": "S0012", "LineDescription": "Hardware: Laptop", "OrderedPurchaseQuantity": 5, "PurchasePrice": 150}
	)


def test_read_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
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

    assert judge.text_yesno(x.response, "Does the message provide the details for purchase order 00000227?")


def test_delete_PurchTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            PurchaseOrderHeadersV2: { Operation: "Create", Key:{PurchaseOrderNumber: "@Out"}, OrderVendorAccountNumber: "US_SI_000009", dataAreaId: "USSI" }
    query: |
        # Task
        Delete an existing purchase order "{init[fnoproxy][PurchaseOrderHeadersV2][PurchaseOrderNumber]}" from the USSI company in Dynamics 365 Finance and Operations.  Once processing has completed, return the PurchaseOrderNumber and output in json format.
    """
    purchase_order_number = fno_test_helper.parse_response_for_value(x.response, "PurchaseOrderNumber")
    # Verify the purchase order record is deleted
    fno_odataquerytool_judge.query_and_assert_deleted(
        f"PurchaseOrderHeadersV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')"
    )


def test_create_PurchaseOrderHeaderOneLine_DataTools_ExplicitEndpoints(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the data_find_entities, data_find_entity_type, and data_create_entity tools to create a new purchase order record with one order line in the USSI company in Dynamics 365 Finance and Operations.  Use the "PurchaseOrderHeadersV2" OData entity endpoint to create the purchase order.  
        Use the "PurchaseOrderLinesV2" OData entity endpoint to create the order line. Once processing has completed, return the PurchaseOrderNumber and output in json format.

        # Data
        {
          "dataAreaId": "USSI",
          "PurchaseOrderHeader": {
            "OrderVendorAccountNumber": "US_SI_000009",
            "PurchaseOrderLines": [
              {
                "ItemNumber": "S0012",
                "OrderedPurchaseQuantity": 5,
                "PurchasePrice": 150
              }            
            ]
          }
        }
    """

    # Get the PurchaseOrderNumber from the response (string or dict)
    purchase_order_number = fno_test_helper.parse_response_for_value(x.response, "PurchaseOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderHeadersV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"PurchaseOrderNumber": purchase_order_number},
    )

    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderLinesV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"ItemNumber": "S0012", "OrderedPurchaseQuantity": 5, "PurchasePrice": 150}
	)


def test_create_PurchaseOrderHeaderOneLine_DataTools(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Use the data_find_entities, data_find_entity_type, and data_create_entity tools to create a new purchase order record with one order line in the USSI company in Dynamics 365 Finance and Operations.  Once processing has completed, return the PurchaseOrderNumber and output in json format.

        # Data
        {
          "dataAreaId": "USSI",
          "PurchaseOrderHeader": {
            "OrderVendorAccountNumber": "US_SI_000009",
            "PurchaseOrderLines": [
              {
                "ItemNumber": "S0012",
                "OrderedPurchaseQuantity": 5,
                "PurchasePrice": 150
              }            
            ]
          }
        }
    """

    # Get the PurchaseOrderNumber from the response (string or dict)
    purchase_order_number = fno_test_helper.parse_response_for_value(x.response, "PurchaseOrderNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderHeadersV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"PurchaseOrderNumber": purchase_order_number},
    )
  
    fno_odataquerytool_judge.query_and_assert_fields(
        f"PurchaseOrderLinesV2?cross-company=true&$filter=(dataAreaId eq 'ussi' and PurchaseOrderNumber eq '{purchase_order_number}')",
        {"ItemNumber": "S0012", "OrderedPurchaseQuantity": 5, "PurchasePrice": 150}
	)

# Directing LLM to use the form tools because the Workers endpoint does not allow setting the WorkerType field.
def test_create_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new worker record in the USMF company in Dynamics 365 Finance and Operations using the form tools.  Once processing has completed, return the PersonnelNumber and output in json format.  

        # Data
        {
          "Legal entity": "USMF",
          "FirstName": "Sophia",
          "LastName": "Doe",
          "EmploymentStartDate": "7-16-2025",
          "EmploymentType": "Warehouse",
          "WorkerType": "Employee",
          "EmploymentCategory": "Intern"
        }
    """

    # Get the PersonnelNumber from the response (string or dict)
    personnel_number = fno_test_helper.parse_response_for_value(x.response, "PersonnelNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"Workers?cross-company=true&$filter=(PersonnelNumber eq '{personnel_number}')",
        {"FirstName": "Sophia", "LastName": "Doe", "WorkerType": "Employee"}
	)


def test_activate_HcmRecruitingRequest(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            HumanResourcesParameters: { Operation: "Update", Key: {"dataAreaId": "USMF"}, RecruitmentSystemType: "HRRecruitment" }
    query: |
        # Task
        Create a new recruiting request using HcmRecruitingRequest menu item and activate it. Once processing has completed, return the RecruitingRequestId in json format.
        Set the start date to 1 week from today's date. Today's date is {init[fnoproxy][CurrentDate]}

        # Data
        {
          "Company": "USMF",
          "Description": "Project MCP",
          "Hiring manager": "Jodi Christiansen",
          "Job Id": "Account manager",
          "External description": "Looking for an experienced account manager to join our team.",
          
        }
    """

    # Get the RequestId from the response (string or dict)
    formatted_future_date = fno_test_helper.get_future_datetime_formatted(7, None, True)
    request_id = fno_test_helper.parse_response_for_value(x.response, "RecruitingRequestId")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"RecruitingRequests?cross-company=true&$filter=(RecruitingRequestId eq '{request_id}')",
        {"Description": "Project MCP", "TitleId": "Account Manager", "Status": "Active", "EstimatedStartDate": formatted_future_date},
    )

# This test depends on Demo data candidate "USMF-000001" existing
def test_update_Candidate_AddComment(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            HumanResourcesParameters: { Operation: "Update", Key: {"dataAreaId": "USMF"}, RecruitmentSystemType: "HRRecruitment" }
    query: |
        # Task
        Add a Comment to the Candidate record "USMF-000001" in candidates to hire in USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Comment": "The first interview went spectacularly well. Rowan is a top contender for this position."
        }
    """

    # Get the CandidateId from the response (string or dict)
    fno_odataquerytool_judge.query_and_assert_fields(
        f"CandidatesToHire?cross-company=true&$filter=(CandidateId eq 'USMF-000001')",
        {"CandidateId": "USMF-000001", "Comments": "The first interview went spectacularly well. Rowan is a top contender for this position."},
    )


# This test depends on Demo data candidate "Graham Barnes" existing
def test_update_Candidate_DoNotHire(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            HumanResourcesParameters: { Operation: "Update", Key: {"dataAreaId": "USMF"}, RecruitmentSystemType: "HRRecruitment" }
    query: |
        # Task
        1. Select the Do not hire action for Candidate "Graham Barnes" in candidates to hire in USMF company in Dynamics 365 Finance and Operations.
        2. Enter "reason code" as "Inexperienced" and add a comment "He lacks the required educational degree for the position."
    """

    # Get the CandidateId from the response (string or dict)
    fno_odataquerytool_judge.query_and_assert_fields(
        f"CandidatesToHire?cross-company=true&$filter=(CandidateId eq 'USMF-000007')",
        {"CandidateId": "USMF-000007", "Comments": "He lacks the required educational degree for the position.", "ApplicantIntegrationResult": "NotHired", "DoNotHireReasonCodeId": "Inexperienced"},
    )
    

def test_update_WorkerAddContactInformation_ExplicitNavigationAndInstructions_ExplicitLinkIInstructions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            EmployeesV2: { Operation: "Create", Key:{PersonnelNumber: "@Out"}, FirstName: "Chuck", "LastName": "MyMan", "EmploymentLegalEntityId": "USMF", "EmploymentStartDate": "2025-11-10"}
    query: |
        # Task
        Add contact information to the worker with personnel number "{init[fnoproxy][EmployeesV2][PersonnelNumber]}" in Dynamics 365 Finance and Operations.  
        Start navigation using the HcmWorkerListPage menu item.
        Click the name link for the worker to open the details page.
        After opening the details page, add the contact information.  Once processing has completed, return the PersonnelNumber and output in json format.  

        # Data
        {
          "Description": "Work",
          "Type": "Phone",
          "ContactNumber": "223-488-06-98"
        }
    """

    # Get the PersonnelNumber from the response (string or dict)
    personnel_number = fno_test_helper.parse_response_for_value(x.response, "PersonnelNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"WorkerContacts?cross-company=true&$filter=(PersonnelNumber eq '{personnel_number}')",
        {"PersonnelNumber": personnel_number, "Description": "Work", "Type": "Phone", "Locator": "223-488-06-98"},
	)


def test_update_WorkerAddContactInformation_ExplicitNavigationAndInstructions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            EmployeesV2: { Operation: "Create", Key:{PersonnelNumber: "@Out"}, FirstName: "Chuck", "LastName": "MyMan", "EmploymentLegalEntityId": "USMF", "EmploymentStartDate": "2025-11-10"}
    query: |
        # Task
        Add contact information to the worker with personnel number "{init[fnoproxy][EmployeesV2][PersonnelNumber]}" in Dynamics 365 Finance and Operations.  
        Start navigation using the HcmWorkerListPage menu item.
        After opening the details page, add the contact information.  Once processing has completed, return the PersonnelNumber and output in json format.  

        # Data
        {
          "Description": "Work",
          "Type": "Phone",
          "ContactNumber": "223-488-06-98"
        }
    """

    # Get the PersonnelNumber from the response (string or dict)
    personnel_number = fno_test_helper.parse_response_for_value(x.response, "PersonnelNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"WorkerContacts?cross-company=true&$filter=(PersonnelNumber eq '{personnel_number}')",
        {"PersonnelNumber": personnel_number, "Description": "Work", "Type": "Phone", "Locator": "223-488-06-98"},
	)


def test_update_WorkerAddContactInformation(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            EmployeesV2: { Operation: "Create", Key:{PersonnelNumber: "@Out"}, FirstName: "Chuck", "LastName": "MyMan", "EmploymentLegalEntityId": "USMF", "EmploymentStartDate": "2025-11-10"}
    query: |
        # Task
        Add contact information to the worker with personnel number "{init[fnoproxy][EmployeesV2][PersonnelNumber]}" in Dynamics 365 Finance and Operations. 
        First, navigate to the HcmWorkerListPage menu item in company USMF.  Filter the list to find the worker by PersonnelNumber.  Open the "Contact information" tab and add the contact information. 
        Once processing has completed, return the PersonnelNumber and output in json format.  

        # Data
        {
          "Description": "Work",
          "Type": "Phone",
          "ContactNumber": "223-488-06-98"
        }
    """

    # Get the PersonnelNumber from the response (string or dict)
    personnel_number = fno_test_helper.parse_response_for_value(x.response, "PersonnelNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"WorkerContacts?cross-company=true&$filter=(PersonnelNumber eq '{personnel_number}')",
        {"PersonnelNumber": personnel_number},
	)


def test_read_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Retrieve details of an existing worker record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "PersonnelNumber": "000133"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the details for worker with personnel number 000133?")


def test_delete_HcmWorkerListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            EmployeesV2: { Operation: "Create", Key:{PersonnelNumber: "@Out"}, FirstName: "Chuck", "LastName": "MyMan", "EmploymentLegalEntityId": "USMF", "EmploymentStartDate": "2025-11-10"}
    query: |
        # Task
        Delete an existing worker record from the USMF company in Dynamics 365 Finance and Operations.  Delete the worker with personnel number "{init[fnoproxy][EmployeesV2][PersonnelNumber]}".  
        Once processing has completed, return the PersonnelNumber and output in json format.  
    """

    # Get the PersonnelNumber from the response (string or dict)
    personnel_number = fno_test_helper.parse_response_for_value(x.response, "PersonnelNumber")
    # Verify that the purchase order was deleted
    fno_odataquerytool_judge.query_and_assert_deleted(
        f"WorkerContacts?cross-company=true&$filter=(PersonnelNumber eq '{personnel_number}')"
	)


def test_create_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new bank account record in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the BankAccount and output in json format.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF CAN",
          "Name": "CAN currency account",
          "BankGroup": "BankUSA",
          "Routing number": "123456780",
          "MainAccount": "110120"
        }
    """

    # Get the BankAccount from the response (string or dict)
    bank_account = fno_test_helper.parse_response_for_value(x.response, "BankAccount")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"BankAccounts?cross-company=true&$filter=(dataAreaId eq 'USMF' and BankAccountId eq '{bank_account}')",
        {"Name": "CAN currency account", "BankGroupId": "BankUSA", "RoutingNumber": "123456780", "BankMainAccountIdDisplayValue": "110120"}
	)


def test_update_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Update the name of an existing bank account in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the BankAccount and output in json format.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF PAYRL",
          "Name": "Payroll account - USD (TEST)"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"BankAccounts?cross-company=true&$filter=(dataAreaId eq 'USMF' and BankAccountId eq 'USMF PAYRL')",
        {"Name": "Payroll account - USD (TEST)", "BankGroupId": "BankUSA", "RoutingNumber": "123456780", "BankMainAccountIdDisplayValue": "110160"}
	)



def test_read_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Retrieve details of an existing bank account record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "BankAccount": "USMF OPER"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the details for bank account 'USMF OPER'?")


def test_delete_BankAccountTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            BankAccounts: { Operation: "Create", BankAccountId: "USMF TEST", dataAreaId: "USMF", "Name": "Name Test", "BankGroupId": "BankUSA", "RoutingNumber": "123456780", "BankMainAccountIdDisplayValue": "110160", "CurrencyCode":"USD" }
    query: |
        Delete an existing bank account with Id "USMF TEST" from the USMF company in Dynamics 365 Finance and Operations.  
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        f"BankAccounts?cross-company=true&$filter=(dataAreaId eq 'USMF' and BankAccountId eq 'USMF TEST')"
	)


def test_create_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new data source in Data Management in the USMF company in Dynamics 365 Finance and Operations.  Do not use the data_* tools.

        # Data
        {
          "company": "USMF",
          "SourceName": "test_source5"
        }
    """

    # No OData coverage for Data Management Framework data sources
    # Verify the response confirms the creation
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message say that the data source 'test_source5' was created successfully?  " \
        "There are no OData endpoints to validate this data, so navigate to the DM_DataManagementWorkspaceMenuItem menu item and then 'Configure data sources' to verify that the data source was created.",
    )


def test_update_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Update the description of an existing data source in Data Management in the USMF company in Dynamics 365 Finance and Operations.  Do not use the data_* tools.

        # Data
        {
          "company": "USMF",
          "SourceName": "EXCEL",
          "Description": "EXCEL - updated description"
        }
    """

    # No OData coverage for Data Management Framework data sources
    # Verify the response confirms the update
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message say that the description for data source 'EXCEL' was updated successfully?  " \
        "There are no OData endpoints to validate this data, so navigate to the DM_DataManagementWorkspaceMenuItem menu item and then 'Configure data sources' to verify that the data source was updated.")


def test_read_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Retrieve details including the Row Delimiter of an existing data source in Data Management from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "SourceName": "TabSeparated"
        }
    """

    assert judge.text_yesno(x.response, "Does the row delimiter for data source 'TabSeparated' contain CR & LF?")


def test_delete_DM_DataManagementWorkspaceMenuItem(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Delete an existing data source in Data Management from the USMF company in Dynamics 365 Finance and Operations.  Do not use the data_* tools.

        # Data
        {
          "company": "USMF",
          "SourceName": "AX"
        }
    """

    # No OData coverage for Data Management Framework data sources
    # Verify the response confirms the deletion
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message say that the data source 'AX' was deleted successfully? " \
        "There are no OData endpoints to validate this data, so navigate to the DM_DataManagementWorkspaceMenuItem menu item and then 'Configure data sources' to verify that the data source was deleted.")


# The expense data tools endpoints are ambiguous, so directing LLM to use the form tools instead.
def test_create_expenseworkspace_formtools(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new expense report for a business trip with specified expenses and payment methods using the form tools.  Once processing has completed, return the ExpenseReportNumber and output in json format.

        # Data
        {
          "company": "USMF",
          "purpose": "testing_expense5",
          "expenses": [
            {
              "Category": "Car Rental",
              "Amount": 110,
              "Currency": "USD",
            }
          ]
        }
    """

    # Get the Expense report number from the response (string or dict)
    expense_report_number = fno_test_helper.parse_response_for_value(x.response, "ExpenseReportNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"ExpMobileReports?cross-company=true&$filter=(ReferenceDataAreaId eq 'USMF' and ExpNumber eq '{expense_report_number}')",
        {"AmountTotal": 110, "Txt2": "testing_expense5"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"Expenses?cross-company=true&$filter=(LegalEntityDataAreaId eq 'USMF' and ExpenseReportNumber eq '{expense_report_number}')",
        {"TransactionAmount": 110, "ExpenseCategory": "Car Rental", "Currency": "USD", "PaymentMethod": "CreditCard"}
	)  


def test_update_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ExpMobileReports: { Operation: "Create", Key:{ExpNumber: "@Out"}, Txt2: "Expense update test", LegalEntity_DataArea: "USMF", ReferenceDataAreaId: "USMF", InterCompanyLE: "USMF" }
    query: |
        # Task
        Update expense report "{init[fnoproxy][ExpMobileReports][ExpNumber]}" by adding a new expense.  Either use the Expenses OData endpoint or the TrvExpRptListPage_MyListPage menu item to add the new expense.  Once processing has completed, return the ExpenseReportNumber and output in json format.

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

    # Get the Expense report number from the response (string or dict)
    expense_report_number = fno_test_helper.parse_response_for_value(x.response, "ExpenseReportNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"ExpMobileReports?cross-company=true&$filter=(ReferenceDataAreaId eq 'USMF' and ExpNumber eq '{expense_report_number}')",
        {"AmountTotal": 150, "Txt2": "Expense update test"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        f"Expenses?cross-company=true&$filter=(LegalEntityDataAreaId eq 'USMF' and ExpenseReportNumber eq '{expense_report_number}')",
        {"TransactionAmount": 150, "ExpenseCategory": "Conference", "Currency": "USD", "PaymentMethod": "CreditCard"}
	)


def test_read_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ExpMobileReports: { Operation: "Create", Key:{ExpNumber: "@Out"}, Txt2: "Expense read test", LegalEntity_DataArea: "USMF", ReferenceDataAreaId: "USMF", InterCompanyLE: "USMF" }
    query: |
        Retrieve all the details of existing expense report "{init[fnoproxy][ExpMobileReports][ExpNumber]}" in company "USMF".  Once processing has completed, return the ExpenseReportNumber and other details in json field and value format like the following:  "ExpenseReportNumber": "VALUE".  Make sure to include ExpenseReportNumber in the response.
    """

    expense_report_number = fno_test_helper.parse_response_for_value(x.response, "ExpenseReportNumber")

    assert judge.text_yesno(x.response, f"Does the message provide details for expense report with {expense_report_number}?")


def test_delete_expenseworkspace(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ExpMobileReports: { Operation: "Create", Key:{ExpNumber: "@Out"}, Txt2: "Expense delete test", LegalEntity_DataArea: "USMF", ReferenceDataAreaId: "USMF", InterCompanyLE: "USMF" }
    query: |
        Delete existing expense report "{init[fnoproxy][ExpMobileReports][ExpNumber]}" from the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the ExpenseReportNumber and output in json format.
    """

    expense_report_number = fno_test_helper.parse_response_for_value(x.response, "ExpenseReportNumber")

    fno_odataquerytool_judge.query_and_assert_deleted(
        f"ExpMobileReports?cross-company=true&$filter=(ReferenceDataAreaId eq 'USMF' and ExpNumber eq '{expense_report_number}')"
	)


def test_create_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new warehouse in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the WarehouseId and output in json format.

        # Data
        {
          "company": "USMF",
          "Warehouse" 1818
          "Warehouse name": "mcp-test5",
          "Site": 1,
          "Type": "Default"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"Warehouses?cross-company=true&$filter=(dataAreaId eq 'USMF' and WarehouseId eq '1818')",
        {"WarehouseName": "mcp-test5", "OperationalSiteId": "1", "WarehouseType": "Standard"}
	)


def test_update_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            Warehouses: { Operation: "Create", Key: {"WarehouseId": "1234"}, WarehouseId: "1234", WarehouseName: "Warehouse update test", dataAreaId: "USMF", OperationalSiteId: "1", WarehouseType: "Standard" }
    query: |
        # Task
        Assign a quarantine warehouse to an existing warehouse in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "Warehouse update test",
          "QuarantineWarehouse": 18
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"Warehouses?cross-company=true&$filter=(dataAreaId eq 'USMF' and WarehouseId eq '1234')",
        {"WarehouseName": "Warehouse update test", "OperationalSiteId": "1", "WarehouseType": "Standard", "QuarantineWarehouseId": "18"}
	)


def test_read_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            Warehouses: { Operation: "Create", Key: {"WarehouseId": "1234"}, WarehouseId: "1234", WarehouseName: "Warehouse update test", dataAreaId: "USMF", OperationalSiteId: "1", WarehouseType: "Standard" }
    query: |
        # Task
        Retrieve details of an existing warehouse from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "1234"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the details for warehouse '1234'?")


def test_delete_InventLocations(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            Warehouses: { Operation: "Create", Key: {"WarehouseId": "12345"}, WarehouseId: "12345", WarehouseName: "Warehouse delete test", dataAreaId: "USMF", OperationalSiteId: "1", WarehouseType: "Standard" }
    query: |
        # Task
        Delete an existing warehouse record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Warehouse": "12345"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        f"Warehouses?cross-company=true&$filter=(dataAreaId eq 'USMF' and WarehouseId eq '12345')",
	)


def test_create_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
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

    fno_odataquerytool_judge.query_and_assert_fields(
        "LanguageCodes?$filter=LanguageCodeId eq 'test_language'&cross-company=true",
        {"LanguageCodeId": "test_language", "Description": "New language"},
    )


def test_update_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            LanguageCodes: { Operation: "Create", Key: {"LanguageCodeId": "test_language1"}, LanguageCodeId: "test_language1", Description: "New language 123" }
    query: |
        # Task
        Update the description of an existing language record in the USMF company in Dynamics 365 Finance and Operations.  Navigate via Human Resources > Setup > Language codes.

        # Data
        {
          "company": "USMF",
          "LanguageID": "test_language1",
          "Description": "Test Language Updated"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "LanguageCodes?$filter=LanguageCodeId eq 'test_language1'&cross-company=true",
        {"LanguageCodeId": "test_language1", "Description": "Test Language Updated"},
    )


def test_read_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            LanguageCodes: { Operation: "Create", Key: {"LanguageCodeId": "test_language2"}, LanguageCodeId: "test_language2", Description: "New language 12345" }
    query: |
        # Task
        Retrieve the details of an existing language record from the USMF company in Dynamics 365 Finance and Operations.  Navigate via Human Resources > Setup > Language codes.

        # Data
        {
          "company": "USMF",
          "Language code": "test_language2"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the details for language 'test_language2'?")


def test_delete_HcmLanguageCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            LanguageCodes: { Operation: "Create", Key: {"LanguageCodeId": "test_language3"}, LanguageCodeId: "test_language3", Description: "Delete language code" }
    query: |
        # Task
        Delete an existing language record from the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "LanguageID": "test_language3"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        "LanguageCodes?$filter=LanguageCodeId eq 'test_language3'&cross-company=true"
	)


def test_create_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new currency exchange rate in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "AMD",
          "ToCurrency": "AFN",
          "ConversionFactor": 10,
          "From date": "1/18/2025",
          "Exchange rate": 48
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "ExchangeRateCurrencyPairs?$filter=(FromCurrencyCode eq 'AMD' and ToCurrencyCode eq 'AFN')&cross-company=true",
        {"FromCurrencyCode": "AMD", "ToCurrencyCode": "AFN", "ExchangeRateDisplayFactor": "Ten"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        "ExchangeRates?$filter=(FromCurrency eq 'AMD' and ToCurrency eq 'AFN')&cross-company=true",
        {"ConversionFactor": "Ten", "StartDate": "2025-01-18T12:00:00Z", "RateTypeName": "Default", "Rate": 48}
	)


def test_create_ExchangeRateDataToolsExplicitEndpoints(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new currency exchange rate in the USMF company in Dynamics 365 Finance and Operations using the data tools.  Use the ExchangeRateCurrencyPairs endpoint first to create the exchange rate pair and then use the ExchangeRates endpoint to create the exchange rate.

        # Data
        # ExchangeRateCurrencyPairs
        {
          "company": "USMF",
          "FromCurrency": "AMD",
          "ToCurrency": "AFN",
          "ConversionFactor": Ten,
        }

        # ExchangeRates
        {
          "From date": "1/18/2025",
          "Exchange rate": 48
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "ExchangeRateCurrencyPairs?$filter=(FromCurrencyCode eq 'AMD' and ToCurrencyCode eq 'AFN')&cross-company=true",
        {"FromCurrencyCode": "AMD", "ToCurrencyCode": "AFN", "ExchangeRateDisplayFactor": "Ten"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        "ExchangeRates?$filter=(FromCurrency eq 'AMD' and ToCurrency eq 'AFN')&cross-company=true",
        {"ConversionFactor": "Ten", "StartDate": "2025-01-18T12:00:00Z", "Rate": 48}
	)

def test_update_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ExchangeRateCurrencyPairs: { Operation: "Create", Key: {"FromCurrencyCode": "ALL", "ToCurrencyCode": "AFN"}, FromCurrencyCode: "ALL", ToCurrencyCode: "AFN", ExchangeRateDisplayFactor: "1", ExchangeRateTypeName: "Default" }
            ExchangeRates: { Operation: "Create", Key: {"FromCurrency": "ALL", "ToCurrency": "AFN"}, FromCurrency: "ALL", ToCurrency: "AFN", StartDate: "2025-01-01", RateTypeName: "Default", Rate: 118, ConversionFactor: "One" }
    query: |
        # Task
        Update the from date between AMD and AFN for a given date in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "ALL",
          "ToCurrency": "AFN",
          "StartDate": "1/1/2025",
          "Exchange rate": 52
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "ExchangeRateCurrencyPairs?$filter=(FromCurrencyCode eq 'ALL' and ToCurrencyCode eq 'AFN')&cross-company=true",
        {"FromCurrencyCode": "ALL", "ToCurrencyCode": "AFN", "ExchangeRateDisplayFactor": "One"}
	)

    fno_odataquerytool_judge.query_and_assert_fields(
        "ExchangeRates?$filter=(FromCurrency eq 'ALL' and ToCurrency eq 'AFN')&cross-company=true",
        {"ConversionFactor": "One", "StartDate": "2025-01-01T12:00:00Z", "RateTypeName": "Default", "Rate": 52}
	)


def test_read_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ExchangeRateCurrencyPairs: { Operation: "Create", Key: {"FromCurrencyCode": "AED", "ToCurrencyCode": "ANG"}, FromCurrencyCode: "AED", ToCurrencyCode: "ANG", ExchangeRateDisplayFactor: "1", ExchangeRateTypeName: "Default" }
            ExchangeRates: { Operation: "Create", Key: {"FromCurrency": "AED", "ToCurrency": "ANG"}, FromCurrency: "AED", ToCurrency: "ANG", StartDate: "2025-01-01", RateTypeName: "Default", Rate: 118, ConversionFactor: "One" }
    query: |
        # Task
        Retrieve the exchange rate for a specific entry in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "AED",
          "ToCurrency": "ANG"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the details for exchange rate from AED to ANG?")


def test_delete_ExchangeRate(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ExchangeRateCurrencyPairs: { Operation: "Create", Key: {"FromCurrencyCode": "AOA", "ToCurrencyCode": "ARS"}, FromCurrencyCode: "AOA", ToCurrencyCode: "ARS", ExchangeRateDisplayFactor: "1", ExchangeRateTypeName: "Default" }
            ExchangeRates: { Operation: "Create", Key: {"FromCurrency": "AOA", "ToCurrency": "ARS"}, FromCurrency: "AOA", ToCurrency: "ARS", StartDate: "2025-01-01", RateTypeName: "Default", Rate: 118, ConversionFactor: "One" }
    query: |
        # Task
        Delete an existing currency exchange rate between AOA and ARS in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "FromCurrency": "AOA",
          "ToCurrency": "ARS"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        "ExchangeRateCurrencyPairs?$filter=(FromCurrencyCode eq 'AOA' and ToCurrencyCode eq 'ARS')&cross-company=true",
	)

    fno_odataquerytool_judge.query_and_assert_deleted(
        "ExchangeRates?$filter=(FromCurrency eq 'AOA' and ToCurrency eq 'ARS')&cross-company=true",
	)


def test_create_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new unit conversion rule from Celsius to Fahrenheit in the USMF company in Dynamics 365 Finance and Operations using the advanced formula layout.

        # Data
        {
          "company": "USMF",
          "From Unit": "°C",
          "To Unit": "°F",
          "FormulaLayout": "Advanced",
          "Rounding": "To nearest",
          "ConversionFormula": {
            "Factor": 1.0,
            "Numerator": 9,
            "Denominator": 5,
            "InnerOffset": 0,
            "OuterOffset": 32
          },
          "Definition": "1 °C = (9/5) * °F + 32"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "UnitOfMeasureConversions?$filter=(FromUnitSymbol eq '°C' and ToUnitSymbol eq '°F')&cross-company=true",
        {"InnerOffset": 0, "OuterOffset": 32, "Rounding": "Nearest", "Numerator": 9, "Factor": 1, "Denominator": 5}
	)


def test_update_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            UnitOfMeasureConversions: { Operation: "Create", Key: {"FromUnitSymbol": "°K", "ToUnitSymbol": "°C"}, FromUnitSymbol: "°K", ToUnitSymbol: "°C", InnerOffset: 0, OuterOffset: 100, "Rounding": "Nearest", "Numerator": 10, "Factor": 1, "Denominator": 11 }
    query: |
        # Task
        Update the conversion formula for the Kelvin to Celcius rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "From Unit": "°K",
          "To Unit": "°C",
          "FormulaLayout": "Advanced",
          "Rounding": "To nearest",
          "ConversionFormula": {
            "Factor": 1.0,
            "Numerator": 9,
            "Denominator": 5,
            "InnerOffset": 9,
            "OuterOffset": 32
          },
          "Definition": "1 °C = (9/5) * °F + 33"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        "UnitOfMeasureConversions?$filter=(FromUnitSymbol eq '°K' and ToUnitSymbol eq '°C')&cross-company=true",
        {"InnerOffset": 9, "OuterOffset": 32, "Rounding": "Nearest", "Numerator": 9, "Factor": 1, "Denominator": 5}
	)


def test_read_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            UnitOfMeasureConversions: { Operation: "Create", Key: {"FromUnitSymbol": "°K", "ToUnitSymbol": "°C"}, FromUnitSymbol: "°K", ToUnitSymbol: "°C", InnerOffset: 0, OuterOffset: 100, "Rounding": "Nearest", "Numerator": 10, "Factor": 1, "Denominator": 11 }
    query: |
        # Task
        Retrieve the unit conversion rule for the Kelvin to Celcius rule in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "From Unit": "°K",
          "To Unit": "°C"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the details for unit conversion from Kelvin to Celcius?")


def test_delete_UnitOfMeasureConversion(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            UnitOfMeasureConversions: { Operation: "Create", Key: {"FromUnitSymbol": "°K", "ToUnitSymbol": "°C"}, FromUnitSymbol: "°K", ToUnitSymbol: "°C", InnerOffset: 0, OuterOffset: 100, "Rounding": "Nearest", "Numerator": 10, "Factor": 1, "Denominator": 11 }
    query: |
        # Task
        Delete the unit conversion rule from Kelvin to Celcius in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "From Unit": "°K",
          "To Unit": "°C"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        "UnitOfMeasureConversions?$filter=(FromUnitSymbol eq '°K' and ToUnitSymbol eq '°C')&cross-company=true",
	)

def test_create_CustPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            SequenceV2Tables: { Operation: "Update", Key: {"NumberSequenceCode": "Gene_113", "ScopeType": Microsoft.Dynamics.DataEntities.NumberSequenceType'DataArea', "ScopeValue": "USMF"}, Continuous: "No" }
    query: |
        # Task
        Create a new customer payment journal in the USMF company in Dynamics 365 Finance and Operations.  Use the form* tools to complete the task.  
        # Steps
        1.  Set the name first.
        2.  Then set the description.
        3.  Once processing has completed, return the JournalBatchNumber and output in json format.

        # Data
        {
          "Company Name": "USMF",
          "Name": "CustPay",
          "Description": "Payment by customer",
        }
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"CustomerPaymentJournalHeaders?cross-company=true&$filter=(dataAreaId eq 'USMF' and JournalBatchNumber eq '{journal_batch_number}')",
        {"JournalName": "CustPay", "Description": "Payment by customer"}
	)


# It appears that init is having issues due to number sequences, so working around by using demo record.
def test_update_CustPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Update the description of existing customer payment journal "00475" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the JournalBatchNumber and output in json format.

        # Data
        {
          "Name": "USMF",
          "Description": "This is my test payment"
        }
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"CustomerPaymentJournalHeaders?cross-company=true&$filter=(dataAreaId eq 'USMF' and JournalBatchNumber eq '{journal_batch_number}')",
        {"JournalName": "CustPay", "Description": "This is my test payment"}
	)

# It appears that init is having issues due to number sequences, so working around by using demo record.
def test_read_CustPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Retrieve the customer payment journal "00475" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the JournalBatchNumber and other details in json field and value format like the following:  "JournalBatchNumber": "VALUE".  Make sure to include JournalBatchNumber in the response.
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    assert judge.text_yesno(x.response, f"Does the message provide the customer payment journal information for journal batch number {journal_batch_number}?")  


# It appears that init is having issues due to number sequences, so working around by using demo record.
def test_delete_CustPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            CustomerPaymentJournalHeaders: { Operation: "Create", Key:{"JournalBatchNumber": "@Out"}, dataAreaId: "USMF", "JournalName": "CustPay", "Description": "Test description" }
    query: |
        # Task
        Delete customer payment journal "{init[fnoproxy][CustomerPaymentJournalHeaders][JournalBatchNumber]}" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the JournalBatchNumber and output in json format.
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    fno_odataquerytool_judge.query_and_assert_deleted(
        f"CustomerPaymentJournalHeaders?cross-company=true&$filter=(dataAreaId eq 'USMF' and JournalBatchNumber eq '{journal_batch_number}')"
    )

def test_create_VendorPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            SequenceV2Tables: { Operation: "Update", Key: {"NumberSequenceCode": "Gene_113", "ScopeType": Microsoft.Dynamics.DataEntities.NumberSequenceType'DataArea', "ScopeValue": "USMF"}, Continuous: "No" }
    query: |
        # Task
        Create a new vendor payment in the USSI company in Dynamics 365 Finance and Operations.  
        # Steps
        1.  Set the name.
        2.  Set the description.
        3.  Once processing has completed, return the JournalBatchNumber and output in json format.

        # Data
        {
          "Name": "VendPay",
          "Description": "Payment by Vendor",
        }
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"VendorPaymentJournalHeaders?cross-company=true&$filter=(dataAreaId eq 'USSI' and JournalBatchNumber eq '{journal_batch_number}')",
        {"JournalName": "VendPay", "Description": "Payment by Vendor"}
	)

def test_update_VendorPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            VendorPaymentJournalHeaders: { Operation: "Create", Key:{"JournalBatchNumber": "@Out"}, dataAreaId: "USSI", "JournalName": "VendPay", "Description": "Test description" }
    query: |
        # Task
        Modify existing vendor payment journal "{init[fnoproxy][VendorPaymentJournalHeaders][JournalBatchNumber]}" in the USSI company in Dynamics 365 Finance and Operations.  Once processing has completed, return the JournalBatchNumber and output in json format.

        # Data
        {
          "Description": "Updated description",
        }
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"VendorPaymentJournalHeaders?cross-company=true&$filter=(dataAreaId eq 'USSI' and JournalBatchNumber eq '{journal_batch_number}')",
        {"JournalName": "VendPay", "Description": "Updated description"}
	)


def test_read_VendorPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            VendorPaymentJournalHeaders: { Operation: "Create", Key:{"JournalBatchNumber": "@Out"}, dataAreaId: "USSI", "JournalName": "VendPay", "Description": "Read test description" }
    query: |
        # Task
        Retrieve the vendor payment journal "{init[fnoproxy][VendorPaymentJournalHeaders][JournalBatchNumber]}" in the USSI company in Dynamics 365 Finance and Operations.  Once processing has completed, return the JournalBatchNumber and other details in json field and value format like the following:  "JournalBatchNumber": "VALUE".  Make sure to include JournalBatchNumber in the response.
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    assert judge.text_yesno(x.response, f"Does the message provide the JournalBatchNumber for a vendor payment journal?") 


def test_delete_VendorPaymentJournal(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            VendorPaymentJournalHeaders: { Operation: "Create", Key: {"JournalBatchNumber": "@Out"}, dataAreaId: "USSI", "JournalName": "VendPay", "Description": "Test description" }
    query: |
        # Task
        Delete a vendor payment journal "{init[fnoproxy][VendorPaymentJournalHeaders][JournalBatchNumber]}" in the USSI company in Dynamics 365 Finance and Operations.  Once processing has completed, return the JournalBatchNumber and output in json format.
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    fno_odataquerytool_judge.query_and_assert_deleted(
        f"VendorPaymentJournalHeaders?cross-company=true&$filter=(dataAreaId eq 'USSI' and JournalBatchNumber eq '{journal_batch_number}')"
    )


# This test covers creation of vendor invoice journal using form tools with explicit navigation. Covers lookup controls that do not bound to a data source.
def test_create_VendorInvoiceJournal_ExplicitNavigation(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            SequenceV2Tables: { Operation: "Update", Key: {"NumberSequenceCode": "Gene_113", "ScopeType": Microsoft.Dynamics.DataEntities.NumberSequenceType'DataArea', "ScopeValue": "USMF"}, Continuous: "No" }
    query: |
        # Task
        Create a new vendor invoice journal using APInvoice journal type using form* tools. Use 'LedgerJournalTable9' menu item in USMF company. Add 1 line added to it for vendor account 1001.
        Specify invoice reference to be INV-0012, and the credit amount to be 200 USD. In financial dimensions for Account, choose 022 as the Department for account dimension values.
        Save all the changes. Once processing has completed, return the JournalBatchNumber and output in json format.
    """

    journal_batch_number = fno_test_helper.parse_response_for_value(x.response, "JournalBatchNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"VendInvoiceJournalHeaders?cross-company=true&$filter=(dataAreaId eq 'USMF' and JournalBatchNumber eq '{journal_batch_number}')",
        {"JournalName": "APInvoice", "Description": "AP Invoice", "dataAreaId": "usmf"}
    )

    fno_odataquerytool_judge.query_and_assert_fields(
        f"VendInvoiceJournalLines?cross-company=true&$filter=(dataAreaId eq 'USMF' and JournalBatchNumber eq '{journal_batch_number}')",
        {"AccountDisplayValue": "1001", "Credit": 200, "Currency": "USD", "OffsetAccountDisplayValue": "606300-001--"}
    )


# This tests is dependent on existing demo data of customer invoices in DEMF for Intrastat reporting for November 2016.
# Judge agent is used here instead of OData validation since there are no details on the shipment batch number in the response related to transfer, to filter the records via OData query.
def test_Intrastats_TransferCustomerInvoices(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        In DEMF legal entity, transfer customer invoices for Intrastat reporting for the November 2016 reporting period using form* tools. Delete any existing records for the period before transferring the invoices.
        Once processing has completed, return the number of records transferred in json format.

    """

    # Verify the response contains the number of records transferred
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the message confirm that there are 20 records transferred for Intrastat reporting for November 2016 in DEMF legal entity? Do not query any OData endpoints for validation. Use only the information in the response messages.",
    )


def test_Intrastat_AddDispatchLine(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        In DEMF, add and validate a dispatch line for Intrastat reporting using form* tools.

        CRITICAL: Select Item Number BEFORE setting Weight/amounts (item selection resets fields).

        Order: Date, Direction, Item (D0001), Weight (3), Invoice/Statistical (1000), Commodity (900 22 33), Save, Validate

        Data: Date=11/25/2016, Direction=Dispatches, Item=D0001, Weight=3, Invoice=1000, Statistical=1000, Commodity=900 22 33

    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"IntrastatsV2?cross-company=true&$filter=(dataAreaId eq 'DEMF' and ItemNumber eq 'D0001' and Date eq 2016-11-25T12:00:00Z)",
        {"Commodity": "900 22 33", "Weight": 3, "InvoiceAmount": 1000, "StatisticalAmount": 1000, "CommodityName": "Projector"}
    )


# A case where a warning is expected when adding an EU sales list dispatch line with a country that is not in the EU.
def test_EUSalesList_AddDispatchLine_Warns(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        In DEMF legal entity, add and validate a dispatch line for EU Sales list reporting in Dynamics 365 Finance and Operations using form* tools.

        # Data
        {
          "Company": "DEMF",
          "Account Number": "DE-010",
          "Country Region": "DEU",
          "Tax Exempt Number": "DE124363748",
          "Invoice Date": "11/25/2016",
          "Item Value": 1000
        }

    """

    assert judge.text_yesno(x.response, """Does the message indicate that there was a warning to
            'Check EU sales list Account number: DE-010 Country/Region DEU is not established as an EU member state.' when the form was saved?""")


    # Verify the dispatch line was added with the correct field values using OData query
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesLists?cross-company=true&$filter=(dataAreaId eq 'DEMF' and AccountNumber eq 'DE-010' and InvoiceDate eq 2016-11-25T12:00:00Z)",
        {"CountryRegionId": "DEU", "TaxExemptNumber": "DE124363748", "ItemsValue": 1000}
    )


# Same test as above, but to show a valid case where no warning is expected.
def test_EUSalesList_AddDispatchLine_Valid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        In DEMF legal entity, add and validate a dispatch line for EU Sales list reporting in Dynamics 365 Finance and Operations using form* tools.

        # Data
        {
          "Company": "DEMF",
          "Account Number": "DE-015",
          "Country Region": "ITA",
          "Tax Exempt Number": "DE124363748",
          "Invoice Date": "11/25/2016",
          "Item Value": 1000
        }

    """

    assert judge.text_yesno(x.response, """Does the message say that the dispatch line was created without any warnings when the form was saved?""")


    # Verify the dispatch line was added with the correct field values using OData query
    fno_odataquerytool_judge.query_and_assert_fields(
        f"SalesLists?cross-company=true&$filter=(dataAreaId eq 'DEMF' and AccountNumber eq 'DE-015' and InvoiceDate eq 2016-11-25T12:00:00Z)",
        {"CountryRegionId": "ITA", "TaxExemptNumber": "DE124363748", "ItemsValue": 1000}
    )


def test_create_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            SequenceV2Tables: { Operation: "Update", Key: {"NumberSequenceCode": "Fixe_17", "ScopeType": Microsoft.Dynamics.DataEntities.NumberSequenceType'DataArea', "ScopeValue": "USMF"}, Continuous: "No" }
    query: |
        # Task
        Create a new fixed asset record in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the FixedAssetNumber and output in json format.

        # Data
        {
          "company": "USMF",
          "FixedAssetGroup": "BUILDINGS",
          "Name": "building-test2",
          "Type": "Financial",
          "MajorType": "OWN_BUILD",
          "PropertyType": "Other",
          "Quantity": 18,
        }
    """

    fixed_asset_number = fno_test_helper.parse_response_for_value(x.response, "FixedAssetNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"FixedAssetsV2?cross-company=true&$filter=(dataAreaId eq 'USMF' and FixedAssetNumber eq '{fixed_asset_number}')",
        {"FixedAssetGroupId": "BUILDINGS", "Name": "building-test2", "Type": "Financial", "MajorTypeId": "OWN_BUILD", "PropertyType": "Other", "Quantity": 18}
    )


def test_update_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            FixedAssetsV2: { Operation: "Create", Key:{"FixedAssetNumber": "@Out"}, dataAreaId: "USMF", "FixedAssetGroupId": "BUILDINGS", "Name": "update test", "Type": "Financial", "MajorTypeId": "OWN_BUILD", "PropertyType": "Other", "Quantity": 18 }
    query: |
        # Task
        Modify existing fixed asset "{init[fnoproxy][FixedAssetsV2][FixedAssetNumber]}" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the FixedAssetNumber and output in json format.

        # Data
        {
          "Quantity": 118,
        }
    """

    fixed_asset_number = fno_test_helper.parse_response_for_value(x.response, "FixedAssetNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"FixedAssetsV2?cross-company=true&$filter=(dataAreaId eq 'USMF' and FixedAssetNumber eq '{fixed_asset_number}')",
        {"FixedAssetGroupId": "BUILDINGS", "Name": "update test", "Type": "Financial", "MajorTypeId": "OWN_BUILD", "PropertyType": "Other", "Quantity": 118}
    )


def test_read_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            FixedAssetsV2: { Operation: "Create", Key: {"FixedAssetNumber": "@Out"}, dataAreaId: "USMF", "FixedAssetGroupId": "BUILDINGS", "Name": "read test", "Type": "Financial", "MajorTypeId": "OWN_BUILD", "PropertyType": "Other", "Quantity": 18 }
    query: |
        # Task
        Retrieve the information of existing fixed asset "{init[fnoproxy][FixedAssetsV2][FixedAssetNumber]}" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the FixedAssetNumber and other details in json field and value format like the following:  "FixedAssetNumber": "VALUE".  Make sure to include FixedAssetNumber in the response.
    """

    fixed_asset_number = fno_test_helper.parse_response_for_value(x.response, "FixedAssetNumber")
    assert judge.text_yesno(x.response, f"Does the message provide the information for fixed asset {fixed_asset_number}?")


def test_delete_FixedAsset(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            FixedAssetsV2: { Operation: "Create", Key:{"FixedAssetNumber": "@Out"}, dataAreaId: "USMF", "FixedAssetGroupId": "BUILDINGS", "Name": "delete test", "Type": "Financial", "MajorTypeId": "OWN_BUILD", "PropertyType": "Other", "Quantity": 18 }
    query: |
        # Task
        Delete existing fixed asset "{init[fnoproxy][FixedAssetsV2][FixedAssetNumber]}" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the FixedAssetNumber and output in json format.  
    """

    fixed_asset_number = fno_test_helper.parse_response_for_value(x.response, "FixedAssetNumber")
    fno_odataquerytool_judge.query_and_assert_deleted(
        f"FixedAssetsV2?cross-company=true&$filter=(dataAreaId eq 'USMF' and FixedAssetNumber eq '{fixed_asset_number}')",
    )

# Using form tools to work around https://msdyneng.visualstudio.com/FinOps/_workitems/edit/1082550
def test_create_BudgetRegisterEntry(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new budget register entry in the USMF company in Dynamics 365 Finance and Operations using form tools.  Once processing has completed, return the EntryNumber and output in json format.

        # Data
        {
          "company": "USMF",
          "Budget model": "FY2018",
          "Budget code": "CarryForward"
        }
    """

    budget_register_entry_header_number = fno_test_helper.parse_response_for_value(x.response, "EntryNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"BudgetRegisterEntryHeaders?cross-company=true&$filter=(dataAreaId eq 'USMF' and EntryNumber eq '{budget_register_entry_header_number}')",
        {"BudgetModelId": "FY2018", "BudgetCode": "CarryForward"}
    )

# Since we can't create the budger register entry in init due to the bug, modifying an existing record in demo data instead.
def test_update_BudgetRegisterEntry(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Modify existing budget register "USMF000008" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the EntryNumber and output in json format.  

        # Data
        {
          "Reason code": "ADJ"
        }
    """

    budget_register_entry_header_number = fno_test_helper.parse_response_for_value(x.response, "EntryNumber")
    fno_odataquerytool_judge.query_and_assert_fields(
        f"BudgetRegisterEntryHeaders?cross-company=true&$filter=(dataAreaId eq 'USMF' and EntryNumber eq '{budget_register_entry_header_number}')",
        {"ReasonCode": "ADJ"}
    )

# Since we can't create the budger register entry in init due to the bug, modifying an existing record in demo data instead.
def test_read_BudgetRegisterEntry(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Retrieve the information for existing budget register "USMF000008" in the USMF company in Dynamics 365 Finance and Operations.
    """

    assert judge.text_yesno(x.response, f"Does the message provide the information for budget register record with entry number USMF000008?")


# Since we can't create the budger register entry in init due to the bug, modifying an existing record in demo data instead.
def test_delete_BudgetRegisterEntry(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Delete the existing budget register "USMF000008" in the USMF company in Dynamics 365 Finance and Operations.  Once processing has completed, return the EntryNumber and other output in json format. 
    """

    budget_register_entry_header_number = fno_test_helper.parse_response_for_value(x.response, "EntryNumber")
    fno_odataquerytool_judge.query_and_assert_deleted(
        f"BudgetRegisterEntryHeaders?cross-company=true&$filter=(dataAreaId eq 'USMF' and EntryNumber eq '{budget_register_entry_header_number}')",
    )

# Set this to use the form tools because the data tools don't work due to not having data in related tables.
def test_create_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Create a new released product in the USMF company in Dynamics 365 Finance and Operations using the form tools.  Initial navigation should start with the EcoResProductDetailsExtendedGrid menu item.  

        # Data
        {
          "company": "USMF",
          "Product number": "118",
          "Item number": "118",
          "Inventory unit": "°C",
          "Purchase unit": "°C",
          "Sales unit": "°C"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"ReleasedProductsV2?cross-company=true&$filter=(dataAreaId eq 'USMF' and ItemNumber eq '118')",
        {"ProductNumber": "118", "InventoryUnitSymbol": "°C", "PurchaseUnitSymbol": "°C", "SalesUnitSymbol": "°C"}
    )

def test_update_EcoResProductDetailsExtendedGrid_ExplicitNavigation(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ProductsV2: { Operation: "Create", Key:{"ProductNumber": "12345"}, ProductNumber: "12345"}        
            ReleasedProductsV2: { Operation: "Create", Key:{"ProductNumber": "12345"}, ProductNumber: "12345", ItemNumber: "12345", dataAreaId: "USMF"}
    query: |
        # Task
        Update the released product with product number "12345" in the USMF company in Dynamics 365 Finance and Operations.  Use the form tools.  Initial navigation should start with the EcoResProductDetailsExtendedGrid menu item.  
        On the details page, the "Net weight" field is available under the "Manage inventory" tab.

        # Data
        {
          "company": "USMF",
          "Net weight": 18
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"ReleasedProductsV2?cross-company=true&$filter=(dataAreaId eq 'USMF' and ProductNumber eq '12345')",
        {"NetProductWeight": 18}
    )

# Same as above but without explicit navigation
def test_update_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ProductsV2: { Operation: "Create", Key:{"ProductNumber": "12345"}, ProductNumber: "12345"}        
            ReleasedProductsV2: { Operation: "Create", Key:{"ProductNumber": "12345"}, ProductNumber: "12345", ItemNumber: "12345", dataAreaId: "USMF"}
    query: |
        # Task
        Update the released product with product number "12345" in the USMF company in Dynamics 365 Finance and Operations.  

        # Data
        {
          "company": "USMF",
          "Net weight": 18
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"ReleasedProductsV2?cross-company=true&$filter=(dataAreaId eq 'USMF' and ProductNumber eq '12345')",
        {"NetProductWeight": 18}
    )

def test_read_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Retrieve information of an existing released product in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "company": "USMF",
          "Item number": "4403"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the information for released product with item number '4403'?")


def test_delete_EcoResProductDetailsExtendedGrid(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            ProductsV2: { Operation: "Create", Key:{"ProductNumber": "123456"}, ProductNumber: "123456"}        
            ReleasedProductsV2: { Operation: "Create", Key:{"ProductNumber": "123456"}, ProductNumber: "123456", ItemNumber: "123456", dataAreaId: "USMF"}
    query: |
        # Task
        Delete an existing released product record in the USMF company in Dynamics 365 Finance and Operations.
        # Data
        {
          "company": "USMF",
          "Product number": "123456"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        f"ReleasedProductsV2?cross-company=true&$filter=(dataAreaId eq 'USMF' and ProductNumber eq '123456')"
    )
    


# Fixed Assets > Setup > Fixed asset attributes
def test_create_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
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

    fno_odataquerytool_judge.query_and_assert_fields(
        f"AcquisitionMethods?cross-company=true&$filter=(dataAreaId eq 'USMF' and AcquisitionMethod eq 'test_method')",
        {"Description": "This is a test."}
    )


def test_update_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AcquisitionMethods: { Operation: "Create", AcquisitionMethod: "Update test", Description: "This is a test.", dataAreaId: "USMF" }
    query: |
        # Task
        Update an existing acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "Update test",
          "Description": "Updated description"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"AcquisitionMethods?cross-company=true&$filter=(dataAreaId eq 'USMF' and AcquisitionMethod eq 'Update test')",
        {"Description": "Updated description"}
    )


def test_read_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AcquisitionMethods: { Operation: "Create", AcquisitionMethod: "Read test", Description: "This is a test.", dataAreaId: "USMF" }
    query: |
        # Task
        Retrieve information of an existing acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "Read test"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the information for the acquisition method 'Read test'?")


def test_delete_AssetAcquisitionMethod(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AcquisitionMethods: { Operation: "Create", AcquisitionMethod: "Delete test", Description: "This is a delete test.", dataAreaId: "USMF" }
    query: |
        # Task
        Delete an existing acquisition method in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "acquisition method": "Delete test"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        f"AcquisitionMethods?cross-company=true&$filter=(dataAreaId eq 'USMF' and AcquisitionMethod eq 'Delete test')",
    )

def test_create_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
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

    fno_odataquerytool_judge.query_and_assert_fields(
        f"AssetActivityCodes?cross-company=true&$filter=(dataAreaId eq 'USMF' and ActivityCode eq 'test_code')",
        {"Description": "This is a test asset code."}
    )


def test_update_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AssetActivityCodes: { Operation: "Create", ActivityCode: "test_update", Description: "This is an update test.", dataAreaId: "USMF" }
    query: |
        # Task
        Update an existing asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "test_update",
          "Description": "This is an updated description."
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"AssetActivityCodes?cross-company=true&$filter=(dataAreaId eq 'USMF' and ActivityCode eq 'test_update')",
        {"Description": "This is an updated description."}
    )


def test_read_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AssetActivityCodes: { Operation: "Create", ActivityCode: "test_read", Description: "This is a read test.", dataAreaId: "USMF" }
    query: |
        # Task
        Retrieve information on an existing asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "test_read"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the information for the asset activity code 'test_read'?")


def test_delete_AssetActivityCode(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AssetActivityCodes: { Operation: "Create", ActivityCode: "test_del", Description: "This is a delete test.", dataAreaId: "USMF" }
    query: |
        # Task
        Delete an existing asset activity code in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset activity code": "test_del"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        f"AssetActivityCodes?cross-company=true&$filter=(dataAreaId eq 'USMF' and ActivityCode eq 'test_del')"
    )


def test_create_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
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

    fno_odataquerytool_judge.query_and_assert_fields(
        f"AssetConditions?cross-company=true&$filter=(dataAreaId eq 'USMF' and ConditionCode eq 'Medium')",
        {"Description": "Medium condition"}
    )


def test_update_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AssetConditions: { Operation: "Create", ConditionCode: "updatecondition", Description: "This is an update test.", dataAreaId: "USMF" }
    query: |
        # Task
        Update an existing fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "updatecondition",
          "Description": "Updated Medium condition"
        }
    """

    fno_odataquerytool_judge.query_and_assert_fields(
        f"AssetConditions?cross-company=true&$filter=(dataAreaId eq 'USMF' and ConditionCode eq 'updatecondition')",
        {"Description": "Updated Medium condition"}
    )


def test_read_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AssetConditions: { Operation: "Create", ConditionCode: "readcondition", Description: "This is a read test.", dataAreaId: "USMF" }
    query: |
        # Task
        Retrieve information of an existing fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "readcondition"
        }
    """

    assert judge.text_yesno(x.response, "Does the message provide the information for the fixed asset condition 'readcondition'?")


def test_delete_AssetConditions(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    init:
        fnoproxy:
            AssetConditions: { Operation: "Create", ConditionCode: "deletecondition", Description: "This is a delete test.", dataAreaId: "USMF" }
    query: |
        # Task
        Delete an existing fixed asset condition in the USMF company in Dynamics 365 Finance and Operations.

        # Data
        {
          "Asset condition": "deletecondition"
        }
    """

    fno_odataquerytool_judge.query_and_assert_deleted(
        f"AssetConditions?cross-company=true&$filter=(dataAreaId eq 'USMF' and ConditionCode eq 'deletecondition')"
    )

def test_create_supportcase(
    x: TestContext,
    judge: Judge,
    judgeAgent: JudgeAgent,
    fno_odataquerytool_judge: fno_odataquerytool,
):
    """!
    query: |
        # Final tool usage instructions
        Use form tools to complete the task. Do not use data tools.

        # Task
        Create a new support case in the USMF company. Category: Sales/Issues/Speakers.  Once processing has completed, return the case id as output in json format.
    """

    # there is no odata entity to validate case management data
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="""
        # Tools to use for validation
        Do not use data tools for validation. Use form tools.
        # Validation steps
        - Go to the All Cases form.
        - Verify that a case with the returned case id exists.
        - Filter the grid to the new case id.
        - Open the details of the case. 
        - Verify that the category is set to Sales/Issues/Speakers. """,
    )

# This test is currently failing because of Bug 5956501: Cannot create a new association in case management. https://dev.azure.com/dynamicscrm/OneCRM/_workitems/edit/5957200
def test_update_supportcase_add_link_to_sales_order(
    x: TestContext,
    judge: Judge,
    judgeAgent: JudgeAgent,
    fno_odataquerytool_judge: fno_odataquerytool,
):
    """!
    query: |
        # Final tool usage instructions
        Use form tools to complete the task. Do not use data tools.

        # Task        
        Find support case "00023" in the USMF company. Link with the sales order "000810" by creating the association on the associations tab.
    """

    # there is no odata entity to validate case management data
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="""
        # Tools to use for validation
        Do not use data tools for validation. Use form tools.
        # Validation steps
        - Go to the All Cases form.
        - Filter the grid to case "00023".
        - Open the details of the case.
        - Open the Associations tab.
        - Check if there is an association between the case and the sales order '000810'. """,
    )


def test_update_FiscalCalendar2025Period6_SetOnHold_MultipleEntities(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Using form tools, change the period status to "On hold" for the Fiscal calendar for Fiscal Year 2025, Period 6 in the ledger calendar for the following legal entities: GBSI, GLCO, and DEMF.
        
    """

    # No OData entity available for fiscal calendar period configuration
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="""
            Does the message confirm that the period status was successfully updated for Fiscal Year 2025, Period 6? Use form tools to validate.

            # Validation steps
            - Navigate to the LedgerCalendars menu item.
            - Find the Fiscal calendar for Fiscal Year 2025.
            - Locate Period 6 in the periods grid.
            - In the Legal entities grid for Period 6, verify that the Period status value equals "On hold" for each of the following legal entities:
              - GBSI
              - GLCO
              - DEMF
        """,
    )


def test_terminate_EmployeeJuneLow_Involuntary(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Using form tools, terminate an employee as of today with a termination reason. Today's date is {init[fnoproxy][CurrentDate]}. The employee details are as follows:

        # Data
        {
          "Employee Name": "June Low",
          "Termination Reason": "Involuntary"
        }
        
    """

    # Get today's date for validation
    today_date = fno_test_helper.get_future_datetime_formatted(0, None, True)

    # Update the time to T23:59:59Z to match the EmploymentEndDate format
    today_date = today_date.replace("T12:00:00Z", "T23:59:59Z")

    # Verify via OData that the employment record has been terminated
    fno_odataquerytool_judge.query_and_assert_fields(
        "EmploymentDetails?$filter=(PersonnelNumber eq '000017')&$orderby=ValidFrom desc&$top=1",
        {"EmploymentEndDate": today_date, "ReasonCodeId": "Involuntary", "BenefitEmploymentStatus": "Terminated"},
    )


def test_create_EmployeeSkill_JuliaFunderburk_Accounting(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        Add a new skill to an employee record with a specific level as of today's date. Today's date is {init[fnoproxy][CurrentDate]}

        # Data
        {
          "Employee Name": "Julia Funderburk",
          "Skill": "Accounting",
          "Level": "4",
        }
    """

    # Get today's date for validation
    today_date = fno_test_helper.get_future_datetime_formatted(0, None, True)

    # Verify via OData that the skill record was created
    fno_odataquerytool_judge.query_and_assert_fields(
        f"WorkerSkills?$filter=(PersonnelNumber eq '000020' and LevelDate eq {today_date})",
        {"PersonnelNumber": "000020", "SkillId": "Accounting", "LevelId": "4"},
    )

#generate Random Number between 1 and 100 with specific Custom API in prompt
def test_generate_RandomNumber_API_Specific(x: TestContext, judge: Judge):

    """!
    query: |
        Use the CustomAPIRandomNumber custom API to generate a random number between 1 and 100.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "CustomAPIRandomNumberActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see the generated random number is between 1 and 100 in the response")

#generate Random Number between 1 and 100 with F&O action prompt
def test_generate_RandomNumber_FnO_Action(x: TestContext, judge: Judge):

    """!
    query: |
        Generate random number between 1 and 100 using an action in F&O.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "CustomAPIRandomNumberActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see the generated random number is between 1 and 100 in the response")

#generate Random Number between 1 and 100 with broad action prompt
def test_generate_RandomNumber_Action_Range_Broad(x: TestContext, judge: Judge):

    """!
    query: |
        Generate random number between 1 and 100 using an action
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "CustomAPIRandomNumberActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see the generated random number is between 1 and 100 in the response")

#generate Random Number between 1 and 100 with broad Custom API in prompt
def test_generate_RandomNumber_API_Broad(x: TestContext, judge: Judge):

    """!
    query: |
        Use custom API to generate a random number between 1 and 100.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "CustomAPIRandomNumberActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see the generated random number is between 1 and 100 in the response")

#generate Random Number between 1 and 100 with broad action prompt
def test_generate_RandomNumber_Action_Broad(x: TestContext, judge: Judge):

    """!
    query: |
        Get a random number using an action in F&O.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "CustomAPIRandomNumberActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see the generated random number in the response")

#generate Random Number between 1 and 100 with synonym 1 broad action prompt
#Known issue due https://dev.azure.com/dynamicscrm/OneCRM/_workitems/edit/5846020
def test_generate_RandomNumber_Synonym_1(x: TestContext, judge: Judge):

    """!
    query: |
        Get a chance number with F&O
    """
    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "CustomAPIRandomNumberActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see the generated random number in the response")

#generate Random Number between 1 and 100 with synonym 2 broad action prompt
#Known issue due https://dev.azure.com/dynamicscrm/OneCRM/_workitems/edit/5846020
def test_generate_RandomNumber_Synonym_2(x: TestContext, judge: Judge):

    """!
    query: |
        Pop a chance number with F&O
    """
    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "CustomAPIRandomNumberActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see the generated random number is between 1 and 100 in the response")

#check MCP server availability with actions in prompt
def test_check_McpServerAvailability(x: TestContext, judge: Judge):

    """!
    query: |
        Use actions to tell me whether the MCP server is available.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "McpStatusCustomAPIActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see if response indicates MCP Server is available")

#check MCP server availability with actions in prompt
#Known issue due https://dev.azure.com/dynamicscrm/OneCRM/_workitems/edit/5846020
def test_check_McpServerAvailability_Synonym(x: TestContext, judge: Judge):

    """!
    query: |
        Use actions to see if MCP Server is up
    """
    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "McpStatusCustomAPIActionMenuItem")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see if response indicates MCP Server is available")

#Get Vendor Invoice Context given Vendor Invoice Number and Invoice Account and action in prompt
def test_GetVendorInvoiceContext_Action(x: TestContext, judge: Judge):

    """!
    query: |
        Get vendor invoice context using actions. Vendor invoice id is "inv 92207" and invoice account "1001" in company usmf.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "VendInvoiceGetInvoiceContextCustomAPI")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see vendor invoice context for Invoice ID 'inv 92207', vendor account '1001', company 'usmf' is provided and invoice context has Vendor Name 'Acme Office Supplies' in the response")

#Get Vendor Invoice Context given Vendor Invoice Number and Invoice Account and action in prompt with synonym
#Known issue due https://dev.azure.com/dynamicscrm/OneCRM/_workitems/edit/5846020
def test_GetVendorInvoiceContext_Action_Synonym(x: TestContext, judge: Judge):

    """!
    query: |
        Retrieve vendor billing background using actions. Vendor invoice id is "inv 92207" and invoice account "1001" in company usmf.
    """
    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "VendInvoiceGetInvoiceContextCustomAPI")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see vendor invoice context for Invoice ID 'inv 92207', vendor account '1001', company 'usmf' is provided and invoice context has Vendor Name 'Acme Office Supplies' in the response")

#Get Vendor Invoice Context given Vendor Invoice Number and Invoice Account in prompt with synonym
#Known issue due https://dev.azure.com/dynamicscrm/OneCRM/_workitems/edit/5846020
def test_GetVendorInvoiceContext_Action_Synonym_2(x: TestContext, judge: Judge):

    """!
    query: |
        Find vendor billing particulars. Vendor invoice id is "inv 92207" and invoice account "1001" in company usmf.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "VendInvoiceGetInvoiceContextCustomAPI")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see vendor invoice context for Invoice ID 'inv 92207', vendor account '1001', company 'usmf' is provided and invoice context has Vendor Name 'Acme Office Supplies' in the response")

#Test Echo Custom API Specific Prompt with action keyword
def test_TestEchoCustomAPI_Specific(x: TestContext, judge: Judge):

    """!
    query: |
        Use actions to echo 'Hello' in F&O.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "McpTestEchoCustomApi")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see 'Hello' is echoed in the response")

#Test Echo Custom API Generic Prompt
def test_TestEchoCustomAPI_Generic(x: TestContext, judge: Judge):

    """!
    query: |
        Echo 'Hello' in F&O.
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "McpTestEchoCustomApi")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see 'Hello' is echoed in the response")

#Test Vendor Invoice Notifcation Specific Prompt
def test_VendorInvoiceNotification_Specific(x: TestContext, judge: Judge):

    """!
    query: |
        Use actions to notify the responsible employee for vendor account 1001 with the message "Risk analysis needed for vendor 1001."
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "VendInvoiceNotifyVendorResponsibleEmployeeCustomAPI")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see Employee was notified with 'Risk analysis needed for vendor 1001.' in the response")

#Test Vendor Invoice Notifcation Generic Prompt
def test_VendorInvoiceNotification_Generic(x: TestContext, judge: Judge):

    """!
    query: |
        Notify the responsible employee for vendor account 1001 with the message "Risk analysis needed for vendor 1001."
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "VendInvoiceNotifyVendorResponsibleEmployeeCustomAPI")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see Employee was notified with 'Risk analysis needed for vendor 1001.' in the response")

#Test Vendor Invoice Notifcation Prompt Synonym
#Known issue due https://dev.azure.com/dynamicscrm/OneCRM/_workitems/edit/5846020
def test_VendorInvoiceNotification_Synonym(x: TestContext, judge: Judge):

    """!
    query: |
       Inform the responsible employee for vendor account 1001 with the message "Risk analysis needed for vendor 1001."
    """

    # Verify custom API tool call was made
    fno_test_helper.validate_custom_api_tool_call(x, "VendInvoiceNotifyVendorResponsibleEmployeeCustomAPI")

    # Verify the response from the agent
    assert judge.text_yesno(x.response, "Check to see Employee was notified with 'Risk analysis needed for vendor 1001.' in the response")
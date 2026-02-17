from thinkingbox.common import Judge, TestContext
from thinkingbox.tools.judgeagent import JudgeAgent

"""!
scenario: fno
"""


# hotel category
# 1.create
def test_hotel1(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Grand Boston Hotel','MerchantAddress':'45 Beacon St, Boston, MA, USA','TransactionDate':'2022-07-14','Subtotal':'865','Tax':'86.5','Tip':'50','Total':'1001.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MA','Description':'Business trip for the Northeast Tech Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-07-11","ItemAmount":"280.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"28.00"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-07-12","ItemAmount":"280.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"28.00"}]},{"ItemName":"Restaurant","TransactionDate":"2022-07-13","ItemAmount":"155.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"15.50"}]},{"ItemName":"Conference room","TransactionDate":"2022-07-12","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"15.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Grand Boston Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Grand Boston Hotel' have all 4 required itemizations'?,",
    )


# 2.create
def test_hotel2(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Pacific Shores Resort','MerchantAddress':'987 Ocean Blvd, San Diego, CA, USA','TransactionDate':'2023-08-22','Subtotal':'640','Tax':'64','Tip':'0','Total':'704','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Client presentation at West Coast Marketing Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-08-20","ItemAmount":"300.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"30.00"}]},{"ItemName":"Room Service","TransactionDate":"2023-08-21","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"19.00"}]},{"ItemName":"Internet access","TransactionDate":"2023-08-21","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"15.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Pacific Shores Resort' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Pacific Shores Resort' have all 3 required itemizations'?,",
    )


# 3.create
def test_hotel3(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Windy City Executive Suites','MerchantAddress':'200 Michigan Ave, Chicago, IL, USA','TransactionDate':'2021-11-09','Subtotal':'510','Tax':'51','Tip':'20','Total':'581','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Attended Midwest Finance Leadership Forum','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-11-07","ItemAmount":"200.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"20.00"}]},{"ItemName":"Restaurant","TransactionDate":"2021-11-08","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"19.00"}]},{"ItemName":"Transportation","TransactionDate":"2021-11-08","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"12.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Windy City Executive Suites' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Windy City Executive Suites' have all 3 required itemizations'?,",
    )


# 4.create
def test_hotel4(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Capitol Plaza Hotel','MerchantAddress':'101 Independence Ave, Washington, DC, USA','TransactionDate':'2020-03-05','Subtotal':'480','Tax':'48','Tip':'0','Total':'528','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'DC','Description':'Policy workshop with federal clients','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-03-03","ItemAmount":"200.00","ItemTax":[{"ItemTaxDescription":"Occupancy Tax","ItemTaxAmount":"20.00"}]},{"ItemName":"Business center","TransactionDate":"2020-03-04","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"12.00"}]},{"ItemName":"Restaurant","TransactionDate":"2020-03-04","ItemAmount":"160.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"16.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Capitol Plaza Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Capitol Plaza Hotel' have all 3 required itemizations'?,",
    )


# 5.create
def test_hotel5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Rocky Mountain Lodge','MerchantAddress':'75 Alpine Way, Denver, CO, USA','TransactionDate':'2023-02-17','Subtotal':'395','Tax':'39.5','Tip':'15','Total':'449.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Winter business strategy offsite','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-02-15","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"15.00"}]},{"ItemName":"Minibar","TransactionDate":"2023-02-16","ItemAmount":"95.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"9.50"}]},{"ItemName":"Restaurant","TransactionDate":"2023-02-16","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"15.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Rocky Mountain Lodge' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Rocky Mountain Lodge' have all 3 required itemizations'?,",
    )


# 6.create
def test_hotel6(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Bayview Executive Hotel','MerchantAddress':'450 Marina Blvd, Miami, FL, USA','TransactionDate':'2022-12-08','Subtotal':'715','Tax':'71.5','Tip':'40','Total':'826.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Attended Southeast Real Estate Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-12-06","ItemAmount":"250.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"25.00"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-12-07","ItemAmount":"250.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"25.00"}]},{"ItemName":"Restaurant","TransactionDate":"2022-12-07","ItemAmount":"215.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"21.50"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Bayview Executive Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Bayview Executive Hotel' have all 3 required itemizations'?,",
    )


# 7.create
def test_hotel7(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Liberty Square Hotel','MerchantAddress':'35 Liberty St, Philadelphia, PA, USA','TransactionDate':'2021-05-19','Subtotal':'570','Tax':'57','Tip':'25','Total':'652','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'PA','Description':'Mid-Atlantic Sales Kickoff Meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-05-17","ItemAmount":"220.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"22.00"}]},{"ItemName":"Conference room","TransactionDate":"2021-05-18","ItemAmount":"200.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"20.00"}]},{"ItemName":"Restaurant","TransactionDate":"2021-05-18","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"15.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Liberty Square Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Liberty Square Hotel' have all 3 required itemizations'?,",
    )


# 8.create
def test_hotel8(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Silicon Valley Suites','MerchantAddress':'600 Innovation Dr, San Jose, CA, USA','TransactionDate':'2023-09-14','Subtotal':'920','Tax':'92','Tip':'60','Total':'1072','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Attended Global AI Developers Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-09-12","ItemAmount":"320.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"32.00"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-09-13","ItemAmount":"320.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"32.00"}]},{"ItemName":"Restaurant","TransactionDate":"2023-09-13","ItemAmount":"280.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"28.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Silicon Valley Suites' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Silicon Valley Suites' have all 3 required itemizations'?,",
    )


# 9.create
def test_hotel9(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Empire Business Hotel','MerchantAddress':'400 Madison Ave, New York, NY, USA','TransactionDate':'2020-12-03','Subtotal':'850','Tax':'85','Tip':'35','Total':'970','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Q4 Corporate Strategy Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-12-01","ItemAmount":"300.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"30.00"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-12-02","ItemAmount":"300.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"30.00"}]},{"ItemName":"Conference room","TransactionDate":"2020-12-02","ItemAmount":"250.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"25.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Empire Business Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Empire Business Hotel' have all 3 required itemizations'?,",
    )


# 10.create
def test_hotel10(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Desert Sands Hotel','MerchantAddress':'123 Palm Way, Phoenix, AZ, USA','TransactionDate':'2021-04-15','Subtotal':'430','Tax':'43','Tip':'10','Total':'483','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Spring regional operations meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-04-13","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.00"}]},{"ItemName":"Restaurant","TransactionDate":"2021-04-14","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"15.00"}]},{"ItemName":"Transportation","TransactionDate":"2021-04-14","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"10.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Desert Sands Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Desert Sands Hotel' have all 3 required itemizations'?,",
    )


# 11.create
def test_hotel11(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Hilton Garden Inn Boston','MerchantAddress':'5 Blossom Street, Boston, MA, USA','TransactionDate':'2022-07-15','Subtotal':'742','Tax':'66.78','Tip':'35','Total':'843.78','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MA','Description':'Business trip for Tech Innovators Conference 2022','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-07-12","ItemAmount":"245.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"22.05"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-07-13","ItemAmount":"245.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"22.05"}]},{"ItemName":"Restaurant","TransactionDate":"2022-07-14","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"9.60"}]},{"ItemName":"Internet access","TransactionDate":"2022-07-14","ItemAmount":"45.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"3.78"}]},{"ItemName":"Loungebar","TransactionDate":"2022-07-14","ItemAmount":"87.00","ItemTax":[{"ItemTaxDescription":"Beverage Tax","ItemTaxAmount":"7.30"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Hilton Garden Inn Boston' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Hilton Garden Inn Boston' have all 5 required itemizations'?,",
    )


# 12.create
def test_hotel12(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Marriott Marquis San Diego Marina','MerchantAddress':'333 W Harbor Dr, San Diego, CA, USA','TransactionDate':'2023-03-10','Subtotal':'525','Tax':'47.25','Tip':'20','Total':'592.25','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip for Spring Marketing Strategy Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-03-08","ItemAmount":"175.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"15.75"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-03-09","ItemAmount":"175.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"15.75"}]},{"ItemName":"Restaurant","TransactionDate":"2023-03-09","ItemAmount":"95.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"8.55"}]},{"ItemName":"Internet access","TransactionDate":"2023-03-09","ItemAmount":"80.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"7.20"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Marriott Marquis San Diego Marina' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Marriott Marquis San Diego Marina' have all 4 required itemizations'?,",
    )


# 13.create
def test_hotel13(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Hyatt Regency Chicago','MerchantAddress':'151 E Wacker Dr, Chicago, IL, USA','TransactionDate':'2021-11-18','Subtotal':'690','Tax':'62.1','Tip':'40','Total':'792.1','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Business trip for Midwest Financial Analysts Meetup','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-11-15","ItemAmount":"230.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"20.70"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-11-16","ItemAmount":"230.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"20.70"}]},{"ItemName":"Restaurant","TransactionDate":"2021-11-17","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"10.80"}]},{"ItemName":"Loungebar","TransactionDate":"2021-11-17","ItemAmount":"110.00","ItemTax":[{"ItemTaxDescription":"Beverage Tax","ItemTaxAmount":"9.90"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Hyatt Regency Chicago' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Hyatt Regency Chicago' have all 4 required itemizations'?,",
    )


# 14.create
def test_hotel14(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Omni Dallas Hotel','MerchantAddress':'555 S Lamar St, Dallas, TX, USA','TransactionDate':'2020-12-09','Subtotal':'410','Tax':'36.9','Tip':'15','Total':'461.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip for Winter Oil & Gas Networking Event','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-12-07","ItemAmount":"135.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"12.15"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-12-08","ItemAmount":"135.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"12.15"}]},{"ItemName":"Restaurant","TransactionDate":"2020-12-08","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"8.10"}]},{"ItemName":"Internet access","TransactionDate":"2020-12-08","ItemAmount":"50.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"4.50"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Omni Dallas Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Omni Dallas Hotel' have all 4 required itemizations'?,",
    )


# 15.create
def test_hotel15(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Westin Seattle','MerchantAddress':'1900 5th Ave, Seattle, WA, USA','TransactionDate':'2019-05-23','Subtotal':'615','Tax':'55.35','Tip':'25','Total':'695.35','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Business trip for Pacific Northwest Software Expo','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2019-05-21","ItemAmount":"205.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.45"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2019-05-22","ItemAmount":"205.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.45"}]},{"ItemName":"Restaurant","TransactionDate":"2019-05-22","ItemAmount":"115.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"10.35"}]},{"ItemName":"Movie","TransactionDate":"2019-05-22","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Entertainment Tax","ItemTaxAmount":"8.10"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Westin Seattle' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Westin Seattle' have all 4 required itemizations'?,",
    )


# 16.create
def test_hotel16(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Loews Miami Beach Hotel','MerchantAddress':'1601 Collins Ave, Miami Beach, FL, USA','TransactionDate':'2021-08-19','Subtotal':'880','Tax':'79.2','Tip':'50','Total':'1009.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip for International Hospitality Industry Forum','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-08-16","ItemAmount":"290.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"26.10"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-08-17","ItemAmount":"290.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"26.10"}]},{"ItemName":"Restaurant","TransactionDate":"2021-08-18","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"16.20"}]},{"ItemName":"Loungebar","TransactionDate":"2021-08-18","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Beverage Tax","ItemTaxAmount":"10.80"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Loews Miami Beach Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Loews Miami Beach Hotel' have all 4 required itemizations'?,",
    )


# 17.create
def test_hotel17(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Hotel Monteleone','MerchantAddress':'214 Royal St, New Orleans, LA, USA','TransactionDate':'2022-02-11','Subtotal':'560','Tax':'50.4','Tip':'20','Total':'630.4','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Business trip for Mardi Gras Event Planning Meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-02-09","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.10"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-02-10","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.10"}]},{"ItemName":"Restaurant","TransactionDate":"2022-02-10","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"8.10"}]},{"ItemName":"Gift shop","TransactionDate":"2022-02-10","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"8.10"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Hotel Monteleone' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Hotel Monteleone' have all 4 required itemizations'?,",
    )


# 18.create
def test_hotel18(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Roosevelt Hotel','MerchantAddress':'45 E 45th St, New York, NY, USA','TransactionDate':'2018-09-21','Subtotal':'780','Tax':'70.2','Tip':'35','Total':'885.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Business trip for Wall Street Investment Strategies Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2018-09-18","ItemAmount":"260.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"23.40"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2018-09-19","ItemAmount":"260.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"23.40"}]},{"ItemName":"Restaurant","TransactionDate":"2018-09-20","ItemAmount":"160.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"14.40"}]},{"ItemName":"Internet access","TransactionDate":"2018-09-20","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Roosevelt Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Roosevelt Hotel' have all 4 required itemizations'?,",
    )


# 19.create
def test_hotel19(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Sheraton Denver Downtown Hotel','MerchantAddress':'1550 Court Pl, Denver, CO, USA','TransactionDate':'2023-10-05','Subtotal':'640','Tax':'57.6','Tip':'28','Total':'725.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Business trip for Rocky Mountain Business Leadership Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-10-03","ItemAmount":"210.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.90"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-10-04","ItemAmount":"210.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.90"}]},{"ItemName":"Restaurant","TransactionDate":"2023-10-04","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"10.80"}]},{"ItemName":"Business center","TransactionDate":"2023-10-04","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Sheraton Denver Downtown Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Sheraton Denver Downtown Hotel' have all 4 required itemizations'?,",
    )


# 20.create
def test_hotel20(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Renaissance Nashville Hotel','MerchantAddress':'611 Commerce St, Nashville, TN, USA','TransactionDate':'2023-05-12','Subtotal':'595','Tax':'53.55','Tip':'25','Total':'673.55','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Business trip for Country Music Industry Networking Forum','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-05-10","ItemAmount":"200.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.00"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-05-11","ItemAmount":"200.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.00"}]},{"ItemName":"Restaurant","TransactionDate":"2023-05-11","ItemAmount":"95.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"8.55"}]},{"ItemName":"Gift shop","TransactionDate":"2023-05-11","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Renaissance Nashville Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Renaissance Nashville Hotel' have all 4 required itemizations'?,",
    )


# 21.create
def test_hotel21(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Fairmont San Francisco','MerchantAddress':'950 Mason St, San Francisco, CA, USA','TransactionDate':'2022-12-08','Subtotal':'670','Tax':'60.3','Tip':'35','Total':'765.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip for West Coast Real Estate Investors Symposium','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-12-06","ItemAmount":"220.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"19.80"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-12-07","ItemAmount":"220.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"19.80"}]},{"ItemName":"Loungebar","TransactionDate":"2022-12-07","ItemAmount":"130.00","ItemTax":[{"ItemTaxDescription":"Beverage Tax","ItemTaxAmount":"11.70"}]},{"ItemName":"Internet access","TransactionDate":"2022-12-07","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Fairmont San Francisco' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Fairmont San Francisco' have all 4 required itemizations'?,",
    )


# 22.create
def test_hotel22(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Waldorf Astoria Orlando','MerchantAddress':'14200 Bonnet Creek Resort Ln, Orlando, FL, USA','TransactionDate':'2021-07-15','Subtotal':'910','Tax':'81.9','Tip':'45','Total':'1036.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip for Hospitality and Tourism Executive Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-07-12","ItemAmount":"300.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.00"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-07-13","ItemAmount":"300.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.00"}]},{"ItemName":"Restaurant","TransactionDate":"2021-07-14","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Conference room","TransactionDate":"2021-07-14","ItemAmount":"160.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"14.40"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Waldorf Astoria Orlando' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Waldorf Astoria Orlando' have all 4 required itemizations'?,",
    )


# 23.create
def test_hotel23(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Ritz-Carlton, New Orleans','MerchantAddress':'921 Canal St, New Orleans, LA, USA','TransactionDate':'2020-02-28','Subtotal':'540','Tax':'48.6','Tip':'20','Total':'608.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Business trip for Mardi Gras Vendor Coordination Meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-02-26","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"16.20"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-02-27","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"16.20"}]},{"ItemName":"Gift certificates/Tangibles","TransactionDate":"2020-02-27","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"8.10"}]},{"ItemName":"Transportation","TransactionDate":"2020-02-27","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"8.10"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Ritz-Carlton, New Orleans' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Ritz-Carlton' have all 4 required itemizations'?,",
    )


# 24.create
def test_hotel24(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Peabody Memphis','MerchantAddress':'149 Union Ave, Memphis, TN, USA','TransactionDate':'2019-09-18','Subtotal':'475','Tax':'42.75','Tip':'18','Total':'535.75','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Business trip for Southern Retail Leadership Meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2019-09-16","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2019-09-17","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Laundry","TransactionDate":"2019-09-17","ItemAmount":"85.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"7.65"}]},{"ItemName":"Minibar","TransactionDate":"2019-09-17","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"8.10"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Peabody Memphis' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Peabody Memphis' have all 4 required itemizations'?,",
    )


# 25.create
def test_hotel25(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Kimpton Hotel Monaco Portland','MerchantAddress':'506 SW Washington St, Portland, OR, USA','TransactionDate':'2023-04-06','Subtotal':'540','Tax':'48.6','Tip':'22','Total':'610.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OR','Description':'Business trip for Northwest Green Energy Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-04-04","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"16.20"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-04-05","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"16.20"}]},{"ItemName":"Business entertainment","TransactionDate":"2023-04-05","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"8.10"}]},{"ItemName":"Health club","TransactionDate":"2023-04-05","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"8.10"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Kimpton Hotel Monaco Portland' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Kimpton Hotel Monaco Portland' have all 4 required itemizations'?,",
    )


# 26.create
def test_hotel26(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Hotel Valencia Riverwalk','MerchantAddress':'150 E Houston St, San Antonio, TX, USA','TransactionDate':'2022-01-25','Subtotal':'450','Tax':'40.5','Tip':'15','Total':'505.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip for Southwest Tech Vendor Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-01-23","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-01-24","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Other","TransactionDate":"2022-01-24","ItemAmount":"75.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"6.75"}]},{"ItemName":"Valet","TransactionDate":"2022-01-24","ItemAmount":"75.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"6.75"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Hotel Valencia Riverwalk' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Hotel Valencia Riverwalk' have all 4 required itemizations'?,",
    )


# 27.create
def test_hotel27(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Broadmoor','MerchantAddress':'1 Lake Ave, Colorado Springs, CO, USA','TransactionDate':'2020-06-19','Subtotal':'780','Tax':'70.2','Tip':'40','Total':'890.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Business trip for National Outdoor Recreation Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-06-16","ItemAmount":"260.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"23.40"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-06-17","ItemAmount":"260.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"23.40"}]},{"ItemName":"Banquet","TransactionDate":"2020-06-18","ItemAmount":"140.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"12.60"}]},{"ItemName":"Transportation","TransactionDate":"2020-06-18","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"10.80"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Broadmoor' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Broadmoor' have all 4 required itemizations'?,",
    )


# 28.create
def test_hotel28(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Langham, Chicago','MerchantAddress':'330 N Wabash Ave, Chicago, IL, USA','TransactionDate':'2021-03-17','Subtotal':'670','Tax':'60.3','Tip':'30','Total':'760.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Business trip for Midwest Legal Professionals Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-03-15","ItemAmount":"220.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"19.80"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-03-16","ItemAmount":"220.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"19.80"}]},{"ItemName":"Business center","TransactionDate":"2021-03-16","ItemAmount":"115.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"10.35"}]},{"ItemName":"Minibar","TransactionDate":"2021-03-16","ItemAmount":"115.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"10.35"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Langham, Chicago' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Langham' have all 4 required itemizations'?,",
    )


# 29.create
def test_hotel29(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Grand Hyatt New York','MerchantAddress':'109 E 42nd St, New York, NY, USA','TransactionDate':'2023-12-14','Subtotal':'845','Tax':'76.05','Tip':'40','Total':'961.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Business trip for Winter Financial Regulation Forum','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-12-11","ItemAmount":"280.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"25.20"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-12-12","ItemAmount":"280.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"25.20"}]},{"ItemName":"Conference room","TransactionDate":"2023-12-13","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Restaurant","TransactionDate":"2023-12-13","ItemAmount":"135.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"12.15"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Grand Hyatt New York' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Grand Hyatt New York' have all 4 required itemizations'?,",
    )


# 30.create
def test_hotel30(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Drake Hotel','MerchantAddress':'140 E Walton Pl, Chicago, IL, USA','TransactionDate':'2022-10-22','Subtotal':'650','Tax':'58.5','Tip':'30','Total':'738.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Business trip for Midwest Manufacturing Expo','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-10-20","ItemAmount":"215.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"19.35"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-10-21","ItemAmount":"215.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"19.35"}]},{"ItemName":"Banquet","TransactionDate":"2022-10-21","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"10.80"}]},{"ItemName":"Internet access","TransactionDate":"2022-10-21","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Drake Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Drake Hotel' have all 4 required itemizations'?,",
    )


# 31.create
def test_hotel31(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Four Seasons Hotel Houston','MerchantAddress':'1300 Lamar St, Houston, TX, USA','TransactionDate':'2021-04-09','Subtotal':'585','Tax':'52.65','Tip':'25','Total':'662.65','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip for Spring Energy Sector Strategy Meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-04-07","ItemAmount":"195.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.55"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-04-08","ItemAmount":"195.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.55"}]},{"ItemName":"Room Service","TransactionDate":"2021-04-08","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"9.00"}]},{"ItemName":"Laundry","TransactionDate":"2021-04-08","ItemAmount":"95.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"8.55"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Four Seasons Hotel Houston' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Four Seasons Hotel Houston' have all 4 required itemizations'?,",
    )


# 32.create
def test_hotel32(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Venetian Resort Las Vegas','MerchantAddress':'3355 S Las Vegas Blvd, Las Vegas, NV, USA','TransactionDate':'2020-08-18','Subtotal':'910','Tax':'81.9','Tip':'50','Total':'1041.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NV','Description':'Business trip for Summer Gaming Industry Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-08-15","ItemAmount":"300.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.00"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-08-16","ItemAmount":"300.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.00"}]},{"ItemName":"Business entertainment","TransactionDate":"2020-08-17","ItemAmount":"160.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"14.40"}]},{"ItemName":"Restaurant","TransactionDate":"2020-08-17","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"13.50"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Venetian Resort Las Vegas' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Venetian Resort Las Vegas' have all 4 required itemizations'?,",
    )


# 33.create
def test_hotel33(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Breakers Palm Beach','MerchantAddress':'1 S County Rd, Palm Beach, FL, USA','TransactionDate':'2023-02-11','Subtotal':'780','Tax':'70.2','Tip':'35','Total':'885.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip for Winter Luxury Retail Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-02-09","ItemAmount":"260.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"23.40"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-02-10","ItemAmount":"260.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"23.40"}]},{"ItemName":"Gift shop","TransactionDate":"2023-02-10","ItemAmount":"140.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"12.60"}]},{"ItemName":"Transportation","TransactionDate":"2023-02-10","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"10.80"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Breakers Palm Beach' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Breakers Palm Beach' have all 4 required itemizations'?,",
    )


# 34.create
def test_hotel34(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Mandarin Oriental Washington DC','MerchantAddress':'1330 Maryland Ave SW, Washington, DC, USA','TransactionDate':'2021-05-20','Subtotal':'640','Tax':'57.6','Tip':'28','Total':'725.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'DC','Description':'Business trip for National Policy Advisory Board Meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-05-18","ItemAmount":"210.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.90"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-05-19","ItemAmount":"210.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.90"}]},{"ItemName":"Business center","TransactionDate":"2021-05-19","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"10.80"}]},{"ItemName":"Minibar","TransactionDate":"2021-05-19","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Mandarin Oriental Washington DC' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Mandarin Oriental Washington DC' have all 4 required itemizations'?,",
    )


# 35.create
def test_hotel35(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Plaza Hotel','MerchantAddress':'768 5th Ave, New York, NY, USA','TransactionDate':'2019-11-09','Subtotal':'890','Tax':'80.1','Tip':'45','Total':'1015.1','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Business trip for International Finance Leaders Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2019-11-06","ItemAmount":"295.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"26.55"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2019-11-07","ItemAmount":"295.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"26.55"}]},{"ItemName":"Banquet","TransactionDate":"2019-11-08","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Other","TransactionDate":"2019-11-08","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"13.50"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Plaza Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Plaza Hotel' have all 4 required itemizations'?,",
    )


# 36.create
def test_hotel36(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Greenbrier','MerchantAddress':'101 Main St W, White Sulphur Springs, WV, USA','TransactionDate':'2020-07-24','Subtotal':'720','Tax':'64.8','Tip':'32','Total':'816.8','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WV','Description':'Business trip for Appalachian Regional Business Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-07-22","ItemAmount":"240.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"21.60"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-07-23","ItemAmount":"240.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"21.60"}]},{"ItemName":"Restaurant","TransactionDate":"2020-07-23","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"10.80"}]},{"ItemName":"Gift shop","TransactionDate":"2020-07-23","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"10.80"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Greenbrier' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Greenbrier' have all 4 required itemizations'?,",
    )


# 37.create
def test_hotel37(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Waldorf Astoria Beverly Hills','MerchantAddress':'9850 Wilshire Blvd, Beverly Hills, CA, USA','TransactionDate':'2022-08-19','Subtotal':'920','Tax':'82.8','Tip':'50','Total':'1052.8','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip for West Coast Luxury Brand Executive Forum','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-08-16","ItemAmount":"310.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.90"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-08-17","ItemAmount":"310.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.90"}]},{"ItemName":"Restaurant","TransactionDate":"2022-08-18","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Loungebar","TransactionDate":"2022-08-18","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Beverage Tax","ItemTaxAmount":"13.50"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Waldorf Astoria Beverly Hills' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Waldorf Astoria Beverly Hills' have all 4 required itemizations'?,",
    )


# 38.create
def test_hotel38(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'InterContinental Miami','MerchantAddress':'100 Chopin Plaza, Miami, FL, USA','TransactionDate':'2023-07-18','Subtotal':'890','Tax':'80.1','Tip':'45','Total':'1015.1','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip for Summer Hospitality Leaders Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-07-15","ItemAmount":"295.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"26.55"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-07-16","ItemAmount":"295.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"26.55"}]},{"ItemName":"Restaurant","TransactionDate":"2023-07-17","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Loungebar","TransactionDate":"2023-07-17","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"Beverage Tax","ItemTaxAmount":"13.50"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'InterContinental Miami' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'InterContinental Miami' have all 4 required itemizations'?,",
    )


# 39.create
def test_hotel39(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Brown Palace Hotel and Spa','MerchantAddress':'321 17th St, Denver, CO, USA','TransactionDate':'2021-05-14','Subtotal':'640','Tax':'57.6','Tip':'28','Total':'725.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Business trip for Rocky Mountain Renewable Energy Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-05-12","ItemAmount":"210.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.90"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-05-13","ItemAmount":"210.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.90"}]},{"ItemName":"Conference room","TransactionDate":"2021-05-13","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"10.80"}]},{"ItemName":"Restaurant","TransactionDate":"2021-05-13","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Brown Palace Hotel and Spa' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Brown Palace Hotel and Spa' have all 4 required itemizations'?,",
    )


# 40.create
def test_hotel40(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Jefferson Hotel','MerchantAddress':'101 W Franklin St, Richmond, VA, USA','TransactionDate':'2020-11-06','Subtotal':'540','Tax':'48.6','Tip':'22','Total':'610.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'VA','Description':'Business trip for East Coast Legal Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-11-04","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"16.20"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-11-05","ItemAmount":"180.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"16.20"}]},{"ItemName":"Business center","TransactionDate":"2020-11-05","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"8.10"}]},{"ItemName":"Gift shop","TransactionDate":"2020-11-05","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"8.10"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Jefferson Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Jefferson Hotel' have all 4 required itemizations'?,",
    )


# 41.create
def test_hotel41(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Roosevelt New Orleans','MerchantAddress':'130 Roosevelt Way, New Orleans, LA, USA','TransactionDate':'2019-02-15','Subtotal':'560','Tax':'50.4','Tip':'20','Total':'630.4','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Business trip for Mardi Gras Event Planning Meeting','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2019-02-13","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.10"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2019-02-14","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.10"}]},{"ItemName":"Transportation","TransactionDate":"2019-02-14","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"8.10"}]},{"ItemName":"Other","TransactionDate":"2019-02-14","ItemAmount":"90.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"8.10"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Roosevelt New Orleans' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Roosevelt New Orleans' have all 4 required itemizations'?,",
    )


# 42.create
def test_hotel42(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Sagamore Resort','MerchantAddress':'110 Sagamore Rd, Bolton Landing, NY, USA','TransactionDate':'2022-08-23','Subtotal':'720','Tax':'64.8','Tip':'32','Total':'816.8','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Business trip for Northeast Outdoor Recreation Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-08-21","ItemAmount":"240.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"21.60"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-08-22","ItemAmount":"240.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"21.60"}]},{"ItemName":"Banquet","TransactionDate":"2022-08-22","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"10.80"}]},{"ItemName":"Room Service","TransactionDate":"2022-08-22","ItemAmount":"120.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"10.80"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Sagamore Resort' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Sagamore Resort' have all 4 required itemizations'?,",
    )


# 43.create
def test_hotel43(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Clift Royal Sonesta Hotel','MerchantAddress':'495 Geary St, San Francisco, CA, USA','TransactionDate':'2020-03-11','Subtotal':'610','Tax':'54.9','Tip':'26','Total':'690.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip for West Coast Startup Pitch Event','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2020-03-09","ItemAmount":"205.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.45"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2020-03-10","ItemAmount":"205.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.45"}]},{"ItemName":"Business entertainment","TransactionDate":"2020-03-10","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"9.00"}]},{"ItemName":"Gift certificates/Tangibles","TransactionDate":"2020-03-10","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Clift Royal Sonesta Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Clift Royal Sonesta Hotel' have all 4 required itemizations'?,",
    )


# 44.create
def test_hotel44(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Biltmore Los Angeles','MerchantAddress':'506 S Grand Ave, Los Angeles, CA, USA','TransactionDate':'2021-09-30','Subtotal':'760','Tax':'68.4','Tip':'38','Total':'866.4','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip for West Coast Real Estate Expo','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-09-28","ItemAmount":"250.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"22.50"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-09-29","ItemAmount":"250.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"22.50"}]},{"ItemName":"Restaurant","TransactionDate":"2021-09-29","ItemAmount":"130.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"11.70"}]},{"ItemName":"Internet access","TransactionDate":"2021-09-29","ItemAmount":"130.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"11.70"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Biltmore Los Angeles' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Biltmore Los Angeles' have all 4 required itemizations'?,",
    )


# 45.create
def test_hotel45(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Royal Hawaiian','MerchantAddress':'2259 Kalakaua Ave, Honolulu, HI, USA','TransactionDate':'2018-06-12','Subtotal':'940','Tax':'84.6','Tip':'50','Total':'1074.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'HI','Description':'Business trip for Pacific Tourism Industry Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2018-06-09","ItemAmount":"310.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.90"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2018-06-10","ItemAmount":"310.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"27.90"}]},{"ItemName":"Banquet","TransactionDate":"2018-06-11","ItemAmount":"160.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"14.40"}]},{"ItemName":"Transportation","TransactionDate":"2018-06-11","ItemAmount":"160.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"14.40"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Royal Hawaiian' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Royal Hawaiian' have all 4 required itemizations'?,",
    )


# 46.create
def test_hotel46(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Omni Parker House','MerchantAddress':'60 School St, Boston, MA, USA','TransactionDate':'2022-04-22','Subtotal':'620','Tax':'55.8','Tip':'27','Total':'702.8','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MA','Description':'Business trip for New England Tech Innovators Meetup','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2022-04-20","ItemAmount":"205.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.45"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2022-04-21","ItemAmount":"205.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"18.45"}]},{"ItemName":"Restaurant","TransactionDate":"2022-04-21","ItemAmount":"110.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"9.90"}]},{"ItemName":"Internet access","TransactionDate":"2022-04-21","ItemAmount":"100.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"9.00"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Omni Parker House' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Omni Parker House' have all 4 required itemizations'?,",
    )


# 47.create
def test_hotel47(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Fontaine','MerchantAddress':'901 W 48th Pl, Kansas City, MO, USA','TransactionDate':'2023-09-15','Subtotal':'570','Tax':'51.3','Tip':'25','Total':'646.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MO','Description':'Business trip for Midwest Logistics & Supply Chain Conference','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2023-09-13","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.10"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2023-09-14","ItemAmount":"190.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"17.10"}]},{"ItemName":"Banquet","TransactionDate":"2023-09-14","ItemAmount":"95.00","ItemTax":[{"ItemTaxDescription":"Meal Tax","ItemTaxAmount":"8.55"}]},{"ItemName":"Transportation","TransactionDate":"2023-09-14","ItemAmount":"95.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"8.55"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Fontaine' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Fontaine' have all 4 required itemizations'?,",
    )


# 48.create
def test_hotel48(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'The Pfister Hotel','MerchantAddress':'424 E Wisconsin Ave, Milwaukee, WI, USA','TransactionDate':'2021-02-20','Subtotal':'460','Tax':'41.4','Tip':'18','Total':'519.4','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WI','Description':'Business trip for Winter Midwest Small Business Summit','PurchasedItems':'[{"ItemName":"Daily Room Rate","TransactionDate":"2021-02-18","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Daily Room Rate","TransactionDate":"2021-02-19","ItemAmount":"150.00","ItemTax":[{"ItemTaxDescription":"State Tax","ItemTaxAmount":"13.50"}]},{"ItemName":"Gift shop","TransactionDate":"2021-02-19","ItemAmount":"80.00","ItemTax":[{"ItemTaxDescription":"Sales Tax","ItemTaxAmount":"7.20"}]},{"ItemName":"Internet access","TransactionDate":"2021-02-19","ItemAmount":"80.00","ItemTax":[{"ItemTaxDescription":"Service Tax","ItemTaxAmount":"7.20"}]}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Pfister Hotel' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'The Pfister Hotel' have all 4 required itemizations'?,",
    )


# car rental category
# 49.create
def test_car_rental1(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF',"MerchantName":"Budget Rent a Car","MerchantAddress":"100 Collins St, Melbourne VIC 3000","TransactionDate":"2024-11-03T22:04:56","Subtotal":"454.17","Tax":"25.56","Tip":"17.45","Total":"497.18","CurrencyCode":"AUD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Australia","Location":"Melbourne","CountryCode":"AU","StateCode":"VIC","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Budget Rent a Car' created successfully in company 'USMF'?",
    )


# 50.create
def test_car_rental2(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Europcar","MerchantAddress":"12 Rue de Lyon, Paris 75012","TransactionDate":"2025-01-02T22:04:56","Subtotal":"454.46","Tax":"62.56","Tip":"32.80","Total":"549.82","CurrencyCode":"EUR","ExpenseCategory":"Car Rental","receiptLanguage":"fr","Country":"France","Location":"Paris","CountryCode":"FR","StateCode":"IDF","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Europcar' created successfully in company 'USSI'?",
    )


# 51.create
def test_car_rental3(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Hertz Rent A Car","MerchantAddress":"456 Sunset Blvd, Los Angeles, CA 90028","TransactionDate":"2025-06-20T22:04:56","Subtotal":"484.80","Tax":"50.80","Tip":"27.44","Total":"563.04","CurrencyCode":"USD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"United States","Location":"Los Angeles","CountryCode":"US","StateCode":"CA","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Hertz Rent A Car' created successfully in company 'USMF'?",
    )


# 52.create
def test_car_rental4(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Thrifty Car Rental","MerchantAddress":"200 Queen St, Auckland 1010","TransactionDate":"2024-11-01T22:04:56","Subtotal":"367.31","Tax":"22.79","Tip":"8.81","Total":"398.91","CurrencyCode":"NZD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"New Zealand","Location":"Auckland","CountryCode":"NZ","StateCode":"AUK","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Thrifty Car Rental' created successfully in company 'USSI'?",
    )


# 53.create
def test_car_rental5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Avis Car Rental","MerchantAddress":"789 Bay Street, Toronto, ON M5G 2C8","TransactionDate":"2025-08-05T22:04:56","Subtotal":"395.74","Tax":"48.05","Tip":"38.61","Total":"482.40","CurrencyCode":"CAD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Canada","Location":"Toronto","CountryCode":"CA","StateCode":"ON","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Avis Car Rental' created successfully in company 'USMF'?",
    )


# 54.create
def test_car_rental6(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Alamo Rent A Car","MerchantAddress":"1 Changi Airport, Singapore 819642","TransactionDate":"2025-04-20T22:04:56","Subtotal":"199.10","Tax":"11.91","Tip":"11.89","Total":"222.90","CurrencyCode":"SGD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Singapore","Location":"Singapore","CountryCode":"SG","StateCode":"SG","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Alamo Rent A Car' created successfully in company 'USSI'?",
    )


# 55.create
def test_car_rental7(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Keddy by Europcar","MerchantAddress":"Via Roma 101, Rome 00184","TransactionDate":"2025-05-30T22:04:56","Subtotal":"324.50","Tax":"29.03","Tip":"29.27","Total":"382.80","CurrencyCode":"EUR","ExpenseCategory":"Car Rental","receiptLanguage":"it","Country":"Italy","Location":"Rome","CountryCode":"IT","StateCode":"LAZ","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Keddy by Europcar' created successfully in company 'USMF'?",
    )


# 56.create
def test_car_rental8(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Enterprise Rent-A-Car","MerchantAddress":"150 Oxford St, London W1D 1DJ","TransactionDate":"2024-10-27T22:04:56","Subtotal":"395.94","Tax":"44.43","Tip":"36.57","Total":"476.94","CurrencyCode":"GBP","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"United Kingdom","Location":"London","CountryCode":"GB","StateCode":"ENG","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Enterprise Rent-A-Car' created successfully in company 'USSI'?",
    )


# 57.create
def test_car_rental9(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Keddy by Europcar","MerchantAddress":"Via Roma 101, Rome 00184","TransactionDate":"2025-07-04T22:04:56","Subtotal":"134.56","Tax":"10.78","Tip":"12.50","Total":"157.84","CurrencyCode":"EUR","ExpenseCategory":"Car Rental","receiptLanguage":"it","Country":"Italy","Location":"Rome","CountryCode":"IT","StateCode":"LAZ","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Keddy by Europcar' created successfully in company 'USMF'?",
    )


# 58.create
def test_car_rental10(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Alamo Rent A Car","MerchantAddress":"1 Changi Airport, Singapore 819642","TransactionDate":"2025-09-22T22:04:56","Subtotal":"379.32","Tax":"22.99","Tip":"19.31","Total":"421.62","CurrencyCode":"SGD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Singapore","Location":"Singapore","CountryCode":"SG","StateCode":"SG","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Alamo Rent A Car' created successfully in company 'USSI'?",
    )


# 59.create
def test_car_rental11(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Avis Car Rental","MerchantAddress":"789 Bay Street, Toronto, ON M5G 2C8","TransactionDate":"2025-03-02T22:04:56","Subtotal":"288.47","Tax":"21.86","Tip":"21.69","Total":"332.02","CurrencyCode":"CAD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Canada","Location":"Toronto","CountryCode":"CA","StateCode":"ON","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Avis Car Rental' created successfully in company 'USMF'?",
    )


# 60.create
def test_car_rental12(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Thrifty Car Rental","MerchantAddress":"200 Queen St, Auckland 1010","TransactionDate":"2025-07-10T22:04:56","Subtotal":"276.02","Tax":"24.84","Tip":"21.30","Total":"322.16","CurrencyCode":"NZD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"New Zealand","Location":"Auckland","CountryCode":"NZ","StateCode":"AUK","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Thrifty Car Rental' created successfully in company 'USSI'?",
    )


# 61.create
def test_car_rental13(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Thrifty Car Rental","MerchantAddress":"200 Queen St, Auckland 1010","TransactionDate":"2025-07-04T22:04:56","Subtotal":"386.09","Tax":"40.09","Tip":"26.07","Total":"452.25","CurrencyCode":"NZD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"New Zealand","Location":"Auckland","CountryCode":"NZ","StateCode":"AUK","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Thrifty Car Rental' created successfully in company 'USMF'?",
    )


# 62.create
def test_car_rental14(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Sixt Rent a Car","MerchantAddress":"Alexanderplatz 3, Berlin 10178","TransactionDate":"2024-11-12T22:04:56","Subtotal":"103.54","Tax":"13.38","Tip":"6.15","Total":"123.07","CurrencyCode":"EUR","ExpenseCategory":"Car Rental","receiptLanguage":"de","Country":"Germany","Location":"Berlin","CountryCode":"DE","StateCode":"BE","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Sixt Rent a Car' created successfully in company 'USSI'?",
    )


# 63.create
def test_car_rental15(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Thrifty Car Rental","MerchantAddress":"200 Queen St, Auckland 1010","TransactionDate":"2025-04-18T22:04:56","Subtotal":"407.21","Tax":"43.13","Tip":"14.71","Total":"465.05","CurrencyCode":"NZD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"New Zealand","Location":"Auckland","CountryCode":"NZ","StateCode":"AUK","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Thrifty Car Rental' created successfully in company 'USMF'?",
    )


# 64.create
def test_car_rental16(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Avis Car Rental","MerchantAddress":"789 Bay Street, Toronto, ON M5G 2C8","TransactionDate":"2025-06-19T22:04:56","Subtotal":"489.55","Tax":"48.95","Tip":"42.64","Total":"581.14","CurrencyCode":"CAD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Canada","Location":"Toronto","CountryCode":"CA","StateCode":"ON","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Avis Car Rental' created successfully in company 'USSI'?",
    )


# 65.create
def test_car_rental17(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Avis Car Rental","MerchantAddress":"789 Bay Street, Toronto, ON M5G 2C8","TransactionDate":"2025-07-01T22:04:56","Subtotal":"234.04","Tax":"18.70","Tip":"12.53","Total":"265.27","CurrencyCode":"CAD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Canada","Location":"Toronto","CountryCode":"CA","StateCode":"ON","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Avis Car Rental' created successfully in company 'USMF'?",
    )


# 66.create
def test_car_rental18(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"National Car Rental","MerchantAddress":"500 Sutter St, San Francisco, CA 94102","TransactionDate":"2025-08-11T22:04:56","Subtotal":"123.11","Tax":"15.38","Tip":"12.20","Total":"150.69","CurrencyCode":"USD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"United States","Location":"San Francisco","CountryCode":"US","StateCode":"CA","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'National Car Rental' created successfully in company 'USSI'?",
    )


# 67.create
def test_car_rental19(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Sixt Rent a Car","MerchantAddress":"Alexanderplatz 3, Berlin 10178","TransactionDate":"2025-09-29T22:04:56","Subtotal":"271.78","Tax":"38.51","Tip":"20.24","Total":"330.53","CurrencyCode":"EUR","ExpenseCategory":"Car Rental","receiptLanguage":"de","Country":"Germany","Location":"Berlin","CountryCode":"DE","StateCode":"BE","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Sixt Rent a Car' created successfully in company 'USMF'?",
    )


# 68.create
def test_car_rental20(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Avis Car Rental","MerchantAddress":"789 Bay Street, Toronto, ON M5G 2C8","TransactionDate":"2025-06-30T22:04:56","Subtotal":"268.83","Tax":"29.22","Tip":"26.06","Total":"324.11","CurrencyCode":"CAD","ExpenseCategory":"Car Rental","receiptLanguage":"en","Country":"Canada","Location":"Toronto","CountryCode":"CA","StateCode":"ON","Description":"Rental car for business travel"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Avis Car Rental' created successfully in company 'USSI'?",
    )


# flight category
# 69.create
def test_flight1(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Air Canada","MerchantAddress":"7373 Boulevard de la Côte-Vertu, Montreal, QC","TransactionDate":"2025-03-14","Subtotal":"979.87","Tax":"127.38","Tip":"0.00","Total":"1107.25","CurrencyCode":"CAD","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"Canada","Location":"Montreal","CountryCode":"CA","StateCode":"QC","Description":"Flight receipt from Air Canada on 2025-03-14","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-03-14","ItemAmount":"783.90"},{"ItemName":"Total airline fee","TransactionDate":"2025-03-14","ItemAmount":"97.99"},{"ItemName":"Total airline Tax","TransactionDate":"2025-03-14","ItemAmount":"127.38"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Air Canada' created successfully in company 'USMF'?",
    )


# 70. create
def test_flight2(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Delta Airlines","MerchantAddress":"1030 Delta Blvd, Atlanta, GA","TransactionDate":"2025-03-05","Subtotal":"985.71","Tax":"128.14","Tip":"0.00","Total":"1113.85","CurrencyCode":"USD","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"United States","Location":"Atlanta","CountryCode":"US","StateCode":"GA","Description":"Flight receipt from Delta Airlines on 2025-03-05","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-03-05","ItemAmount":"788.57"},{"ItemName":"Total airline fee","TransactionDate":"2025-03-05","ItemAmount":"98.57"},{"ItemName":"Total airline Tax","TransactionDate":"2025-03-05","ItemAmount":"128.14"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Delta Airlines' created successfully in company 'USSI'?",
    )


# 71.create
def test_flight3(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"United Airlines","MerchantAddress":"233 S Wacker Dr, Chicago, IL","TransactionDate":"2024-11-16","Subtotal":"1159.60","Tax":"150.75","Tip":"0.00","Total":"1310.35","CurrencyCode":"EUR","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"Germany","Location":"Cologne","CountryCode":"DE","StateCode":"NW","Description":"Flight receipt from United Airlines on 2024-11-16","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2024-11-16","ItemAmount":"927.68"},{"ItemName":"Total airline fee","TransactionDate":"2024-11-16","ItemAmount":"115.96"},{"ItemName":"Total airline Tax","TransactionDate":"2024-11-16","ItemAmount":"150.75"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'United Airlines' created successfully in company 'USMF'?",
    )


# 72.create
def test_flight4(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"American Airlines","MerchantAddress":"1 Skyview Dr, Fort Worth, TX","TransactionDate":"2025-07-18","Subtotal":"931.51","Tax":"121.10","Tip":"0.00","Total":"1052.61","CurrencyCode":"EUR","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"United Kingdom","Location":"London","CountryCode":"GB","StateCode":"ENG","Description":"Flight receipt from American Airlines on 2025-07-18","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-07-18","ItemAmount":"745.21"},{"ItemName":"Total airline fee","TransactionDate":"2025-07-18","ItemAmount":"93.15"},{"ItemName":"Total airline Tax","TransactionDate":"2025-07-18","ItemAmount":"121.10"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'American Airlines' created successfully in company 'USSI'?",
    )


# 73.create
def test_flight5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Lufthansa","MerchantAddress":"Venloer Str. 151-153, Cologne, Germany","TransactionDate":"2025-05-27","Subtotal":"1059.42","Tax":"137.72","Tip":"0.00","Total":"1197.14","CurrencyCode":"EUR","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"United Arab Emirates","Location":"Dubai","CountryCode":"AE","StateCode":"DU","Description":"Flight receipt from Lufthansa on 2025-05-27","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-05-27","ItemAmount":"847.54"},{"ItemName":"Total airline fee","TransactionDate":"2025-05-27","ItemAmount":"105.94"},{"ItemName":"Total airline Tax","TransactionDate":"2025-05-27","ItemAmount":"137.72"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Lufthansa' created successfully in company 'USMF'?",
    )


# 74.create
def test_flight6(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"British Airways","MerchantAddress":"Waterside, Harmondsworth, UK","TransactionDate":"2025-10-05","Subtotal":"636.85","Tax":"82.79","Tip":"0.00","Total":"719.64","CurrencyCode":"EUR","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"Australia","Location":"Sydney","CountryCode":"AU","StateCode":"NSW","Description":"Flight receipt from British Airways on 2025-10-05","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-10-05","ItemAmount":"509.48"},{"ItemName":"Total airline fee","TransactionDate":"2025-10-05","ItemAmount":"63.69"},{"ItemName":"Total airline Tax","TransactionDate":"2025-10-05","ItemAmount":"82.79"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'British Airways' created successfully in company 'USSI'?",
    )


# 75.create
def test_flight7(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Emirates","MerchantAddress":"Emirates Group HQ, Dubai, UAE","TransactionDate":"2025-07-29","Subtotal":"936.31","Tax":"121.72","Tip":"0.00","Total":"1058.03","CurrencyCode":"EUR","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"France","Location":"Paris","CountryCode":"FR","StateCode":"IDF","Description":"Flight receipt from Emirates on 2025-07-29","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-07-29","ItemAmount":"749.05"},{"ItemName":"Total airline fee","TransactionDate":"2025-07-29","ItemAmount":"93.63"},{"ItemName":"Total airline Tax","TransactionDate":"2025-07-29","ItemAmount":"121.72"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Emirates' created successfully in company 'USMF'?",
    )


# 76.create
def test_flight8(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Qantas","MerchantAddress":"10 Bourke Rd, Mascot NSW, Australia","TransactionDate":"2025-03-02","Subtotal":"489.65","Tax":"63.65","Tip":"0.00","Total":"553.30","CurrencyCode":"EUR","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"Singapore","Location":"Singapore","CountryCode":"SG","StateCode":"SG","Description":"Flight receipt from Qantas on 2025-03-02","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-03-02","ItemAmount":"391.72"},{"ItemName":"Total airline fee","TransactionDate":"2025-03-02","ItemAmount":"48.97"},{"ItemName":"Total airline Tax","TransactionDate":"2025-03-02","ItemAmount":"63.65"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Qantas' created successfully in company 'USSI'?",
    )


# 77.create
def test_flight9(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Air France","MerchantAddress":"45 Rue de Paris, Roissy-en-France, France","TransactionDate":"2025-07-31","Subtotal":"1069.81","Tax":"139.08","Tip":"0.00","Total":"1208.89","CurrencyCode":"CAD","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"Canada","Location":"Montreal","CountryCode":"CA","StateCode":"QC","Description":"Flight receipt from Air France on 2025-07-31","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-07-31","ItemAmount":"855.85"},{"ItemName":"Total airline fee","TransactionDate":"2025-07-31","ItemAmount":"106.98"},{"ItemName":"Total airline Tax","TransactionDate":"2025-07-31","ItemAmount":"139.08"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Air France' created successfully in company 'USMF'?",
    )


# 78.create
def test_flight10(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Singapore Airlines","MerchantAddress":"Airline House, 25 Airline Rd, Singapore","TransactionDate":"2025-09-20","Subtotal":"468.90","Tax":"60.96","Tip":"0.00","Total":"529.86","CurrencyCode":"USD","ExpenseCategory":"Flight","receiptLanguage":"en-US","Country":"United States","Location":"Atlanta","CountryCode":"US","StateCode":"GA","Description":"Flight receipt from Singapore Airlines on 2025-09-20","Itemizations":[{"ItemName":"Total airline fare","TransactionDate":"2025-09-20","ItemAmount":"375.12"},{"ItemName":"Total airline fee","TransactionDate":"2025-09-20","ItemAmount":"46.89"},{"ItemName":"Total airline Tax","TransactionDate":"2025-09-20","ItemAmount":"60.96"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Singapore Airlines' created successfully in company 'USSI'?",
    )


# gift category
# 79.create
def test_gift1(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"The Giving Tree","MerchantAddress":"789 Pine Rd, Gotham","TransactionDate":"2025-09-23","Subtotal":"82.34","Tax":"8.23","Tip":"0.00","Total":"90.57","CurrencyCode":"CAD","ExpenseCategory":"Gift","receiptLanguage":"en-CA","Country":"Canada","Location":"Gotham","CountryCode":"CA","StateCode":"ON","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-09-23","ItemAmount":"20.01"},{"ItemName":"Tangible gift","TransactionDate":"2025-09-23","ItemAmount":"62.33"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Giving Tree' created successfully in company 'USMF'?",
    )


# 80.create
def test_gift2(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"The Giving Tree","MerchantAddress":"456 Oak Ave, Metropolis","TransactionDate":"2025-01-17","Subtotal":"340.57","Tax":"34.06","Tip":"0.00","Total":"374.63","CurrencyCode":"USD","ExpenseCategory":"Gift","receiptLanguage":"en-US","Country":"United States","Location":"Metropolis","CountryCode":"US","StateCode":"CA","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-01-17","ItemAmount":"149.70"},{"ItemName":"Tangible gift","TransactionDate":"2025-01-17","ItemAmount":"190.87"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Giving Tree' created successfully in company 'USSI'?",
    )


# 81.create
def test_gift3(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Wrapped Wonders","MerchantAddress":"654 Cedar Ln, Central City","TransactionDate":"2025-07-12","Subtotal":"170.89","Tax":"17.09","Tip":"0.00","Total":"187.98","CurrencyCode":"GBP","ExpenseCategory":"Gift","receiptLanguage":"en-GB","Country":"United Kingdom","Location":"Central City","CountryCode":"GB","StateCode":"","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-07-12","ItemAmount":"32.49"},{"ItemName":"Tangible gift","TransactionDate":"2025-07-12","ItemAmount":"138.40"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Wrapped Wonders' created successfully in company 'USMF'?",
    )


# 82.create
def test_gift4(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Wrapped Wonders","MerchantAddress":"321 Birch St, Star City","TransactionDate":"2025-02-28","Subtotal":"210.45","Tax":"21.05","Tip":"0.00","Total":"231.50","CurrencyCode":"USD","ExpenseCategory":"Gift","receiptLanguage":"en-US","Country":"United States","Location":"Star City","CountryCode":"US","StateCode":"WA","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-02-28","ItemAmount":"75.20"},{"ItemName":"Tangible gift","TransactionDate":"2025-02-28","ItemAmount":"135.25"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Wrapped Wonders' created successfully in company 'USSI'?",
    )


# 83.create
def test_gift5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"The Giving Tree","MerchantAddress":"789 Pine Rd, Gotham","TransactionDate":"2025-06-12","Subtotal":"327.34","Tax":"32.73","Tip":"0.00","Total":"360.07","CurrencyCode":"AUD","ExpenseCategory":"Gift","receiptLanguage":"en-AU","Country":"Australia","Location":"Gotham","CountryCode":"AU","StateCode":"NSW","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-06-12","ItemAmount":"189.92"},{"ItemName":"Tangible gift","TransactionDate":"2025-06-12","ItemAmount":"137.42"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Giving Tree' created successfully in company 'USMF'?",
    )


# 84.create
def test_gift6(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Present Perfect","MerchantAddress":"123 Elm St, Springfield","TransactionDate":"2025-03-19","Subtotal":"275.56","Tax":"27.56","Tip":"0.00","Total":"303.12","CurrencyCode":"AUD","ExpenseCategory":"Gift","receiptLanguage":"en-AU","Country":"Australia","Location":"Springfield","CountryCode":"AU","StateCode":"NSW","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-03-19","ItemAmount":"102.99"},{"ItemName":"Tangible gift","TransactionDate":"2025-03-19","ItemAmount":"172.57"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Present Perfect' created successfully in company 'USSI'?",
    )


# 85.create
def test_gift7(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Generous Goods","MerchantAddress":"321 Maple Blvd, Star City","TransactionDate":"2025-06-18","Subtotal":"203.82","Tax":"20.39","Tip":"0.00","Total":"224.21","CurrencyCode":"GBP","ExpenseCategory":"Gift","receiptLanguage":"en-GB","Country":"United Kingdom","Location":"Star City","CountryCode":"GB","StateCode":"","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-06-18","ItemAmount":"37.67"},{"ItemName":"Tangible gift","TransactionDate":"2025-06-18","ItemAmount":"166.15"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Generous Goods' created successfully in company 'USMF'?",
    )


# 86.create
def test_gift8(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"The Giving Tree","MerchantAddress":"321 Maple Blvd, Star City","TransactionDate":"2025-03-10","Subtotal":"82.65","Tax":"8.26","Tip":"0.00","Total":"90.91","CurrencyCode":"EUR","ExpenseCategory":"Gift","receiptLanguage":"de-DE","Country":"Germany","Location":"Star City","CountryCode":"DE","StateCode":"BE","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-03-10","ItemAmount":"41.83"},{"ItemName":"Tangible gift","TransactionDate":"2025-03-10","ItemAmount":"40.82"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Giving Tree' created successfully in company 'USSI'?",
    )


# 87.create
def test_gift9(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Present Perfect","MerchantAddress":"123 Elm St, Springfield","TransactionDate":"2025-08-22","Subtotal":"145.78","Tax":"14.58","Tip":"0.00","Total":"160.36","CurrencyCode":"CAD","ExpenseCategory":"Gift","receiptLanguage":"en-CA","Country":"Canada","Location":"Springfield","CountryCode":"CA","StateCode":"ON","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-08-22","ItemAmount":"58.31"},{"ItemName":"Tangible gift","TransactionDate":"2025-08-22","ItemAmount":"87.47"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Present Perfect' created successfully in company 'USMF'?",
    )


# 88.create
def test_gift10(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Generous Goods","MerchantAddress":"321 Maple Blvd, Star City","TransactionDate":"2025-07-27","Subtotal":"184.64","Tax":"18.46","Tip":"0.00","Total":"203.10","CurrencyCode":"EUR","ExpenseCategory":"Gift","receiptLanguage":"de-DE","Country":"Germany","Location":"Star City","CountryCode":"DE","StateCode":"BE","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-07-27","ItemAmount":"82.51"},{"ItemName":"Tangible gift","TransactionDate":"2025-07-27","ItemAmount":"102.13"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Generous Goods' created successfully in company 'USSI'?",
    )


# 89.create
def test_gift11(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Wrapped Wonders","MerchantAddress":"789 Pine Rd, Gotham","TransactionDate":"2025-01-21","Subtotal":"297.18","Tax":"29.72","Tip":"0.00","Total":"326.90","CurrencyCode":"GBP","ExpenseCategory":"Gift","receiptLanguage":"en-GB","Country":"United Kingdom","Location":"Gotham","CountryCode":"GB","StateCode":"","Description":"Gift purchase receipt","Itemizations":[{"ItemName":"Gift certificate","TransactionDate":"2025-01-21","ItemAmount":"188.12"},{"ItemName":"Tangible gift","TransactionDate":"2025-01-21","ItemAmount":"109.06"}]}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Wrapped Wonders' created successfully in company 'USMF'?",
    )


# 90.create
def test_gift12(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Le Petit Café","MerchantAddress":"12 Rue Cler, Paris 75007","TransactionDate":"2025-02-16T21:59:42","Subtotal":"131.85","Tax":"12.25","Tip":"13.74","Total":"157.84","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"fr","Country":"France","Location":"Paris","CountryCode":"FR","StateCode":"IDF","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Le Petit Café' created successfully in company 'USSI'?",
    )


# business meal category
# 91.create
def test_business_meal1(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Le Petit Café","MerchantAddress":"12 Rue Cler, Paris 75007","TransactionDate":"2025-08-11T18:30:00","Subtotal":"145.20","Tax":"13.50","Tip":"15.00","Total":"173.70","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"fr","Country":"France","Location":"Paris","CountryCode":"FR","StateCode":"IDF","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Le Petit Café' created successfully in company 'USMF'?",
    )


# 92.create
def test_business_meal2(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"La Piazza","MerchantAddress":"Via Roma 45, Rome 00184","TransactionDate":"2025-09-24T21:59:42","Subtotal":"105.91","Tax":"5.38","Tip":"12.05","Total":"123.34","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"it","Country":"Italy","Location":"Rome","CountryCode":"IT","StateCode":"RM","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'La Piazza' created successfully in company 'USSI'?",
    )


# 93.create
def test_business_meal3(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Olive Garden","MerchantAddress":"123 Main St, Orlando, FL 32801","TransactionDate":"2025-08-01T21:59:42","Subtotal":"53.35","Tax":"7.19","Tip":"9.26","Total":"69.80","CurrencyCode":"USD","ExpenseCategory":"Meal","receiptLanguage":"en","Country":"United States","Location":"Orlando","CountryCode":"US","StateCode":"FL","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Olive Garden' created successfully in company 'USMF'?",
    )


# 94.create
def test_business_meal4(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"The Maple Diner","MerchantAddress":"456 King St W, Toronto, ON M5V 1L7","TransactionDate":"2025-01-16T21:59:42","Subtotal":"128.66","Tax":"16.01","Tip":"19.40","Total":"164.07","CurrencyCode":"CAD","ExpenseCategory":"Meal","receiptLanguage":"en","Country":"Canada","Location":"Toronto","CountryCode":"CA","StateCode":"ON","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Maple Diner' created successfully in company 'USSI'?",
    )


# 95.create
def test_business_meal5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Sakura Sushi","MerchantAddress":"2-1-1 Nihonbashi, Tokyo 103-0027","TransactionDate":"2025-09-26T21:59:42","Subtotal":"79.69","Tax":"7.25","Tip":"11.27","Total":"98.21","CurrencyCode":"JPY","ExpenseCategory":"Meal","receiptLanguage":"ja","Country":"Japan","Location":"Tokyo","CountryCode":"JP","StateCode":"13","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Sakura Sushi' created successfully in company 'USMF'?",
    )


# 96.create
def test_business_meal6(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"El Gaucho","MerchantAddress":"Av. Santa Fe 1234, Buenos Aires C1059","TransactionDate":"2025-06-08T21:59:42","Subtotal":"62.52","Tax":"5.30","Tip":"7.98","Total":"75.80","CurrencyCode":"ARS","ExpenseCategory":"Meal","receiptLanguage":"es","Country":"Argentina","Location":"Buenos Aires","CountryCode":"AR","StateCode":"BA","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'El Gaucho' created successfully in company 'USSI'?",
    )


# 97.create
def test_business_meal7(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Sakura Sushi","MerchantAddress":"2-1-1 Nihonbashi, Tokyo 103-0027","TransactionDate":"2024-12-06T21:59:42","Subtotal":"41.98","Tax":"2.86","Tip":"7.17","Total":"52.01","CurrencyCode":"JPY","ExpenseCategory":"Meal","receiptLanguage":"ja","Country":"Japan","Location":"Tokyo","CountryCode":"JP","StateCode":"13","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Sakura Sushi' created successfully in company 'USMF'?",
    )


# 98.create
def test_business_meal8(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"The Fish Market","MerchantAddress":"Pier 39, San Francisco, CA 94133","TransactionDate":"2025-06-20T21:59:42","Subtotal":"111.77","Tax":"10.75","Tip":"16.22","Total":"138.74","CurrencyCode":"USD","ExpenseCategory":"Meal","receiptLanguage":"en","Country":"United States","Location":"San Francisco","CountryCode":"US","StateCode":"CA","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Fish Market' created successfully in company 'USSI'?",
    )


# 99.create
def test_business_meal9(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"The Fish Market","MerchantAddress":"Pier 39, San Francisco, CA 94133","TransactionDate":"2025-03-22T21:59:42","Subtotal":"113.51","Tax":"13.80","Tip":"14.19","Total":"141.50","CurrencyCode":"USD","ExpenseCategory":"Meal","receiptLanguage":"en","Country":"United States","Location":"San Francisco","CountryCode":"US","StateCode":"CA","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Fish Market' created successfully in company 'USMF'?",
    )


# 100.create
def test_business_meal10(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"La Piazza","MerchantAddress":"Via Roma 45, Rome 00184","TransactionDate":"2025-06-30T21:59:42","Subtotal":"114.04","Tax":"15.78","Tip":"13.21","Total":"143.03","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"it","Country":"Italy","Location":"Rome","CountryCode":"IT","StateCode":"RM","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'La Piazza' created successfully in company 'USSI'?",
    )


# 101.create
def test_business_meal11(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"The Fish Market","MerchantAddress":"Pier 39, San Francisco, CA 94133","TransactionDate":"2025-07-06T21:59:42","Subtotal":"67.14","Tax":"6.45","Tip":"7.96","Total":"81.55","CurrencyCode":"USD","ExpenseCategory":"Meal","receiptLanguage":"en","Country":"United States","Location":"San Francisco","CountryCode":"US","StateCode":"CA","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Fish Market' created successfully in company 'USMF'?",
    )


# 102.create
def test_business_meal12(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"The Maple Diner","MerchantAddress":"456 King St W, Toronto, ON M5V 1L7","TransactionDate":"2025-07-12T21:59:42","Subtotal":"63.45","Tax":"4.05","Tip":"9.02","Total":"76.52","CurrencyCode":"CAD","ExpenseCategory":"Meal","receiptLanguage":"en","Country":"Canada","Location":"Toronto","CountryCode":"CA","StateCode":"ON","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'The Maple Diner' created successfully in company 'USSI'?",
    )


# 103.create
def test_business_meal13(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Sakura Sushi","MerchantAddress":"2-1-1 Nihonbashi, Tokyo 103-0027","TransactionDate":"2025-06-04T21:59:42","Subtotal":"125.24","Tax":"8.71","Tip":"20.75","Total":"154.70","CurrencyCode":"JPY","ExpenseCategory":"Meal","receiptLanguage":"ja","Country":"Japan","Location":"Tokyo","CountryCode":"JP","StateCode":"13","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Sakura Sushi' created successfully in company 'USMF'?",
    )


# 104.create
def test_business_meal14(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Zum Alten Fritz","MerchantAddress":"Friedrichstraße 123, Berlin 10117","TransactionDate":"2025-03-26T21:59:42","Subtotal":"93.97","Tax":"7.40","Tip":"13.93","Total":"115.30","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"de","Country":"Germany","Location":"Berlin","CountryCode":"DE","StateCode":"BE","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Zum Alten Fritz' created successfully in company 'USSI'?",
    )


# 105.create
def test_business_meal15(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Zum Alten Fritz","MerchantAddress":"Friedrichstraße 123, Berlin 10117","TransactionDate":"2025-04-21T21:59:42","Subtotal":"102.62","Tax":"12.76","Tip":"11.13","Total":"126.51","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"de","Country":"Germany","Location":"Berlin","CountryCode":"DE","StateCode":"BE","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Zum Alten Fritz' created successfully in company 'USMF'?",
    )


# 106.create
def test_business_meal16(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Zum Alten Fritz","MerchantAddress":"Friedrichstraße 123, Berlin 10117","TransactionDate":"2025-04-20T21:59:42","Subtotal":"110.97","Tax":"15.63","Tip":"15.54","Total":"142.14","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"de","Country":"Germany","Location":"Berlin","CountryCode":"DE","StateCode":"BE","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Zum Alten Fritz' created successfully in company 'USSI'?",
    )


# 107.create
def test_business_meal17(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Le Petit Café","MerchantAddress":"12 Rue Cler, Paris 75007","TransactionDate":"2025-05-14T21:59:42","Subtotal":"86.07","Tax":"5.38","Tip":"13.33","Total":"104.78","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"fr","Country":"France","Location":"Paris","CountryCode":"FR","StateCode":"IDF","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Le Petit Café' created successfully in company 'USMF'?",
    )


# 108.create
def test_business_meal18(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"El Asador","MerchantAddress":"Calle de Alcalá 45, Madrid 28014","TransactionDate":"2025-04-05T21:59:42","Subtotal":"140.72","Tax":"18.86","Tip":"23.45","Total":"183.03","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"es","Country":"Spain","Location":"Madrid","CountryCode":"ES","StateCode":"MD","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'El Asador' created successfully in company 'USSI'?",
    )


# 109.create
def test_business_meal19(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USMF company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USMF', "MerchantName":"Sakura Sushi","MerchantAddress":"2-1-1 Nihonbashi, Tokyo 103-0027","TransactionDate":"2025-08-01T21:59:42","Subtotal":"145.87","Tax":"21.44","Tip":"16.33","Total":"183.64","CurrencyCode":"JPY","ExpenseCategory":"Meal","receiptLanguage":"ja","Country":"Japan","Location":"Tokyo","CountryCode":"JP","StateCode":"13","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Sakura Sushi' created successfully in company 'USMF'?",
    )


# 110.create
def test_business_meal20(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations.

        # Data
        {'Company':'USSI', "MerchantName":"Zum Alten Fritz","MerchantAddress":"Friedrichstraße 123, Berlin 10117","TransactionDate":"2025-01-21T21:59:42","Subtotal":"111.14","Tax":"9.03","Tip":"12.00","Total":"132.17","CurrencyCode":"EUR","ExpenseCategory":"Meal","receiptLanguage":"de","Country":"Germany","Location":"Berlin","CountryCode":"DE","StateCode":"BE","Description":"Business meal"}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Zum Alten Fritz' created successfully in company 'USSI'?",
    )

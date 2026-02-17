from thinkingbox.common import Judge, TestContext
from thinkingbox.tools.judgeagent import JudgeAgent

"""!
scenario: fno
"""


def test_expense_hotel_1(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

        # Data
        {'Company':'USSI','MerchantName':'Hilton Coral Springs Airport','MerchantAddress':'170 Davis St, Coral Springs, FL 20593, USA','TransactionDate':'2022-10-16',,'Total':'814.81','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Sunnyvale for Project Management Summit. 4 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-12","Item Amount":"150.32"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-12","Item Tax Amount":"9.55"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-12","Item Tax Amount":"6.37"},{"Item Name":"Hotel Telephone","Transaction Date":"2022-10-12","Item Amount":"11.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-12","Item Amount":"28.72"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-13","Item Amount":"154.01"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-13","Item Tax Amount":"9.79"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-13","Item Tax Amount":"6.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-13","Item Amount":"31.31"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-14","Item Amount":"150.95"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-14","Item Tax Amount":"9.59"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-14","Item Tax Amount":"6.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-14","Item Amount":"31.64"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-15","Item Amount":"158.89"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-15","Item Tax Amount":"10.10"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-15","Item Tax Amount":"6.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-15","Item Amount":"31.96"}]'}
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the expense line with MerchantName 'Hilton Coral Springs Airport' created successfully in company 'USSI'?",
    )
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Does the expense line with MerchantName 'Hilton Coral Springs Airport' have all 17 required itemizations'?,",
    )


# def test_expense_hotel_2(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Winston-Salem Downtown','MerchantAddress':'648 Rogers St, Winston-Salem, NC 50970, USA','TransactionDate':'2019-11-14',,'Total':'1052.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Santa Ana for partnership development. Attended Legal Technology Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-11","Item Amount":"233.23"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-11","Item Tax Amount":"17.67"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-11","Item Tax Amount":"5.89"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-11","Item Tax Amount":"5.89"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-11-11","Item Amount":"87.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-11","Item Amount":"42.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-12","Item Amount":"241.19"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-12","Item Tax Amount":"18.28"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-12","Item Tax Amount":"6.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-12","Item Amount":"40.55"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-13","Item Amount":"234.37"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-13","Item Tax Amount":"17.76"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-13","Item Tax Amount":"5.92"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-13","Item Tax Amount":"5.92"},{"Item Name":"Incidentals","Transaction Date":"2019-11-13","Item Amount":"33.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-13","Item Amount":"56.64"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Winston-Salem Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Winston-Salem Downtown' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_3(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Louisville Airport','MerchantAddress':'606 Campbell St, Louisville, KY 20262, USA','TransactionDate':'2023-07-24',,'Total':'1627.38','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Corporate trip - Mobile Technology Conference conference in Jersey City. product demos and customer meetings over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-20","Item Amount":"293.69"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-20","Item Tax Amount":"23.75"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-20","Item Tax Amount":"7.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-20","Item Amount":"30.04"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-21","Item Amount":"296.06"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-21","Item Tax Amount":"23.94"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-21","Item Tax Amount":"7.98"},{"Item Name":"Gift and Entertainment","Transaction Date":"2023-07-21","Item Amount":"112.01"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-21","Item Amount":"47.70"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-22","Item Amount":"317.45"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-22","Item Tax Amount":"25.67"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-22","Item Tax Amount":"8.56"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-22","Item Tax Amount":"8.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-22","Item Amount":"34.37"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-23","Item Amount":"283.63"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-23","Item Tax Amount":"22.94"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-23","Item Tax Amount":"7.65"},{"Item Name":"Laundry","Transaction Date":"2023-07-23","Item Amount":"38.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-23","Item Amount":"36.88"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Louisville Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Louisville Airport' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_4(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Santa Rosa Railroad Square','MerchantAddress':'458 Maple Dr, Santa Rosa, CA 11252, USA','TransactionDate':'2025-02-04',,'Total':'496.75','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OR','Description':'Corporate trip - Business Intelligence Summit conference in Salem. vendor negotiations and contract reviews over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-02","Item Amount":"116.26"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-02","Item Tax Amount":"3.22"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-02","Item Tax Amount":"9.65"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-02","Item Tax Amount":"3.22"},{"Item Name":"Laundry","Transaction Date":"2025-02-02","Item Amount":"24.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-02","Item Amount":"63.44"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-03","Item Amount":"128.11"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-03","Item Tax Amount":"3.55"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-03","Item Tax Amount":"10.64"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-03","Item Tax Amount":"3.55"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-02-03","Item Amount":"65.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-03","Item Amount":"65.36"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Santa Rosa Railroad Square' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Santa Rosa Railroad Square' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_5(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Reno Downtown','MerchantAddress':'760 Perry Blvd, Reno, NV 85713, USA','TransactionDate':'2023-04-23',,'Total':'449.67','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company business trip - Attended Corporate Strategy Summit in Clearwater. 3 business nights; technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-20","Item Amount":"93.92"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-20","Item Tax Amount":"4.54"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-20","Item Tax Amount":"1.51"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-20","Item Tax Amount":"1.51"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-20","Item Amount":"25.45"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-21","Item Amount":"104.04"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-21","Item Tax Amount":"5.03"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-21","Item Tax Amount":"1.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-21","Item Amount":"37.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-22","Item Amount":"83.30"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-22","Item Tax Amount":"4.02"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-22","Item Tax Amount":"1.34"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-22","Item Tax Amount":"1.34"},{"Item Name":"Gift and Entertainment","Transaction Date":"2023-04-22","Item Amount":"27.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-22","Item Amount":"27.74"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-04-23","Item Amount":"29.63"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Reno Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Reno Downtown' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_6(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Huntington Beach Huntington Pier','MerchantAddress':'433 Taylor Ave, Huntington Beach, CA 51234, USA','TransactionDate':'2021-06-20',,'Total':'348.08','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Marketing Analytics Summit conference in Victorville. product demos and customer meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-18","Item Amount":"93.39"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-18","Item Tax Amount":"8.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-18","Item Amount":"65.38"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-19","Item Amount":"124.88"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-19","Item Tax Amount":"11.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-19","Item Amount":"44.87"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Huntington Beach Huntington Pier' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Huntington Beach Huntington Pier' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_7(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Buffalo Elmwood Village','MerchantAddress':'503 First St, Buffalo, NY 32515, USA','TransactionDate':'2021-04-05',,'Total':'736.69','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company travel - FinTech Conference in Knoxville. 2 business nights for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-03","Item Amount":"238.71"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-03","Item Tax Amount":"4.71"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-03","Item Tax Amount":"14.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-03","Item Amount":"62.00"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-04","Item Amount":"250.88"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-04","Item Tax Amount":"4.95"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-04","Item Tax Amount":"14.85"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-04-04","Item Amount":"83.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-04","Item Amount":"62.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Buffalo Elmwood Village' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Buffalo Elmwood Village' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_8(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Long Beach Naples','MerchantAddress':'577 Adams Dr, Long Beach, CA 46108, USA','TransactionDate':'2022-08-02',,'Total':'303.06','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Fremont for Real Estate Investment Summit. 1 night stay for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-01","Item Amount":"194.39"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-01","Item Tax Amount":"13.99"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-01","Item Amount":"75.73"},{"Item Name":"Incidentals","Transaction Date":"2022-08-01","Item Amount":"18.95"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Long Beach Naples' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Long Beach Naples' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_9(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Tampa Westshore','MerchantAddress':'987 Adams St, Tampa, FL 58474, USA','TransactionDate':'2025-07-30',,'Total':'1232.57','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended IoT Solutions Summit in Thousand Oaks. 4 business nights; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-26","Item Amount":"172.97"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-26","Item Tax Amount":"10.83"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-26","Item Tax Amount":"3.61"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-26","Item Tax Amount":"3.61"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-07-26","Item Amount":"50.33"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-26","Item Amount":"94.99"},{"Item Name":"Incidentals","Transaction Date":"2025-07-26","Item Amount":"19.28"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-27","Item Amount":"158.61"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-27","Item Tax Amount":"9.93"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-27","Item Tax Amount":"3.31"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-27","Item Tax Amount":"3.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-27","Item Amount":"98.44"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-28","Item Amount":"163.00"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-28","Item Tax Amount":"10.21"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-28","Item Tax Amount":"3.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-28","Item Amount":"90.28"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-29","Item Amount":"177.75"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-29","Item Tax Amount":"11.13"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-29","Item Tax Amount":"3.71"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-29","Item Tax Amount":"3.71"},{"Item Name":"Laundry","Transaction Date":"2025-07-29","Item Amount":"33.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-29","Item Amount":"106.28"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Tampa Westshore' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Tampa Westshore' have all 22 required itemizations'?,",
#     )


# def test_expense_hotel_10(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Richmond El Cerrito','MerchantAddress':'679 Carter St, Richmond, CA 25441, USA','TransactionDate':'2022-03-03',,'Total':'479.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Santa Ana for technology implementation. Attended Marketing Analytics Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-02","Item Amount":"187.00"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-02","Item Tax Amount":"13.34"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-02","Item Tax Amount":"4.45"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-02","Item Tax Amount":"4.45"},{"Item Name":"Entertainment External","Transaction Date":"2022-03-02","Item Amount":"89.74"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-03-02","Item Amount":"105.66"},{"Item Name":"Hotel Telephone","Transaction Date":"2022-03-02","Item Amount":"16.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-02","Item Amount":"58.97"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Richmond El Cerrito' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Richmond El Cerrito' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_11(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Fairfield Suisun City','MerchantAddress':'701 Bell St, Fairfield, CA 78025, USA','TransactionDate':'2020-03-19',,'Total':'849.37','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Business travel to West Valley City for DevOps World. 3 nights stay for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-03-16","Item Amount":"123.02"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-16","Item Tax Amount":"4.34"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-16","Item Tax Amount":"6.51"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-03-16","Item Amount":"81.40"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-03-17","Item Amount":"127.93"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-17","Item Tax Amount":"4.51"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-17","Item Tax Amount":"6.77"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-03-17","Item Amount":"58.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-03-18","Item Amount":"121.29"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-18","Item Tax Amount":"4.28"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-18","Item Tax Amount":"6.42"},{"Item Name":"Entertainment External","Transaction Date":"2020-03-18","Item Amount":"61.03"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-03-18","Item Amount":"25.92"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-03-18","Item Amount":"148.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-03-18","Item Amount":"69.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Fairfield Suisun City' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Fairfield Suisun City' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_12(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Aurora Eola','MerchantAddress':'396 King Dr, Aurora, IL 63131, USA','TransactionDate':'2019-09-22',,'Total':'428.74','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'RI','Description':'Company business trip - Attended Digital Transformation Summit in Providence. 1 business night; partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-21","Item Amount":"241.78"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-21","Item Tax Amount":"17.89"},{"Item Name":"Entertainment External","Transaction Date":"2019-09-21","Item Amount":"99.61"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-21","Item Amount":"69.46"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Aurora Eola' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Aurora Eola' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_13(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Paterson Riverside','MerchantAddress':'840 Rivera Ave, Paterson, NJ 67308, USA','TransactionDate':'2021-08-23',,'Total':'339.61','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Long Beach for board meetings. Attended E-commerce Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-08-22","Item Amount":"228.99"},{"Item Name":"Hotel Tax","Transaction Date":"2021-08-22","Item Tax Amount":"20.06"},{"Item Name":"Hotel Tax","Transaction Date":"2021-08-22","Item Tax Amount":"6.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-08-22","Item Amount":"83.87"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Paterson Riverside' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Paterson Riverside' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_14(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Corpus Christi Downtown','MerchantAddress':'381 Kelly Dr, Corpus Christi, TX 74252, USA','TransactionDate':'2019-12-05',,'Total':'953.45','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company travel - Sales Leadership Conference in Killeen. 4 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-01","Item Amount":"171.82"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-01","Item Tax Amount":"8.50"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-01","Item Amount":"24.46"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-02","Item Amount":"207.53"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-02","Item Tax Amount":"10.26"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-12-02","Item Amount":"15.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-02","Item Amount":"32.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-03","Item Amount":"207.99"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-03","Item Tax Amount":"10.29"},{"Item Name":"Laundry","Transaction Date":"2019-12-03","Item Amount":"36.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-03","Item Amount":"20.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-04","Item Amount":"181.13"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-04","Item Tax Amount":"8.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-04","Item Amount":"18.10"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Corpus Christi Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Corpus Christi Downtown' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_15(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Santa Maria Airport','MerchantAddress':'782 Allen Ave, Santa Maria, CA 13269, USA','TransactionDate':'2020-08-05',,'Total':'596.23','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Business travel to West Jordan for Analytics Leadership Summit. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-08-03","Item Amount":"192.81"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-03","Item Tax Amount":"3.41"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-03","Item Tax Amount":"3.41"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-03","Item Tax Amount":"10.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-08-03","Item Amount":"76.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-08-04","Item Amount":"178.25"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-04","Item Tax Amount":"3.15"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-04","Item Tax Amount":"9.45"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-08-04","Item Amount":"56.01"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-08-04","Item Amount":"62.54"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Santa Maria Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Santa Maria Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_16(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Boise Boise State','MerchantAddress':'360 Jenkins Ave, Boise, ID 65908, USA','TransactionDate':'2025-06-12',,'Total':'1027.04','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Business travel to Lansing for Corporate Strategy Summit. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-10","Item Amount":"304.03"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-10","Item Tax Amount":"16.31"},{"Item Name":"Incidentals","Transaction Date":"2025-06-10","Item Amount":"12.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-10","Item Amount":"106.85"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-11","Item Amount":"303.40"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-11","Item Tax Amount":"16.27"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-06-11","Item Amount":"147.38"},{"Item Name":"Laundry","Transaction Date":"2025-06-11","Item Amount":"21.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-11","Item Amount":"99.28"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Boise Boise State' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Boise Boise State' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_17(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Garden Grove Harbor Boulevard','MerchantAddress':'204 Kelly Dr, Garden Grove, CA 57989, USA','TransactionDate':'2022-10-13',,'Total':'372.24','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Business trip to Grand Rapids for compliance audit. Attended IoT Solutions Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-12","Item Amount":"228.53"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-12","Item Tax Amount":"11.41"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-12","Item Tax Amount":"3.80"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-12","Item Tax Amount":"3.80"},{"Item Name":"Laundry","Transaction Date":"2022-10-12","Item Amount":"37.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-12","Item Amount":"87.03"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Garden Grove Harbor Boulevard' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Garden Grove Harbor Boulevard' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_18(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Pomona Airport','MerchantAddress':'527 First St, Pomona, CA 53539, USA','TransactionDate':'2019-01-15',,'Total':'393.64','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Retail Innovation Conference conference in Lancaster. product demos and customer meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-13","Item Amount":"84.99"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-13","Item Tax Amount":"5.93"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-13","Item Tax Amount":"1.98"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-01-13","Item Amount":"25.05"},{"Item Name":"Incidentals","Transaction Date":"2019-01-13","Item Amount":"47.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-13","Item Amount":"20.38"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-14","Item Amount":"75.85"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-14","Item Tax Amount":"5.30"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-14","Item Tax Amount":"1.77"},{"Item Name":"Hotel Deposit","Transaction Date":"2019-01-14","Item Amount":"108.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-14","Item Amount":"16.58"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Pomona Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Pomona Airport' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_19(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Tulsa Downtown','MerchantAddress':'263 Edwards Ave, Tulsa, OK 72284, USA','TransactionDate':'2020-10-10',,'Total':'450.41','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to El Paso for team training. Attended Data Science Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-08","Item Amount":"152.93"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-08","Item Tax Amount":"8.15"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-08","Item Tax Amount":"12.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-08","Item Amount":"43.27"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-09","Item Amount":"162.51"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-09","Item Tax Amount":"8.66"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-09","Item Tax Amount":"12.98"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-09","Item Amount":"49.69"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Tulsa Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Tulsa Downtown' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_20(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Lafayette Acadiana Mall','MerchantAddress':'532 Pine St, Lafayette, LA 24713, USA','TransactionDate':'2021-02-14',,'Total':'507.87','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Fullerton for Real Estate Investment Summit. 3 nights stay for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-11","Item Amount":"115.13"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-11","Item Tax Amount":"6.09"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-11","Item Tax Amount":"2.03"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-11","Item Tax Amount":"2.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-11","Item Amount":"29.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-12","Item Amount":"87.53"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-12","Item Tax Amount":"4.63"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-12","Item Tax Amount":"1.54"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-12","Item Tax Amount":"1.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-12","Item Amount":"29.90"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-13","Item Amount":"78.82"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-13","Item Tax Amount":"4.17"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-13","Item Tax Amount":"1.39"},{"Item Name":"Entertainment External","Transaction Date":"2021-02-13","Item Amount":"61.78"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-02-13","Item Amount":"42.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-13","Item Amount":"39.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Lafayette Acadiana Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Lafayette Acadiana Mall' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_21(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Elk Grove Old Town','MerchantAddress':'336 Johnson Ave, Elk Grove, CA 58020, USA','TransactionDate':'2023-08-17',,'Total':'1790.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Business travel to St. Paul for Product Management Summit. 4 nights stay for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-13","Item Amount":"320.47"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-13","Item Tax Amount":"27.22"},{"Item Name":"Laundry","Transaction Date":"2023-08-13","Item Amount":"19.87"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-13","Item Amount":"83.02"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-14","Item Amount":"321.91"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-14","Item Tax Amount":"27.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-14","Item Amount":"89.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-15","Item Amount":"338.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-15","Item Tax Amount":"28.71"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-15","Item Amount":"86.13"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-16","Item Amount":"339.71"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-16","Item Tax Amount":"28.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-16","Item Amount":"79.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Elk Grove Old Town' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Elk Grove Old Town' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_22(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Columbia Columbiana Centre','MerchantAddress':'810 First St, Columbia, SC 52232, USA','TransactionDate':'2025-01-24',,'Total':'614.88','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Data Science Summit conference in Pasadena. sales presentations and client onboarding over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-22","Item Amount":"183.15"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-22","Item Tax Amount":"10.26"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-22","Item Tax Amount":"15.39"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-01-22","Item Amount":"52.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-22","Item Amount":"78.46"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-23","Item Amount":"181.39"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-23","Item Tax Amount":"10.16"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-23","Item Tax Amount":"15.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-23","Item Amount":"68.06"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Columbia Columbiana Centre' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Columbia Columbiana Centre' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_23(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Visalia Tulare','MerchantAddress':'506 Mill St, Visalia, CA 76602, USA','TransactionDate':'2024-02-25',,'Total':'412.89','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Product Management Summit in Escondido. 2 business nights; partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-02-23","Item Amount":"142.02"},{"Item Name":"Hotel Tax","Transaction Date":"2024-02-23","Item Tax Amount":"6.82"},{"Item Name":"Laundry","Transaction Date":"2024-02-23","Item Amount":"25.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-02-23","Item Amount":"28.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-02-24","Item Amount":"168.34"},{"Item Name":"Hotel Tax","Transaction Date":"2024-02-24","Item Tax Amount":"8.09"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-02-24","Item Amount":"14.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-02-24","Item Amount":"19.22"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Visalia Tulare' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Visalia Tulare' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_24(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Grand Prairie Great Southwest','MerchantAddress':'280 Washington Ave, Grand Prairie, TX 95857, USA','TransactionDate':'2025-05-26',,'Total':'1306.35','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Oceanside for Retail Innovation Conference. 4 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-05-22","Item Amount":"269.77"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-22","Item Tax Amount":"17.47"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-22","Item Tax Amount":"5.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-05-22","Item Amount":"24.65"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-05-23","Item Amount":"275.68"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-23","Item Tax Amount":"17.85"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-23","Item Tax Amount":"5.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-05-23","Item Amount":"23.81"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-05-24","Item Amount":"265.47"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-24","Item Tax Amount":"17.19"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-24","Item Tax Amount":"5.73"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-24","Item Tax Amount":"5.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-05-24","Item Amount":"26.87"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-05-25","Item Amount":"278.54"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-25","Item Tax Amount":"18.03"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-25","Item Tax Amount":"6.01"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-25","Item Tax Amount":"6.01"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-05-25","Item Amount":"35.77"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Grand Prairie Great Southwest' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Grand Prairie Great Southwest' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_25(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Lincoln Airport','MerchantAddress':'997 Oak St, Lincoln, NE 33242, USA','TransactionDate':'2019-10-14',,'Total':'392.53','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Business travel to Thornton for Supply Chain Management Conference. 2 nights stay for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-12","Item Amount":"83.97"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-12","Item Tax Amount":"4.71"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-12","Item Tax Amount":"1.57"},{"Item Name":"Entertainment External","Transaction Date":"2019-10-12","Item Amount":"43.81"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-10-12","Item Amount":"25.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-12","Item Amount":"48.93"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-13","Item Amount":"75.50"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-13","Item Tax Amount":"4.24"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-13","Item Tax Amount":"1.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-13","Item Amount":"53.58"},{"Item Name":"Incidentals","Transaction Date":"2019-10-13","Item Amount":"49.14"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Lincoln Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Lincoln Airport' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_26(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Hialeah Westland Mall','MerchantAddress':'715 Watson St, Hialeah, FL 78470, USA','TransactionDate':'2024-12-08',,'Total':'167.88','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'GA','Description':'Company travel - Project Management Summit in Columbus. 1 business night for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-07","Item Amount":"87.33"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-07","Item Tax Amount":"2.25"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-07","Item Tax Amount":"6.74"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-07","Item Tax Amount":"2.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-07","Item Amount":"48.79"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-12-08","Item Amount":"20.52"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Hialeah Westland Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Hialeah Westland Mall' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_27(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard McAllen Airport','MerchantAddress':'779 Martinez Blvd, McAllen, TX 26766, USA','TransactionDate':'2024-05-26',,'Total':'1208.89','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Cybersecurity Conference in Vallejo. 4 business nights for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-22","Item Amount":"198.94"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-22","Item Tax Amount":"9.61"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-05-22","Item Amount":"175.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-22","Item Amount":"45.75"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-23","Item Amount":"195.08"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-23","Item Tax Amount":"9.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-23","Item Amount":"46.59"},{"Item Name":"Incidentals","Transaction Date":"2024-05-23","Item Amount":"17.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-24","Item Amount":"189.48"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-24","Item Tax Amount":"9.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-24","Item Amount":"50.54"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-25","Item Amount":"198.86"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-25","Item Tax Amount":"9.61"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-25","Item Amount":"53.50"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard McAllen Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard McAllen Airport' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_28(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Philadelphia Center City','MerchantAddress':'688 School St, Philadelphia, PA 50058, USA','TransactionDate':'2024-09-19',,'Total':'367.66','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'VA','Description':'Corporate trip - Real Estate Investment Summit conference in Richmond. strategic planning sessions over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-18","Item Amount":"139.47"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-18","Item Tax Amount":"8.04"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-09-18","Item Amount":"154.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-18","Item Amount":"65.77"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Philadelphia Center City' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Philadelphia Center City' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_29(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Newark University Heights','MerchantAddress':'689 Barnes Ave, Newark, NJ 53565, USA','TransactionDate':'2020-11-08',,'Total':'471.82','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company travel - Cybersecurity Conference in Brownsville. 1 business night for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-07","Item Amount":"244.62"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-07","Item Tax Amount":"14.58"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-11-07","Item Amount":"95.96"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-11-07","Item Amount":"19.74"},{"Item Name":"Incidentals","Transaction Date":"2020-11-07","Item Amount":"47.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-07","Item Amount":"49.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Newark University Heights' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Newark University Heights' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_30(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Reno Midtown','MerchantAddress':'328 King Dr, Reno, NV 14749, USA','TransactionDate':'2024-04-05',,'Total':'753.17','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MS','Description':'Business trip to Jackson for vendor negotiations. Attended Data Science Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-03","Item Amount":"252.46"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-03","Item Tax Amount":"18.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-03","Item Amount":"85.20"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-04","Item Amount":"270.38"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-04","Item Tax Amount":"19.69"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-04-04","Item Amount":"6.50"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-04","Item Amount":"90.32"},{"Item Name":"Incidentals","Transaction Date":"2024-04-04","Item Amount":"10.23"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Reno Midtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Reno Midtown' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_31(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Philadelphia University City','MerchantAddress':'101 Nguyen Dr, Philadelphia, PA 24181, USA','TransactionDate':'2021-04-12',,'Total':'609.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company business trip - Attended Data Science Summit in Murfreesboro. 2 business nights; customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-10","Item Amount":"172.46"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-10","Item Tax Amount":"4.88"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-10","Item Tax Amount":"4.88"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-10","Item Tax Amount":"14.64"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-04-10","Item Amount":"6.37"},{"Item Name":"Incidentals","Transaction Date":"2021-04-10","Item Amount":"12.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-10","Item Amount":"69.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-11","Item Amount":"191.71"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-11","Item Tax Amount":"5.42"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-11","Item Tax Amount":"5.42"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-11","Item Tax Amount":"16.27"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-04-11","Item Amount":"25.77"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-11","Item Amount":"80.06"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Philadelphia University City' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Philadelphia University City' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_32(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn St. Louis Clayton','MerchantAddress':'648 Foster Dr, St. Louis, MO 17865, USA','TransactionDate':'2019-02-13',,'Total':'833.96','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Company business trip - Attended Product Management Summit in Durham. 4 business nights; stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-09","Item Amount":"111.48"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-09","Item Tax Amount":"9.09"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-02-09","Item Amount":"74.36"},{"Item Name":"Laundry","Transaction Date":"2019-02-09","Item Amount":"16.27"},{"Item Name":"Incidentals","Transaction Date":"2019-02-09","Item Amount":"11.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-09","Item Amount":"48.06"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-10","Item Amount":"119.24"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-10","Item Tax Amount":"9.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-10","Item Amount":"56.46"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-11","Item Amount":"118.78"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-11","Item Tax Amount":"9.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-11","Item Amount":"62.65"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-12","Item Amount":"118.39"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-12","Item Tax Amount":"9.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-12","Item Amount":"59.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn St. Louis Clayton' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn St. Louis Clayton' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_33(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Simi Valley Airport','MerchantAddress':'155 Stewart Blvd, Simi Valley, CA 42392, USA','TransactionDate':'2020-05-07',,'Total':'1224.55','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Escondido for investor relations. Attended Innovation Leadership Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-04","Item Amount":"292.37"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-04","Item Tax Amount":"22.68"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-05-04","Item Amount":"37.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-04","Item Amount":"81.32"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-05","Item Amount":"268.11"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-05","Item Tax Amount":"20.80"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-05","Item Amount":"65.94"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-06","Item Amount":"292.03"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-06","Item Tax Amount":"22.65"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-05-06","Item Amount":"19.35"},{"Item Name":"Incidentals","Transaction Date":"2020-05-06","Item Amount":"27.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-06","Item Amount":"74.42"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Simi Valley Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Simi Valley Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_34(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Plano Shops at Legacy','MerchantAddress':'618 Park Ave, Plano, TX 74382, USA','TransactionDate':'2025-04-26',,'Total':'518.12','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'VA','Description':'Corporate trip - Innovation Leadership Conference conference in Richmond. market research and competitive analysis over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-25","Item Amount":"280.06"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-25","Item Tax Amount":"11.13"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-25","Item Tax Amount":"16.70"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-04-25","Item Amount":"66.46"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-04-25","Item Amount":"51.55"},{"Item Name":"Hotel Telephone","Transaction Date":"2025-04-25","Item Amount":"23.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-25","Item Amount":"68.87"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Plano Shops at Legacy' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Plano Shops at Legacy' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_35(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Dallas Uptown','MerchantAddress':'565 Washington Ave, Dallas, TX 66245, USA','TransactionDate':'2023-10-11',,'Total':'370.24','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Pasadena for product launch. Attended Tech Innovation Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-09","Item Amount":"103.58"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-09","Item Tax Amount":"6.31"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-09","Item Tax Amount":"2.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-09","Item Tax Amount":"2.10"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-10-09","Item Amount":"22.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-09","Item Amount":"37.36"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-10","Item Amount":"109.59"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-10","Item Tax Amount":"6.67"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-10","Item Tax Amount":"2.22"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-10","Item Tax Amount":"2.22"},{"Item Name":"Laundry","Transaction Date":"2023-10-10","Item Amount":"25.80"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-10","Item Amount":"33.58"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-10-11","Item Amount":"16.11"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Dallas Uptown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Dallas Uptown' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_36(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Tampa Hyde Park','MerchantAddress':'249 Myers St, Tampa, FL 97892, USA','TransactionDate':'2024-03-25',,'Total':'1188.29','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Business trip to Shreveport for compliance audit. Attended Enterprise Software Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-22","Item Amount":"247.59"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-22","Item Tax Amount":"17.02"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-22","Item Tax Amount":"11.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-22","Item Amount":"57.72"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-23","Item Amount":"273.67"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-23","Item Tax Amount":"18.81"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-23","Item Tax Amount":"12.54"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-03-23","Item Amount":"21.82"},{"Item Name":"Incidentals","Transaction Date":"2024-03-23","Item Amount":"42.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-23","Item Amount":"53.95"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-24","Item Amount":"243.02"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-24","Item Tax Amount":"16.71"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-24","Item Tax Amount":"11.14"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-03-24","Item Amount":"118.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-24","Item Amount":"41.81"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Tampa Hyde Park' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Tampa Hyde Park' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_37(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Rochester University','MerchantAddress':'411 Edwards Ave, Rochester, NY 79557, USA','TransactionDate':'2024-11-29',,'Total':'527.41','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Visalia for Blockchain Conference. 2 nights stay for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-11-27","Item Amount":"89.06"},{"Item Name":"Hotel Tax","Transaction Date":"2024-11-27","Item Tax Amount":"6.32"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-11-27","Item Amount":"25.34"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-11-27","Item Amount":"11.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-11-27","Item Amount":"53.22"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-11-28","Item Amount":"98.06"},{"Item Name":"Hotel Tax","Transaction Date":"2024-11-28","Item Tax Amount":"6.95"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-11-28","Item Amount":"185.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-11-28","Item Amount":"50.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Rochester University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Rochester University' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_38(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Los Angeles Santa Monica','MerchantAddress':'296 Reyes Dr, Los Angeles, CA 84280, USA','TransactionDate':'2022-03-24',,'Total':'211.02','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'RI','Description':'Company travel - Manufacturing Excellence Summit in Providence. 1 business night for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-23","Item Amount":"122.32"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-23","Item Tax Amount":"2.06"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-23","Item Tax Amount":"6.18"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-23","Item Tax Amount":"2.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-23","Item Amount":"78.40"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Los Angeles Santa Monica' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Los Angeles Santa Monica' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_39(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton San Antonio Downtown','MerchantAddress':'570 Allen Ave, San Antonio, TX 56612, USA','TransactionDate':'2020-03-27',,'Total':'1123.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Bakersfield for Cloud Computing Expo. 4 nights stay for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-03-23","Item Amount":"124.36"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-23","Item Tax Amount":"6.14"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-23","Item Tax Amount":"4.09"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-03-23","Item Amount":"160.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-03-23","Item Amount":"64.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-03-24","Item Amount":"145.03"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-24","Item Tax Amount":"7.16"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-24","Item Tax Amount":"4.77"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-03-24","Item Amount":"15.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-03-24","Item Amount":"70.78"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-03-25","Item Amount":"126.85"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-25","Item Tax Amount":"6.26"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-25","Item Tax Amount":"4.17"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-03-25","Item Amount":"75.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-03-25","Item Amount":"69.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-03-26","Item Amount":"146.26"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-26","Item Tax Amount":"7.22"},{"Item Name":"Hotel Tax","Transaction Date":"2020-03-26","Item Tax Amount":"4.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-03-26","Item Amount":"79.84"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton San Antonio Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton San Antonio Downtown' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_40(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Hartford Airport','MerchantAddress':'935 Murphy St, Hartford, CT 27862, USA','TransactionDate':'2023-07-13',,'Total':'649.02','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to Frisco for board meetings. Attended Quality Assurance Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-11","Item Amount":"206.37"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-11","Item Tax Amount":"12.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-11","Item Tax Amount":"18.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-11","Item Amount":"45.22"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-12","Item Amount":"221.07"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-12","Item Tax Amount":"12.97"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-12","Item Tax Amount":"19.45"},{"Item Name":"Gift and Entertainment","Transaction Date":"2023-07-12","Item Amount":"71.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-12","Item Amount":"41.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Hartford Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Hartford Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_41(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Fort Worth Alliance','MerchantAddress':'534 Morris Ave, Fort Worth, TX 96543, USA','TransactionDate':'2023-10-22',,'Total':'540.51','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Corporate trip - Digital Marketing Conference conference in Davie. product demos and customer meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-20","Item Amount":"164.53"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-20","Item Tax Amount":"10.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-20","Item Amount":"20.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-21","Item Amount":"169.11"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-21","Item Tax Amount":"10.50"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-10-21","Item Amount":"104.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-21","Item Amount":"34.85"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-10-22","Item Amount":"26.26"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Fort Worth Alliance' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Fort Worth Alliance' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_42(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Tulsa Downtown','MerchantAddress':'216 Fisher Dr, Tulsa, OK 76991, USA','TransactionDate':'2025-10-04',,'Total':'811.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to San Jose for technology implementation. Attended Energy Sector Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-01","Item Amount":"210.77"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-01","Item Tax Amount":"14.98"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-01","Item Tax Amount":"9.99"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-01","Item Amount":"66.39"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-02","Item Amount":"180.48"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-02","Item Tax Amount":"12.83"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-02","Item Tax Amount":"8.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-02","Item Amount":"57.02"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-03","Item Amount":"178.29"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-03","Item Tax Amount":"12.67"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-03","Item Tax Amount":"8.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-03","Item Amount":"51.35"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Tulsa Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Tulsa Downtown' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_43(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Bridgeport North End','MerchantAddress':'751 Scott St, Bridgeport, CT 91271, USA','TransactionDate':'2023-12-20',,'Total':'393.14','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended DevOps World in Orange. 2 business nights; team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-18","Item Amount":"150.67"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-18","Item Tax Amount":"11.78"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-18","Item Tax Amount":"7.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-18","Item Amount":"49.55"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-19","Item Amount":"112.40"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-19","Item Tax Amount":"8.79"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-19","Item Tax Amount":"5.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-19","Item Amount":"46.24"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Bridgeport North End' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Bridgeport North End' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_44(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Escondido Airport','MerchantAddress':'677 Miller Blvd, Escondido, CA 75186, USA','TransactionDate':'2021-06-15',,'Total':'1676.7','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Orange for Real Estate Investment Summit. 3 nights stay for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-12","Item Amount":"342.77"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-12","Item Tax Amount":"30.45"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-12","Item Tax Amount":"20.30"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-06-12","Item Amount":"76.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-12","Item Amount":"61.45"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-13","Item Amount":"345.16"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-13","Item Tax Amount":"30.67"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-13","Item Tax Amount":"20.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-13","Item Amount":"63.01"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-14","Item Amount":"372.99"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-14","Item Tax Amount":"33.14"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-14","Item Tax Amount":"22.09"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-06-14","Item Amount":"164.26"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-14","Item Amount":"67.06"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-06-15","Item Amount":"26.39"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Escondido Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Escondido Airport' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_45(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel San Bernardino Hospitality Lane','MerchantAddress':'895 Rodriguez Dr, San Bernardino, CA 11873, USA','TransactionDate':'2022-09-09',,'Total':'566.43','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Digital Marketing Conference conference in Houston. product demos and customer meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-07","Item Amount":"176.79"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-07","Item Tax Amount":"14.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-07","Item Amount":"75.73"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-08","Item Amount":"172.44"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-08","Item Tax Amount":"14.42"},{"Item Name":"Incidentals","Transaction Date":"2022-09-08","Item Amount":"39.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-08","Item Amount":"72.65"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel San Bernardino Hospitality Lane' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel San Bernardino Hospitality Lane' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_46(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Pembroke Pines Flamingo Pines','MerchantAddress':'885 Walker St, Pembroke Pines, FL 98522, USA','TransactionDate':'2025-10-05',,'Total':'463.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business trip to Cleveland for investor relations. Attended Manufacturing Excellence Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-02","Item Amount":"85.06"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-02","Item Tax Amount":"6.01"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-02","Item Amount":"66.05"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-03","Item Amount":"90.16"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-03","Item Tax Amount":"6.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-03","Item Amount":"62.50"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-04","Item Amount":"77.93"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-04","Item Tax Amount":"5.51"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-04","Item Amount":"64.01"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Pembroke Pines Flamingo Pines' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Pembroke Pines Flamingo Pines' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_47(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Stockton Brookside','MerchantAddress':'496 Market St, Stockton, CA 43781, USA','TransactionDate':'2025-09-04',,'Total':'625.09','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Sacramento for Quality Assurance Conference. 2 nights stay for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-09-02","Item Amount":"149.20"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-02","Item Tax Amount":"10.29"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-02","Item Tax Amount":"6.86"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-09-02","Item Amount":"165.11"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-09-02","Item Amount":"56.51"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-09-03","Item Amount":"128.64"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-03","Item Tax Amount":"8.87"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-03","Item Tax Amount":"5.91"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-09-03","Item Amount":"21.41"},{"Item Name":"Laundry","Transaction Date":"2025-09-03","Item Amount":"25.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-09-03","Item Amount":"47.06"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Stockton Brookside' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Stockton Brookside' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_48(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Mesquite Airport','MerchantAddress':'176 Johnson Ave, Mesquite, TX 38669, USA','TransactionDate':'2023-08-08',,'Total':'1591.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OK','Description':'Company travel - IoT Solutions Summit in Norman. 4 business nights for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-04","Item Amount":"299.86"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-04","Item Tax Amount":"19.53"},{"Item Name":"Laundry","Transaction Date":"2023-08-04","Item Amount":"17.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-04","Item Amount":"71.36"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-05","Item Amount":"301.28"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-05","Item Tax Amount":"19.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-05","Item Amount":"81.49"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-06","Item Amount":"282.58"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-06","Item Tax Amount":"18.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-06","Item Amount":"77.18"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-07","Item Amount":"300.96"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-07","Item Tax Amount":"19.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-07","Item Amount":"82.60"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Mesquite Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Mesquite Airport' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_49(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont San Antonio Airport','MerchantAddress':'264 Nelson St, San Antonio, TX 95157, USA','TransactionDate':'2021-10-18',,'Total':'480.18','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'GA','Description':'Business travel to Savannah for Change Management Conference. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-16","Item Amount":"178.38"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-16","Item Tax Amount":"12.52"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-16","Item Tax Amount":"4.17"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-16","Item Tax Amount":"4.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-16","Item Amount":"32.51"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-17","Item Amount":"183.42"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-17","Item Tax Amount":"12.87"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-17","Item Tax Amount":"4.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-17","Item Amount":"47.85"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont San Antonio Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont San Antonio Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_50(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Cedar Rapids Airport','MerchantAddress':'509 Third St, Cedar Rapids, IA 88531, USA','TransactionDate':'2019-04-27',,'Total':'456.42','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to Irving for product launch. Attended Blockchain Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-25","Item Amount":"181.83"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-25","Item Tax Amount":"8.06"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-25","Item Tax Amount":"12.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-25","Item Amount":"28.55"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-26","Item Amount":"179.76"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-26","Item Tax Amount":"7.97"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-26","Item Tax Amount":"11.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-26","Item Amount":"26.20"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Cedar Rapids Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Cedar Rapids Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_51(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Corona Dos Lagos','MerchantAddress':'457 Myers St, Corona, CA 24564, USA','TransactionDate':'2022-04-08',,'Total':'419.15','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Real Estate Investment Summit in Irving. 2 business nights; sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-06","Item Amount":"88.98"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-06","Item Tax Amount":"4.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-06","Item Tax Amount":"7.13"},{"Item Name":"Hotel Telephone","Transaction Date":"2022-04-06","Item Amount":"23.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-06","Item Amount":"35.42"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-07","Item Amount":"92.95"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-07","Item Tax Amount":"4.96"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-07","Item Tax Amount":"7.45"},{"Item Name":"Entertainment External","Transaction Date":"2022-04-07","Item Amount":"36.76"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-04-07","Item Amount":"87.98"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-07","Item Amount":"29.30"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Corona Dos Lagos' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Corona Dos Lagos' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_52(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Santa Clarita Airport','MerchantAddress':'391 Walker St, Santa Clarita, CA 58335, USA','TransactionDate':'2023-10-16',,'Total':'766.84','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Corporate trip - Tech Innovation Conference conference in Grand Rapids. operational excellence workshops over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-13","Item Amount":"216.04"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-13","Item Tax Amount":"3.59"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-13","Item Tax Amount":"3.59"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-13","Item Tax Amount":"10.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-13","Item Amount":"44.41"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-14","Item Amount":"191.94"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-14","Item Tax Amount":"3.19"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-14","Item Tax Amount":"3.19"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-14","Item Tax Amount":"9.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-14","Item Amount":"30.92"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-15","Item Amount":"199.88"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-15","Item Tax Amount":"3.32"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-15","Item Tax Amount":"9.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-15","Item Amount":"36.50"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Santa Clarita Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Santa Clarita Airport' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_53(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Overland Park Blue Valley','MerchantAddress':'992 Phillips Ave, Overland Park, KS 74218, USA','TransactionDate':'2021-06-05',,'Total':'406.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Company business trip - Attended IoT Solutions Summit in Naperville. 1 business night; board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-04","Item Amount":"322.23"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-04","Item Tax Amount":"17.98"},{"Item Name":"Laundry","Transaction Date":"2021-06-04","Item Amount":"20.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-04","Item Amount":"45.98"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Overland Park Blue Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Overland Park Blue Valley' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_54(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Abilene Buffalo Gap','MerchantAddress':'637 Ramirez Blvd, Abilene, TX 29513, USA','TransactionDate':'2019-06-15',,'Total':'513.92','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Corporate trip - Manufacturing Excellence Summit conference in Chattanooga. compliance training and audits over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-13","Item Amount":"169.67"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-13","Item Tax Amount":"9.15"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-13","Item Tax Amount":"13.72"},{"Item Name":"Laundry","Transaction Date":"2019-06-13","Item Amount":"29.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-13","Item Amount":"44.54"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-14","Item Amount":"189.12"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-14","Item Tax Amount":"10.19"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-14","Item Tax Amount":"15.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-14","Item Amount":"32.80"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Abilene Buffalo Gap' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Abilene Buffalo Gap' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_55(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Orange Chapman University','MerchantAddress':'238 Pine St, Orange, CA 62189, USA','TransactionDate':'2021-04-18',,'Total':'767.83','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Amarillo for Innovation Leadership Conference. 4 nights stay for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-14","Item Amount":"127.97"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-14","Item Tax Amount":"3.31"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-14","Item Tax Amount":"9.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-14","Item Amount":"23.48"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-15","Item Amount":"106.75"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-15","Item Tax Amount":"2.76"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-15","Item Tax Amount":"8.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-15","Item Amount":"47.65"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-16","Item Amount":"103.86"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-16","Item Tax Amount":"2.68"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-16","Item Tax Amount":"8.05"},{"Item Name":"Laundry","Transaction Date":"2021-04-16","Item Amount":"36.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-16","Item Amount":"24.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-17","Item Amount":"127.02"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-17","Item Tax Amount":"3.28"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-17","Item Tax Amount":"9.84"},{"Item Name":"Entertainment External","Transaction Date":"2021-04-17","Item Amount":"75.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-17","Item Amount":"46.42"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Orange Chapman University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Orange Chapman University' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_56(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Richmond El Cerrito','MerchantAddress':'122 Third St, Richmond, CA 27561, USA','TransactionDate':'2022-07-13',,'Total':'397.45','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Quality Assurance Conference in Stockton. 1 business night; board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-12","Item Amount":"293.82"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-12","Item Tax Amount":"15.79"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-12","Item Tax Amount":"5.26"},{"Item Name":"Incidentals","Transaction Date":"2022-07-12","Item Amount":"29.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-12","Item Amount":"53.58"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Richmond El Cerrito' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Richmond El Cerrito' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_57(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Garland DART','MerchantAddress':'520 Adams St, Garland, TX 24623, USA','TransactionDate':'2019-02-12',,'Total':'516.62','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Business travel to Rockford for Mobile Technology Conference. 2 nights stay for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-10","Item Amount":"144.59"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-10","Item Tax Amount":"8.56"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-10","Item Tax Amount":"2.85"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-10","Item Tax Amount":"2.85"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-02-10","Item Amount":"71.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-10","Item Amount":"33.84"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-11","Item Amount":"170.36"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-11","Item Tax Amount":"10.09"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-11","Item Tax Amount":"3.36"},{"Item Name":"Hotel Breakfast","Transaction Date":"2019-02-11","Item Amount":"16.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-11","Item Amount":"52.35"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Garland DART' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Garland DART' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_58(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Tallahassee Airport','MerchantAddress':'641 Clark St, Tallahassee, FL 77204, USA','TransactionDate':'2022-08-29',,'Total':'1014.92','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Santa Ana for Real Estate Investment Summit. 2 nights stay for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-27","Item Amount":"371.95"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-27","Item Tax Amount":"18.92"},{"Item Name":"Incidentals","Transaction Date":"2022-08-27","Item Amount":"19.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-27","Item Amount":"84.19"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-28","Item Amount":"380.55"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-28","Item Tax Amount":"19.36"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-08-28","Item Amount":"12.66"},{"Item Name":"Laundry","Transaction Date":"2022-08-28","Item Amount":"16.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-28","Item Amount":"90.61"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Tallahassee Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Tallahassee Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_59(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Santa Clara Santana Row','MerchantAddress':'170 Water St, Santa Clara, CA 40845, USA','TransactionDate':'2022-08-27',,'Total':'1672.63','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Company business trip - Attended Analytics Leadership Summit in Sterling Heights. 4 business nights; client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-23","Item Amount":"280.65"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-23","Item Tax Amount":"21.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-23","Item Amount":"57.36"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-24","Item Amount":"279.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-24","Item Tax Amount":"21.36"},{"Item Name":"Entertainment External","Transaction Date":"2022-08-24","Item Amount":"101.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-24","Item Amount":"66.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-25","Item Amount":"310.24"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-25","Item Tax Amount":"23.69"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-08-25","Item Amount":"56.36"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-08-25","Item Amount":"29.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-25","Item Amount":"50.90"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-26","Item Amount":"281.23"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-26","Item Tax Amount":"21.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-26","Item Amount":"71.42"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Santa Clara Santana Row' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Santa Clara Santana Row' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_60(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Ontario Ontario Airport','MerchantAddress':'992 Diaz St, Ontario, CA 56197, USA','TransactionDate':'2019-04-16',,'Total':'768.79','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company travel - FinTech Conference in Carrollton. 3 business nights for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-13","Item Amount":"163.37"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-13","Item Tax Amount":"6.78"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-13","Item Tax Amount":"10.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-13","Item Amount":"76.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-14","Item Amount":"173.24"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-14","Item Tax Amount":"7.19"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-14","Item Tax Amount":"10.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-14","Item Amount":"62.85"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-15","Item Amount":"175.51"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-15","Item Tax Amount":"7.28"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-15","Item Tax Amount":"10.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-15","Item Amount":"63.88"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Ontario Ontario Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Ontario Ontario Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_61(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Akron Airport','MerchantAddress':'611 Williams Dr, Akron, OH 22943, USA','TransactionDate':'2020-12-23',,'Total':'449.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Business trip to Gilbert for strategic planning. Attended Business Intelligence Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-21","Item Amount":"134.65"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-21","Item Tax Amount":"7.77"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-21","Item Tax Amount":"5.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-21","Item Amount":"34.49"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-22","Item Amount":"138.22"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-22","Item Tax Amount":"7.98"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-22","Item Tax Amount":"5.32"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-12-22","Item Amount":"38.61"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-12-22","Item Amount":"6.38"},{"Item Name":"Laundry","Transaction Date":"2020-12-22","Item Amount":"33.98"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-22","Item Amount":"36.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Akron Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Akron Airport' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_62(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Pembroke Pines Century Village','MerchantAddress':'767 Parker Dr, Pembroke Pines, FL 67374, USA','TransactionDate':'2020-04-06',,'Total':'1463.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business travel to Toledo for Tech Innovation Conference. 4 nights stay for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-02","Item Amount":"261.50"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-02","Item Tax Amount":"14.29"},{"Item Name":"Entertainment External","Transaction Date":"2020-04-02","Item Amount":"48.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-02","Item Amount":"58.01"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-03","Item Amount":"259.08"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-03","Item Tax Amount":"14.16"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-04-03","Item Amount":"13.85"},{"Item Name":"Laundry","Transaction Date":"2020-04-03","Item Amount":"37.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-03","Item Amount":"50.07"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-04","Item Amount":"269.93"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-04","Item Tax Amount":"14.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-04","Item Amount":"71.05"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-05","Item Amount":"281.53"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-05","Item Tax Amount":"15.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-05","Item Amount":"54.21"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Pembroke Pines Century Village' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Pembroke Pines Century Village' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_63(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Cedar Rapids Airport','MerchantAddress':'620 Williams Dr, Cedar Rapids, IA 38578, USA','TransactionDate':'2021-09-05',,'Total':'627.45','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Manufacturing Excellence Summit in Oceanside. 2 business nights; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-03","Item Amount":"115.30"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-03","Item Tax Amount":"8.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-03","Item Tax Amount":"2.99"},{"Item Name":"Entertainment External","Transaction Date":"2021-09-03","Item Amount":"21.86"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-09-03","Item Amount":"182.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-03","Item Amount":"68.28"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-04","Item Amount":"142.26"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-04","Item Tax Amount":"11.05"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-04","Item Tax Amount":"3.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-04","Item Amount":"70.41"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Cedar Rapids Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Cedar Rapids Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_64(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Berkeley Downtown','MerchantAddress':'724 Commerce St, Berkeley, CA 87964, USA','TransactionDate':'2020-04-10',,'Total':'400.24','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip to Hollywood for strategic planning. Attended Retail Innovation Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-09","Item Amount":"274.33"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-09","Item Tax Amount":"22.53"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-09","Item Tax Amount":"15.02"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-04-09","Item Amount":"16.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-09","Item Amount":"71.55"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Berkeley Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Berkeley Downtown' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_65(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Woodbridge Woodbridge Center','MerchantAddress':'602 Adams St, Woodbridge, NJ 51925, USA','TransactionDate':'2025-09-03',,'Total':'340.71','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Company travel - Innovation Leadership Conference in Chandler. 1 business night for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-09-02","Item Amount":"154.53"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-02","Item Tax Amount":"9.97"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-02","Item Tax Amount":"3.32"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-02","Item Tax Amount":"3.32"},{"Item Name":"Entertainment External","Transaction Date":"2025-09-02","Item Amount":"82.73"},{"Item Name":"Incidentals","Transaction Date":"2025-09-02","Item Amount":"26.26"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-09-02","Item Amount":"60.58"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Woodbridge Woodbridge Center' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Woodbridge Woodbridge Center' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_66(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Columbus Downtown','MerchantAddress':'529 School St, Columbus, OH 22460, USA','TransactionDate':'2024-12-06',,'Total':'569.93','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Business travel to Tacoma for DevOps World. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-04","Item Amount":"171.29"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-04","Item Tax Amount":"8.90"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-04","Item Tax Amount":"13.35"},{"Item Name":"Entertainment External","Transaction Date":"2024-12-04","Item Amount":"39.21"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-12-04","Item Amount":"10.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-04","Item Amount":"72.92"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-05","Item Amount":"159.74"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-05","Item Tax Amount":"8.30"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-05","Item Tax Amount":"12.45"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-12-05","Item Amount":"18.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-05","Item Amount":"54.94"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Columbus Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Columbus Downtown' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_67(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Columbus Airport','MerchantAddress':'100 State St, Columbus, OH 60669, USA','TransactionDate':'2020-04-11',,'Total':'692.41','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Corporate trip - AI & Machine Learning Conference conference in Chicago. team building and training sessions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-09","Item Amount":"282.80"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-09","Item Tax Amount":"23.60"},{"Item Name":"Incidentals","Transaction Date":"2020-04-09","Item Amount":"19.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-09","Item Amount":"36.90"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-10","Item Amount":"267.16"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-10","Item Tax Amount":"22.30"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-10","Item Amount":"40.45"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Columbus Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Columbus Airport' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_68(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Denver Capitol Hill','MerchantAddress':'204 Torres Ave, Denver, CO 85291, USA','TransactionDate':'2020-10-15',,'Total':'1018.35','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - AI & Machine Learning Conference conference in Pomona. compliance training and audits over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-11","Item Amount":"129.82"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-11","Item Tax Amount":"9.71"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-11","Item Tax Amount":"6.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-11","Item Amount":"69.73"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-12","Item Amount":"153.96"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-12","Item Tax Amount":"11.52"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-12","Item Tax Amount":"7.68"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-10-12","Item Amount":"43.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-12","Item Amount":"75.48"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-13","Item Amount":"164.76"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-13","Item Tax Amount":"12.32"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-13","Item Tax Amount":"8.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-13","Item Amount":"66.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-14","Item Amount":"141.62"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-14","Item Tax Amount":"10.59"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-14","Item Tax Amount":"7.06"},{"Item Name":"Incidentals","Transaction Date":"2020-10-14","Item Amount":"36.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-14","Item Amount":"63.29"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Denver Capitol Hill' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Denver Capitol Hill' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_69(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Elk Grove Airport','MerchantAddress':'731 Rogers St, Elk Grove, CA 94182, USA','TransactionDate':'2021-05-13',,'Total':'178.86','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Company business trip - Attended Manufacturing Excellence Summit in Phoenix. 1 business night; board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-12","Item Amount":"72.18"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-12","Item Tax Amount":"4.91"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-12","Item Tax Amount":"1.64"},{"Item Name":"Laundry","Transaction Date":"2021-05-12","Item Amount":"22.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-12","Item Amount":"77.74"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Elk Grove Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Elk Grove Airport' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_70(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Hampton Langley AFB','MerchantAddress':'749 Wilson Way, Hampton, VA 55494, USA','TransactionDate':'2023-05-07',,'Total':'601.25','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip to Port St. Lucie for board meetings. Attended E-commerce Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-05-05","Item Amount":"202.88"},{"Item Name":"Hotel Tax","Transaction Date":"2023-05-05","Item Tax Amount":"15.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-05-05","Item Amount":"32.24"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-05-06","Item Amount":"211.86"},{"Item Name":"Hotel Tax","Transaction Date":"2023-05-06","Item Tax Amount":"16.23"},{"Item Name":"Entertainment External","Transaction Date":"2023-05-06","Item Amount":"53.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-05-06","Item Amount":"44.89"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-05-07","Item Amount":"23.93"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Hampton Langley AFB' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Hampton Langley AFB' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_71(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Arlington Downtown','MerchantAddress':'148 Business District Way, Arlington, TX 48179, USA','TransactionDate':'2022-12-06',,'Total':'318.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OK','Description':'Company business trip - Attended Supply Chain Management Conference in Oklahoma City. 1 business night; quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-12-05","Item Amount":"197.73"},{"Item Name":"Hotel Tax","Transaction Date":"2022-12-05","Item Tax Amount":"14.45"},{"Item Name":"Hotel Tax","Transaction Date":"2022-12-05","Item Tax Amount":"4.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-12-05","Item Amount":"56.44"},{"Item Name":"Incidentals","Transaction Date":"2022-12-05","Item Amount":"44.61"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Arlington Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Arlington Downtown' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_72(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Atlanta Virginia Highland','MerchantAddress':'867 Court St, Atlanta, GA 54837, USA','TransactionDate':'2025-03-07',,'Total':'665.43','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Project Management Summit conference in Santa Ana. merger and acquisition discussions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-03-05","Item Amount":"247.49"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-05","Item Tax Amount":"12.35"},{"Item Name":"Laundry","Transaction Date":"2025-03-05","Item Amount":"36.21"},{"Item Name":"Incidentals","Transaction Date":"2025-03-05","Item Amount":"42.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-03-05","Item Amount":"38.05"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-03-06","Item Amount":"240.04"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-06","Item Tax Amount":"11.98"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-03-06","Item Amount":"37.31"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Atlanta Virginia Highland' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Atlanta Virginia Highland' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_73(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Denver Downtown','MerchantAddress':'126 Ramirez Blvd, Denver, CO 25848, USA','TransactionDate':'2022-09-20',,'Total':'518.37','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to Garland for partnership development. Attended IoT Solutions Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-18","Item Amount":"169.88"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-18","Item Tax Amount":"3.36"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-18","Item Tax Amount":"10.08"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-09-18","Item Amount":"22.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-18","Item Amount":"22.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-19","Item Amount":"181.47"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-19","Item Tax Amount":"3.59"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-19","Item Tax Amount":"10.76"},{"Item Name":"Entertainment External","Transaction Date":"2022-09-19","Item Amount":"67.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-19","Item Amount":"27.04"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Denver Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Denver Downtown' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_74(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Dallas Deep Ellum','MerchantAddress':'657 Commerce St, Dallas, TX 90766, USA','TransactionDate':'2023-11-29',,'Total':'199.75','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Company travel - Real Estate Investment Summit in Kent. 1 business night for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-11-28","Item Amount":"98.92"},{"Item Name":"Hotel Tax","Transaction Date":"2023-11-28","Item Tax Amount":"5.00"},{"Item Name":"Gift and Entertainment","Transaction Date":"2023-11-28","Item Amount":"36.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-11-28","Item Amount":"59.65"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Dallas Deep Ellum' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Dallas Deep Ellum' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_75(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Killeen Harker Heights','MerchantAddress':'380 Robinson Ave, Killeen, TX 32637, USA','TransactionDate':'2025-10-22',,'Total':'476.87','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'VA','Description':'Company travel - Supply Chain Management Conference in Virginia Beach. 3 business nights for client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-19","Item Amount":"117.89"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-19","Item Tax Amount":"8.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-19","Item Amount":"36.09"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-20","Item Amount":"124.14"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-20","Item Tax Amount":"8.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-20","Item Amount":"26.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-21","Item Amount":"116.06"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-21","Item Tax Amount":"7.98"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-21","Item Amount":"31.31"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Killeen Harker Heights' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Killeen Harker Heights' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_76(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Overland Park Metcalf','MerchantAddress':'495 Cruz St, Overland Park, KS 99117, USA','TransactionDate':'2021-07-02',,'Total':'904.59','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Company travel - Mobile Technology Conference in Grand Rapids. 4 business nights for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-28","Item Amount":"170.91"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-28","Item Tax Amount":"11.54"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-28","Item Tax Amount":"7.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-28","Item Amount":"34.18"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-29","Item Amount":"154.62"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-29","Item Tax Amount":"10.44"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-29","Item Tax Amount":"6.96"},{"Item Name":"Laundry","Transaction Date":"2021-06-29","Item Amount":"34.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-29","Item Amount":"55.16"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-30","Item Amount":"139.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-30","Item Tax Amount":"9.43"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-30","Item Tax Amount":"6.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-30","Item Amount":"35.45"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-01","Item Amount":"154.04"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-01","Item Tax Amount":"10.40"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-01","Item Tax Amount":"6.93"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-01","Item Amount":"56.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Overland Park Metcalf' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Overland Park Metcalf' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_77(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Pasadena Airport','MerchantAddress':'456 Hughes Ave, Pasadena, CA 27284, USA','TransactionDate':'2021-04-06',,'Total':'1371','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'RI','Description':'Business travel to Providence for IoT Solutions Summit. 4 nights stay for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-02","Item Amount":"230.78"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-02","Item Tax Amount":"11.18"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-02","Item Tax Amount":"16.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-02","Item Amount":"65.03"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-03","Item Amount":"236.02"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-03","Item Tax Amount":"11.44"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-03","Item Tax Amount":"17.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-03","Item Amount":"70.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-04","Item Amount":"251.12"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-04","Item Tax Amount":"12.17"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-04","Item Tax Amount":"18.26"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-04","Item Amount":"67.63"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-05","Item Amount":"256.87"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-05","Item Tax Amount":"12.45"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-05","Item Tax Amount":"18.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-05","Item Amount":"75.09"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Pasadena Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Pasadena Airport' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_78(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Plano Legacy West','MerchantAddress':'234 Church St, Plano, TX 43903, USA','TransactionDate':'2022-12-20',,'Total':'171.99','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NV','Description':'Business trip to Las Vegas for quarterly reviews. Attended Tech Innovation Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-12-19","Item Amount":"122.58"},{"Item Name":"Hotel Tax","Transaction Date":"2022-12-19","Item Tax Amount":"9.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-12-19","Item Amount":"40.01"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Plano Legacy West' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Plano Legacy West' have all 3 required itemizations'?,",
#     )


# def test_expense_hotel_79(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Mesa Downtown','MerchantAddress':'474 Court St, Mesa, AZ 67784, USA','TransactionDate':'2021-06-26',,'Total':'583.66','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Corporate trip - Cloud Computing Expo conference in Cincinnati. technical workshops and knowledge sharing over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-25","Item Amount":"279.84"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-25","Item Tax Amount":"20.81"},{"Item Name":"Entertainment External","Transaction Date":"2021-06-25","Item Amount":"105.24"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-06-25","Item Amount":"107.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-25","Item Amount":"70.71"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Mesa Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Mesa Downtown' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_80(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Bakersfield Downtown','MerchantAddress':'946 Kelly Dr, Bakersfield, CA 51397, USA','TransactionDate':'2024-04-07',,'Total':'1531.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Company travel - Supply Chain Management Conference in Buffalo. 4 business nights for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-03","Item Amount":"306.86"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-03","Item Tax Amount":"21.87"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-03","Item Tax Amount":"7.29"},{"Item Name":"Entertainment External","Transaction Date":"2024-04-03","Item Amount":"43.78"},{"Item Name":"Laundry","Transaction Date":"2024-04-03","Item Amount":"26.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-03","Item Amount":"26.51"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-04","Item Amount":"303.26"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-04","Item Tax Amount":"21.61"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-04","Item Tax Amount":"7.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-04","Item Amount":"26.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-05","Item Amount":"308.76"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-05","Item Tax Amount":"22.00"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-05","Item Tax Amount":"7.33"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-05","Item Amount":"31.04"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-06","Item Amount":"305.02"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-06","Item Tax Amount":"21.74"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-06","Item Tax Amount":"7.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-06","Item Amount":"36.52"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Bakersfield Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Bakersfield Downtown' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_81(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Port St. Lucie PGA Village','MerchantAddress':'138 Jackson Blvd, Port St. Lucie, FL 26254, USA','TransactionDate':'2021-07-22',,'Total':'1518.97','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to McKinney for investor relations. Attended Mobile Technology Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-18","Item Amount":"297.47"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-18","Item Tax Amount":"8.81"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-18","Item Tax Amount":"8.81"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-18","Item Tax Amount":"26.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-18","Item Amount":"47.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-19","Item Amount":"300.03"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-19","Item Tax Amount":"8.88"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-19","Item Tax Amount":"26.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-19","Item Amount":"47.99"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-20","Item Amount":"289.66"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-20","Item Tax Amount":"8.57"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-20","Item Tax Amount":"25.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-20","Item Amount":"43.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-21","Item Amount":"306.11"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-21","Item Tax Amount":"9.06"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-21","Item Tax Amount":"27.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-21","Item Amount":"36.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Port St. Lucie PGA Village' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Port St. Lucie PGA Village' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_82(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Kansas City Plaza','MerchantAddress':'902 Second Ave, Kansas City, MO 36652, USA','TransactionDate':'2022-01-19',,'Total':'437.96','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to Killeen for sales presentations. Attended Marketing Analytics Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-17","Item Amount":"171.99"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-17","Item Tax Amount":"3.62"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-17","Item Tax Amount":"3.62"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-17","Item Tax Amount":"10.87"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-17","Item Amount":"53.05"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-18","Item Amount":"147.67"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-18","Item Tax Amount":"3.11"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-18","Item Tax Amount":"9.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-18","Item Amount":"34.69"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Kansas City Plaza' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Kansas City Plaza' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_83(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Hartford Airport','MerchantAddress':'551 Turner St, Hartford, CT 39989, USA','TransactionDate':'2024-05-07',,'Total':'296.64','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to Pasadena for quarterly reviews. Attended Blockchain Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-06","Item Amount":"169.79"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-06","Item Tax Amount":"5.01"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-06","Item Tax Amount":"15.03"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-05-06","Item Amount":"59.84"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-05-06","Item Amount":"21.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-06","Item Amount":"25.84"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Hartford Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Hartford Airport' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_84(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Naperville Promenade Bolingbrook','MerchantAddress':'653 Airport Blvd, Naperville, IL 48161, USA','TransactionDate':'2019-07-20',,'Total':'1307.41','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Corporate trip - Customer Experience Summit conference in Orlando. compliance training and audits over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-07-17","Item Amount":"338.55"},{"Item Name":"Hotel Tax","Transaction Date":"2019-07-17","Item Tax Amount":"22.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-07-17","Item Amount":"61.51"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-07-18","Item Amount":"344.67"},{"Item Name":"Hotel Tax","Transaction Date":"2019-07-18","Item Tax Amount":"22.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-07-18","Item Amount":"73.19"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-07-19","Item Amount":"344.85"},{"Item Name":"Hotel Tax","Transaction Date":"2019-07-19","Item Tax Amount":"22.59"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-07-19","Item Amount":"13.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-07-19","Item Amount":"63.90"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Naperville Promenade Bolingbrook' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Naperville Promenade Bolingbrook' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_85(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Sioux Falls Empire Mall','MerchantAddress':'212 Pine St, Sioux Falls, SD 82037, USA','TransactionDate':'2019-09-07',,'Total':'360.68','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Corporate trip - Retail Innovation Conference conference in Mesa. team building and training sessions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-05","Item Amount":"110.77"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-05","Item Tax Amount":"5.98"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-05","Item Amount":"92.34"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-06","Item Amount":"74.54"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-06","Item Tax Amount":"4.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-06","Item Amount":"73.02"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Sioux Falls Empire Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Sioux Falls Empire Mall' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_86(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Boston Beacon Hill','MerchantAddress':'914 Madison Ave, Boston, MA 58973, USA','TransactionDate':'2021-02-18',,'Total':'328.28','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Energy Sector Conference conference in Oxnard. customer support and service reviews over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-16","Item Amount":"58.16"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-16","Item Tax Amount":"3.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-16","Item Tax Amount":"1.22"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-16","Item Tax Amount":"1.22"},{"Item Name":"Entertainment External","Transaction Date":"2021-02-16","Item Amount":"45.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-16","Item Amount":"40.02"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-17","Item Amount":"80.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-17","Item Tax Amount":"5.03"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-17","Item Tax Amount":"1.68"},{"Item Name":"Incidentals","Transaction Date":"2021-02-17","Item Amount":"43.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-17","Item Amount":"48.85"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Boston Beacon Hill' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Boston Beacon Hill' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_87(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Fort Worth Downtown','MerchantAddress':'729 Spring St, Fort Worth, TX 27439, USA','TransactionDate':'2024-03-13',,'Total':'790.81','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - DevOps World conference in Dallas. market research and competitive analysis over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-11","Item Amount":"279.30"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-11","Item Tax Amount":"5.69"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-11","Item Tax Amount":"5.69"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-11","Item Tax Amount":"17.08"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-11","Item Amount":"74.32"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-12","Item Amount":"282.53"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-12","Item Tax Amount":"5.76"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-12","Item Tax Amount":"5.76"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-12","Item Tax Amount":"17.28"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-03-12","Item Amount":"24.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-12","Item Amount":"72.93"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Fort Worth Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Fort Worth Downtown' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_88(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Santa Ana South Coast Plaza','MerchantAddress':'208 Lee Ave, Santa Ana, CA 33006, USA','TransactionDate':'2024-03-05',,'Total':'367.38','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Real Estate Investment Summit conference in Houston. team building and training sessions over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-02","Item Amount":"104.17"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-02","Item Tax Amount":"6.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-02","Item Amount":"33.71"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-03","Item Amount":"73.75"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-03","Item Tax Amount":"4.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-03","Item Amount":"24.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-04","Item Amount":"84.47"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-04","Item Tax Amount":"5.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-04","Item Amount":"29.19"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Santa Ana South Coast Plaza' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Santa Ana South Coast Plaza' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_89(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Des Moines West Des Moines','MerchantAddress':'267 Parker Dr, Des Moines, IA 85577, USA','TransactionDate':'2024-01-22',,'Total':'649.44','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'KY','Description':'Business travel to Lexington for DevOps World. 2 nights stay for client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-20","Item Amount":"150.47"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-20","Item Tax Amount":"10.03"},{"Item Name":"Laundry","Transaction Date":"2024-01-20","Item Amount":"39.26"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-20","Item Amount":"40.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-21","Item Amount":"154.28"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-21","Item Tax Amount":"10.28"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-01-21","Item Amount":"198.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-21","Item Amount":"46.18"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Des Moines West Des Moines' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Des Moines West Des Moines' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_90(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Victorville Mall of Victor Valley','MerchantAddress':'863 Union St, Victorville, CA 70786, USA','TransactionDate':'2020-09-27',,'Total':'771.31','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Pembroke Pines for HR Leadership Summit. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-25","Item Amount":"269.54"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-25","Item Tax Amount":"22.46"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-09-25","Item Amount":"24.40"},{"Item Name":"Incidentals","Transaction Date":"2020-09-25","Item Amount":"22.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-25","Item Amount":"71.67"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-26","Item Amount":"265.45"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-26","Item Tax Amount":"22.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-26","Item Amount":"73.25"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Victorville Mall of Victor Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Victorville Mall of Victor Valley' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_91(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Jersey City Downtown','MerchantAddress':'678 Cruz St, Jersey City, NJ 44968, USA','TransactionDate':'2025-01-15',,'Total':'245.15','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IA','Description':'Corporate trip - Quality Assurance Conference conference in Cedar Rapids. product demos and customer meetings over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-14","Item Amount":"118.30"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-14","Item Tax Amount":"7.09"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-14","Item Tax Amount":"10.63"},{"Item Name":"Entertainment External","Transaction Date":"2025-01-14","Item Amount":"77.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-14","Item Amount":"31.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Jersey City Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Jersey City Downtown' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_92(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Irvine John Wayne Airport','MerchantAddress':'586 Diaz St, Irvine, CA 86779, USA','TransactionDate':'2022-08-06',,'Total':'770.95','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Business travel to Kent for Digital Transformation Summit. 2 nights stay for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-04","Item Amount":"274.67"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-04","Item Tax Amount":"13.93"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-04","Item Tax Amount":"20.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-04","Item Amount":"67.00"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-05","Item Amount":"282.12"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-05","Item Tax Amount":"14.30"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-05","Item Tax Amount":"21.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-05","Item Amount":"76.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Irvine John Wayne Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Irvine John Wayne Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_93(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Brownsville Airport','MerchantAddress':'638 Edwards Ave, Brownsville, TX 30128, USA','TransactionDate':'2023-07-05',,'Total':'970','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CT','Description':'Business travel to New Haven for Customer Experience Summit. 2 nights stay for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-03","Item Amount":"398.40"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-03","Item Tax Amount":"34.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-03","Item Amount":"61.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-04","Item Amount":"386.49"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-04","Item Tax Amount":"33.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-04","Item Amount":"55.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Brownsville Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Brownsville Airport' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_94(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Bellevue Crossroads','MerchantAddress':'991 Cedar Ave, Bellevue, WA 57895, USA','TransactionDate':'2023-12-30',,'Total':'643.06','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NE','Description':'Company business trip - Attended Manufacturing Excellence Summit in Lincoln. 3 business nights; team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-27","Item Amount":"133.52"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-27","Item Tax Amount":"6.62"},{"Item Name":"Laundry","Transaction Date":"2023-12-27","Item Amount":"29.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-27","Item Amount":"53.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-28","Item Amount":"104.21"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-28","Item Tax Amount":"5.16"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-12-28","Item Amount":"22.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-28","Item Amount":"70.04"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-29","Item Amount":"135.38"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-29","Item Tax Amount":"6.71"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-12-29","Item Amount":"11.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-29","Item Amount":"64.50"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Bellevue Crossroads' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Bellevue Crossroads' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_95(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Cleveland Downtown','MerchantAddress':'596 Miller Blvd, Cleveland, OH 97648, USA','TransactionDate':'2024-05-16',,'Total':'1180.74','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - E-commerce Summit in Oceanside. 4 business nights for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-12","Item Amount":"223.26"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-12","Item Tax Amount":"16.99"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-12","Item Amount":"35.82"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-13","Item Amount":"230.34"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-13","Item Tax Amount":"17.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-13","Item Amount":"38.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-14","Item Amount":"252.10"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-14","Item Tax Amount":"19.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-14","Item Amount":"32.61"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-15","Item Amount":"257.28"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-15","Item Tax Amount":"19.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-15","Item Amount":"37.71"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Cleveland Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Cleveland Downtown' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_96(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Lexington Airport','MerchantAddress':'882 Brown Ave, Lexington, KY 74642, USA','TransactionDate':'2023-09-01',,'Total':'1751.47','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AR','Description':'Company business trip - Attended Analytics Leadership Summit in Little Rock. 4 business nights; client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-28","Item Amount":"326.20"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-28","Item Tax Amount":"22.30"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-28","Item Tax Amount":"14.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-28","Item Amount":"58.60"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-29","Item Amount":"338.02"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-29","Item Tax Amount":"23.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-29","Item Tax Amount":"15.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-29","Item Amount":"58.06"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-30","Item Amount":"348.90"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-30","Item Tax Amount":"23.85"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-30","Item Tax Amount":"15.90"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-30","Item Amount":"68.69"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-31","Item Amount":"322.61"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-31","Item Tax Amount":"22.05"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-31","Item Tax Amount":"14.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-31","Item Amount":"78.23"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Lexington Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Lexington Airport' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_97(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Overland Park Metcalf','MerchantAddress':'204 Myers St, Overland Park, KS 41652, USA','TransactionDate':'2019-11-24',,'Total':'646.73','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'KY','Description':'Business travel to Louisville for Digital Transformation Summit. 4 nights stay for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-20","Item Amount":"114.03"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-20","Item Tax Amount":"7.16"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-20","Item Tax Amount":"2.39"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-20","Item Tax Amount":"2.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-20","Item Amount":"29.34"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-21","Item Amount":"80.58"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-21","Item Tax Amount":"5.06"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-21","Item Tax Amount":"1.69"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-21","Item Tax Amount":"1.69"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-11-21","Item Amount":"62.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-21","Item Amount":"29.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-22","Item Amount":"77.67"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-22","Item Tax Amount":"4.88"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-22","Item Tax Amount":"1.63"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-22","Item Tax Amount":"1.63"},{"Item Name":"Incidentals","Transaction Date":"2019-11-22","Item Amount":"31.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-22","Item Amount":"33.95"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-23","Item Amount":"85.08"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"5.35"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"1.78"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"1.78"},{"Item Name":"Entertainment External","Transaction Date":"2019-11-23","Item Amount":"22.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-23","Item Amount":"42.10"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Overland Park Metcalf' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Overland Park Metcalf' have all 23 required itemizations'?,",
#     )


# def test_expense_hotel_98(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Rancho Cucamonga Airport','MerchantAddress':'627 Church St, Rancho Cucamonga, CA 52754, USA','TransactionDate':'2020-04-18',,'Total':'384.02','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Corporate trip - Energy Sector Conference conference in Cincinnati. market research and competitive analysis over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-17","Item Amount":"283.48"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-17","Item Tax Amount":"23.33"},{"Item Name":"Incidentals","Transaction Date":"2020-04-17","Item Amount":"30.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-17","Item Amount":"33.42"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-04-18","Item Amount":"13.09"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Rancho Cucamonga Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Rancho Cucamonga Airport' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_99(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Oakland Airport','MerchantAddress':'732 Brooks Ave, Oakland, CA 74306, USA','TransactionDate':'2021-12-10',,'Total':'395.49','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AL','Description':'Business trip to Huntsville for partnership development. Attended FinTech Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-08","Item Amount":"122.36"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-08","Item Tax Amount":"10.59"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-08","Item Tax Amount":"3.53"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-12-08","Item Amount":"11.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-08","Item Amount":"39.55"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-09","Item Amount":"106.86"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-09","Item Tax Amount":"9.24"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-09","Item Tax Amount":"3.08"},{"Item Name":"Incidentals","Transaction Date":"2021-12-09","Item Amount":"42.11"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-09","Item Amount":"47.01"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Oakland Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Oakland Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_100(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Orange Old Town Orange','MerchantAddress':'556 Roosevelt Way, Orange, CA 74355, USA','TransactionDate':'2022-10-06',,'Total':'159.48','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company business trip - Attended Analytics Leadership Summit in Orlando. 1 business night; operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-05","Item Amount":"106.21"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-05","Item Tax Amount":"5.59"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-05","Item Tax Amount":"1.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-05","Item Amount":"27.02"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-10-06","Item Amount":"18.80"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Orange Old Town Orange' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Orange Old Town Orange' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_101(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Santa Clarita Valencia','MerchantAddress':'690 Smith St, Santa Clarita, CA 95606, USA','TransactionDate':'2023-05-01',,'Total':'897.29','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company travel - Business Intelligence Summit in Clarksville. 3 business nights for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-28","Item Amount":"202.32"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-28","Item Tax Amount":"12.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-28","Item Amount":"37.82"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-29","Item Amount":"188.75"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-29","Item Tax Amount":"11.70"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-04-29","Item Amount":"28.94"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-04-29","Item Amount":"141.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-29","Item Amount":"16.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-30","Item Amount":"198.93"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-30","Item Tax Amount":"12.33"},{"Item Name":"Incidentals","Transaction Date":"2023-04-30","Item Amount":"29.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-30","Item Amount":"16.48"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Santa Clarita Valencia' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Santa Clarita Valencia' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_102(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Mesa Superstition','MerchantAddress':'362 Long Ave, Mesa, AZ 85788, USA','TransactionDate':'2019-10-14',,'Total':'243.19','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IN','Description':'Company business trip - Attended Blockchain Conference in Fort Wayne. 1 business night; stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-13","Item Amount":"161.06"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-13","Item Tax Amount":"11.00"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-10-13","Item Amount":"7.64"},{"Item Name":"Incidentals","Transaction Date":"2019-10-13","Item Amount":"20.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-13","Item Amount":"43.31"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Mesa Superstition' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Mesa Superstition' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_103(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Woodbridge Airport','MerchantAddress':'385 Reyes Dr, Woodbridge, NJ 43503, USA','TransactionDate':'2024-04-21',,'Total':'775.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Company travel - Quality Assurance Conference in Cary. 2 business nights for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-19","Item Amount":"272.53"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-19","Item Tax Amount":"23.38"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-04-19","Item Amount":"32.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-19","Item Amount":"52.85"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-20","Item Amount":"263.06"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-20","Item Tax Amount":"22.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-20","Item Amount":"60.84"},{"Item Name":"Incidentals","Transaction Date":"2024-04-20","Item Amount":"48.48"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Woodbridge Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Woodbridge Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_104(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Syracuse University Hill','MerchantAddress':'792 Butler St, Syracuse, NY 33804, USA','TransactionDate':'2021-04-08',,'Total':'333.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Company travel - Sales Leadership Conference in Buffalo. 1 business night for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-07","Item Amount":"138.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-07","Item Tax Amount":"6.82"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-07","Item Tax Amount":"10.23"},{"Item Name":"Entertainment External","Transaction Date":"2021-04-07","Item Amount":"101.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-07","Item Amount":"76.32"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Syracuse University Hill' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Syracuse University Hill' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_105(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Madison University','MerchantAddress':'526 Madison Ave, Madison, WI 50484, USA','TransactionDate':'2022-01-25',,'Total':'1324.34','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Business travel to St. Paul for Legal Technology Conference. 4 nights stay for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-21","Item Amount":"183.32"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-21","Item Tax Amount":"6.19"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-21","Item Tax Amount":"9.28"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-01-21","Item Amount":"198.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-21","Item Amount":"63.76"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-22","Item Amount":"198.66"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-22","Item Tax Amount":"6.70"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-22","Item Tax Amount":"10.06"},{"Item Name":"Laundry","Transaction Date":"2022-01-22","Item Amount":"18.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-22","Item Amount":"68.93"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-23","Item Amount":"197.53"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-23","Item Tax Amount":"6.67"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-23","Item Tax Amount":"10.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-23","Item Amount":"50.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-24","Item Amount":"192.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-24","Item Tax Amount":"6.50"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-24","Item Tax Amount":"9.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-24","Item Amount":"63.37"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-01-25","Item Amount":"23.54"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Madison University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Madison University' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_106(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Lubbock Tech Terrace','MerchantAddress':'751 Martin Dr, Lubbock, TX 39544, USA','TransactionDate':'2021-11-14',,'Total':'911.87','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Corona for strategic planning. Attended Change Management Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-10","Item Amount":"139.51"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-10","Item Tax Amount":"7.85"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-10","Item Tax Amount":"5.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-10","Item Amount":"57.10"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-11","Item Amount":"129.17"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-11","Item Tax Amount":"7.27"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-11","Item Tax Amount":"4.85"},{"Item Name":"Entertainment External","Transaction Date":"2021-11-11","Item Amount":"54.92"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-11-11","Item Amount":"10.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-11","Item Amount":"66.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-12","Item Amount":"152.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-12","Item Tax Amount":"8.61"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-12","Item Tax Amount":"5.74"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-12","Item Amount":"56.44"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-13","Item Amount":"135.80"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-13","Item Tax Amount":"7.64"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-13","Item Tax Amount":"5.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-13","Item Amount":"56.87"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Lubbock Tech Terrace' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Lubbock Tech Terrace' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_107(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Chula Vista Eastlake','MerchantAddress':'850 Thomas St, Chula Vista, CA 35501, USA','TransactionDate':'2020-08-15',,'Total':'1074.22','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company travel - E-commerce Summit in Clearwater. 2 business nights for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-08-13","Item Amount":"326.40"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-13","Item Tax Amount":"18.87"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-13","Item Tax Amount":"28.31"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-08-13","Item Amount":"56.31"},{"Item Name":"Laundry","Transaction Date":"2020-08-13","Item Amount":"21.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-08-13","Item Amount":"107.48"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-08-14","Item Amount":"342.91"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-14","Item Tax Amount":"19.83"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-14","Item Tax Amount":"29.74"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-08-14","Item Amount":"18.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-08-14","Item Amount":"104.09"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Chula Vista Eastlake' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Chula Vista Eastlake' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_108(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Dallas DFW Airport','MerchantAddress':'527 Cox Blvd, Dallas, TX 47388, USA','TransactionDate':'2020-07-04',,'Total':'967.81','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Business trip to Fayetteville for market expansion. Attended IoT Solutions Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-02","Item Amount":"319.15"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-02","Item Tax Amount":"25.40"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-02","Item Tax Amount":"16.93"},{"Item Name":"Entertainment External","Transaction Date":"2020-07-02","Item Amount":"132.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-02","Item Amount":"31.58"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-03","Item Amount":"341.00"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-03","Item Tax Amount":"27.14"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-03","Item Tax Amount":"18.09"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-07-03","Item Amount":"18.84"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-03","Item Amount":"37.14"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Dallas DFW Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Dallas DFW Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_109(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Henderson Airport Area','MerchantAddress':'718 Myers St, Henderson, NV 24432, USA','TransactionDate':'2021-11-14',,'Total':'1079.28','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Company travel - Change Management Conference in Lakewood. 4 business nights for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-10","Item Amount":"170.49"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-10","Item Tax Amount":"11.41"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-11-10","Item Amount":"20.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-10","Item Amount":"77.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-11","Item Amount":"181.85"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-11","Item Tax Amount":"12.17"},{"Item Name":"Incidentals","Transaction Date":"2021-11-11","Item Amount":"14.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-11","Item Amount":"87.14"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-12","Item Amount":"167.05"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-12","Item Tax Amount":"11.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-12","Item Amount":"80.88"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-13","Item Amount":"154.17"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-13","Item Tax Amount":"10.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-13","Item Amount":"80.38"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Henderson Airport Area' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Henderson Airport Area' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_110(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Vancouver Airport','MerchantAddress':'516 Cook Blvd, Vancouver, WA 20720, USA','TransactionDate':'2024-05-30',,'Total':'788.29','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Palmdale for IoT Solutions Summit. 2 nights stay for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-28","Item Amount":"264.61"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-28","Item Tax Amount":"17.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-28","Item Amount":"85.39"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-29","Item Amount":"254.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-29","Item Tax Amount":"16.78"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-05-29","Item Amount":"42.87"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-29","Item Amount":"78.20"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-05-30","Item Amount":"28.54"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Vancouver Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Vancouver Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_111(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Cape Coral Pine Island','MerchantAddress':'685 Second Ave, Cape Coral, FL 40144, USA','TransactionDate':'2025-11-18',,'Total':'529.33','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'VA','Description':'Corporate trip - Energy Sector Conference conference in Virginia Beach. customer support and service reviews over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-15","Item Amount":"90.77"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-15","Item Tax Amount":"5.05"},{"Item Name":"Hotel Telephone","Transaction Date":"2025-11-15","Item Amount":"9.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-15","Item Amount":"88.09"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-16","Item Amount":"74.28"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-16","Item Tax Amount":"4.14"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-16","Item Amount":"81.50"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-17","Item Amount":"75.25"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-17","Item Tax Amount":"4.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-17","Item Amount":"73.54"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-11-18","Item Amount":"23.42"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Cape Coral Pine Island' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Cape Coral Pine Island' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_112(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Alexandria Del Ray','MerchantAddress':'633 Commerce St, Alexandria, VA 73805, USA','TransactionDate':'2020-02-11',,'Total':'537.84','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CT','Description':'Business trip to New Haven for market expansion. Attended Sales Leadership Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-09","Item Amount":"153.82"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-09","Item Tax Amount":"12.01"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-09","Item Amount":"47.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-10","Item Amount":"141.37"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-10","Item Tax Amount":"11.04"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-02-10","Item Amount":"46.11"},{"Item Name":"Incidentals","Transaction Date":"2020-02-10","Item Amount":"39.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-10","Item Amount":"69.72"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-02-11","Item Amount":"16.08"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Alexandria Del Ray' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Alexandria Del Ray' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_113(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Killeen Airport','MerchantAddress':'934 Second Ave, Killeen, TX 62855, USA','TransactionDate':'2021-12-28',,'Total':'348.98','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company business trip - Attended Healthcare IT Summit in Nashville. 2 business nights; operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-26","Item Amount":"107.12"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-26","Item Tax Amount":"6.41"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-26","Item Tax Amount":"9.61"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-26","Item Amount":"43.70"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-27","Item Amount":"110.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-27","Item Tax Amount":"6.58"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-27","Item Tax Amount":"9.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-27","Item Amount":"55.58"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Killeen Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Killeen Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_114(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Augusta Hill Acres','MerchantAddress':'385 Thompson Ave, Augusta, GA 98153, USA','TransactionDate':'2020-07-26',,'Total':'996.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Business travel to West Jordan for Sales Leadership Conference. 4 nights stay for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-22","Item Amount":"205.20"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-22","Item Tax Amount":"11.13"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-22","Item Tax Amount":"16.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-22","Item Amount":"29.69"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-23","Item Amount":"199.18"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-23","Item Tax Amount":"10.81"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-23","Item Tax Amount":"16.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-23","Item Amount":"35.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-24","Item Amount":"174.50"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-24","Item Tax Amount":"9.47"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-24","Item Tax Amount":"14.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-24","Item Amount":"41.65"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-25","Item Amount":"177.93"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-25","Item Tax Amount":"9.65"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-25","Item Tax Amount":"14.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-25","Item Amount":"30.48"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Augusta Hill Acres' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Augusta Hill Acres' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_115(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Santa Clara Mission College','MerchantAddress':'618 Madison Ave, Santa Clara, CA 44171, USA','TransactionDate':'2025-11-20',,'Total':'571.29','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - HR Leadership Summit in Fairfield. 2 business nights for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-18","Item Amount":"227.44"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-18","Item Tax Amount":"13.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-18","Item Amount":"42.94"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-19","Item Amount":"232.46"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-19","Item Tax Amount":"13.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-19","Item Amount":"42.12"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Santa Clara Mission College' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Santa Clara Mission College' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_116(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Birmingham Airport','MerchantAddress':'226 Garcia St, Birmingham, AL 97957, USA','TransactionDate':'2019-04-19',,'Total':'352.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Business trip to Yonkers for product launch. Attended Mobile Technology Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-18","Item Amount":"277.38"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-18","Item Tax Amount":"24.94"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-18","Item Tax Amount":"8.31"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-18","Item Tax Amount":"8.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-18","Item Amount":"33.26"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Birmingham Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Birmingham Airport' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_117(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Provo Orem','MerchantAddress':'610 Lewis Ave, Provo, UT 73455, USA','TransactionDate':'2020-02-23',,'Total':'555.19','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to McAllen for Legal Technology Conference. 4 nights stay for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-19","Item Amount":"85.47"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-19","Item Tax Amount":"1.94"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-19","Item Tax Amount":"5.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-19","Item Amount":"32.06"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-20","Item Amount":"90.45"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-20","Item Tax Amount":"2.05"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-20","Item Tax Amount":"6.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-20","Item Amount":"29.74"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-21","Item Amount":"97.58"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-21","Item Tax Amount":"2.21"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-21","Item Tax Amount":"6.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-21","Item Amount":"24.75"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-22","Item Amount":"109.08"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-22","Item Tax Amount":"2.47"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-22","Item Tax Amount":"2.47"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-22","Item Tax Amount":"7.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-22","Item Amount":"20.80"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-02-23","Item Amount":"28.10"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Provo Orem' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Provo Orem' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_118(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Phoenix Scottsdale','MerchantAddress':'934 Richardson Ave, Phoenix, AZ 75827, USA','TransactionDate':'2019-08-21',,'Total':'1527.76','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Business trip to Sterling Heights for market expansion. Attended DevOps World. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-18","Item Amount":"349.98"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-18","Item Tax Amount":"23.91"},{"Item Name":"Incidentals","Transaction Date":"2019-08-18","Item Amount":"41.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-18","Item Amount":"88.71"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-19","Item Amount":"354.59"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-19","Item Tax Amount":"24.22"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-08-19","Item Amount":"67.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-19","Item Amount":"103.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-20","Item Amount":"362.36"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-20","Item Tax Amount":"24.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-20","Item Amount":"86.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Phoenix Scottsdale' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Phoenix Scottsdale' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_119(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Carrollton Downtown','MerchantAddress':'217 Davis St, Carrollton, TX 65202, USA','TransactionDate':'2023-02-22',,'Total':'724.86','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MO','Description':'Company business trip - Attended Energy Sector Conference in St. Louis. 4 business nights; merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-02-18","Item Amount":"70.70"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-18","Item Tax Amount":"2.02"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-18","Item Tax Amount":"6.07"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-02-18","Item Amount":"12.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-02-18","Item Amount":"77.17"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-02-19","Item Amount":"84.99"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-19","Item Tax Amount":"2.43"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-19","Item Tax Amount":"2.43"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-19","Item Tax Amount":"7.29"},{"Item Name":"Incidentals","Transaction Date":"2023-02-19","Item Amount":"25.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-02-19","Item Amount":"65.21"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-02-20","Item Amount":"83.83"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-20","Item Tax Amount":"2.40"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-20","Item Tax Amount":"2.40"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-20","Item Tax Amount":"7.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-02-20","Item Amount":"78.17"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-02-21","Item Amount":"102.13"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-21","Item Tax Amount":"2.92"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-21","Item Tax Amount":"8.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-02-21","Item Amount":"80.80"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Carrollton Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Carrollton Downtown' have all 20 required itemizations'?,",
#     )


# def test_expense_hotel_120(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Cleveland Ohio City','MerchantAddress':'349 Ward Ave, Cleveland, OH 16240, USA','TransactionDate':'2019-11-25',,'Total':'1098.63','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - IoT Solutions Summit in Long Beach. 3 business nights for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-22","Item Amount":"205.35"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-22","Item Tax Amount":"13.52"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-22","Item Tax Amount":"4.51"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-22","Item Tax Amount":"4.51"},{"Item Name":"Hotel Deposit","Transaction Date":"2019-11-22","Item Amount":"140.59"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-11-22","Item Amount":"8.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-22","Item Amount":"70.51"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-23","Item Amount":"207.52"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"13.66"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"4.55"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"4.55"},{"Item Name":"Entertainment External","Transaction Date":"2019-11-23","Item Amount":"68.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-23","Item Amount":"58.82"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-24","Item Amount":"206.15"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-24","Item Tax Amount":"13.57"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-24","Item Tax Amount":"4.52"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-24","Item Tax Amount":"4.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-24","Item Amount":"64.88"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Cleveland Ohio City' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Cleveland Ohio City' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_121(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Santa Ana Downtown','MerchantAddress':'508 School St, Santa Ana, CA 83437, USA','TransactionDate':'2019-10-07',,'Total':'726.13','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Business trip to Baton Rouge for technology implementation. Attended FinTech Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-04","Item Amount":"143.65"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-04","Item Tax Amount":"3.56"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-04","Item Tax Amount":"10.67"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-04","Item Tax Amount":"3.56"},{"Item Name":"Entertainment External","Transaction Date":"2019-10-04","Item Amount":"36.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-04","Item Amount":"65.45"},{"Item Name":"Incidentals","Transaction Date":"2019-10-04","Item Amount":"49.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-05","Item Amount":"120.24"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-05","Item Tax Amount":"8.93"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-05","Item Tax Amount":"2.98"},{"Item Name":"Hotel Breakfast","Transaction Date":"2019-10-05","Item Amount":"21.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-05","Item Amount":"67.51"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-06","Item Amount":"117.50"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-06","Item Tax Amount":"8.73"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-06","Item Tax Amount":"2.91"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-06","Item Amount":"61.78"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Santa Ana Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Santa Ana Downtown' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_122(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Vancouver Riverfront','MerchantAddress':'889 Kelly Dr, Vancouver, WA 94127, USA','TransactionDate':'2022-11-18',,'Total':'271.71','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Healthcare IT Summit in Fremont. 1 business night for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-17","Item Amount":"149.29"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-17","Item Tax Amount":"9.49"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-17","Item Tax Amount":"6.33"},{"Item Name":"Incidentals","Transaction Date":"2022-11-17","Item Amount":"40.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-17","Item Amount":"65.96"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Vancouver Riverfront' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Vancouver Riverfront' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_123(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Cincinnati Hyde Park','MerchantAddress':'925 Richardson Ave, Cincinnati, OH 74656, USA','TransactionDate':'2022-11-16',,'Total':'439.69','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company travel - Product Management Summit in Clarksville. 2 business nights for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-14","Item Amount":"137.22"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-14","Item Tax Amount":"2.24"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-14","Item Tax Amount":"6.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-14","Item Amount":"36.46"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-15","Item Amount":"119.09"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-15","Item Tax Amount":"1.94"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-15","Item Tax Amount":"5.83"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-11-15","Item Amount":"44.13"},{"Item Name":"Laundry","Transaction Date":"2022-11-15","Item Amount":"21.35"},{"Item Name":"Incidentals","Transaction Date":"2022-11-15","Item Amount":"20.11"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-15","Item Amount":"44.60"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Cincinnati Hyde Park' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Cincinnati Hyde Park' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_124(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Carrollton Town Square','MerchantAddress':'255 James Ave, Carrollton, TX 61317, USA','TransactionDate':'2023-06-17',,'Total':'948.23','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Business trip to Durham for sales presentations. Attended Digital Marketing Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-14","Item Amount":"240.38"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-14","Item Tax Amount":"15.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-14","Item Amount":"69.90"},{"Item Name":"Incidentals","Transaction Date":"2023-06-14","Item Amount":"19.09"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-15","Item Amount":"206.82"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-15","Item Tax Amount":"13.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-15","Item Amount":"57.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-16","Item Amount":"240.52"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-16","Item Tax Amount":"15.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-16","Item Amount":"68.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Carrollton Town Square' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Carrollton Town Square' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_125(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Little Rock River Market','MerchantAddress':'985 Wilson Way, Little Rock, AR 90000, USA','TransactionDate':'2019-12-09',,'Total':'719.81','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company business trip - Attended Customer Experience Summit in Davie. 3 business nights; client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-06","Item Amount":"185.20"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-06","Item Tax Amount":"14.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-06","Item Amount":"36.47"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-07","Item Amount":"182.76"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-07","Item Tax Amount":"14.04"},{"Item Name":"Incidentals","Transaction Date":"2019-12-07","Item Amount":"12.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-07","Item Amount":"38.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-08","Item Amount":"182.20"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-08","Item Tax Amount":"14.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-08","Item Amount":"39.80"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Little Rock River Market' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Little Rock River Market' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_126(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Chicago River North','MerchantAddress':'946 Morgan Ave, Chicago, IL 76737, USA','TransactionDate':'2024-01-21',,'Total':'1035.91','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'GA','Description':'Corporate trip - Product Management Summit conference in Atlanta. board meetings and investor presentations over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-18","Item Amount":"227.10"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-18","Item Tax Amount":"12.35"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-01-18","Item Amount":"182.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-18","Item Amount":"35.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-19","Item Amount":"225.40"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-19","Item Tax Amount":"12.26"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-19","Item Amount":"17.03"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-20","Item Amount":"223.03"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-20","Item Tax Amount":"12.13"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-01-20","Item Amount":"71.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-20","Item Amount":"16.48"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Chicago River North' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Chicago River North' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_127(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Pomona Airport','MerchantAddress':'863 Hill Ave, Pomona, CA 25289, USA','TransactionDate':'2019-10-20',,'Total':'1110.12','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Clearwater for HR Leadership Summit. 4 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-16","Item Amount":"186.32"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-16","Item Tax Amount":"16.38"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-16","Item Tax Amount":"5.46"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-16","Item Tax Amount":"5.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-16","Item Amount":"23.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-17","Item Amount":"191.08"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-17","Item Tax Amount":"16.80"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-17","Item Tax Amount":"5.60"},{"Item Name":"Hotel Deposit","Transaction Date":"2019-10-17","Item Amount":"118.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-17","Item Amount":"25.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-18","Item Amount":"182.52"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-18","Item Tax Amount":"16.04"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-18","Item Tax Amount":"5.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-18","Item Amount":"29.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-19","Item Amount":"187.43"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-19","Item Tax Amount":"16.48"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-19","Item Tax Amount":"5.49"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-19","Item Tax Amount":"5.49"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-10-19","Item Amount":"46.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-19","Item Amount":"21.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Pomona Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Pomona Airport' have all 20 required itemizations'?,",
#     )


# def test_expense_hotel_128(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Oceanside Camp Pendleton','MerchantAddress':'431 Moore St, Oceanside, CA 63229, USA','TransactionDate':'2024-06-17',,'Total':'703.13','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'VA','Description':'Company business trip - Attended Manufacturing Excellence Summit in Virginia Beach. 4 business nights; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-13","Item Amount":"111.50"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-13","Item Tax Amount":"8.74"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-13","Item Amount":"59.09"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-14","Item Amount":"109.77"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-14","Item Tax Amount":"8.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-14","Item Amount":"65.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-15","Item Amount":"96.35"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-15","Item Tax Amount":"7.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-15","Item Amount":"57.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-16","Item Amount":"111.11"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-16","Item Tax Amount":"8.71"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-16","Item Amount":"57.94"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Oceanside Camp Pendleton' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Oceanside Camp Pendleton' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_129(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Midland University','MerchantAddress':'700 Reyes Dr, Midland, TX 37177, USA','TransactionDate':'2022-05-22',,'Total':'505.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company travel - Business Intelligence Summit in Tallahassee. 1 business night for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-21","Item Amount":"171.39"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-21","Item Tax Amount":"12.50"},{"Item Name":"Entertainment External","Transaction Date":"2022-05-21","Item Amount":"30.88"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-05-21","Item Amount":"192.46"},{"Item Name":"Laundry","Transaction Date":"2022-05-21","Item Amount":"36.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-21","Item Amount":"61.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Midland University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Midland University' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_130(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Rancho Cucamonga Victoria Gardens','MerchantAddress':'952 Bennett Blvd, Rancho Cucamonga, CA 83699, USA','TransactionDate':'2025-03-04',,'Total':'388.74','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'KS','Description':'Business trip to Kansas City for quarterly reviews. Attended Corporate Strategy Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-03-03","Item Amount":"272.89"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-03","Item Tax Amount":"13.19"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-03","Item Tax Amount":"4.40"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-03","Item Tax Amount":"4.40"},{"Item Name":"Hotel Telephone","Transaction Date":"2025-03-03","Item Amount":"10.67"},{"Item Name":"Incidentals","Transaction Date":"2025-03-03","Item Amount":"46.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-03-03","Item Amount":"37.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Rancho Cucamonga Victoria Gardens' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Rancho Cucamonga Victoria Gardens' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_131(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Omaha Old Market','MerchantAddress':'914 Wright Ave, Omaha, NE 44255, USA','TransactionDate':'2019-08-21',,'Total':'1923.85','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Irving for DevOps World. 4 nights stay for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-17","Item Amount":"358.50"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-17","Item Tax Amount":"9.48"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-17","Item Tax Amount":"28.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-17","Item Amount":"32.71"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-18","Item Amount":"360.31"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-18","Item Tax Amount":"9.53"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-18","Item Tax Amount":"9.53"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-18","Item Tax Amount":"28.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-18","Item Amount":"34.42"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-19","Item Amount":"385.79"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-19","Item Tax Amount":"10.20"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-19","Item Tax Amount":"10.20"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-19","Item Tax Amount":"30.60"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-08-19","Item Amount":"20.77"},{"Item Name":"Incidentals","Transaction Date":"2019-08-19","Item Amount":"19.98"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-19","Item Amount":"35.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-20","Item Amount":"357.85"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-20","Item Tax Amount":"9.46"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-20","Item Tax Amount":"28.38"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-08-20","Item Amount":"112.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-20","Item Amount":"31.22"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Omaha Old Market' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Omaha Old Market' have all 21 required itemizations'?,",
#     )


# def test_expense_hotel_132(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Jersey City Newport','MerchantAddress':'872 Airport Blvd, Jersey City, NJ 81031, USA','TransactionDate':'2021-05-10',,'Total':'1147.31','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Retail Innovation Conference in Bakersfield. 4 business nights for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-06","Item Amount":"187.12"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-06","Item Tax Amount":"15.14"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-06","Item Tax Amount":"5.05"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-06","Item Tax Amount":"5.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-06","Item Amount":"55.92"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-07","Item Amount":"156.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-07","Item Tax Amount":"12.68"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-07","Item Tax Amount":"4.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-07","Item Amount":"63.97"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-08","Item Amount":"156.62"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-08","Item Tax Amount":"12.67"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-08","Item Tax Amount":"4.22"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-08","Item Tax Amount":"4.22"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-05-08","Item Amount":"168.87"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-08","Item Amount":"45.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-09","Item Amount":"172.56"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-09","Item Tax Amount":"13.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-09","Item Tax Amount":"4.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-09","Item Tax Amount":"4.65"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-05-09","Item Amount":"8.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-09","Item Amount":"45.65"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Jersey City Newport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Jersey City Newport' have all 21 required itemizations'?,",
#     )


# def test_expense_hotel_133(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Coral Springs University Drive','MerchantAddress':'616 Lincoln Blvd, Coral Springs, FL 55595, USA','TransactionDate':'2022-02-20',,'Total':'805.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Blockchain Conference in Killeen. 2 business nights; team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-18","Item Amount":"191.83"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-18","Item Tax Amount":"5.56"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-18","Item Tax Amount":"5.56"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-18","Item Tax Amount":"16.67"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-02-18","Item Amount":"185.65"},{"Item Name":"Laundry","Transaction Date":"2022-02-18","Item Amount":"20.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-18","Item Amount":"66.99"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-19","Item Amount":"218.20"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-19","Item Tax Amount":"6.32"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-19","Item Tax Amount":"6.32"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-19","Item Tax Amount":"18.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-19","Item Amount":"63.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Coral Springs University Drive' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Coral Springs University Drive' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_134(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Tallahassee Downtown','MerchantAddress':'939 Barnes Ave, Tallahassee, FL 17873, USA','TransactionDate':'2024-03-30',,'Total':'868.97','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IA','Description':'Company business trip - Attended IoT Solutions Summit in Cedar Rapids. 3 business nights; operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-27","Item Amount":"202.75"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-27","Item Tax Amount":"10.86"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-27","Item Tax Amount":"3.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-27","Item Amount":"36.65"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-28","Item Amount":"200.70"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-28","Item Tax Amount":"10.75"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-28","Item Tax Amount":"3.58"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-03-28","Item Amount":"36.31"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-03-28","Item Amount":"24.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-28","Item Amount":"59.93"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-29","Item Amount":"217.15"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-29","Item Tax Amount":"11.63"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-29","Item Tax Amount":"3.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-29","Item Amount":"46.82"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Tallahassee Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Tallahassee Downtown' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_135(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft San Jose Silicon Valley','MerchantAddress':'517 Lee Ave, San Jose, CA 47950, USA','TransactionDate':'2020-04-24',,'Total':'730.36','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MO','Description':'Company travel - Tech Innovation Conference in Columbia. 2 business nights for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-22","Item Amount":"220.11"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-22","Item Tax Amount":"13.09"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-22","Item Tax Amount":"8.73"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-04-22","Item Amount":"101.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-22","Item Amount":"40.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-23","Item Amount":"197.80"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-23","Item Tax Amount":"11.77"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-23","Item Tax Amount":"7.84"},{"Item Name":"Entertainment External","Transaction Date":"2020-04-23","Item Amount":"88.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-23","Item Amount":"40.75"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft San Jose Silicon Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft San Jose Silicon Valley' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_136(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Las Vegas Airport','MerchantAddress':'285 Wilson Way, Las Vegas, NV 26210, USA','TransactionDate':'2021-05-26',,'Total':'1356.89','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Blockchain Conference conference in Los Angeles. vendor negotiations and contract reviews over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-22","Item Amount":"213.77"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-22","Item Tax Amount":"13.00"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-22","Item Tax Amount":"4.33"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-22","Item Amount":"88.39"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-23","Item Amount":"196.63"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-23","Item Tax Amount":"11.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-23","Item Tax Amount":"3.99"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-05-23","Item Amount":"136.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-23","Item Amount":"81.71"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-24","Item Amount":"215.99"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-24","Item Tax Amount":"13.13"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-24","Item Tax Amount":"4.38"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-24","Item Tax Amount":"4.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-24","Item Amount":"74.15"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-25","Item Amount":"205.80"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-25","Item Tax Amount":"12.51"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-25","Item Tax Amount":"4.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-25","Item Amount":"71.97"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Las Vegas Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Las Vegas Airport' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_137(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Murfreesboro Avenue Murfreesboro','MerchantAddress':'580 Turner St, Murfreesboro, TN 71173, USA','TransactionDate':'2020-11-04',,'Total':'520.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'PA','Description':'Corporate trip - Quality Assurance Conference conference in Pittsburgh. team building and training sessions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-02","Item Amount":"212.83"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-02","Item Tax Amount":"10.65"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-11-02","Item Amount":"5.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-02","Item Amount":"18.95"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-03","Item Amount":"196.58"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-03","Item Tax Amount":"9.83"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-11-03","Item Amount":"12.86"},{"Item Name":"Laundry","Transaction Date":"2020-11-03","Item Amount":"20.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-03","Item Amount":"32.52"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Murfreesboro Avenue Murfreesboro' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Murfreesboro Avenue Murfreesboro' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_138(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Pomona Airport','MerchantAddress':'166 Cooper St, Pomona, CA 18564, USA','TransactionDate':'2025-04-04',,'Total':'821.29','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OR','Description':'Company business trip - Attended Cloud Computing Expo in Portland. 2 business nights; stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-02","Item Amount":"194.03"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-02","Item Tax Amount":"9.39"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-04-02","Item Amount":"156.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-02","Item Amount":"77.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-03","Item Amount":"200.93"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-03","Item Tax Amount":"9.72"},{"Item Name":"Entertainment External","Transaction Date":"2025-04-03","Item Amount":"90.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-03","Item Amount":"83.09"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Pomona Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Pomona Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_139(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Chandler San Tan','MerchantAddress':'213 Lewis Ave, Chandler, AZ 62297, USA','TransactionDate':'2024-06-12',,'Total':'1930.87','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Thousand Oaks for strategic planning. Attended Innovation Leadership Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-08","Item Amount":"381.45"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-08","Item Tax Amount":"19.29"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-08","Item Tax Amount":"12.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-08","Item Amount":"79.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-09","Item Amount":"383.48"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-09","Item Tax Amount":"19.39"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-09","Item Tax Amount":"12.93"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-09","Item Amount":"57.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-10","Item Amount":"390.67"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-10","Item Tax Amount":"19.76"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-10","Item Tax Amount":"13.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-10","Item Amount":"79.49"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-11","Item Amount":"373.53"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-11","Item Tax Amount":"18.89"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-11","Item Tax Amount":"12.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-11","Item Amount":"55.73"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Chandler San Tan' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Chandler San Tan' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_140(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Spokane Downtown','MerchantAddress':'248 Morales Blvd, Spokane, WA 70040, USA','TransactionDate':'2021-07-09',,'Total':'1075.17','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IA','Description':'Business trip to Cedar Rapids for product launch. Attended Digital Transformation Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-07","Item Amount":"341.86"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-07","Item Tax Amount":"18.62"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-07","Item Tax Amount":"6.21"},{"Item Name":"Entertainment External","Transaction Date":"2021-07-07","Item Amount":"107.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-07","Item Amount":"93.81"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-08","Item Amount":"362.40"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-08","Item Tax Amount":"19.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-08","Item Tax Amount":"6.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-08","Item Amount":"87.68"},{"Item Name":"Incidentals","Transaction Date":"2021-07-08","Item Amount":"31.04"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Spokane Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Spokane Downtown' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_141(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Henderson Lake Las Vegas','MerchantAddress':'834 Bennett Blvd, Henderson, NV 66469, USA','TransactionDate':'2021-01-10',,'Total':'325.84','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - IoT Solutions Summit in Irvine. 3 business nights for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-07","Item Amount":"51.67"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-07","Item Tax Amount":"3.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-07","Item Amount":"37.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-08","Item Amount":"55.52"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-08","Item Tax Amount":"3.28"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-08","Item Amount":"42.48"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-09","Item Amount":"85.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-09","Item Tax Amount":"5.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-09","Item Amount":"42.40"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Henderson Lake Las Vegas' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Henderson Lake Las Vegas' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_142(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Plano Shops at Legacy','MerchantAddress':'246 Bennett Blvd, Plano, TX 86052, USA','TransactionDate':'2024-05-22',,'Total':'613.59','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AL','Description':'Corporate trip - Digital Marketing Conference conference in Montgomery. board meetings and investor presentations over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-20","Item Amount":"206.04"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-20","Item Tax Amount":"18.27"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-20","Item Tax Amount":"6.09"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-20","Item Tax Amount":"6.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-20","Item Amount":"69.09"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-21","Item Amount":"205.09"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-21","Item Tax Amount":"18.18"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-21","Item Tax Amount":"6.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-21","Item Amount":"78.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Plano Shops at Legacy' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Plano Shops at Legacy' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_143(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Fairfield Airport','MerchantAddress':'898 Long Ave, Fairfield, CA 23547, USA','TransactionDate':'2019-02-10',,'Total':'501.35','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'GA','Description':'Business trip to Columbus for vendor negotiations. Attended Cloud Computing Expo. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-06","Item Amount":"47.56"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-06","Item Tax Amount":"2.68"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-06","Item Tax Amount":"1.79"},{"Item Name":"Laundry","Transaction Date":"2019-02-06","Item Amount":"22.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-06","Item Amount":"39.96"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-07","Item Amount":"78.72"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-07","Item Tax Amount":"4.44"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-07","Item Tax Amount":"2.96"},{"Item Name":"Entertainment External","Transaction Date":"2019-02-07","Item Amount":"43.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-07","Item Amount":"35.19"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-08","Item Amount":"71.42"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-08","Item Tax Amount":"4.03"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-08","Item Tax Amount":"2.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-08","Item Amount":"40.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-02-09","Item Amount":"46.63"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-09","Item Tax Amount":"2.63"},{"Item Name":"Hotel Tax","Transaction Date":"2019-02-09","Item Tax Amount":"1.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-02-09","Item Amount":"52.63"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Fairfield Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Fairfield Airport' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_144(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Hialeah Palmetto','MerchantAddress':'489 Richardson Ave, Hialeah, FL 95687, USA','TransactionDate':'2020-07-22',,'Total':'1282.93','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WI','Description':'Company business trip - Attended Product Management Summit in Milwaukee. 3 business nights; compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-19","Item Amount":"292.14"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-19","Item Tax Amount":"7.62"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-19","Item Tax Amount":"22.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-19","Item Amount":"46.74"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-20","Item Amount":"279.76"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-20","Item Tax Amount":"7.30"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-20","Item Tax Amount":"21.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-20","Item Amount":"45.17"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-21","Item Amount":"287.15"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-21","Item Tax Amount":"7.49"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-21","Item Tax Amount":"7.49"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-21","Item Tax Amount":"22.47"},{"Item Name":"Entertainment External","Transaction Date":"2020-07-21","Item Amount":"127.53"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-07-21","Item Amount":"75.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-21","Item Amount":"31.91"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Hialeah Palmetto' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Hialeah Palmetto' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_145(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn McKinney Adriatica','MerchantAddress':'237 Court St, McKinney, TX 64453, USA','TransactionDate':'2019-06-15',,'Total':'575.88','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MS','Description':'Business trip to Jackson for partnership development. Attended Energy Sector Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-14","Item Amount":"342.35"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-14","Item Tax Amount":"23.96"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-14","Item Tax Amount":"7.99"},{"Item Name":"Entertainment External","Transaction Date":"2019-06-14","Item Amount":"105.77"},{"Item Name":"Laundry","Transaction Date":"2019-06-14","Item Amount":"30.65"},{"Item Name":"Incidentals","Transaction Date":"2019-06-14","Item Amount":"24.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-14","Item Amount":"40.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn McKinney Adriatica' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn McKinney Adriatica' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_146(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Virginia Beach Oceanfront','MerchantAddress':'413 Young St, Virginia Beach, VA 81052, USA','TransactionDate':'2020-04-20',,'Total':'582.65','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Corporate trip - Digital Transformation Summit conference in Mesa. product demos and customer meetings over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-17","Item Amount":"89.28"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-17","Item Tax Amount":"5.19"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-17","Item Tax Amount":"1.73"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-17","Item Tax Amount":"1.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-17","Item Amount":"70.69"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-18","Item Amount":"109.58"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-18","Item Tax Amount":"6.37"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-18","Item Tax Amount":"2.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-18","Item Amount":"58.64"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-19","Item Amount":"81.18"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-19","Item Tax Amount":"4.72"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-19","Item Tax Amount":"1.57"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-04-19","Item Amount":"93.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-19","Item Amount":"56.82"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Virginia Beach Oceanfront' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Virginia Beach Oceanfront' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_147(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Columbus University','MerchantAddress':'728 Price Blvd, Columbus, GA 19605, USA','TransactionDate':'2020-10-29',,'Total':'490.17','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MO','Description':'Company travel - Business Intelligence Summit in Columbia. 2 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-27","Item Amount":"163.10"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-27","Item Tax Amount":"9.97"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-27","Item Tax Amount":"6.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-27","Item Amount":"49.15"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-28","Item Amount":"139.92"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-28","Item Tax Amount":"8.55"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-28","Item Tax Amount":"5.70"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-10-28","Item Amount":"65.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-28","Item Amount":"41.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Columbus University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Columbus University' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_148(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Fullerton Airport','MerchantAddress':'981 Butler St, Fullerton, CA 61325, USA','TransactionDate':'2023-08-07',,'Total':'1084.13','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business trip to Toledo for product launch. Attended Legal Technology Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-04","Item Amount":"298.38"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-04","Item Tax Amount":"5.41"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-04","Item Tax Amount":"16.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-04","Item Amount":"50.45"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-05","Item Amount":"294.72"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-05","Item Tax Amount":"5.34"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-05","Item Tax Amount":"16.03"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-05","Item Tax Amount":"5.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-05","Item Amount":"33.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-06","Item Amount":"284.65"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-06","Item Tax Amount":"5.16"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-06","Item Tax Amount":"15.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-06","Item Amount":"53.07"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Fullerton Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Fullerton Airport' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_149(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Worcester Shrewsbury Street','MerchantAddress':'984 Cook Blvd, Worcester, MA 42470, USA','TransactionDate':'2020-07-17',,'Total':'1376.18','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CT','Description':'Company travel - Healthcare IT Summit in Hartford. 4 business nights for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-13","Item Amount":"290.25"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-13","Item Tax Amount":"15.37"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-13","Item Tax Amount":"5.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-13","Item Amount":"41.58"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-14","Item Amount":"287.19"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-14","Item Tax Amount":"15.21"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-14","Item Tax Amount":"5.07"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-14","Item Tax Amount":"5.07"},{"Item Name":"Laundry","Transaction Date":"2020-07-14","Item Amount":"32.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-14","Item Amount":"38.24"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-15","Item Amount":"264.01"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-15","Item Tax Amount":"13.98"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-15","Item Tax Amount":"4.66"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-15","Item Tax Amount":"4.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-15","Item Amount":"33.53"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-07-16","Item Amount":"265.83"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-16","Item Tax Amount":"14.08"},{"Item Name":"Hotel Tax","Transaction Date":"2020-07-16","Item Tax Amount":"4.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-07-16","Item Amount":"35.47"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Worcester Shrewsbury Street' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Worcester Shrewsbury Street' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_150(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Warren Tech Center','MerchantAddress':'316 Ward Ave, Warren, MI 97828, USA','TransactionDate':'2025-03-04',,'Total':'285.31','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Stockton for strategic planning. Attended Enterprise Software Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-03-03","Item Amount":"146.63"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-03","Item Tax Amount":"7.73"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-03","Item Tax Amount":"5.16"},{"Item Name":"Entertainment External","Transaction Date":"2025-03-03","Item Amount":"33.05"},{"Item Name":"Laundry","Transaction Date":"2025-03-03","Item Amount":"17.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-03-03","Item Amount":"55.49"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-03-04","Item Amount":"19.77"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Warren Tech Center' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Warren Tech Center' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_151(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Concord Clayton','MerchantAddress':'959 Kelly Dr, Concord, CA 92531, USA','TransactionDate':'2021-10-11',,'Total':'455.49','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CT','Description':'Company business trip - Attended Cloud Computing Expo in Hartford. 2 business nights; market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-09","Item Amount":"170.60"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-09","Item Tax Amount":"9.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-09","Item Amount":"48.08"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-10","Item Amount":"153.27"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-10","Item Tax Amount":"8.41"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-10-10","Item Amount":"20.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-10","Item Amount":"44.91"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Concord Clayton' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Concord Clayton' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_152(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Denton Airport','MerchantAddress':'349 Mill St, Denton, TX 74668, USA','TransactionDate':'2019-08-13',,'Total':'234.48','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Business travel to Elizabeth for Project Management Summit. 1 night stay for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-12","Item Amount":"183.79"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-12","Item Tax Amount":"7.09"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-12","Item Tax Amount":"10.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-12","Item Amount":"32.97"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Denton Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Denton Airport' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_153(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Thousand Oaks Airport','MerchantAddress':'151 Wood Dr, Thousand Oaks, CA 67498, USA','TransactionDate':'2019-11-24',,'Total':'155.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'KS','Description':'Company travel - Corporate Strategy Summit in Topeka. 1 business night for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-23","Item Amount":"100.50"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"6.81"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-23","Item Tax Amount":"4.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-23","Item Amount":"43.73"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Thousand Oaks Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Thousand Oaks Airport' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_154(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Durham Research Triangle','MerchantAddress':'688 Walker St, Durham, NC 97969, USA','TransactionDate':'2021-07-02',,'Total':'1470.34','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Customer Experience Summit in Oceanside. 4 business nights; customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-28","Item Amount":"211.55"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-28","Item Tax Amount":"12.72"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-28","Item Tax Amount":"8.48"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-06-28","Item Amount":"143.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-28","Item Amount":"91.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-29","Item Amount":"230.59"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-29","Item Tax Amount":"13.86"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-29","Item Tax Amount":"9.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-29","Item Amount":"85.96"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-30","Item Amount":"217.87"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-30","Item Tax Amount":"13.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-30","Item Tax Amount":"8.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-30","Item Amount":"91.53"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-01","Item Amount":"209.40"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-01","Item Tax Amount":"12.59"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-01","Item Tax Amount":"8.39"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-07-01","Item Amount":"16.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-01","Item Amount":"84.21"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Durham Research Triangle' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Durham Research Triangle' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_155(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Killeen Airport','MerchantAddress':'728 Main St, Killeen, TX 98577, USA','TransactionDate':'2021-11-12',,'Total':'277.86','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company travel - Manufacturing Excellence Summit in Lubbock. 1 business night for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-11","Item Amount":"172.25"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-11","Item Tax Amount":"9.12"},{"Item Name":"Entertainment External","Transaction Date":"2021-11-11","Item Amount":"20.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-11","Item Amount":"76.46"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Killeen Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Killeen Airport' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_156(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Provo Orem','MerchantAddress':'566 Perry Blvd, Provo, UT 49080, USA','TransactionDate':'2025-11-21',,'Total':'211.09','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Company travel - Customer Experience Summit in Salt Lake City. 1 business night for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-20","Item Amount":"92.83"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-20","Item Tax Amount":"3.45"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-20","Item Tax Amount":"5.17"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-11-20","Item Amount":"72.24"},{"Item Name":"Hotel Telephone","Transaction Date":"2025-11-20","Item Amount":"8.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-20","Item Amount":"29.35"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Provo Orem' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Provo Orem' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_157(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Chandler Ahwatukee','MerchantAddress':'832 Kelly Dr, Chandler, AZ 61506, USA','TransactionDate':'2021-05-08',,'Total':'400.21','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Corporate trip - HR Leadership Summit conference in West Valley City. technical workshops and knowledge sharing over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-07","Item Amount":"195.58"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-07","Item Tax Amount":"9.08"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-07","Item Tax Amount":"13.62"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-05-07","Item Amount":"73.73"},{"Item Name":"Laundry","Transaction Date":"2021-05-07","Item Amount":"33.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-07","Item Amount":"56.82"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-05-08","Item Amount":"17.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Chandler Ahwatukee' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Chandler Ahwatukee' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_158(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Baltimore BWI','MerchantAddress':'912 Taylor Ave, Baltimore, MD 46345, USA','TransactionDate':'2019-10-13',,'Total':'457.99','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company business trip - Attended Business Intelligence Summit in Woodbridge. 2 business nights; board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-11","Item Amount":"174.42"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-11","Item Tax Amount":"10.60"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-11","Item Tax Amount":"3.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-11","Item Amount":"25.20"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-12","Item Amount":"174.49"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-12","Item Tax Amount":"10.60"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-12","Item Tax Amount":"3.53"},{"Item Name":"Laundry","Transaction Date":"2019-10-12","Item Amount":"26.80"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-12","Item Amount":"28.82"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Baltimore BWI' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Baltimore BWI' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_159(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Kansas City Plaza','MerchantAddress':'779 Roosevelt Way, Kansas City, MO 42250, USA','TransactionDate':'2021-06-26',,'Total':'1751.73','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Real Estate Investment Summit conference in Huntington Beach. vendor negotiations and contract reviews over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-22","Item Amount":"299.85"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-22","Item Tax Amount":"25.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-22","Item Amount":"83.03"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-23","Item Amount":"303.53"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-23","Item Tax Amount":"25.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-23","Item Amount":"97.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-24","Item Amount":"305.40"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-24","Item Tax Amount":"25.51"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-24","Item Amount":"81.01"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-25","Item Amount":"283.75"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-25","Item Tax Amount":"23.70"},{"Item Name":"Entertainment External","Transaction Date":"2021-06-25","Item Amount":"107.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-25","Item Amount":"91.08"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Kansas City Plaza' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Kansas City Plaza' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_160(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Joliet Airport','MerchantAddress':'346 Morris Ave, Joliet, IL 89940, USA','TransactionDate':'2024-11-29',,'Total':'702.42','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Stockton for Innovation Leadership Conference. 2 nights stay for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-11-27","Item Amount":"257.20"},{"Item Name":"Hotel Tax","Transaction Date":"2024-11-27","Item Tax Amount":"18.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-11-27","Item Amount":"44.72"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-11-28","Item Amount":"257.76"},{"Item Name":"Hotel Tax","Transaction Date":"2024-11-28","Item Tax Amount":"18.89"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-11-28","Item Amount":"25.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-11-28","Item Amount":"39.79"},{"Item Name":"Incidentals","Transaction Date":"2024-11-28","Item Amount":"39.74"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Joliet Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Joliet Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_161(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta McKinney Stonebridge','MerchantAddress':'235 Stewart Blvd, McKinney, TX 21968, USA','TransactionDate':'2022-11-16',,'Total':'409.55','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Tallahassee for Blockchain Conference. 3 nights stay for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-13","Item Amount":"64.82"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-13","Item Tax Amount":"2.22"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-13","Item Tax Amount":"3.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-13","Item Amount":"61.24"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-14","Item Amount":"87.82"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-14","Item Tax Amount":"3.00"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-14","Item Tax Amount":"4.50"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-14","Item Amount":"48.08"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-15","Item Amount":"69.61"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-15","Item Tax Amount":"2.38"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-15","Item Tax Amount":"3.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-15","Item Amount":"58.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta McKinney Stonebridge' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta McKinney Stonebridge' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_162(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Tulsa South Tulsa','MerchantAddress':'385 Oak St, Tulsa, OK 48396, USA','TransactionDate':'2020-08-11',,'Total':'429.89','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'VA','Description':'Business travel to Richmond for HR Leadership Summit. 1 night stay for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-08-10","Item Amount":"295.22"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-10","Item Tax Amount":"8.33"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-10","Item Tax Amount":"25.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-08-10","Item Amount":"66.15"},{"Item Name":"Incidentals","Transaction Date":"2020-08-10","Item Amount":"35.19"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Tulsa South Tulsa' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Tulsa South Tulsa' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_163(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Miramar Pembroke Lakes Mall','MerchantAddress':'481 Kelly Dr, Miramar, FL 13916, USA','TransactionDate':'2021-07-18',,'Total':'588.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Corporate trip - Data Science Summit conference in Cape Coral. product demos and customer meetings over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-15","Item Amount":"116.32"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-15","Item Tax Amount":"8.86"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-15","Item Tax Amount":"5.90"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-15","Item Amount":"25.89"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-16","Item Amount":"124.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-16","Item Tax Amount":"9.51"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-16","Item Tax Amount":"6.34"},{"Item Name":"Entertainment External","Transaction Date":"2021-07-16","Item Amount":"92.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-16","Item Amount":"31.63"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-17","Item Amount":"106.41"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-17","Item Tax Amount":"8.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-17","Item Tax Amount":"5.40"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-07-17","Item Amount":"19.30"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-17","Item Amount":"27.23"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Miramar Pembroke Lakes Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Miramar Pembroke Lakes Mall' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_164(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Killeen Fort Hood','MerchantAddress':'395 Reed Ave, Killeen, TX 84422, USA','TransactionDate':'2020-09-22',,'Total':'624.56','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Jacksonville for HR Leadership Summit. 2 nights stay for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-20","Item Amount":"240.49"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-20","Item Tax Amount":"15.09"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-20","Item Tax Amount":"10.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-20","Item Amount":"41.10"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-21","Item Amount":"249.83"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-21","Item Tax Amount":"15.68"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-21","Item Tax Amount":"10.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-21","Item Amount":"41.86"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Killeen Fort Hood' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Killeen Fort Hood' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_165(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Charleston Airport','MerchantAddress':'213 Third St, Charleston, SC 33563, USA','TransactionDate':'2024-06-29',,'Total':'1205.01','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Enterprise Software Summit in Dallas. 3 business nights; board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-26","Item Amount":"309.73"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-26","Item Tax Amount":"12.86"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-26","Item Tax Amount":"19.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-26","Item Amount":"72.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-27","Item Amount":"308.07"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-27","Item Tax Amount":"12.79"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-27","Item Tax Amount":"19.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-27","Item Amount":"61.45"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-06-28","Item Amount":"294.18"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-28","Item Tax Amount":"12.21"},{"Item Name":"Hotel Tax","Transaction Date":"2024-06-28","Item Tax Amount":"18.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-06-28","Item Amount":"63.94"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Charleston Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Charleston Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_166(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Newark Airport','MerchantAddress':'688 Moore St, Newark, NJ 17052, USA','TransactionDate':'2023-02-02',,'Total':'198.44','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Business travel to Aurora for Digital Marketing Conference. 1 night stay for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-02-01","Item Amount":"137.77"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-01","Item Tax Amount":"10.66"},{"Item Name":"Laundry","Transaction Date":"2023-02-01","Item Amount":"17.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-02-01","Item Amount":"32.64"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Newark Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Newark Airport' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_167(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Bakersfield Airport','MerchantAddress':'861 Convention Center Dr, Bakersfield, CA 10913, USA','TransactionDate':'2022-04-21',,'Total':'1350.19','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Business travel to Minneapolis for Mobile Technology Conference. 4 nights stay for client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-17","Item Amount":"266.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-17","Item Tax Amount":"17.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-17","Item Amount":"50.45"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-18","Item Amount":"259.78"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-18","Item Tax Amount":"16.62"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-04-18","Item Amount":"14.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-18","Item Amount":"71.17"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-19","Item Amount":"244.73"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-19","Item Tax Amount":"15.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-19","Item Amount":"57.55"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-20","Item Amount":"250.27"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-20","Item Tax Amount":"16.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-20","Item Amount":"70.02"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Bakersfield Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Bakersfield Airport' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_168(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Eugene Airport','MerchantAddress':'570 Hall Blvd, Eugene, OR 39677, USA','TransactionDate':'2024-07-24',,'Total':'1398.89','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Killeen for Manufacturing Excellence Summit. 4 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-20","Item Amount":"200.13"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-20","Item Tax Amount":"3.39"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-20","Item Tax Amount":"3.39"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-20","Item Tax Amount":"10.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-20","Item Amount":"57.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-21","Item Amount":"202.75"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-21","Item Tax Amount":"3.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-21","Item Tax Amount":"10.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-21","Item Amount":"57.39"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-22","Item Amount":"204.18"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-22","Item Tax Amount":"3.46"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-22","Item Tax Amount":"3.46"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-22","Item Tax Amount":"10.38"},{"Item Name":"Entertainment External","Transaction Date":"2024-07-22","Item Amount":"129.69"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-07-22","Item Amount":"93.90"},{"Item Name":"Laundry","Transaction Date":"2024-07-22","Item Amount":"27.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-22","Item Amount":"79.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-23","Item Amount":"210.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-23","Item Tax Amount":"3.57"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-23","Item Tax Amount":"3.57"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-23","Item Tax Amount":"10.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-23","Item Amount":"69.73"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Eugene Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Eugene Airport' have all 22 required itemizations'?,",
#     )


# def test_expense_hotel_169(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Columbia Columbiana Centre','MerchantAddress':'321 Fisher Dr, Columbia, SC 13192, USA','TransactionDate':'2020-01-13',,'Total':'682.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Business trip to West Jordan for vendor negotiations. Attended Customer Experience Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-10","Item Amount":"147.15"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-10","Item Tax Amount":"8.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-10","Item Amount":"58.08"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-11","Item Amount":"148.19"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-11","Item Tax Amount":"9.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-11","Item Amount":"49.42"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-12","Item Amount":"153.37"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-12","Item Tax Amount":"9.33"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-12","Item Amount":"49.17"},{"Item Name":"Incidentals","Transaction Date":"2020-01-12","Item Amount":"49.71"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Columbia Columbiana Centre' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Columbia Columbiana Centre' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_170(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Abilene Downtown','MerchantAddress':'631 Roosevelt Way, Abilene, TX 93150, USA','TransactionDate':'2023-03-18',,'Total':'485.64','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OK','Description':'Company business trip - Attended IoT Solutions Summit in Oklahoma City. 2 business nights; compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-16","Item Amount":"176.36"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-16","Item Tax Amount":"15.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-16","Item Amount":"66.68"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-17","Item Amount":"165.53"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-17","Item Tax Amount":"14.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-17","Item Amount":"46.74"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Abilene Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Abilene Downtown' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_171(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Corona The Crossings','MerchantAddress':'218 Richardson Ave, Corona, CA 71542, USA','TransactionDate':'2022-03-06',,'Total':'1325.64','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Dallas for Sales Leadership Conference. 4 nights stay for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-02","Item Amount":"263.18"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-02","Item Tax Amount":"18.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-02","Item Amount":"59.03"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-03","Item Amount":"269.96"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-03","Item Tax Amount":"18.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-03","Item Amount":"51.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-04","Item Amount":"237.15"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-04","Item Tax Amount":"16.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-04","Item Amount":"55.73"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-05","Item Amount":"257.96"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-05","Item Tax Amount":"17.97"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-03-05","Item Amount":"21.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-05","Item Amount":"37.88"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Corona The Crossings' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Corona The Crossings' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_172(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Chesapeake Deep Creek','MerchantAddress':'350 Clark St, Chesapeake, VA 41659, USA','TransactionDate':'2024-08-08',,'Total':'939.47','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Berkeley for sales presentations. Attended AI & Machine Learning Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-08-06","Item Amount":"377.73"},{"Item Name":"Hotel Tax","Transaction Date":"2024-08-06","Item Tax Amount":"23.91"},{"Item Name":"Hotel Tax","Transaction Date":"2024-08-06","Item Tax Amount":"15.94"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-08-06","Item Amount":"47.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-08-06","Item Amount":"30.61"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-08-07","Item Amount":"371.56"},{"Item Name":"Hotel Tax","Transaction Date":"2024-08-07","Item Tax Amount":"23.52"},{"Item Name":"Hotel Tax","Transaction Date":"2024-08-07","Item Tax Amount":"15.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-08-07","Item Amount":"33.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Chesapeake Deep Creek' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Chesapeake Deep Creek' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_173(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Berkeley University of California','MerchantAddress':'324 Mill St, Berkeley, CA 73106, USA','TransactionDate':'2022-06-22',,'Total':'1082.26','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NV','Description':'Company travel - Digital Transformation Summit in Henderson. 3 business nights for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-19","Item Amount":"281.58"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-19","Item Tax Amount":"17.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-19","Item Amount":"31.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-20","Item Amount":"263.98"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-20","Item Tax Amount":"16.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-20","Item Amount":"35.58"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-21","Item Amount":"282.17"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-21","Item Tax Amount":"17.34"},{"Item Name":"Entertainment External","Transaction Date":"2022-06-21","Item Amount":"88.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-21","Item Amount":"48.01"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Berkeley University of California' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Berkeley University of California' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_174(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Scottsdale Airport','MerchantAddress':'438 Richardson Ave, Scottsdale, AZ 91056, USA','TransactionDate':'2023-09-29',,'Total':'434.83','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Corporate trip - Quality Assurance Conference conference in Sterling Heights. merger and acquisition discussions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-27","Item Amount":"171.63"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-27","Item Tax Amount":"10.77"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-27","Item Tax Amount":"3.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-27","Item Amount":"44.82"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-28","Item Amount":"138.15"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-28","Item Tax Amount":"8.67"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-28","Item Tax Amount":"2.89"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-28","Item Tax Amount":"2.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-28","Item Amount":"51.42"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Scottsdale Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Scottsdale Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_175(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Tampa Downtown','MerchantAddress':'243 Maple Dr, Tampa, FL 24499, USA','TransactionDate':'2024-12-25',,'Total':'536.15','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Corporate trip - Project Management Summit conference in Thornton. market research and competitive analysis over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-22","Item Amount":"126.06"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-22","Item Tax Amount":"6.59"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-22","Item Tax Amount":"2.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-22","Item Amount":"62.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-23","Item Amount":"109.81"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-23","Item Tax Amount":"5.74"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-23","Item Tax Amount":"1.91"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-23","Item Amount":"55.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-24","Item Amount":"93.87"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-24","Item Tax Amount":"4.91"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-24","Item Tax Amount":"1.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-24","Item Amount":"65.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Tampa Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Tampa Downtown' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_176(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Fullerton Harbor Boulevard','MerchantAddress':'649 Evans Blvd, Fullerton, CA 31276, USA','TransactionDate':'2021-03-06',,'Total':'764.15','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Corporate trip - E-commerce Summit conference in Fort Lauderdale. client sessions and project planning over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-04","Item Amount":"314.70"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-04","Item Tax Amount":"22.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-04","Item Amount":"53.07"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-05","Item Amount":"300.15"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-05","Item Tax Amount":"21.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-05","Item Amount":"51.82"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Fullerton Harbor Boulevard' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Fullerton Harbor Boulevard' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_177(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Dallas Deep Ellum','MerchantAddress':'573 Cedar Ave, Dallas, TX 56547, USA','TransactionDate':'2021-05-15',,'Total':'1251.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Corporate trip - Blockchain Conference conference in Woodbridge. team building and training sessions over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-11","Item Amount":"212.92"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-11","Item Tax Amount":"14.12"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-11","Item Tax Amount":"9.41"},{"Item Name":"Incidentals","Transaction Date":"2021-05-11","Item Amount":"34.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-11","Item Amount":"66.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-12","Item Amount":"196.24"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-12","Item Tax Amount":"13.01"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-12","Item Tax Amount":"8.67"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-05-12","Item Amount":"21.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-12","Item Amount":"71.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-13","Item Amount":"190.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-13","Item Tax Amount":"12.64"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-13","Item Tax Amount":"8.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-13","Item Amount":"66.71"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-05-14","Item Amount":"215.71"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-14","Item Tax Amount":"14.30"},{"Item Name":"Hotel Tax","Transaction Date":"2021-05-14","Item Tax Amount":"9.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-05-14","Item Amount":"85.53"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Dallas Deep Ellum' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Dallas Deep Ellum' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_178(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Fullerton Downtown Fullerton','MerchantAddress':'388 Torres Ave, Fullerton, CA 38148, USA','TransactionDate':'2023-09-16',,'Total':'260.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Pomona for FinTech Conference. 1 night stay for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-15","Item Amount":"104.68"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-15","Item Tax Amount":"7.19"},{"Item Name":"Gift and Entertainment","Transaction Date":"2023-09-15","Item Amount":"52.88"},{"Item Name":"Laundry","Transaction Date":"2023-09-15","Item Amount":"36.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-15","Item Amount":"59.37"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Fullerton Downtown Fullerton' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Fullerton Downtown Fullerton' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_179(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Montgomery Old Cloverdale','MerchantAddress':'787 First St, Montgomery, AL 84354, USA','TransactionDate':'2024-09-06',,'Total':'137.74','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Company travel - Supply Chain Management Conference in Tacoma. 1 business night for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-05","Item Amount":"111.95"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-05","Item Tax Amount":"6.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-05","Item Amount":"19.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Montgomery Old Cloverdale' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Montgomery Old Cloverdale' have all 3 required itemizations'?,",
#     )


# def test_expense_hotel_180(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Austin Downtown','MerchantAddress':'645 Scott St, Austin, TX 46879, USA','TransactionDate':'2024-10-29',,'Total':'771.16','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business trip to Dayton for investor relations. Attended Cybersecurity Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-27","Item Amount":"215.07"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-27","Item Tax Amount":"16.52"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-27","Item Tax Amount":"11.01"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-10-27","Item Amount":"82.33"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-10-27","Item Amount":"73.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-27","Item Amount":"49.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-28","Item Amount":"220.30"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-28","Item Tax Amount":"16.92"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-28","Item Tax Amount":"11.28"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-10-28","Item Amount":"19.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-28","Item Amount":"55.39"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Austin Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Austin Downtown' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_181(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Rochester Airport','MerchantAddress':'295 King Dr, Rochester, NY 37002, USA','TransactionDate':'2022-03-06',,'Total':'288.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Simi Valley for investor relations. Attended Legal Technology Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-05","Item Amount":"173.93"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-05","Item Tax Amount":"9.17"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-05","Item Tax Amount":"3.06"},{"Item Name":"Laundry","Transaction Date":"2022-03-05","Item Amount":"29.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-05","Item Amount":"72.64"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Rochester Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Rochester Airport' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_182(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western St. Petersburg Grand Central','MerchantAddress':'768 Peterson Dr, St. Petersburg, FL 79522, USA','TransactionDate':'2023-01-23',,'Total':'321.37','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Business trip to Knoxville for sales presentations. Attended Enterprise Software Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-21","Item Amount":"121.87"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-21","Item Tax Amount":"9.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-21","Item Amount":"40.27"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-22","Item Amount":"106.85"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-22","Item Tax Amount":"8.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-22","Item Amount":"33.71"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western St. Petersburg Grand Central' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western St. Petersburg Grand Central' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_183(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Oklahoma City Midtown','MerchantAddress':'992 Lincoln Blvd, Oklahoma City, OK 79131, USA','TransactionDate':'2019-01-28',,'Total':'642.84','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Company business trip - Attended FinTech Conference in Baton Rouge. 2 business nights; partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-26","Item Amount":"205.36"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-26","Item Tax Amount":"18.24"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-26","Item Tax Amount":"12.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-26","Item Amount":"42.69"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-27","Item Amount":"215.58"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-27","Item Tax Amount":"19.15"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-27","Item Tax Amount":"12.76"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-01-27","Item Amount":"63.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-27","Item Amount":"53.54"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Oklahoma City Midtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Oklahoma City Midtown' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_184(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Toledo Sylvania','MerchantAddress':'672 Parker Dr, Toledo, OH 72087, USA','TransactionDate':'2022-03-20',,'Total':'357.63','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company travel - Cybersecurity Conference in Elizabeth. 2 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-18","Item Amount":"102.46"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-18","Item Tax Amount":"6.17"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-18","Item Tax Amount":"2.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-18","Item Amount":"60.28"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-19","Item Amount":"115.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-19","Item Tax Amount":"6.97"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-19","Item Tax Amount":"2.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-19","Item Amount":"61.62"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Toledo Sylvania' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Toledo Sylvania' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_185(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Philadelphia University City','MerchantAddress':'590 Walker St, Philadelphia, PA 88666, USA','TransactionDate':'2020-08-12',,'Total':'362.14','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'PA','Description':'Corporate trip - Customer Experience Summit conference in Scranton. operational excellence workshops over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-08-11","Item Amount":"253.18"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-11","Item Tax Amount":"17.97"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-11","Item Tax Amount":"5.99"},{"Item Name":"Hotel Tax","Transaction Date":"2020-08-11","Item Tax Amount":"5.99"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-08-11","Item Amount":"79.01"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Philadelphia University City' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Philadelphia University City' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_186(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Tucson University','MerchantAddress':'675 Oak St, Tucson, AZ 75303, USA','TransactionDate':'2024-09-30',,'Total':'501.02','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Company business trip - Attended Product Management Summit in Bellevue. 2 business nights; client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-28","Item Amount":"56.98"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-28","Item Tax Amount":"4.38"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-09-28","Item Amount":"19.56"},{"Item Name":"Laundry","Transaction Date":"2024-09-28","Item Amount":"25.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-28","Item Amount":"61.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-29","Item Amount":"77.67"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-29","Item Tax Amount":"5.97"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-09-29","Item Amount":"185.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-29","Item Amount":"64.26"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Tucson University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Tucson University' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_187(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Dallas Deep Ellum','MerchantAddress':'854 Myers St, Dallas, TX 64668, USA','TransactionDate':'2020-11-12',,'Total':'291.85','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Business travel to Pueblo for Cloud Computing Expo. 1 night stay for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-11","Item Amount":"126.58"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-11","Item Tax Amount":"7.19"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-11","Item Tax Amount":"4.80"},{"Item Name":"Entertainment External","Transaction Date":"2020-11-11","Item Amount":"67.77"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-11-11","Item Amount":"22.99"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-11","Item Amount":"62.52"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Dallas Deep Ellum' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Dallas Deep Ellum' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_188(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Milwaukee East Side','MerchantAddress':'398 Adams St, Milwaukee, WI 38664, USA','TransactionDate':'2023-06-22',,'Total':'791.88','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Jacksonville for Energy Sector Conference. 4 nights stay for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-18","Item Amount":"130.23"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-18","Item Tax Amount":"9.61"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-18","Item Tax Amount":"3.20"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-18","Item Tax Amount":"3.20"},{"Item Name":"Incidentals","Transaction Date":"2023-06-18","Item Amount":"26.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-18","Item Amount":"57.04"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-19","Item Amount":"126.74"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-19","Item Tax Amount":"9.35"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-19","Item Tax Amount":"3.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-19","Item Amount":"60.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-20","Item Amount":"106.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-20","Item Tax Amount":"7.83"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-20","Item Tax Amount":"2.61"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-20","Item Amount":"61.49"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-21","Item Amount":"114.12"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-21","Item Tax Amount":"8.42"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-21","Item Tax Amount":"2.81"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-21","Item Tax Amount":"2.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-21","Item Amount":"56.08"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Milwaukee East Side' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Milwaukee East Side' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_189(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Syracuse University Hill','MerchantAddress':'866 Bennett Blvd, Syracuse, NY 33659, USA','TransactionDate':'2019-03-14',,'Total':'760.69','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Huntington Beach for Blockchain Conference. 3 nights stay for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-11","Item Amount":"133.15"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-11","Item Tax Amount":"6.41"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-11","Item Tax Amount":"4.27"},{"Item Name":"Hotel Deposit","Transaction Date":"2019-03-11","Item Amount":"132.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-11","Item Amount":"46.22"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-12","Item Amount":"143.16"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-12","Item Tax Amount":"6.89"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-12","Item Tax Amount":"4.59"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-03-12","Item Amount":"52.60"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-03-12","Item Amount":"11.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-12","Item Amount":"37.96"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-13","Item Amount":"129.12"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-13","Item Tax Amount":"6.21"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-13","Item Tax Amount":"4.14"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-13","Item Amount":"42.53"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Syracuse University Hill' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Syracuse University Hill' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_190(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Jersey City Liberty State Park','MerchantAddress':'620 Anderson Dr, Jersey City, NJ 24302, USA','TransactionDate':'2020-10-17',,'Total':'155.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Digital Transformation Summit conference in Grand Prairie. vendor negotiations and contract reviews over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-16","Item Amount":"96.67"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-16","Item Tax Amount":"1.66"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-16","Item Tax Amount":"4.99"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-10-16","Item Amount":"7.04"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-16","Item Amount":"45.22"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Jersey City Liberty State Park' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Jersey City Liberty State Park' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_191(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Torrance Airport','MerchantAddress':'741 Moore St, Torrance, CA 32924, USA','TransactionDate':'2019-11-26',,'Total':'172.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Business Intelligence Summit in Santa Maria. 1 business night for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-25","Item Amount":"93.99"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-25","Item Tax Amount":"7.43"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-25","Item Tax Amount":"2.48"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-11-25","Item Amount":"19.28"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-25","Item Amount":"49.21"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Torrance Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Torrance Airport' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_192(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Columbia Forest Acres','MerchantAddress':'869 Cook Blvd, Columbia, SC 93901, USA','TransactionDate':'2024-10-12',,'Total':'664.59','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MS','Description':'Business trip to Jackson for technology implementation. Attended Cloud Computing Expo. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-10","Item Amount":"224.60"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-10","Item Tax Amount":"15.94"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-10-10","Item Amount":"78.83"},{"Item Name":"Incidentals","Transaction Date":"2024-10-10","Item Amount":"35.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-10","Item Amount":"37.60"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-11","Item Amount":"213.23"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-11","Item Tax Amount":"15.13"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-10-11","Item Amount":"20.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-11","Item Amount":"24.02"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Columbia Forest Acres' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Columbia Forest Acres' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_193(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Norman Downtown','MerchantAddress':'413 Walker St, Norman, OK 29522, USA','TransactionDate':'2025-07-22',,'Total':'330.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Business trip to Paterson for compliance audit. Attended Corporate Strategy Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-21","Item Amount":"240.56"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-21","Item Tax Amount":"8.72"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-21","Item Tax Amount":"13.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-21","Item Amount":"67.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Norman Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Norman Downtown' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_194(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Sunnyvale Airport','MerchantAddress':'144 Wood Dr, Sunnyvale, CA 68869, USA','TransactionDate':'2024-10-13',,'Total':'1538.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Houston for Enterprise Software Summit. 4 nights stay for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-09","Item Amount":"278.16"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-09","Item Tax Amount":"6.04"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-09","Item Tax Amount":"18.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-09","Item Amount":"92.07"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-10","Item Amount":"279.51"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-10","Item Tax Amount":"6.07"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-10","Item Tax Amount":"18.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-10","Item Amount":"77.73"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-11","Item Amount":"273.58"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-11","Item Tax Amount":"5.94"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-11","Item Tax Amount":"5.94"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-11","Item Tax Amount":"17.82"},{"Item Name":"Laundry","Transaction Date":"2024-10-11","Item Amount":"24.77"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-11","Item Amount":"78.38"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-12","Item Amount":"255.30"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-12","Item Tax Amount":"5.54"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-12","Item Tax Amount":"5.54"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-12","Item Tax Amount":"16.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-12","Item Amount":"72.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Sunnyvale Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Sunnyvale Airport' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_195(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Raleigh Downtown','MerchantAddress':'131 Collins St, Raleigh, NC 56073, USA','TransactionDate':'2022-08-28',,'Total':'831.7','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company travel - Change Management Conference in Elizabeth. 2 business nights for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-26","Item Amount":"210.11"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-26","Item Tax Amount":"16.72"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-26","Item Tax Amount":"11.15"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-08-26","Item Amount":"77.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-26","Item Amount":"71.63"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-27","Item Amount":"182.77"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-27","Item Tax Amount":"14.55"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-27","Item Tax Amount":"9.70"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-08-27","Item Amount":"21.22"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-08-27","Item Amount":"141.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-27","Item Amount":"74.47"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Raleigh Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Raleigh Downtown' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_196(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Jersey City The Heights','MerchantAddress':'736 Hill Ave, Jersey City, NJ 54956, USA','TransactionDate':'2021-12-23',,'Total':'931.54','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'SC','Description':'Business travel to Columbia for Digital Transformation Summit. 3 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-20","Item Amount":"214.99"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-20","Item Tax Amount":"4.68"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-20","Item Tax Amount":"4.68"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-20","Item Tax Amount":"14.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-20","Item Amount":"55.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-21","Item Amount":"236.06"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-21","Item Tax Amount":"5.14"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-21","Item Tax Amount":"15.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-21","Item Amount":"53.78"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-22","Item Amount":"237.72"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-22","Item Tax Amount":"5.18"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-22","Item Tax Amount":"15.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-22","Item Amount":"69.20"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Jersey City The Heights' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Jersey City The Heights' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_197(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin West Valley City Hunter','MerchantAddress':'784 Morgan Ave, West Valley City, UT 57768, USA','TransactionDate':'2021-10-19',,'Total':'593.71','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OR','Description':'Business trip to Eugene for market expansion. Attended Manufacturing Excellence Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-16","Item Amount":"121.18"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-16","Item Tax Amount":"9.66"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-16","Item Tax Amount":"6.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-16","Item Amount":"61.41"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-17","Item Amount":"123.77"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-17","Item Tax Amount":"9.86"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-17","Item Tax Amount":"6.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-17","Item Amount":"45.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-18","Item Amount":"144.52"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-18","Item Tax Amount":"11.52"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-18","Item Tax Amount":"7.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-18","Item Amount":"45.79"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin West Valley City Hunter' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin West Valley City Hunter' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_198(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Provo Riverwoods','MerchantAddress':'883 Cox Blvd, Provo, UT 32200, USA','TransactionDate':'2020-02-20',,'Total':'584.7','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Corporate trip - Mobile Technology Conference conference in Lafayette. product demos and customer meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-18","Item Amount":"136.71"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-18","Item Tax Amount":"11.67"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-18","Item Tax Amount":"7.78"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-02-18","Item Amount":"174.16"},{"Item Name":"Incidentals","Transaction Date":"2020-02-18","Item Amount":"15.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-18","Item Amount":"35.22"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-19","Item Amount":"136.25"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-19","Item Tax Amount":"11.63"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-19","Item Tax Amount":"7.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-19","Item Amount":"48.47"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Provo Riverwoods' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Provo Riverwoods' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_199(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Surprise Litchfield Park','MerchantAddress':'922 Harbor Blvd, Surprise, AZ 73859, USA','TransactionDate':'2021-12-29',,'Total':'433.22','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Coral Springs for Corporate Strategy Summit. 2 nights stay for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-27","Item Amount":"163.97"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-27","Item Tax Amount":"14.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-27","Item Amount":"41.52"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-28","Item Amount":"152.62"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-28","Item Tax Amount":"13.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-28","Item Amount":"47.21"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Surprise Litchfield Park' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Surprise Litchfield Park' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_200(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Milwaukee Downtown','MerchantAddress':'590 Adams Dr, Milwaukee, WI 93755, USA','TransactionDate':'2020-01-12',,'Total':'698.26','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Hollywood for Quality Assurance Conference. 3 nights stay for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-09","Item Amount":"135.28"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-09","Item Tax Amount":"7.09"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-09","Item Tax Amount":"2.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-09","Item Amount":"76.32"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-10","Item Amount":"153.47"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-10","Item Tax Amount":"8.05"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-10","Item Tax Amount":"2.68"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-10","Item Tax Amount":"2.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-10","Item Amount":"75.54"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-11","Item Amount":"154.51"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-11","Item Tax Amount":"8.10"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-11","Item Tax Amount":"2.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-11","Item Amount":"69.48"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Milwaukee Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Milwaukee Downtown' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_201(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Abilene Downtown','MerchantAddress':'568 Watson St, Abilene, TX 53646, USA','TransactionDate':'2022-04-15',,'Total':'151.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Blockchain Conference conference in Abilene. strategic planning sessions over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-14","Item Amount":"87.81"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-14","Item Tax Amount":"2.47"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-14","Item Tax Amount":"2.47"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-14","Item Tax Amount":"7.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-14","Item Amount":"51.35"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Abilene Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Abilene Downtown' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_202(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Madison Middleton','MerchantAddress':'4493 Johnson Ave, Madison, WI 70408, USA','TransactionDate':'2022-10-15',,'Total':'936.61','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WI','Description':'Corporate trip - Energy Sector Conference conference in Madison. stakeholder reviews and partner meetings over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-11","Item Amount":"180.45"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-11","Item Tax Amount":"9.62"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-11","Item Tax Amount":"14.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-11","Item Amount":"44.29"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-12","Item Amount":"171.58"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-12","Item Tax Amount":"9.15"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-12","Item Tax Amount":"13.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-12","Item Amount":"43.48"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-13","Item Amount":"152.08"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-13","Item Tax Amount":"8.11"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-13","Item Tax Amount":"12.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-13","Item Amount":"55.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-10-14","Item Amount":"157.80"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-14","Item Tax Amount":"8.41"},{"Item Name":"Hotel Tax","Transaction Date":"2022-10-14","Item Tax Amount":"12.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-10-14","Item Amount":"43.46"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Madison Middleton' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Madison Middleton' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_203(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Jersey City Journal Square','MerchantAddress':'4010 Stewart Blvd, Jersey City, NJ 97024, USA','TransactionDate':'2024-01-04',,'Total':'175.35','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company travel - Product Management Summit in Jersey City. 1 business night for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-03","Item Amount":"124.73"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-03","Item Tax Amount":"7.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-03","Item Amount":"26.17"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-01-04","Item Amount":"17.40"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Jersey City Journal Square' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Jersey City Journal Square' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_204(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Charleston West Ashley','MerchantAddress':'3279 Main St, Charleston, SC 32762, USA','TransactionDate':'2024-01-01',,'Total':'1039.87','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'SC','Description':'Business travel to Charleston for Change Management Conference. 4 nights stay for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-28","Item Amount":"191.31"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-28","Item Tax Amount":"15.81"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-28","Item Tax Amount":"10.54"},{"Item Name":"Laundry","Transaction Date":"2023-12-28","Item Amount":"28.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-28","Item Amount":"23.29"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-29","Item Amount":"186.80"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-29","Item Tax Amount":"15.43"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-29","Item Tax Amount":"10.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-29","Item Amount":"27.13"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-30","Item Amount":"204.83"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-30","Item Tax Amount":"16.92"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-30","Item Tax Amount":"11.28"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-30","Item Amount":"32.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-31","Item Amount":"192.00"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-31","Item Tax Amount":"15.86"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-31","Item Tax Amount":"10.58"},{"Item Name":"Gift and Entertainment","Transaction Date":"2023-12-31","Item Amount":"16.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-31","Item Amount":"30.04"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Charleston West Ashley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Charleston West Ashley' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_205(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Elk Grove Laguna Gateway','MerchantAddress':'791 Torres Ave, Elk Grove, CA 77804, USA','TransactionDate':'2020-05-11',,'Total':'333.75','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Elk Grove for E-commerce Summit. 1 night stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-10","Item Amount":"116.13"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-10","Item Tax Amount":"8.70"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-05-10","Item Amount":"106.37"},{"Item Name":"Laundry","Transaction Date":"2020-05-10","Item Amount":"34.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-10","Item Amount":"37.17"},{"Item Name":"Incidentals","Transaction Date":"2020-05-10","Item Amount":"31.26"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Elk Grove Laguna Gateway' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Elk Grove Laguna Gateway' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_206(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Brownsville Downtown','MerchantAddress':'5479 Martinez Blvd, Brownsville, TX 26214, USA','TransactionDate':'2025-09-22',,'Total':'1276.25','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended IoT Solutions Summit in Brownsville. 4 business nights; merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-09-18","Item Amount":"226.72"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-18","Item Tax Amount":"7.76"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-18","Item Tax Amount":"11.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-09-18","Item Amount":"72.99"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-09-19","Item Amount":"228.29"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-19","Item Tax Amount":"7.81"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-19","Item Tax Amount":"11.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-09-19","Item Amount":"63.80"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-09-20","Item Amount":"236.38"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-20","Item Tax Amount":"8.09"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-20","Item Tax Amount":"12.14"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-09-20","Item Amount":"82.21"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-09-21","Item Amount":"218.97"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-21","Item Tax Amount":"7.50"},{"Item Name":"Hotel Tax","Transaction Date":"2025-09-21","Item Tax Amount":"11.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-09-21","Item Amount":"68.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Brownsville Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Brownsville Downtown' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_207(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Victorville Mall of Victor Valley','MerchantAddress':'611 Peterson Dr, Victorville, CA 23555, USA','TransactionDate':'2022-06-25',,'Total':'490.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - FinTech Conference conference in Victorville. technical workshops and knowledge sharing over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-23","Item Amount":"164.34"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-23","Item Tax Amount":"13.07"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-23","Item Tax Amount":"8.71"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-06-23","Item Amount":"43.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-23","Item Amount":"58.16"},{"Item Name":"Incidentals","Transaction Date":"2022-06-23","Item Amount":"16.40"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-24","Item Amount":"127.92"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-24","Item Tax Amount":"10.17"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-24","Item Tax Amount":"6.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-24","Item Amount":"41.43"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Victorville Mall of Victor Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Victorville Mall of Victor Valley' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_208(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Minneapolis Uptown','MerchantAddress':'8073 Rivera Ave, Minneapolis, MN 58544, USA','TransactionDate':'2022-02-16',,'Total':'663.89','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Business trip to Minneapolis for quarterly reviews. Attended Tech Innovation Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-12","Item Amount":"83.17"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-12","Item Tax Amount":"5.39"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-12","Item Tax Amount":"3.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-12","Item Amount":"45.67"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-13","Item Amount":"85.42"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-13","Item Tax Amount":"5.53"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-13","Item Tax Amount":"3.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-13","Item Amount":"42.31"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-14","Item Amount":"85.32"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-14","Item Tax Amount":"5.53"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-14","Item Tax Amount":"3.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-14","Item Amount":"43.93"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-15","Item Amount":"68.39"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-15","Item Tax Amount":"4.43"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-15","Item Tax Amount":"2.95"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-02-15","Item Amount":"104.17"},{"Item Name":"Incidentals","Transaction Date":"2022-02-15","Item Amount":"26.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-15","Item Amount":"44.31"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Minneapolis Uptown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Minneapolis Uptown' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_209(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Oklahoma City Downtown','MerchantAddress':'8071 Morris Ave, Oklahoma City, OK 57265, USA','TransactionDate':'2021-04-12',,'Total':'646.79','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OK','Description':'Business travel to Oklahoma City for Mobile Technology Conference. 2 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-10","Item Amount":"174.39"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-10","Item Tax Amount":"11.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-10","Item Amount":"83.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-11","Item Amount":"187.27"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-11","Item Tax Amount":"12.45"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-04-11","Item Amount":"98.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-11","Item Amount":"78.50"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Oklahoma City Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Oklahoma City Downtown' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_210(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Fort Worth Cultural District','MerchantAddress':'2975 Collins St, Fort Worth, TX 22094, USA','TransactionDate':'2025-07-06',,'Total':'1311.72','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Fort Worth for FinTech Conference. 4 nights stay for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-02","Item Amount":"249.04"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-02","Item Tax Amount":"5.26"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-02","Item Tax Amount":"15.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-02","Item Amount":"66.92"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-03","Item Amount":"243.32"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-03","Item Tax Amount":"5.14"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-03","Item Tax Amount":"15.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-03","Item Amount":"65.78"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-04","Item Amount":"246.05"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-04","Item Tax Amount":"5.20"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-04","Item Tax Amount":"15.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-04","Item Amount":"52.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-05","Item Amount":"234.04"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-05","Item Tax Amount":"4.95"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-05","Item Tax Amount":"14.84"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-05","Item Amount":"71.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Fort Worth Cultural District' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Fort Worth Cultural District' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_211(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Midland University','MerchantAddress':'5183 Cox Blvd, Midland, TX 40025, USA','TransactionDate':'2023-12-13',,'Total':'1324.25','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Healthcare IT Summit in Midland. 4 business nights; product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-09","Item Amount":"231.08"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-09","Item Tax Amount":"6.11"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-09","Item Tax Amount":"18.34"},{"Item Name":"Incidentals","Transaction Date":"2023-12-09","Item Amount":"19.11"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-09","Item Amount":"68.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-10","Item Amount":"239.65"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-10","Item Tax Amount":"6.34"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-10","Item Tax Amount":"6.34"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-10","Item Tax Amount":"19.02"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-12-10","Item Amount":"22.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-10","Item Amount":"69.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-11","Item Amount":"232.81"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-11","Item Tax Amount":"6.16"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-11","Item Tax Amount":"6.16"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-11","Item Tax Amount":"18.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-11","Item Amount":"70.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-12","Item Amount":"204.01"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-12","Item Tax Amount":"5.40"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-12","Item Tax Amount":"5.40"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-12","Item Tax Amount":"16.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-12","Item Amount":"52.95"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Midland University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Midland University' have all 21 required itemizations'?,",
#     )


# def test_expense_hotel_212(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Aurora Fox Valley','MerchantAddress':'6920 Walker St, Aurora, IL 87865, USA','TransactionDate':'2022-01-12',,'Total':'821.78','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Corporate trip - FinTech Conference conference in Aurora. board meetings and investor presentations over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-09","Item Amount":"198.73"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-09","Item Tax Amount":"9.96"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-09","Item Tax Amount":"14.94"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-01-09","Item Amount":"24.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-09","Item Amount":"35.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-10","Item Amount":"201.29"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-10","Item Tax Amount":"10.09"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-10","Item Tax Amount":"15.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-10","Item Amount":"35.16"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-11","Item Amount":"203.31"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-11","Item Tax Amount":"10.19"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-11","Item Tax Amount":"15.28"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-11","Item Amount":"48.08"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Aurora Fox Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Aurora Fox Valley' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_213(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Ann Arbor University of Michigan','MerchantAddress':'5196 Moore St, Ann Arbor, MI 47754, USA','TransactionDate':'2021-03-15',,'Total':'148.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Business travel to Ann Arbor for Data Science Summit. 1 night stay for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-14","Item Amount":"118.34"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-14","Item Tax Amount":"6.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-14","Item Amount":"23.35"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Ann Arbor University of Michigan' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Ann Arbor University of Michigan' have all 3 required itemizations'?,",
#     )


# def test_expense_hotel_214(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Brownsville Los Fresnos','MerchantAddress':'2720 Nelson St, Brownsville, TX 11664, USA','TransactionDate':'2021-12-08',,'Total':'493.18','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company travel - HR Leadership Summit in Brownsville. 4 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-04","Item Amount":"63.98"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-04","Item Tax Amount":"3.59"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-04","Item Tax Amount":"5.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-04","Item Amount":"47.16"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-05","Item Amount":"69.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-05","Item Tax Amount":"3.91"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-05","Item Tax Amount":"5.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-05","Item Amount":"49.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-06","Item Amount":"66.64"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-06","Item Tax Amount":"3.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-06","Item Tax Amount":"5.61"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-06","Item Amount":"41.09"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-07","Item Amount":"74.34"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-07","Item Tax Amount":"4.17"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-07","Item Tax Amount":"6.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-07","Item Amount":"42.56"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Brownsville Los Fresnos' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Brownsville Los Fresnos' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_215(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Stamford Airport','MerchantAddress':'5005 Airport Blvd, Stamford, CT 52041, USA','TransactionDate':'2024-09-04',,'Total':'803.19','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CT','Description':'Business travel to Stamford for HR Leadership Summit. 3 nights stay for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-01","Item Amount":"155.66"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-01","Item Tax Amount":"9.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-01","Item Amount":"87.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-02","Item Amount":"164.80"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-02","Item Tax Amount":"9.73"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-09-02","Item Amount":"18.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-02","Item Amount":"89.89"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-03","Item Amount":"164.08"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-03","Item Tax Amount":"9.69"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-09-03","Item Amount":"7.61"},{"Item Name":"Incidentals","Transaction Date":"2024-09-03","Item Amount":"16.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-03","Item Amount":"69.96"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Stamford Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Stamford Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_216(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Visalia Downtown','MerchantAddress':'3617 Union St, Visalia, CA 67143, USA','TransactionDate':'2025-08-13',,'Total':'722.04','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended E-commerce Summit in Visalia. 2 business nights; sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-08-11","Item Amount":"285.97"},{"Item Name":"Hotel Tax","Transaction Date":"2025-08-11","Item Tax Amount":"17.51"},{"Item Name":"Hotel Tax","Transaction Date":"2025-08-11","Item Tax Amount":"11.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-08-11","Item Amount":"56.34"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-08-12","Item Amount":"271.63"},{"Item Name":"Hotel Tax","Transaction Date":"2025-08-12","Item Tax Amount":"16.63"},{"Item Name":"Hotel Tax","Transaction Date":"2025-08-12","Item Tax Amount":"11.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-08-12","Item Amount":"38.92"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-08-13","Item Amount":"12.28"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Visalia Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Visalia Downtown' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_217(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Boise Airport','MerchantAddress':'8175 Brooks Ave, Boise, ID 10981, USA','TransactionDate':'2023-07-12',,'Total':'853.1','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'ID','Description':'Corporate trip - Data Science Summit conference in Boise. operational excellence workshops over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-10","Item Amount":"309.61"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-10","Item Tax Amount":"24.49"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-10","Item Tax Amount":"8.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-10","Item Amount":"66.55"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-11","Item Amount":"313.95"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-11","Item Tax Amount":"24.83"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-11","Item Tax Amount":"8.28"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-11","Item Tax Amount":"8.28"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-07-11","Item Amount":"14.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-11","Item Amount":"57.18"},{"Item Name":"Incidentals","Transaction Date":"2023-07-11","Item Amount":"17.32"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Boise Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Boise Airport' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_218(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Richmond Downtown','MerchantAddress':'2827 Morales Blvd, Richmond, CA 38250, USA','TransactionDate':'2021-09-14',,'Total':'937.04','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Data Science Summit in Richmond. 3 business nights for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-11","Item Amount":"198.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-11","Item Tax Amount":"17.70"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-11","Item Tax Amount":"11.80"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-11","Item Amount":"53.61"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-12","Item Amount":"193.51"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-12","Item Tax Amount":"17.29"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-12","Item Tax Amount":"11.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-12","Item Amount":"53.20"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-13","Item Amount":"225.88"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-13","Item Tax Amount":"20.18"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-13","Item Tax Amount":"13.45"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-09-13","Item Amount":"71.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-13","Item Amount":"49.30"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Richmond Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Richmond Downtown' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_219(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Pittsburgh Downtown','MerchantAddress':'6978 Richardson Ave, Pittsburgh, PA 11092, USA','TransactionDate':'2021-09-21',,'Total':'947.85','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'PA','Description':'Corporate trip - Manufacturing Excellence Summit conference in Pittsburgh. team building and training sessions over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-18","Item Amount":"248.43"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-18","Item Tax Amount":"14.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-18","Item Amount":"62.44"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-19","Item Amount":"237.00"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-19","Item Tax Amount":"13.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-19","Item Amount":"65.87"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-20","Item Amount":"233.02"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-20","Item Tax Amount":"13.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-20","Item Amount":"60.33"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Pittsburgh Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Pittsburgh Downtown' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_220(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Palmdale Palmdale Boulevard','MerchantAddress':'1377 Lincoln Blvd, Palmdale, CA 20856, USA','TransactionDate':'2024-12-27',,'Total':'289.57','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Marketing Analytics Summit conference in Palmdale. merger and acquisition discussions over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-26","Item Amount":"213.22"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-26","Item Tax Amount":"18.97"},{"Item Name":"Incidentals","Transaction Date":"2024-12-26","Item Amount":"22.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-26","Item Amount":"35.09"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Palmdale Palmdale Boulevard' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Palmdale Palmdale Boulevard' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_221(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Newark North Ward','MerchantAddress':'8952 Ross Ave, Newark, NJ 49414, USA','TransactionDate':'2023-12-30',,'Total':'985.73','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company business trip - Attended Enterprise Software Summit in Newark. 3 business nights; board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-27","Item Amount":"225.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-27","Item Tax Amount":"13.05"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-27","Item Tax Amount":"4.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-27","Item Amount":"57.78"},{"Item Name":"Incidentals","Transaction Date":"2023-12-27","Item Amount":"19.14"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-28","Item Amount":"249.67"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-28","Item Tax Amount":"4.82"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-28","Item Tax Amount":"14.47"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-28","Item Tax Amount":"4.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-28","Item Amount":"64.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-29","Item Amount":"220.95"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-29","Item Tax Amount":"12.81"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-29","Item Tax Amount":"4.27"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-12-29","Item Amount":"19.61"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-29","Item Amount":"70.12"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Newark North Ward' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Newark North Ward' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_222(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Salt Lake City Airport','MerchantAddress':'480 Moore St, Salt Lake City, UT 10122, USA','TransactionDate':'2025-01-20',,'Total':'201.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Company business trip - Attended Project Management Summit in Salt Lake City. 1 business night; team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-19","Item Amount":"148.93"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-19","Item Tax Amount":"4.19"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-19","Item Tax Amount":"12.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-19","Item Amount":"35.61"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Salt Lake City Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Salt Lake City Airport' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_223(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Visalia Sequoia Mall','MerchantAddress':'2154 Taylor Ave, Visalia, CA 37781, USA','TransactionDate':'2020-11-15',,'Total':'590.42','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Visalia for Business Intelligence Summit. 3 nights stay for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-12","Item Amount":"82.12"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-12","Item Tax Amount":"5.58"},{"Item Name":"Entertainment External","Transaction Date":"2020-11-12","Item Amount":"82.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-12","Item Amount":"66.44"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-13","Item Amount":"96.76"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-13","Item Tax Amount":"6.57"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-11-13","Item Amount":"15.19"},{"Item Name":"Incidentals","Transaction Date":"2020-11-13","Item Amount":"13.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-13","Item Amount":"68.78"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-14","Item Amount":"84.85"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-14","Item Tax Amount":"5.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-14","Item Amount":"62.48"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Visalia Sequoia Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Visalia Sequoia Mall' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_224(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Fairfield Suisun City','MerchantAddress':'3668 Sullivan Ave, Fairfield, CA 93988, USA','TransactionDate':'2023-09-16',,'Total':'459.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Manufacturing Excellence Summit in Fairfield. 1 business night for client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-15","Item Amount":"170.45"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-15","Item Tax Amount":"10.42"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-15","Item Tax Amount":"6.95"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-09-15","Item Amount":"186.97"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-09-15","Item Amount":"16.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-15","Item Amount":"67.87"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Fairfield Suisun City' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Fairfield Suisun City' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_225(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Woodbridge Colonia','MerchantAddress':'5514 Martinez Blvd, Woodbridge, NJ 77107, USA','TransactionDate':'2019-05-25',,'Total':'851.38','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company business trip - Attended Real Estate Investment Summit in Woodbridge. 3 business nights; customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-05-22","Item Amount":"187.26"},{"Item Name":"Hotel Tax","Transaction Date":"2019-05-22","Item Tax Amount":"15.53"},{"Item Name":"Hotel Tax","Transaction Date":"2019-05-22","Item Tax Amount":"10.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-05-22","Item Amount":"37.84"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-05-23","Item Amount":"216.45"},{"Item Name":"Hotel Tax","Transaction Date":"2019-05-23","Item Tax Amount":"17.95"},{"Item Name":"Hotel Tax","Transaction Date":"2019-05-23","Item Tax Amount":"11.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-05-23","Item Amount":"50.05"},{"Item Name":"Incidentals","Transaction Date":"2019-05-23","Item Amount":"47.31"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-05-24","Item Amount":"190.24"},{"Item Name":"Hotel Tax","Transaction Date":"2019-05-24","Item Tax Amount":"15.78"},{"Item Name":"Hotel Tax","Transaction Date":"2019-05-24","Item Tax Amount":"10.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-05-24","Item Amount":"40.12"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Woodbridge Colonia' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Woodbridge Colonia' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_226(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Warren Downtown','MerchantAddress':'9842 Ramirez Blvd, Warren, MI 44113, USA','TransactionDate':'2021-03-11',,'Total':'911.09','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Corporate trip - HR Leadership Summit conference in Warren. partnership development meetings over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-08","Item Amount":"260.57"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-08","Item Tax Amount":"12.89"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-08","Item Tax Amount":"8.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-08","Item Amount":"39.22"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-09","Item Amount":"251.83"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-09","Item Tax Amount":"12.46"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-09","Item Tax Amount":"8.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-09","Item Amount":"23.52"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-10","Item Amount":"244.26"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-10","Item Tax Amount":"12.09"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-10","Item Tax Amount":"8.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-10","Item Amount":"29.28"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Warren Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Warren Downtown' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_227(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Thousand Oaks The Oaks','MerchantAddress':'5938 Thomas St, Thousand Oaks, CA 61444, USA','TransactionDate':'2024-08-21',,'Total':'328.15','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Thousand Oaks for HR Leadership Summit. 1 night stay for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-08-20","Item Amount":"225.21"},{"Item Name":"Hotel Tax","Transaction Date":"2024-08-20","Item Tax Amount":"15.35"},{"Item Name":"Hotel Tax","Transaction Date":"2024-08-20","Item Tax Amount":"5.12"},{"Item Name":"Hotel Tax","Transaction Date":"2024-08-20","Item Tax Amount":"5.12"},{"Item Name":"Incidentals","Transaction Date":"2024-08-20","Item Amount":"43.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-08-20","Item Amount":"33.46"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Thousand Oaks The Oaks' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Thousand Oaks The Oaks' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_228(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Chattanooga Downtown','MerchantAddress':'2098 Wilson Way, Chattanooga, TN 87358, USA','TransactionDate':'2024-12-29',,'Total':'294.7','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company travel - Corporate Strategy Summit in Chattanooga. 1 business night for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-28","Item Amount":"240.51"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-28","Item Tax Amount":"10.88"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-28","Item Tax Amount":"16.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-28","Item Amount":"26.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Chattanooga Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Chattanooga Downtown' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_229(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Buffalo Elmwood Village','MerchantAddress':'5757 Executive Way, Buffalo, NY 73652, USA','TransactionDate':'2022-07-23',,'Total':'1106.68','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Company travel - Analytics Leadership Summit in Buffalo. 4 business nights for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-19","Item Amount":"149.56"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-19","Item Tax Amount":"9.29"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-19","Item Tax Amount":"6.20"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-07-19","Item Amount":"82.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-19","Item Amount":"81.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-20","Item Amount":"163.37"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-20","Item Tax Amount":"10.15"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-20","Item Tax Amount":"6.77"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-20","Item Amount":"76.64"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-21","Item Amount":"165.78"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-21","Item Tax Amount":"10.30"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-21","Item Tax Amount":"6.87"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-21","Item Amount":"71.29"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-22","Item Amount":"173.27"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-22","Item Tax Amount":"10.77"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-22","Item Tax Amount":"7.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-22","Item Amount":"74.94"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Buffalo Elmwood Village' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Buffalo Elmwood Village' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_230(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Salinas Northridge Mall','MerchantAddress':'8134 Bell St, Salinas, CA 11522, USA','TransactionDate':'2022-01-19',,'Total':'839.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Manufacturing Excellence Summit conference in Salinas. team building and training sessions over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-15","Item Amount":"156.74"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-15","Item Tax Amount":"9.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-15","Item Amount":"49.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-16","Item Amount":"122.41"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-16","Item Tax Amount":"7.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-16","Item Amount":"71.23"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-17","Item Amount":"134.13"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-17","Item Tax Amount":"8.06"},{"Item Name":"Laundry","Transaction Date":"2022-01-17","Item Amount":"34.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-17","Item Amount":"61.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-18","Item Amount":"125.03"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-18","Item Tax Amount":"7.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-18","Item Amount":"52.45"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Salinas Northridge Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Salinas Northridge Mall' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_231(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Clearwater Downtown','MerchantAddress':'6601 James Ave, Clearwater, FL 79570, USA','TransactionDate':'2019-11-19',,'Total':'1026.77','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Corporate trip - Digital Transformation Summit conference in Clearwater. partnership development meetings over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-16","Item Amount":"239.86"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-16","Item Tax Amount":"16.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-16","Item Amount":"92.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-17","Item Amount":"236.39"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-17","Item Tax Amount":"16.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-17","Item Amount":"71.42"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-18","Item Amount":"247.39"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-18","Item Tax Amount":"16.74"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-11-18","Item Amount":"7.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-18","Item Amount":"83.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Clearwater Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Clearwater Downtown' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_232(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Denver LoDo','MerchantAddress':'3063 Flores St, Denver, CO 36357, USA','TransactionDate':'2021-04-25',,'Total':'393.24','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Business travel to Denver for Cloud Computing Expo. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-23","Item Amount":"114.53"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-23","Item Tax Amount":"9.80"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-23","Item Tax Amount":"3.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-23","Item Amount":"36.22"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-24","Item Amount":"93.10"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-24","Item Tax Amount":"7.97"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-24","Item Tax Amount":"2.66"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-04-24","Item Amount":"79.32"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-04-24","Item Amount":"21.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-24","Item Amount":"24.94"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Denver LoDo' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Denver LoDo' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_233(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni San Jose Silicon Valley','MerchantAddress':'3074 Elm Ave, San Jose, CA 25100, USA','TransactionDate':'2020-11-19',,'Total':'452.45','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Energy Sector Conference conference in San Jose. vendor negotiations and contract reviews over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-17","Item Amount":"151.03"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-17","Item Tax Amount":"12.50"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-17","Item Tax Amount":"4.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-17","Item Amount":"48.54"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-18","Item Amount":"176.77"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-18","Item Tax Amount":"14.64"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-18","Item Tax Amount":"4.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-18","Item Amount":"39.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni San Jose Silicon Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni San Jose Silicon Valley' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_234(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Sacramento Airport','MerchantAddress':'5669 Ward Ave, Sacramento, CA 84933, USA','TransactionDate':'2023-03-25',,'Total':'891.37','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Quality Assurance Conference in Sacramento. 4 business nights for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-21","Item Amount":"146.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-21","Item Tax Amount":"7.88"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-21","Item Tax Amount":"5.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-21","Item Amount":"78.98"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-22","Item Amount":"113.39"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-22","Item Tax Amount":"6.11"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-22","Item Tax Amount":"4.08"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-22","Item Amount":"90.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-23","Item Amount":"121.02"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-23","Item Tax Amount":"6.53"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-23","Item Tax Amount":"4.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-23","Item Amount":"88.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-24","Item Amount":"122.77"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-24","Item Tax Amount":"6.62"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-24","Item Tax Amount":"4.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-24","Item Amount":"84.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Sacramento Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Sacramento Airport' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_235(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Minneapolis Downtown','MerchantAddress':'2874 Rivera Ave, Minneapolis, MN 15410, USA','TransactionDate':'2025-11-12',,'Total':'868.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Company travel - Marketing Analytics Summit in Minneapolis. 4 business nights for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-08","Item Amount":"114.93"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-08","Item Tax Amount":"8.14"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-08","Item Amount":"74.90"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-09","Item Amount":"105.18"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-09","Item Tax Amount":"7.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-09","Item Amount":"62.47"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-10","Item Amount":"126.82"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-10","Item Tax Amount":"8.98"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-11-10","Item Amount":"23.86"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-11-10","Item Amount":"85.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-10","Item Amount":"68.32"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-11","Item Amount":"103.65"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-11","Item Tax Amount":"7.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-11","Item Amount":"70.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Minneapolis Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Minneapolis Downtown' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_236(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Torrance Rolling Hills','MerchantAddress':'6062 Stewart Blvd, Torrance, CA 49671, USA','TransactionDate':'2024-07-06',,'Total':'1103.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Marketing Analytics Summit in Torrance. 4 business nights; quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-02","Item Amount":"180.75"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-02","Item Tax Amount":"13.96"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-02","Item Tax Amount":"4.65"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-02","Item Tax Amount":"4.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-02","Item Amount":"56.74"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-03","Item Amount":"180.12"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-03","Item Tax Amount":"13.91"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-03","Item Tax Amount":"4.64"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-07-03","Item Amount":"94.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-03","Item Amount":"42.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-04","Item Amount":"198.82"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-04","Item Tax Amount":"15.35"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-04","Item Tax Amount":"5.12"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-04","Item Tax Amount":"5.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-04","Item Amount":"49.88"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-07-05","Item Amount":"169.79"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-05","Item Tax Amount":"13.11"},{"Item Name":"Hotel Tax","Transaction Date":"2024-07-05","Item Tax Amount":"4.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-07-05","Item Amount":"44.93"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Torrance Rolling Hills' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Torrance Rolling Hills' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_237(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Mobile Airport','MerchantAddress':'9675 Taylor Ave, Mobile, AL 12802, USA','TransactionDate':'2021-03-06',,'Total':'1268.74','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AL','Description':'Company travel - Legal Technology Conference in Mobile. 4 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-02","Item Amount":"176.54"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-02","Item Tax Amount":"15.33"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-02","Item Tax Amount":"5.11"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-03-02","Item Amount":"176.43"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-03-02","Item Amount":"16.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-02","Item Amount":"77.08"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-03","Item Amount":"185.81"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-03","Item Tax Amount":"16.14"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-03","Item Tax Amount":"5.38"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-03","Item Tax Amount":"5.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-03","Item Amount":"59.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-04","Item Amount":"177.37"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-04","Item Tax Amount":"15.40"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-04","Item Tax Amount":"5.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-04","Item Amount":"61.16"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-05","Item Amount":"172.36"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-05","Item Tax Amount":"14.97"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-05","Item Tax Amount":"4.99"},{"Item Name":"Incidentals","Transaction Date":"2021-03-05","Item Amount":"13.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-05","Item Amount":"64.72"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Mobile Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Mobile Airport' have all 20 required itemizations'?,",
#     )


# def test_expense_hotel_238(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Fort Worth Downtown','MerchantAddress':'6092 Water St, Fort Worth, TX 15523, USA','TransactionDate':'2020-10-06',,'Total':'416.91','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Tech Innovation Conference in Fort Worth. 2 business nights; merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-04","Item Amount":"137.21"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-04","Item Tax Amount":"6.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-04","Item Amount":"62.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-05","Item Amount":"150.13"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-05","Item Tax Amount":"7.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-05","Item Amount":"52.96"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Fort Worth Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Fort Worth Downtown' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_239(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Wichita Downtown','MerchantAddress':'8102 Martinez Blvd, Wichita, KS 62125, USA','TransactionDate':'2019-06-17',,'Total':'1144.96','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'KS','Description':'Corporate trip - Cybersecurity Conference conference in Wichita. vendor negotiations and contract reviews over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-15","Item Amount":"340.81"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-15","Item Tax Amount":"7.17"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-15","Item Tax Amount":"21.52"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-15","Item Tax Amount":"7.17"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-06-15","Item Amount":"117.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-15","Item Amount":"87.80"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-16","Item Amount":"325.78"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-16","Item Tax Amount":"6.86"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-16","Item Tax Amount":"20.57"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-16","Item Tax Amount":"6.86"},{"Item Name":"Hotel Deposit","Transaction Date":"2019-06-16","Item Amount":"100.75"},{"Item Name":"Incidentals","Transaction Date":"2019-06-16","Item Amount":"12.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-16","Item Amount":"89.47"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Wichita Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Wichita Downtown' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_240(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Omaha Airport','MerchantAddress':'2155 Peterson Dr, Omaha, NE 46319, USA','TransactionDate':'2022-11-16',,'Total':'389.04','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NE','Description':'Corporate trip - Analytics Leadership Summit conference in Omaha. customer support and service reviews over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-14","Item Amount":"94.11"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-14","Item Tax Amount":"1.74"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-14","Item Tax Amount":"5.21"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-14","Item Tax Amount":"1.74"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-14","Item Amount":"43.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-15","Item Amount":"100.69"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-15","Item Tax Amount":"1.86"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-15","Item Tax Amount":"5.58"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-15","Item Tax Amount":"1.86"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-11-15","Item Amount":"90.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-15","Item Amount":"42.28"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Omaha Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Omaha Airport' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_241(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Embassy Suites Abilene Mall of Abilene','MerchantAddress':'7526 Roberts Dr, Abilene, TX 36939, USA','TransactionDate':'2022-01-13',,'Total':'270.78','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Digital Transformation Summit in Abilene. 2 business nights; team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-11","Item Amount":"100.87"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-11","Item Tax Amount":"6.91"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-11","Item Amount":"18.38"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-12","Item Amount":"117.82"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-12","Item Tax Amount":"8.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-12","Item Amount":"18.73"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Embassy Suites Abilene Mall of Abilene' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Embassy Suites Abilene Mall of Abilene' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_242(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Riverside Downtown','MerchantAddress':'9615 Rodriguez Dr, Riverside, CA 48440, USA','TransactionDate':'2024-12-11',,'Total':'685.96','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Blockchain Conference conference in Riverside. client sessions and project planning over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-09","Item Amount":"233.95"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-09","Item Tax Amount":"11.99"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-09","Item Tax Amount":"4.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-09","Item Amount":"57.61"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-10","Item Amount":"203.02"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-10","Item Tax Amount":"10.40"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-10","Item Tax Amount":"3.47"},{"Item Name":"Entertainment External","Transaction Date":"2024-12-10","Item Amount":"55.39"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-12-10","Item Amount":"14.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-10","Item Amount":"66.73"},{"Item Name":"Incidentals","Transaction Date":"2024-12-10","Item Amount":"24.44"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Riverside Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Riverside Downtown' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_243(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Buffalo Amherst','MerchantAddress':'4756 Maple Dr, Buffalo, NY 17535, USA','TransactionDate':'2025-06-30',,'Total':'959.51','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Business trip to Buffalo for investor relations. Attended Real Estate Investment Summit. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-26","Item Amount":"172.01"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-26","Item Tax Amount":"13.22"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-26","Item Tax Amount":"8.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-26","Item Amount":"57.85"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-27","Item Amount":"170.04"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-27","Item Tax Amount":"13.07"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-27","Item Tax Amount":"8.71"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-27","Item Amount":"50.93"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-28","Item Amount":"167.16"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-28","Item Tax Amount":"12.85"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-28","Item Tax Amount":"8.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-28","Item Amount":"53.21"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-29","Item Amount":"162.59"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-29","Item Tax Amount":"12.50"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-29","Item Tax Amount":"8.33"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-29","Item Amount":"39.67"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Buffalo Amherst' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Buffalo Amherst' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_244(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Moreno Valley Canyon Springs','MerchantAddress':'391 Ortiz St, Moreno Valley, CA 43930, USA','TransactionDate':'2021-06-24',,'Total':'248.42','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended HR Leadership Summit in Moreno Valley. 1 business night; product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-23","Item Amount":"159.57"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-23","Item Tax Amount":"11.70"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-23","Item Tax Amount":"7.80"},{"Item Name":"Laundry","Transaction Date":"2021-06-23","Item Amount":"29.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-23","Item Amount":"39.71"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Moreno Valley Canyon Springs' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Moreno Valley Canyon Springs' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_245(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Louisville Downtown','MerchantAddress':'9278 Long Ave, Louisville, KY 14497, USA','TransactionDate':'2022-09-09',,'Total':'386.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'KY','Description':'Company business trip - Attended HR Leadership Summit in Louisville. 1 business night; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-08","Item Amount":"230.02"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-08","Item Tax Amount":"4.28"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-08","Item Tax Amount":"4.28"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-08","Item Tax Amount":"12.83"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-09-08","Item Amount":"39.07"},{"Item Name":"Incidentals","Transaction Date":"2022-09-08","Item Amount":"29.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-08","Item Amount":"66.38"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Louisville Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Louisville Downtown' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_246(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Eugene Gateway','MerchantAddress':'9714 Cox Blvd, Eugene, OR 52401, USA','TransactionDate':'2024-10-26',,'Total':'377.19','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OR','Description':'Company travel - Quality Assurance Conference in Eugene. 1 business night for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-25","Item Amount":"248.06"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-25","Item Tax Amount":"12.66"},{"Item Name":"Laundry","Transaction Date":"2024-10-25","Item Amount":"37.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-25","Item Amount":"53.93"},{"Item Name":"Incidentals","Transaction Date":"2024-10-25","Item Amount":"25.15"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Eugene Gateway' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Eugene Gateway' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_247(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Corpus Christi Flour Bluff','MerchantAddress':'8246 Butler St, Corpus Christi, TX 80448, USA','TransactionDate':'2025-06-09',,'Total':'747.38','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to Corpus Christi for strategic planning. Attended IoT Solutions Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-06","Item Amount":"148.06"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-06","Item Tax Amount":"7.04"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-06","Item Tax Amount":"10.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-06","Item Amount":"80.17"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-07","Item Amount":"144.45"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-07","Item Tax Amount":"6.87"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-07","Item Tax Amount":"10.30"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-07","Item Amount":"97.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-08","Item Amount":"138.14"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-08","Item Tax Amount":"6.57"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-08","Item Tax Amount":"9.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-08","Item Amount":"88.12"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Corpus Christi Flour Bluff' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Corpus Christi Flour Bluff' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_248(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Elk Grove Laguna Gateway','MerchantAddress':'7221 Main St, Elk Grove, CA 73765, USA','TransactionDate':'2020-12-29',,'Total':'514.78','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Digital Marketing Conference in Elk Grove. 3 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-26","Item Amount":"99.68"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-26","Item Tax Amount":"5.71"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-26","Item Amount":"33.13"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-27","Item Amount":"93.08"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-27","Item Tax Amount":"5.33"},{"Item Name":"Entertainment External","Transaction Date":"2020-12-27","Item Amount":"62.23"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-12-27","Item Amount":"24.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-27","Item Amount":"34.68"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-28","Item Amount":"108.10"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-28","Item Tax Amount":"6.19"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-12-28","Item Amount":"17.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-28","Item Amount":"25.34"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Elk Grove Laguna Gateway' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Elk Grove Laguna Gateway' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_249(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Cape Coral Downtown','MerchantAddress':'4023 Barnes Ave, Cape Coral, FL 80584, USA','TransactionDate':'2024-12-12',,'Total':'810.56','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company travel - Product Management Summit in Cape Coral. 3 business nights for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-09","Item Amount":"197.13"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-09","Item Tax Amount":"4.42"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-09","Item Tax Amount":"13.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-09","Item Amount":"48.81"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-10","Item Amount":"189.69"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-10","Item Tax Amount":"4.26"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-10","Item Tax Amount":"12.77"},{"Item Name":"Laundry","Transaction Date":"2024-12-10","Item Amount":"29.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-10","Item Amount":"64.56"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-12-11","Item Amount":"162.25"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-11","Item Tax Amount":"3.64"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-11","Item Tax Amount":"10.92"},{"Item Name":"Hotel Tax","Transaction Date":"2024-12-11","Item Tax Amount":"3.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-12-11","Item Amount":"65.63"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Cape Coral Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Cape Coral Downtown' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_250(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni North Las Vegas Eldorado','MerchantAddress':'9261 Harris Blvd, North Las Vegas, NV 47581, USA','TransactionDate':'2019-08-06',,'Total':'386.48','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NV','Description':'Company travel - Retail Innovation Conference in North Las Vegas. 1 business night for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-08-05","Item Amount":"283.90"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-05","Item Tax Amount":"16.36"},{"Item Name":"Hotel Tax","Transaction Date":"2019-08-05","Item Tax Amount":"24.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-08-05","Item Amount":"61.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni North Las Vegas Eldorado' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni North Las Vegas Eldorado' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_251(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree West Jordan Herriman','MerchantAddress':'2174 Diaz St, West Jordan, UT 53856, USA','TransactionDate':'2025-04-26',,'Total':'674.65','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Business travel to West Jordan for AI & Machine Learning Conference. 2 nights stay for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-24","Item Amount":"237.98"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-24","Item Tax Amount":"6.89"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-24","Item Tax Amount":"20.67"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-04-24","Item Amount":"80.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-24","Item Amount":"27.02"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-25","Item Amount":"211.04"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-25","Item Tax Amount":"6.11"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-25","Item Tax Amount":"18.33"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-25","Item Amount":"47.67"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-04-26","Item Amount":"18.25"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree West Jordan Herriman' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree West Jordan Herriman' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_252(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Columbia University of Missouri','MerchantAddress':'2440 Ross Ave, Columbia, MO 33137, USA','TransactionDate':'2025-06-10',,'Total':'986','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MO','Description':'Company business trip - Attended Healthcare IT Summit in Columbia. 3 business nights; sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-07","Item Amount":"207.85"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-07","Item Tax Amount":"6.13"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-07","Item Tax Amount":"18.40"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-07","Item Tax Amount":"6.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-07","Item Amount":"72.37"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-08","Item Amount":"203.27"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-08","Item Tax Amount":"17.99"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-08","Item Tax Amount":"6.00"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-06-08","Item Amount":"14.84"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-08","Item Amount":"49.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-09","Item Amount":"212.50"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-09","Item Tax Amount":"18.81"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-09","Item Tax Amount":"6.27"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-06-09","Item Amount":"82.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-09","Item Amount":"62.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Columbia University of Missouri' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Columbia University of Missouri' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_253(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western St. Paul Grand Avenue','MerchantAddress':'4345 Convention Center Dr, St. Paul, MN 82905, USA','TransactionDate':'2019-01-07',,'Total':'487.03','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Business trip to St. Paul for technology implementation. Attended Digital Transformation Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-05","Item Amount":"156.94"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-05","Item Tax Amount":"11.40"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-05","Item Tax Amount":"7.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-05","Item Amount":"69.40"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-06","Item Amount":"152.10"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-06","Item Tax Amount":"11.05"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-06","Item Tax Amount":"7.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-06","Item Amount":"71.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western St. Paul Grand Avenue' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western St. Paul Grand Avenue' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_254(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Santa Rosa Bennett Valley','MerchantAddress':'8480 Kelly Dr, Santa Rosa, CA 14428, USA','TransactionDate':'2021-04-28',,'Total':'463.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Santa Rosa for partnership development. Attended IoT Solutions Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-26","Item Amount":"120.58"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-26","Item Tax Amount":"10.39"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-26","Item Tax Amount":"6.93"},{"Item Name":"Incidentals","Transaction Date":"2021-04-26","Item Amount":"47.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-26","Item Amount":"66.41"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-27","Item Amount":"121.84"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-27","Item Tax Amount":"10.50"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-27","Item Tax Amount":"7.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-27","Item Amount":"71.95"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Santa Rosa Bennett Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Santa Rosa Bennett Valley' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_255(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Glendale Americana','MerchantAddress':'6295 Taylor Ave, Glendale, CA 55574, USA','TransactionDate':'2020-05-06',,'Total':'711.46','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Glendale for Digital Transformation Summit. 2 nights stay for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-04","Item Amount":"232.45"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-04","Item Tax Amount":"20.33"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-04","Item Tax Amount":"6.78"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-04","Item Tax Amount":"6.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-04","Item Amount":"80.01"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-05","Item Amount":"242.40"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-05","Item Tax Amount":"21.20"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-05","Item Tax Amount":"7.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-05","Item Amount":"94.44"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Glendale Americana' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Glendale Americana' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_256(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Garden Grove Village Green','MerchantAddress':'5399 Richardson Ave, Garden Grove, CA 56418, USA','TransactionDate':'2021-07-27',,'Total':'549.78','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Garden Grove for client meetings. Attended HR Leadership Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-25","Item Amount":"177.07"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-25","Item Tax Amount":"10.01"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-25","Item Tax Amount":"3.34"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-25","Item Tax Amount":"3.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-25","Item Amount":"66.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-26","Item Amount":"164.44"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-26","Item Tax Amount":"9.29"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-26","Item Tax Amount":"3.10"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-07-26","Item Amount":"9.88"},{"Item Name":"Laundry","Transaction Date":"2021-07-26","Item Amount":"27.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-26","Item Amount":"75.79"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Garden Grove Village Green' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Garden Grove Village Green' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_257(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Fremont Newark Border','MerchantAddress':'486 Ortiz St, Fremont, CA 86526, USA','TransactionDate':'2019-09-29',,'Total':'1385.96','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Fremont for client meetings. Attended Customer Experience Summit. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-25","Item Amount":"220.55"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-25","Item Tax Amount":"17.30"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-25","Item Tax Amount":"11.53"},{"Item Name":"Entertainment External","Transaction Date":"2019-09-25","Item Amount":"43.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-25","Item Amount":"76.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-26","Item Amount":"218.00"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-26","Item Tax Amount":"17.10"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-26","Item Tax Amount":"11.40"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-09-26","Item Amount":"13.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-26","Item Amount":"84.88"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-27","Item Amount":"223.81"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-27","Item Tax Amount":"17.55"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-27","Item Tax Amount":"11.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-27","Item Amount":"67.41"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-28","Item Amount":"244.73"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-28","Item Tax Amount":"19.19"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-28","Item Tax Amount":"12.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-28","Item Amount":"74.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Fremont Newark Border' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Fremont Newark Border' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_258(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Eugene Airport','MerchantAddress':'1464 Murphy St, Eugene, OR 61172, USA','TransactionDate':'2021-04-07',,'Total':'774.81','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OR','Description':'Company travel - Manufacturing Excellence Summit in Eugene. 2 business nights for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-05","Item Amount":"293.54"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-05","Item Tax Amount":"11.03"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-05","Item Tax Amount":"16.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-05","Item Amount":"75.55"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-06","Item Amount":"278.95"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-06","Item Tax Amount":"10.48"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-06","Item Tax Amount":"15.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-06","Item Amount":"73.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Eugene Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Eugene Airport' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_259(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Denton Downtown','MerchantAddress':'3744 Mill St, Denton, TX 38485, USA','TransactionDate':'2020-09-06',,'Total':'293.66','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Blockchain Conference conference in Denton. market research and competitive analysis over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-05","Item Amount":"203.89"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-05","Item Tax Amount":"10.98"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-05","Item Tax Amount":"16.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-05","Item Amount":"62.32"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Denton Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Denton Downtown' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_260(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Surprise Litchfield Park','MerchantAddress':'1267 Lewis Ave, Surprise, AZ 77812, USA','TransactionDate':'2025-10-24',,'Total':'382.51','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Corporate trip - Retail Innovation Conference conference in Surprise. stakeholder reviews and partner meetings over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-23","Item Amount":"73.42"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-23","Item Tax Amount":"6.24"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-23","Item Tax Amount":"4.16"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-10-23","Item Amount":"92.40"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-10-23","Item Amount":"143.63"},{"Item Name":"Laundry","Transaction Date":"2025-10-23","Item Amount":"26.77"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-23","Item Amount":"35.89"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Surprise Litchfield Park' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Surprise Litchfield Park' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_261(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Baton Rouge Downtown','MerchantAddress':'2036 Walker St, Baton Rouge, LA 97055, USA','TransactionDate':'2025-07-04',,'Total':'1592.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Company business trip - Attended Data Science Summit in Baton Rouge. 3 business nights; team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-01","Item Amount":"391.98"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-01","Item Tax Amount":"29.76"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-01","Item Tax Amount":"9.92"},{"Item Name":"Entertainment External","Transaction Date":"2025-07-01","Item Amount":"106.30"},{"Item Name":"Laundry","Transaction Date":"2025-07-01","Item Amount":"20.77"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-01","Item Amount":"39.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-02","Item Amount":"381.12"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-02","Item Tax Amount":"28.93"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-02","Item Tax Amount":"9.64"},{"Item Name":"Hotel Telephone","Transaction Date":"2025-07-02","Item Amount":"12.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-02","Item Amount":"60.20"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-07-03","Item Amount":"396.12"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-03","Item Tax Amount":"10.02"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-03","Item Tax Amount":"30.07"},{"Item Name":"Hotel Tax","Transaction Date":"2025-07-03","Item Tax Amount":"10.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-07-03","Item Amount":"55.52"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Baton Rouge Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Baton Rouge Downtown' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_262(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Santa Ana Civic Center','MerchantAddress':'6077 Airport Blvd, Santa Ana, CA 12168, USA','TransactionDate':'2022-09-14',,'Total':'317.09','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Business Intelligence Summit in Santa Ana. 1 business night for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-13","Item Amount":"72.61"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-13","Item Tax Amount":"6.21"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-09-13","Item Amount":"54.23"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-09-13","Item Amount":"142.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-13","Item Amount":"41.91"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Santa Ana Civic Center' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Santa Ana Civic Center' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_263(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Cleveland Airport','MerchantAddress':'1150 James Ave, Cleveland, OH 87205, USA','TransactionDate':'2020-11-27',,'Total':'516.62','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Corporate trip - Digital Transformation Summit conference in Cleveland. market research and competitive analysis over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-25","Item Amount":"181.93"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-25","Item Tax Amount":"12.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-25","Item Amount":"63.24"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-26","Item Amount":"178.91"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-26","Item Tax Amount":"12.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-26","Item Amount":"67.49"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Cleveland Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Cleveland Airport' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_264(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Thornton Eastlake','MerchantAddress':'7418 Wilson Way, Thornton, CO 60464, USA','TransactionDate':'2023-04-22',,'Total':'1479.14','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Corporate trip - DevOps World conference in Thornton. market research and competitive analysis over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-18","Item Amount":"275.24"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-18","Item Tax Amount":"21.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-18","Item Amount":"70.13"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-19","Item Amount":"260.64"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-19","Item Tax Amount":"20.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-19","Item Amount":"84.47"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-20","Item Amount":"257.97"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-20","Item Tax Amount":"20.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-20","Item Amount":"76.76"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-21","Item Amount":"284.85"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-21","Item Tax Amount":"22.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-21","Item Amount":"84.32"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Thornton Eastlake' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Thornton Eastlake' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_265(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft St. Louis Airport','MerchantAddress':'8364 Broadway, St. Louis, MO 51017, USA','TransactionDate':'2025-03-23',,'Total':'862.36','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MO','Description':'Business trip to St. Louis for investor relations. Attended Energy Sector Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-03-20","Item Amount":"241.31"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-20","Item Tax Amount":"15.95"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-20","Item Tax Amount":"5.32"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-20","Item Tax Amount":"5.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-03-20","Item Amount":"33.66"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-03-21","Item Amount":"225.52"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-21","Item Tax Amount":"14.90"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-21","Item Tax Amount":"4.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-03-21","Item Amount":"43.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-03-22","Item Amount":"218.75"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-22","Item Tax Amount":"14.46"},{"Item Name":"Hotel Tax","Transaction Date":"2025-03-22","Item Tax Amount":"4.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-03-22","Item Amount":"34.27"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft St. Louis Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft St. Louis Airport' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_266(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Baltimore Inner Harbor','MerchantAddress':'732 Convention Center Dr, Baltimore, MD 25484, USA','TransactionDate':'2021-12-25',,'Total':'757.34','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MD','Description':'Company travel - Customer Experience Summit in Baltimore. 3 business nights for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-22","Item Amount":"181.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-22","Item Tax Amount":"11.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-22","Item Amount":"53.08"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-23","Item Amount":"205.64"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-23","Item Tax Amount":"12.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-23","Item Amount":"47.26"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-24","Item Amount":"189.72"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-24","Item Tax Amount":"11.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-24","Item Amount":"44.74"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Baltimore Inner Harbor' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Baltimore Inner Harbor' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_267(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Omaha Airport','MerchantAddress':'4367 Young St, Omaha, NE 34157, USA','TransactionDate':'2019-01-27',,'Total':'887.75','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NE','Description':'Business travel to Omaha for E-commerce Summit. 3 nights stay for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-24","Item Amount":"125.23"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-24","Item Tax Amount":"11.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-24","Item Amount":"70.08"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-25","Item Amount":"118.08"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-25","Item Tax Amount":"10.50"},{"Item Name":"Hotel Deposit","Transaction Date":"2019-01-25","Item Amount":"169.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-25","Item Amount":"74.14"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-01-26","Item Amount":"109.59"},{"Item Name":"Hotel Tax","Transaction Date":"2019-01-26","Item Tax Amount":"9.74"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-01-26","Item Amount":"70.63"},{"Item Name":"Incidentals","Transaction Date":"2019-01-26","Item Amount":"38.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-01-26","Item Amount":"80.29"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Omaha Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Omaha Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_268(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Sunnyvale Butcher's Corner','MerchantAddress':'7970 Phillips Ave, Sunnyvale, CA 32904, USA','TransactionDate':'2021-02-09',,'Total':'1015.23','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Business Intelligence Summit in Sunnyvale. 4 business nights; market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-05","Item Amount":"192.97"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-05","Item Tax Amount":"16.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-05","Item Amount":"45.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-06","Item Amount":"187.37"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-06","Item Tax Amount":"15.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-06","Item Amount":"46.20"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-07","Item Amount":"181.46"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-07","Item Tax Amount":"15.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-07","Item Amount":"57.46"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-08","Item Amount":"195.13"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-08","Item Tax Amount":"16.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-08","Item Amount":"44.57"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Sunnyvale Butcher's Corner' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Sunnyvale Butcher's Corner' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_269(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Henderson Gibson','MerchantAddress':'8089 Phillips Ave, Henderson, NV 59112, USA','TransactionDate':'2023-09-30',,'Total':'1114.84','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NV','Description':'Company travel - Supply Chain Management Conference in Henderson. 3 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-27","Item Amount":"261.13"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-27","Item Tax Amount":"23.48"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-27","Item Tax Amount":"15.66"},{"Item Name":"Entertainment External","Transaction Date":"2023-09-27","Item Amount":"54.67"},{"Item Name":"Laundry","Transaction Date":"2023-09-27","Item Amount":"37.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-27","Item Amount":"49.02"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-28","Item Amount":"235.59"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-28","Item Tax Amount":"21.19"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-28","Item Tax Amount":"14.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-28","Item Amount":"50.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-29","Item Amount":"240.50"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-29","Item Tax Amount":"21.63"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-29","Item Tax Amount":"14.42"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-09-29","Item Amount":"16.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-29","Item Amount":"59.16"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Henderson Gibson' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Henderson Gibson' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_270(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Tucson Foothills','MerchantAddress':'6496 Butler St, Tucson, AZ 94328, USA','TransactionDate':'2022-12-19',,'Total':'477.43','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Company business trip - Attended Energy Sector Conference in Tucson. 1 business night; strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-12-18","Item Amount":"210.01"},{"Item Name":"Hotel Tax","Transaction Date":"2022-12-18","Item Tax Amount":"11.50"},{"Item Name":"Hotel Tax","Transaction Date":"2022-12-18","Item Tax Amount":"7.67"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-12-18","Item Amount":"167.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-12-18","Item Amount":"59.96"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-12-19","Item Amount":"20.66"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Tucson Foothills' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Tucson Foothills' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_271(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Salt Lake City Downtown','MerchantAddress':'6748 State St, Salt Lake City, UT 18952, USA','TransactionDate':'2020-04-29',,'Total':'230.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Company business trip - Attended FinTech Conference in Salt Lake City. 1 business night; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-28","Item Amount":"128.72"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-28","Item Tax Amount":"10.54"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-04-28","Item Amount":"22.74"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-28","Item Amount":"68.90"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Salt Lake City Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Salt Lake City Downtown' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_272(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Orange Chapman University','MerchantAddress':'8694 Allen Ave, Orange, CA 10247, USA','TransactionDate':'2020-05-28',,'Total':'955.53','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Orange for Analytics Leadership Summit. 3 nights stay for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-25","Item Amount":"200.64"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-25","Item Tax Amount":"15.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-25","Item Amount":"47.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-26","Item Amount":"192.07"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-26","Item Tax Amount":"14.67"},{"Item Name":"Incidentals","Transaction Date":"2020-05-26","Item Amount":"49.51"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-26","Item Amount":"48.18"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-27","Item Amount":"206.04"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-27","Item Tax Amount":"15.73"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-05-27","Item Amount":"89.69"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-05-27","Item Amount":"14.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-27","Item Amount":"61.29"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Orange Chapman University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Orange Chapman University' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_273(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Santa Clarita Newhall','MerchantAddress':'1626 Cooper St, Santa Clarita, CA 39824, USA','TransactionDate':'2024-02-22',,'Total':'305.33','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Digital Transformation Summit in Santa Clarita. 2 business nights; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-02-20","Item Amount":"94.42"},{"Item Name":"Hotel Tax","Transaction Date":"2024-02-20","Item Tax Amount":"5.80"},{"Item Name":"Hotel Tax","Transaction Date":"2024-02-20","Item Tax Amount":"1.93"},{"Item Name":"Hotel Tax","Transaction Date":"2024-02-20","Item Tax Amount":"1.93"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-02-20","Item Amount":"29.21"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-02-21","Item Amount":"106.87"},{"Item Name":"Hotel Tax","Transaction Date":"2024-02-21","Item Tax Amount":"6.56"},{"Item Name":"Hotel Tax","Transaction Date":"2024-02-21","Item Tax Amount":"2.19"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-02-21","Item Amount":"18.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-02-21","Item Amount":"37.97"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Santa Clarita Newhall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Santa Clarita Newhall' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_274(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn West Palm Beach Downtown','MerchantAddress':'307 Cruz St, West Palm Beach, FL 32178, USA','TransactionDate':'2025-02-23',,'Total':'844.42','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Corporate trip - IoT Solutions Summit conference in West Palm Beach. quarterly business reviews over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-20","Item Amount":"188.65"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-20","Item Tax Amount":"16.39"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-20","Item Tax Amount":"10.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-20","Item Amount":"61.10"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-21","Item Amount":"174.76"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-21","Item Tax Amount":"15.18"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-21","Item Tax Amount":"10.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-21","Item Amount":"47.42"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-22","Item Amount":"171.02"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-22","Item Tax Amount":"14.86"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-22","Item Tax Amount":"9.90"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-02-22","Item Amount":"51.38"},{"Item Name":"Laundry","Transaction Date":"2025-02-22","Item Amount":"17.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-22","Item Amount":"55.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn West Palm Beach Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn West Palm Beach Downtown' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_275(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Pomona Airport','MerchantAddress':'6505 Reyes Dr, Pomona, CA 39067, USA','TransactionDate':'2023-01-10',,'Total':'790.04','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Customer Experience Summit in Pomona. 4 business nights; client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-06","Item Amount":"99.81"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-06","Item Tax Amount":"7.04"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-06","Item Tax Amount":"4.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-06","Item Amount":"37.00"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-07","Item Amount":"124.86"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-07","Item Tax Amount":"8.81"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-07","Item Tax Amount":"5.87"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-01-07","Item Amount":"114.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-07","Item Amount":"34.02"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-08","Item Amount":"126.10"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-08","Item Tax Amount":"8.90"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-08","Item Tax Amount":"5.93"},{"Item Name":"Laundry","Transaction Date":"2023-01-08","Item Amount":"20.11"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-08","Item Amount":"25.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-09","Item Amount":"117.23"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-09","Item Tax Amount":"8.27"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-09","Item Tax Amount":"5.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-09","Item Amount":"35.50"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Pomona Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Pomona Airport' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_276(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Bridgeport Airport','MerchantAddress':'470 Howard St, Bridgeport, CT 10967, USA','TransactionDate':'2021-08-08',,'Total':'1531.31','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CT','Description':'Business trip to Bridgeport for partnership development. Attended Sales Leadership Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-08-05","Item Amount":"316.60"},{"Item Name":"Hotel Tax","Transaction Date":"2021-08-05","Item Tax Amount":"23.62"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-08-05","Item Amount":"186.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-08-05","Item Amount":"77.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-08-06","Item Amount":"323.32"},{"Item Name":"Hotel Tax","Transaction Date":"2021-08-06","Item Tax Amount":"24.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-08-06","Item Amount":"93.24"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-08-07","Item Amount":"319.20"},{"Item Name":"Hotel Tax","Transaction Date":"2021-08-07","Item Tax Amount":"23.81"},{"Item Name":"Incidentals","Transaction Date":"2021-08-07","Item Amount":"43.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-08-07","Item Amount":"80.82"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-08-08","Item Amount":"18.37"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Bridgeport Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Bridgeport Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_277(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Hialeah Palmetto','MerchantAddress':'9367 White St, Hialeah, FL 27946, USA','TransactionDate':'2021-02-27',,'Total':'227.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Hialeah for Legal Technology Conference. 1 night stay for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-26","Item Amount":"94.69"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-26","Item Tax Amount":"5.33"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-26","Item Tax Amount":"3.55"},{"Item Name":"Entertainment External","Transaction Date":"2021-02-26","Item Amount":"78.74"},{"Item Name":"Incidentals","Transaction Date":"2021-02-26","Item Amount":"20.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-26","Item Amount":"25.06"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Hialeah Palmetto' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Hialeah Palmetto' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_278(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt North Las Vegas Downtown','MerchantAddress':'517 Taylor Ave, North Las Vegas, NV 95177, USA','TransactionDate':'2021-07-18',,'Total':'292.02','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NV','Description':'Business travel to North Las Vegas for Manufacturing Excellence Summit. 1 night stay for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-17","Item Amount":"181.00"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-17","Item Tax Amount":"14.04"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-17","Item Tax Amount":"9.36"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-07-17","Item Amount":"17.27"},{"Item Name":"Incidentals","Transaction Date":"2021-07-17","Item Amount":"23.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-17","Item Amount":"46.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt North Las Vegas Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt North Las Vegas Downtown' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_279(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Fullerton Sunny Hills','MerchantAddress':'3435 Executive Way, Fullerton, CA 99861, USA','TransactionDate':'2023-03-09',,'Total':'1168.82','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Fullerton for Manufacturing Excellence Summit. 4 nights stay for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-05","Item Amount":"195.75"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-05","Item Tax Amount":"9.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-05","Item Amount":"78.85"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-06","Item Amount":"234.66"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-06","Item Tax Amount":"11.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-06","Item Amount":"55.95"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-07","Item Amount":"216.33"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-07","Item Tax Amount":"10.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-07","Item Amount":"71.64"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-08","Item Amount":"217.49"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-08","Item Tax Amount":"10.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-08","Item Amount":"55.82"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Fullerton Sunny Hills' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Fullerton Sunny Hills' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_280(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Lansing Meridian Mall','MerchantAddress':'7874 Wilson Way, Lansing, MI 88517, USA','TransactionDate':'2023-01-08',,'Total':'195.75','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Corporate trip - Corporate Strategy Summit conference in Lansing. merger and acquisition discussions over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-07","Item Amount":"145.51"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-07","Item Tax Amount":"2.56"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-07","Item Tax Amount":"2.56"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-07","Item Tax Amount":"7.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-07","Item Amount":"37.43"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Lansing Meridian Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Lansing Meridian Mall' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_281(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Bellevue Crossroads','MerchantAddress':'882 Roberts Dr, Bellevue, WA 96269, USA','TransactionDate':'2022-02-25',,'Total':'1098.61','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Company business trip - Attended Customer Experience Summit in Bellevue. 4 business nights; compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-21","Item Amount":"214.20"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-21","Item Tax Amount":"14.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-21","Item Amount":"42.37"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-22","Item Amount":"197.67"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-22","Item Tax Amount":"13.34"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-02-22","Item Amount":"23.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-22","Item Amount":"64.41"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-23","Item Amount":"178.01"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-23","Item Tax Amount":"12.01"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-02-23","Item Amount":"41.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-23","Item Amount":"42.46"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-02-24","Item Amount":"189.01"},{"Item Name":"Hotel Tax","Transaction Date":"2022-02-24","Item Tax Amount":"12.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-02-24","Item Amount":"52.94"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Bellevue Crossroads' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Bellevue Crossroads' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_282(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Pomona Phillips Ranch','MerchantAddress':'5649 Foster Dr, Pomona, CA 22576, USA','TransactionDate':'2020-09-20',,'Total':'1241.29','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Project Management Summit conference in Pomona. technical workshops and knowledge sharing over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-16","Item Amount":"187.61"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-16","Item Tax Amount":"15.32"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-09-16","Item Amount":"24.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-16","Item Amount":"63.38"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-17","Item Amount":"152.46"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-17","Item Tax Amount":"12.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-17","Item Amount":"68.74"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-18","Item Amount":"181.57"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-18","Item Tax Amount":"14.83"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-09-18","Item Amount":"157.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-18","Item Amount":"85.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-19","Item Amount":"190.72"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-19","Item Tax Amount":"15.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-19","Item Amount":"71.79"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Pomona Phillips Ranch' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Pomona Phillips Ranch' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_283(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Grand Prairie Great Southwest','MerchantAddress':'4722 Jackson Blvd, Grand Prairie, TX 65809, USA','TransactionDate':'2020-04-08',,'Total':'903.29','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Project Management Summit in Grand Prairie. 3 business nights; board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-05","Item Amount":"142.50"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-05","Item Tax Amount":"4.12"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-05","Item Tax Amount":"12.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-05","Item Amount":"74.06"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-06","Item Amount":"173.08"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-06","Item Tax Amount":"5.01"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-06","Item Tax Amount":"5.01"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-06","Item Tax Amount":"15.03"},{"Item Name":"Entertainment External","Transaction Date":"2020-04-06","Item Amount":"106.63"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-04-06","Item Amount":"17.04"},{"Item Name":"Laundry","Transaction Date":"2020-04-06","Item Amount":"39.61"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-06","Item Amount":"63.75"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-04-07","Item Amount":"152.60"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-07","Item Tax Amount":"4.42"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-07","Item Tax Amount":"4.42"},{"Item Name":"Hotel Tax","Transaction Date":"2020-04-07","Item Tax Amount":"13.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-04-07","Item Amount":"70.39"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Grand Prairie Great Southwest' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Grand Prairie Great Southwest' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_284(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Tacoma Airport','MerchantAddress':'4053 Long Ave, Tacoma, WA 82439, USA','TransactionDate':'2023-10-12',,'Total':'1035.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Company business trip - Attended Cloud Computing Expo in Tacoma. 3 business nights; strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-09","Item Amount":"248.95"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-09","Item Tax Amount":"7.97"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-09","Item Tax Amount":"11.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-09","Item Amount":"70.37"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-10","Item Amount":"263.67"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-10","Item Tax Amount":"8.44"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-10","Item Tax Amount":"12.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-10","Item Amount":"56.56"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-10-11","Item Amount":"264.87"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-11","Item Tax Amount":"8.48"},{"Item Name":"Hotel Tax","Transaction Date":"2023-10-11","Item Tax Amount":"12.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-10-11","Item Amount":"68.93"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Tacoma Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Tacoma Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_285(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Fairfield Solano Town Center','MerchantAddress':'7008 Jackson Blvd, Fairfield, CA 10555, USA','TransactionDate':'2019-09-12',,'Total':'446.18','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Fairfield for Real Estate Investment Summit. 2 nights stay for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-10","Item Amount":"111.34"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-10","Item Tax Amount":"7.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-10","Item Amount":"69.93"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-11","Item Amount":"112.71"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-11","Item Tax Amount":"7.64"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-09-11","Item Amount":"7.53"},{"Item Name":"Laundry","Transaction Date":"2019-09-11","Item Amount":"31.74"},{"Item Name":"Incidentals","Transaction Date":"2019-09-11","Item Amount":"40.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-11","Item Amount":"57.12"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Fairfield Solano Town Center' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Fairfield Solano Town Center' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_286(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Boston Logan','MerchantAddress':'1721 Morris Ave, Boston, MA 83167, USA','TransactionDate':'2021-03-24',,'Total':'706.63','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MA','Description':'Company business trip - Attended Enterprise Software Summit in Boston. 4 business nights; stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-20","Item Amount":"86.66"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-20","Item Tax Amount":"1.94"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-20","Item Tax Amount":"1.94"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-20","Item Tax Amount":"5.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-20","Item Amount":"61.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-21","Item Amount":"77.48"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-21","Item Tax Amount":"1.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-21","Item Tax Amount":"5.21"},{"Item Name":"Entertainment External","Transaction Date":"2021-03-21","Item Amount":"63.32"},{"Item Name":"Laundry","Transaction Date":"2021-03-21","Item Amount":"25.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-21","Item Amount":"40.47"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-22","Item Amount":"93.98"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-22","Item Tax Amount":"2.11"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-22","Item Tax Amount":"2.11"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-22","Item Tax Amount":"6.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-22","Item Amount":"49.24"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-23","Item Amount":"100.26"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-23","Item Tax Amount":"2.25"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-23","Item Tax Amount":"2.25"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-23","Item Tax Amount":"6.75"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-03-23","Item Amount":"19.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-23","Item Amount":"50.28"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Boston Logan' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Boston Logan' have all 22 required itemizations'?,",
#     )


# def test_expense_hotel_287(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Woodbridge Avenel','MerchantAddress':'9002 Garcia St, Woodbridge, NJ 65288, USA','TransactionDate':'2019-11-14',,'Total':'725.07','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company travel - Cybersecurity Conference in Woodbridge. 4 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-10","Item Amount":"107.46"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-10","Item Tax Amount":"7.88"},{"Item Name":"Entertainment External","Transaction Date":"2019-11-10","Item Amount":"40.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-10","Item Amount":"48.70"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-11","Item Amount":"89.49"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-11","Item Tax Amount":"6.56"},{"Item Name":"Gift and Entertainment","Transaction Date":"2019-11-11","Item Amount":"47.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-11","Item Amount":"67.70"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-12","Item Amount":"92.87"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-12","Item Tax Amount":"6.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-12","Item Amount":"50.39"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-11-13","Item Amount":"89.92"},{"Item Name":"Hotel Tax","Transaction Date":"2019-11-13","Item Tax Amount":"6.60"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-11-13","Item Amount":"14.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-11-13","Item Amount":"47.75"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Woodbridge Avenel' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Woodbridge Avenel' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_288(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Pasadena Airport','MerchantAddress':'1567 Moore St, Pasadena, CA 12680, USA','TransactionDate':'2021-04-15',,'Total':'547.85','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Pasadena for Marketing Analytics Summit. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-13","Item Amount":"196.26"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-13","Item Tax Amount":"10.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-13","Item Tax Amount":"3.58"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-13","Item Tax Amount":"3.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-13","Item Amount":"65.74"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-14","Item Amount":"196.27"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-14","Item Tax Amount":"10.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-14","Item Tax Amount":"3.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-14","Item Amount":"57.36"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Pasadena Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Pasadena Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_289(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Omaha Midtown','MerchantAddress':'822 Campbell St, Omaha, NE 53942, USA','TransactionDate':'2021-06-22',,'Total':'317.65','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NE','Description':'Company business trip - Attended Mobile Technology Conference in Omaha. 1 business night; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-21","Item Amount":"141.02"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-21","Item Tax Amount":"8.79"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-21","Item Tax Amount":"2.93"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-21","Item Tax Amount":"2.93"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-06-21","Item Amount":"55.04"},{"Item Name":"Incidentals","Transaction Date":"2021-06-21","Item Amount":"45.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-21","Item Amount":"61.56"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Omaha Midtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Omaha Midtown' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_290(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn New York Times Square','MerchantAddress':'2709 Ward Ave, New York, NY 11134, USA','TransactionDate':'2024-01-10',,'Total':'359.03','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NY','Description':'Corporate trip - Supply Chain Management Conference conference in New York. merger and acquisition discussions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-08","Item Amount":"86.43"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-08","Item Tax Amount":"6.05"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-08","Item Tax Amount":"4.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-08","Item Amount":"80.41"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-09","Item Amount":"89.74"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-09","Item Tax Amount":"6.28"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-09","Item Tax Amount":"4.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-09","Item Amount":"81.90"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn New York Times Square' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn New York Times Square' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_291(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Oxnard Seabridge','MerchantAddress':'2334 Baker Ave, Oxnard, CA 52491, USA','TransactionDate':'2020-06-21',,'Total':'859.85','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Oxnard for Legal Technology Conference. 2 nights stay for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-06-19","Item Amount":"345.84"},{"Item Name":"Hotel Tax","Transaction Date":"2020-06-19","Item Tax Amount":"26.70"},{"Item Name":"Hotel Tax","Transaction Date":"2020-06-19","Item Tax Amount":"8.90"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-06-19","Item Amount":"45.00"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-06-20","Item Amount":"317.00"},{"Item Name":"Hotel Tax","Transaction Date":"2020-06-20","Item Tax Amount":"24.48"},{"Item Name":"Hotel Tax","Transaction Date":"2020-06-20","Item Tax Amount":"8.16"},{"Item Name":"Laundry","Transaction Date":"2020-06-20","Item Amount":"38.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-06-20","Item Amount":"44.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Oxnard Seabridge' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Oxnard Seabridge' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_292(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Stockton Airport','MerchantAddress':'9869 Kelly Dr, Stockton, CA 61721, USA','TransactionDate':'2022-01-21',,'Total':'880.85','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Cloud Computing Expo in Stockton. 3 business nights; market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-18","Item Amount":"232.52"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-18","Item Tax Amount":"19.08"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-18","Item Tax Amount":"6.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-18","Item Amount":"34.91"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-19","Item Amount":"226.33"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-19","Item Tax Amount":"18.57"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-19","Item Tax Amount":"6.19"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-19","Item Tax Amount":"6.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-19","Item Amount":"41.16"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-20","Item Amount":"227.13"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-20","Item Tax Amount":"18.63"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-20","Item Tax Amount":"6.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-20","Item Amount":"37.57"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Stockton Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Stockton Airport' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_293(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Hartford West Hartford','MerchantAddress':'7378 Wood Dr, Hartford, CT 97848, USA','TransactionDate':'2023-09-19',,'Total':'439','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CT','Description':'Company business trip - Attended HR Leadership Summit in Hartford. 3 business nights; operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-16","Item Amount":"76.61"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-16","Item Tax Amount":"5.77"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-16","Item Tax Amount":"1.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-16","Item Amount":"41.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-17","Item Amount":"101.50"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-17","Item Tax Amount":"7.64"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-17","Item Tax Amount":"2.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-17","Item Amount":"26.87"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-18","Item Amount":"91.92"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-18","Item Tax Amount":"6.92"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-18","Item Tax Amount":"2.31"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-18","Item Tax Amount":"2.31"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-09-18","Item Amount":"9.86"},{"Item Name":"Incidentals","Transaction Date":"2023-09-18","Item Amount":"28.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-18","Item Amount":"33.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Hartford West Hartford' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Hartford West Hartford' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_294(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Omni Elk Grove Laguna Gateway','MerchantAddress':'7590 Diaz St, Elk Grove, CA 53097, USA','TransactionDate':'2024-03-25',,'Total':'297.7','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Product Management Summit in Elk Grove. 1 business night; market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-24","Item Amount":"222.15"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-24","Item Tax Amount":"12.55"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-24","Item Amount":"63.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Omni Elk Grove Laguna Gateway' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Omni Elk Grove Laguna Gateway' have all 3 required itemizations'?,",
#     )


# def test_expense_hotel_295(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Pomona Fairplex','MerchantAddress':'281 Parker Dr, Pomona, CA 61777, USA','TransactionDate':'2019-06-20',,'Total':'373.27','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Pomona for team training. Attended Project Management Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-19","Item Amount":"157.72"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-19","Item Tax Amount":"9.95"},{"Item Name":"Entertainment External","Transaction Date":"2019-06-19","Item Amount":"100.88"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-06-19","Item Amount":"8.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-19","Item Amount":"95.96"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Pomona Fairplex' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Pomona Fairplex' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_296(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Elizabeth Jersey Gardens','MerchantAddress':'6612 Rivera Ave, Elizabeth, NJ 90849, USA','TransactionDate':'2022-08-26',,'Total':'1627.15','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company business trip - Attended AI & Machine Learning Conference in Elizabeth. 4 business nights; product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-22","Item Amount":"333.07"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-22","Item Tax Amount":"7.57"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-22","Item Tax Amount":"22.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-22","Item Amount":"46.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-23","Item Amount":"305.57"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-23","Item Tax Amount":"6.94"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-23","Item Tax Amount":"20.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-23","Item Amount":"40.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-24","Item Amount":"304.47"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-24","Item Tax Amount":"6.92"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-24","Item Tax Amount":"20.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-24","Item Amount":"38.31"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-25","Item Amount":"321.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-25","Item Tax Amount":"7.31"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-25","Item Tax Amount":"7.31"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-25","Item Tax Amount":"21.93"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-08-25","Item Amount":"46.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-25","Item Amount":"49.31"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-08-26","Item Amount":"18.45"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Elizabeth Jersey Gardens' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Elizabeth Jersey Gardens' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_297(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree North Las Vegas Aliante','MerchantAddress':'8817 Executive Way, North Las Vegas, NV 88747, USA','TransactionDate':'2021-07-27',,'Total':'471.15','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NV','Description':'Corporate trip - IoT Solutions Summit conference in North Las Vegas. market research and competitive analysis over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-25","Item Amount":"164.94"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-25","Item Tax Amount":"9.04"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-25","Item Amount":"57.91"},{"Item Name":"Incidentals","Transaction Date":"2021-07-25","Item Amount":"29.24"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-26","Item Amount":"142.43"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-26","Item Tax Amount":"7.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-26","Item Amount":"41.78"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-07-27","Item Amount":"18.00"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree North Las Vegas Aliante' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree North Las Vegas Aliante' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_298(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Riverside Airport','MerchantAddress':'6191 Maple Dr, Riverside, CA 25711, USA','TransactionDate':'2019-03-24',,'Total':'1242.76','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Riverside for Enterprise Software Summit. 4 nights stay for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-20","Item Amount":"195.03"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-20","Item Tax Amount":"11.90"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-20","Item Tax Amount":"7.93"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-20","Item Amount":"59.41"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-21","Item Amount":"210.40"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-21","Item Tax Amount":"12.84"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-21","Item Tax Amount":"8.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-21","Item Amount":"63.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-22","Item Amount":"223.43"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-22","Item Tax Amount":"13.63"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-22","Item Tax Amount":"9.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-22","Item Amount":"56.76"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-23","Item Amount":"213.72"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-23","Item Tax Amount":"13.04"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-23","Item Tax Amount":"8.69"},{"Item Name":"Hotel Breakfast","Transaction Date":"2019-03-23","Item Amount":"29.10"},{"Item Name":"Hotel Deposit","Transaction Date":"2019-03-23","Item Amount":"50.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-23","Item Amount":"55.70"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Riverside Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Riverside Airport' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_299(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Lansing Michigan State University','MerchantAddress':'694 Anderson Dr, Lansing, MI 60758, USA','TransactionDate':'2025-05-03',,'Total':'189.71','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Company business trip - Attended IoT Solutions Summit in Lansing. 1 business night; client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-05-02","Item Amount":"150.58"},{"Item Name":"Hotel Tax","Transaction Date":"2025-05-02","Item Tax Amount":"8.08"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-05-02","Item Amount":"31.05"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Lansing Michigan State University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Lansing Michigan State University' have all 3 required itemizations'?,",
#     )


# def test_expense_hotel_300(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Dayton Downtown','MerchantAddress':'2753 Rodriguez Dr, Dayton, OH 98899, USA','TransactionDate':'2024-11-18',,'Total':'367.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business trip to Dayton for compliance audit. Attended Cloud Computing Expo. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-11-17","Item Amount":"144.47"},{"Item Name":"Hotel Tax","Transaction Date":"2024-11-17","Item Tax Amount":"11.54"},{"Item Name":"Entertainment External","Transaction Date":"2024-11-17","Item Amount":"88.87"},{"Item Name":"Laundry","Transaction Date":"2024-11-17","Item Amount":"27.90"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-11-17","Item Amount":"66.93"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-11-18","Item Amount":"27.34"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Dayton Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Dayton Downtown' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_301(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Fort Lauderdale Las Olas','MerchantAddress':'2555 Downtown Dr, Fort Lauderdale, FL 74013, USA','TransactionDate':'2021-04-28',,'Total':'671.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company travel - Mobile Technology Conference in Fort Lauderdale. 2 business nights for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-26","Item Amount":"240.32"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-26","Item Tax Amount":"15.05"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-26","Item Tax Amount":"5.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-26","Item Amount":"40.31"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-27","Item Amount":"235.67"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-27","Item Tax Amount":"14.76"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-27","Item Tax Amount":"4.92"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-27","Item Tax Amount":"4.92"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-04-27","Item Amount":"76.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-27","Item Amount":"33.42"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Fort Lauderdale Las Olas' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Fort Lauderdale Las Olas' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_302(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Palmdale Airport','MerchantAddress':'6441 Green Blvd, Palmdale, CA 57556, USA','TransactionDate':'2024-10-15',,'Total':'1516.83','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Blockchain Conference in Palmdale. 4 business nights for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-11","Item Amount":"254.80"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-11","Item Tax Amount":"17.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-11","Item Tax Amount":"5.81"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-11","Item Tax Amount":"5.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-11","Item Amount":"67.27"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-12","Item Amount":"269.07"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-12","Item Tax Amount":"18.42"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-12","Item Tax Amount":"6.14"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-12","Item Tax Amount":"6.14"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-12","Item Amount":"86.04"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-13","Item Amount":"240.23"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-13","Item Tax Amount":"16.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-13","Item Tax Amount":"5.48"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-13","Item Tax Amount":"5.48"},{"Item Name":"Entertainment External","Transaction Date":"2024-10-13","Item Amount":"48.88"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-10-13","Item Amount":"12.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-13","Item Amount":"87.72"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-14","Item Amount":"251.34"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-14","Item Tax Amount":"17.20"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-14","Item Tax Amount":"5.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-14","Item Amount":"89.10"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Palmdale Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Palmdale Airport' have all 21 required itemizations'?,",
#     )


# def test_expense_hotel_303(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Santa Ana Civic Center','MerchantAddress':'8238 Green Blvd, Santa Ana, CA 43674, USA','TransactionDate':'2025-10-06',,'Total':'248.86','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Digital Marketing Conference in Santa Ana. 2 business nights; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-04","Item Amount":"70.54"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-04","Item Tax Amount":"5.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-04","Item Amount":"56.96"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-10-05","Item Amount":"55.02"},{"Item Name":"Hotel Tax","Transaction Date":"2025-10-05","Item Tax Amount":"4.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-10-05","Item Amount":"56.28"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Santa Ana Civic Center' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Santa Ana Civic Center' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_304(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Warren Airport','MerchantAddress':'9038 Elm Ave, Warren, MI 36666, USA','TransactionDate':'2021-11-26',,'Total':'738.5','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Corporate trip - Corporate Strategy Summit conference in Warren. team building and training sessions over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-23","Item Amount":"182.95"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-23","Item Tax Amount":"8.86"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-23","Item Tax Amount":"2.95"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-23","Item Tax Amount":"2.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-23","Item Amount":"42.80"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-24","Item Amount":"183.31"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-24","Item Tax Amount":"8.87"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-24","Item Tax Amount":"2.96"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-24","Item Amount":"39.47"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-25","Item Amount":"193.07"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-25","Item Tax Amount":"9.35"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-25","Item Tax Amount":"3.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-25","Item Amount":"57.84"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Warren Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Warren Airport' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_305(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Lubbock South Lubbock','MerchantAddress':'7271 Smith St, Lubbock, TX 66168, USA','TransactionDate':'2025-06-26',,'Total':'1764.12','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Product Management Summit in Lubbock. 4 business nights; customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-22","Item Amount":"321.13"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-22","Item Tax Amount":"22.86"},{"Item Name":"Entertainment External","Transaction Date":"2025-06-22","Item Amount":"95.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-22","Item Amount":"68.70"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-23","Item Amount":"305.48"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-23","Item Tax Amount":"21.75"},{"Item Name":"Incidentals","Transaction Date":"2025-06-23","Item Amount":"11.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-23","Item Amount":"64.29"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-24","Item Amount":"309.94"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-24","Item Tax Amount":"22.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-24","Item Amount":"77.75"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-25","Item Amount":"323.85"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-25","Item Tax Amount":"23.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-25","Item Amount":"79.33"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-06-26","Item Amount":"17.55"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Lubbock South Lubbock' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Lubbock South Lubbock' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_306(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Lincoln University','MerchantAddress':'1299 Morgan Ave, Lincoln, NE 55690, USA','TransactionDate':'2021-02-04',,'Total':'213.72','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NE','Description':'Business trip to Lincoln for board meetings. Attended Innovation Leadership Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-03","Item Amount":"101.94"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-03","Item Tax Amount":"2.32"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-03","Item Tax Amount":"6.95"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-02-03","Item Amount":"45.08"},{"Item Name":"Laundry","Transaction Date":"2021-02-03","Item Amount":"24.04"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-03","Item Amount":"33.39"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Lincoln University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Lincoln University' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_307(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Minneapolis Northeast','MerchantAddress':'3292 Baker Ave, Minneapolis, MN 63734, USA','TransactionDate':'2024-09-06',,'Total':'387.71','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Company business trip - Attended Cybersecurity Conference in Minneapolis. 1 business night; stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-05","Item Amount":"241.30"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-05","Item Tax Amount":"7.79"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-05","Item Tax Amount":"11.69"},{"Item Name":"Entertainment External","Transaction Date":"2024-09-05","Item Amount":"79.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-05","Item Amount":"47.12"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Minneapolis Northeast' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Minneapolis Northeast' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_308(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Hollywood Young Circle','MerchantAddress':'502 Rivera Ave, Hollywood, FL 56346, USA','TransactionDate':'2025-11-21',,'Total':'1149','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip to Hollywood for compliance audit. Attended Customer Experience Summit. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-17","Item Amount":"219.17"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-17","Item Tax Amount":"12.41"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-17","Item Tax Amount":"8.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-17","Item Amount":"33.54"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-18","Item Amount":"233.63"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-18","Item Tax Amount":"13.23"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-18","Item Tax Amount":"8.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-18","Item Amount":"18.01"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-19","Item Amount":"227.68"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-19","Item Tax Amount":"12.89"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-19","Item Tax Amount":"8.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-19","Item Amount":"18.56"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-20","Item Amount":"221.04"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-20","Item Tax Amount":"12.51"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-20","Item Tax Amount":"8.34"},{"Item Name":"Entertainment External","Transaction Date":"2025-11-20","Item Amount":"21.78"},{"Item Name":"Laundry","Transaction Date":"2025-11-20","Item Amount":"17.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-20","Item Amount":"35.25"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-11-21","Item Amount":"18.15"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Hollywood Young Circle' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Hollywood Young Circle' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_309(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Fontana South Fontana','MerchantAddress':'194 Madison Ave, Fontana, CA 12799, USA','TransactionDate':'2019-06-30',,'Total':'1161.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Fontana for AI & Machine Learning Conference. 3 nights stay for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-27","Item Amount":"251.65"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-27","Item Tax Amount":"14.76"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-27","Item Amount":"103.70"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-28","Item Amount":"255.25"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-28","Item Tax Amount":"14.97"},{"Item Name":"Laundry","Transaction Date":"2019-06-28","Item Amount":"29.89"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-28","Item Amount":"96.04"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-29","Item Amount":"275.88"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-29","Item Tax Amount":"16.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-29","Item Amount":"103.07"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Fontana South Fontana' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Fontana South Fontana' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_310(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Ontario Airport','MerchantAddress':'4280 Lincoln Blvd, Ontario, CA 60488, USA','TransactionDate':'2023-11-08',,'Total':'345.53','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Real Estate Investment Summit in Ontario. 1 business night for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-11-07","Item Amount":"260.61"},{"Item Name":"Hotel Tax","Transaction Date":"2023-11-07","Item Tax Amount":"12.74"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-11-07","Item Amount":"54.92"},{"Item Name":"Hotel Breakfast","Transaction Date":"2023-11-08","Item Amount":"17.26"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Ontario Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Ontario Airport' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_311(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Chandler Downtown','MerchantAddress':'798 Commerce St, Chandler, AZ 25798, USA','TransactionDate':'2024-05-31',,'Total':'832.28','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Company travel - Enterprise Software Summit in Chandler. 3 business nights for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-28","Item Amount":"187.56"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-28","Item Tax Amount":"16.35"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-28","Item Tax Amount":"5.45"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-28","Item Tax Amount":"5.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-28","Item Amount":"60.88"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-29","Item Amount":"175.14"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-29","Item Tax Amount":"15.27"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-29","Item Tax Amount":"5.09"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-29","Item Amount":"83.42"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-30","Item Amount":"175.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-30","Item Tax Amount":"15.30"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-30","Item Tax Amount":"5.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-30","Item Amount":"81.83"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Chandler Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Chandler Downtown' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_312(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Cedar Rapids Czech & Slovak Museum','MerchantAddress':'7127 Parker Dr, Cedar Rapids, IA 45958, USA','TransactionDate':'2024-10-22',,'Total':'1314.72','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IA','Description':'Business travel to Cedar Rapids for Business Intelligence Summit. 4 nights stay for client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-18","Item Amount":"237.02"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-18","Item Tax Amount":"9.54"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-18","Item Tax Amount":"14.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-18","Item Amount":"80.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-19","Item Amount":"222.29"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-19","Item Tax Amount":"8.95"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-19","Item Tax Amount":"13.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-19","Item Amount":"73.87"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-20","Item Amount":"217.31"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-20","Item Tax Amount":"8.75"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-20","Item Tax Amount":"13.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-20","Item Amount":"74.07"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-21","Item Amount":"231.78"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-21","Item Tax Amount":"9.33"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-21","Item Tax Amount":"13.99"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-21","Item Amount":"86.38"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Cedar Rapids Czech & Slovak Museum' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Cedar Rapids Czech & Slovak Museum' have all 16 required itemizations'?,",
#     )


# def test_expense_hotel_313(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Mobile Midtown','MerchantAddress':'202 Business District Way, Mobile, AL 23947, USA','TransactionDate':'2020-05-11',,'Total':'473.72','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AL','Description':'Business travel to Mobile for E-commerce Summit. 1 night stay for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-10","Item Amount":"255.34"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-10","Item Tax Amount":"18.90"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-10","Item Tax Amount":"12.60"},{"Item Name":"Entertainment External","Transaction Date":"2020-05-10","Item Amount":"108.40"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-05-10","Item Amount":"17.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-10","Item Amount":"60.83"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Mobile Midtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Mobile Midtown' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_314(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Simi Valley Simi Valley Mall','MerchantAddress':'4730 Nelson St, Simi Valley, CA 15516, USA','TransactionDate':'2024-01-08',,'Total':'825.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Simi Valley for HR Leadership Summit. 4 nights stay for client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-04","Item Amount":"147.03"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-04","Item Tax Amount":"7.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-04","Item Amount":"42.84"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-05","Item Amount":"170.89"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-05","Item Tax Amount":"9.08"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-05","Item Amount":"33.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-06","Item Amount":"170.39"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-06","Item Tax Amount":"9.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-06","Item Amount":"21.17"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-01-07","Item Amount":"163.07"},{"Item Name":"Hotel Tax","Transaction Date":"2024-01-07","Item Tax Amount":"8.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-01-07","Item Amount":"42.50"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Simi Valley Simi Valley Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Simi Valley Simi Valley Mall' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_315(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Evansville Airport','MerchantAddress':'4937 Morgan Ave, Evansville, IN 66459, USA','TransactionDate':'2022-03-13',,'Total':'536.92','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IN','Description':'Business travel to Evansville for Retail Innovation Conference. 2 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-11","Item Amount":"169.20"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-11","Item Tax Amount":"9.83"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-11","Item Tax Amount":"14.74"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-11","Item Amount":"59.78"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-12","Item Amount":"176.81"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-12","Item Tax Amount":"10.27"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-12","Item Tax Amount":"15.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-12","Item Amount":"54.40"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-03-13","Item Amount":"26.48"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Evansville Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Evansville Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_316(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Madison Downtown','MerchantAddress':'2483 Washington Ave, Madison, WI 21973, USA','TransactionDate':'2021-01-08',,'Total':'1030.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WI','Description':'Company travel - Marketing Analytics Summit in Madison. 3 business nights for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-05","Item Amount":"184.87"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-05","Item Tax Amount":"6.54"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-05","Item Tax Amount":"9.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-05","Item Amount":"59.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-06","Item Amount":"215.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-06","Item Tax Amount":"7.64"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-06","Item Tax Amount":"11.46"},{"Item Name":"Hotel Deposit","Transaction Date":"2021-01-06","Item Amount":"178.73"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-01-06","Item Amount":"16.92"},{"Item Name":"Incidentals","Transaction Date":"2021-01-06","Item Amount":"20.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-06","Item Amount":"42.76"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-07","Item Amount":"201.72"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-07","Item Tax Amount":"7.14"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-07","Item Tax Amount":"10.70"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-07","Item Amount":"56.57"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Madison Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Madison Downtown' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_317(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton West Valley City Valley Fair Mall','MerchantAddress':'9849 Price Blvd, West Valley City, UT 18229, USA','TransactionDate':'2021-12-15',,'Total':'1145.89','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Business trip to West Valley City for team training. Attended Cybersecurity Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-11","Item Amount":"211.58"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-11","Item Tax Amount":"18.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-11","Item Amount":"43.13"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-12","Item Amount":"215.09"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-12","Item Tax Amount":"18.80"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-12","Item Amount":"48.74"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-13","Item Amount":"224.14"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-13","Item Tax Amount":"19.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-13","Item Amount":"41.28"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-14","Item Amount":"232.16"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-14","Item Tax Amount":"20.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-14","Item Amount":"52.60"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton West Valley City Valley Fair Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton West Valley City Valley Fair Mall' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_318(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Grand Rapids East Hills','MerchantAddress':'6281 Flores St, Grand Rapids, MI 70709, USA','TransactionDate':'2020-09-06',,'Total':'254.35','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Company business trip - Attended Change Management Conference in Grand Rapids. 1 business night; stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-05","Item Amount":"185.57"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-05","Item Tax Amount":"6.80"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-05","Item Tax Amount":"10.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-05","Item Amount":"51.79"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Grand Rapids East Hills' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Grand Rapids East Hills' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_319(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Jersey City Downtown','MerchantAddress':'6165 Bailey Blvd, Jersey City, NJ 54275, USA','TransactionDate':'2020-01-21',,'Total':'350.34','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Company business trip - Attended IoT Solutions Summit in Jersey City. 1 business night; sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-20","Item Amount":"138.30"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-20","Item Tax Amount":"7.60"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-20","Item Tax Amount":"11.40"},{"Item Name":"Entertainment External","Transaction Date":"2020-01-20","Item Amount":"77.62"},{"Item Name":"Hotel Telephone","Transaction Date":"2020-01-20","Item Amount":"18.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-20","Item Amount":"77.67"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-01-21","Item Amount":"19.07"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Jersey City Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Jersey City Downtown' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_320(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Midland Airport','MerchantAddress':'9799 Foster Dr, Midland, TX 91094, USA','TransactionDate':'2022-07-17',,'Total':'1123.13','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business trip to Midland for product launch. Attended FinTech Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-14","Item Amount":"274.84"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-14","Item Tax Amount":"7.65"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-14","Item Tax Amount":"22.94"},{"Item Name":"Incidentals","Transaction Date":"2022-07-14","Item Amount":"14.64"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-14","Item Amount":"57.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-15","Item Amount":"240.33"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-15","Item Tax Amount":"6.69"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-15","Item Tax Amount":"6.69"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-15","Item Tax Amount":"20.06"},{"Item Name":"Laundry","Transaction Date":"2022-07-15","Item Amount":"24.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-15","Item Amount":"69.21"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-07-16","Item Amount":"270.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-16","Item Tax Amount":"7.53"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-16","Item Tax Amount":"7.53"},{"Item Name":"Hotel Tax","Transaction Date":"2022-07-16","Item Tax Amount":"22.60"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-07-16","Item Amount":"13.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-07-16","Item Amount":"56.52"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Midland Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Midland Airport' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_321(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Torrance Airport','MerchantAddress':'4709 Lewis Ave, Torrance, CA 49270, USA','TransactionDate':'2025-08-07',,'Total':'326.21','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Energy Sector Conference conference in Torrance. technical workshops and knowledge sharing over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-08-06","Item Amount":"113.49"},{"Item Name":"Hotel Tax","Transaction Date":"2025-08-06","Item Tax Amount":"8.87"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-08-06","Item Amount":"78.60"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-08-06","Item Amount":"75.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-08-06","Item Amount":"50.04"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Torrance Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Torrance Airport' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_322(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Modesto Vintage Faire','MerchantAddress':'8439 Gray St, Modesto, CA 34589, USA','TransactionDate':'2020-05-13',,'Total':'1073.7','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Digital Transformation Summit in Modesto. 3 business nights for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-10","Item Amount":"211.82"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-10","Item Tax Amount":"10.44"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-10","Item Tax Amount":"6.96"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-05-10","Item Amount":"155.94"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-10","Item Amount":"54.47"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-11","Item Amount":"244.27"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-11","Item Tax Amount":"12.04"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-11","Item Tax Amount":"8.03"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-11","Item Amount":"56.17"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-05-12","Item Amount":"220.07"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-12","Item Tax Amount":"10.85"},{"Item Name":"Hotel Tax","Transaction Date":"2020-05-12","Item Tax Amount":"7.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-05-12","Item Amount":"75.41"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Modesto Vintage Faire' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Modesto Vintage Faire' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_323(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Escondido North County Fair','MerchantAddress':'8196 Carter St, Escondido, CA 32259, USA','TransactionDate':'2023-08-15',,'Total':'841.2','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Escondido for product launch. Attended Cybersecurity Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-11","Item Amount":"138.80"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-11","Item Tax Amount":"11.13"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-11","Item Tax Amount":"7.42"},{"Item Name":"Entertainment External","Transaction Date":"2023-08-11","Item Amount":"30.59"},{"Item Name":"Laundry","Transaction Date":"2023-08-11","Item Amount":"20.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-11","Item Amount":"39.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-12","Item Amount":"144.73"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-12","Item Tax Amount":"11.60"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-12","Item Tax Amount":"7.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-12","Item Amount":"46.30"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-13","Item Amount":"128.17"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-13","Item Tax Amount":"10.27"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-13","Item Tax Amount":"6.85"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-13","Item Amount":"46.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-08-14","Item Amount":"121.59"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-14","Item Tax Amount":"9.75"},{"Item Name":"Hotel Tax","Transaction Date":"2023-08-14","Item Tax Amount":"6.50"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-08-14","Item Amount":"52.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Escondido North County Fair' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Escondido North County Fair' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_324(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Worcester Airport','MerchantAddress':'6718 Flores St, Worcester, MA 58468, USA','TransactionDate':'2021-04-20',,'Total':'653.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MA','Description':'Company travel - Manufacturing Excellence Summit in Worcester. 3 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-17","Item Amount":"140.24"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-17","Item Tax Amount":"7.45"},{"Item Name":"Incidentals","Transaction Date":"2021-04-17","Item Amount":"31.48"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-17","Item Amount":"59.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-18","Item Amount":"154.55"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-18","Item Tax Amount":"8.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-18","Item Amount":"61.27"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-19","Item Amount":"122.16"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-19","Item Tax Amount":"6.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-19","Item Amount":"62.11"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Worcester Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Worcester Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_325(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Brownsville Downtown','MerchantAddress':'5448 Fisher Dr, Brownsville, TX 49969, USA','TransactionDate':'2022-11-03',,'Total':'671.36','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Analytics Leadership Summit conference in Brownsville. merger and acquisition discussions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-01","Item Amount":"200.68"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-01","Item Tax Amount":"12.06"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-11-01","Item Amount":"38.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-01","Item Amount":"75.69"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-02","Item Amount":"193.49"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-02","Item Tax Amount":"11.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-02","Item Amount":"92.76"},{"Item Name":"Incidentals","Transaction Date":"2022-11-02","Item Amount":"46.76"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Brownsville Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Brownsville Downtown' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_326(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Cincinnati Hyde Park','MerchantAddress':'314 Gomez Ave, Cincinnati, OH 19787, USA','TransactionDate':'2021-01-21',,'Total':'236.19','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business trip to Cincinnati for client meetings. Attended Corporate Strategy Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-20","Item Amount":"106.61"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-20","Item Tax Amount":"6.92"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-20","Item Tax Amount":"2.31"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-01-20","Item Amount":"18.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-20","Item Amount":"52.89"},{"Item Name":"Incidentals","Transaction Date":"2021-01-20","Item Amount":"48.65"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Cincinnati Hyde Park' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Cincinnati Hyde Park' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_327(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Cary Crossroads','MerchantAddress':'5218 Madison Ave, Cary, NC 92305, USA','TransactionDate':'2021-10-16',,'Total':'823.06','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Business trip to Cary for quarterly reviews. Attended Project Management Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-13","Item Amount":"164.15"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-13","Item Tax Amount":"9.60"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-13","Item Tax Amount":"14.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-13","Item Amount":"63.97"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-14","Item Amount":"183.81"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-14","Item Tax Amount":"10.75"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-14","Item Tax Amount":"16.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-14","Item Amount":"74.18"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-10-15","Item Amount":"187.28"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-15","Item Tax Amount":"10.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-10-15","Item Tax Amount":"16.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-10-15","Item Amount":"71.40"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Cary Crossroads' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Cary Crossroads' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_328(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Modesto Airport','MerchantAddress':'9966 Adams St, Modesto, CA 17631, USA','TransactionDate':'2022-05-10',,'Total':'1650.57','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Project Management Summit in Modesto. 4 business nights for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-06","Item Amount":"312.62"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-06","Item Tax Amount":"24.35"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-06","Item Tax Amount":"16.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-06","Item Amount":"57.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-07","Item Amount":"279.67"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-07","Item Tax Amount":"21.78"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-07","Item Tax Amount":"14.52"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-07","Item Amount":"59.60"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-08","Item Amount":"311.33"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-08","Item Tax Amount":"24.25"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-08","Item Tax Amount":"16.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-08","Item Amount":"55.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-09","Item Amount":"281.10"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-09","Item Tax Amount":"21.89"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-09","Item Tax Amount":"14.60"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-05-09","Item Amount":"73.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-09","Item Amount":"65.90"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Modesto Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Modesto Airport' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_329(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Lansing Michigan State University','MerchantAddress':'4324 Torres Ave, Lansing, MI 15042, USA','TransactionDate':'2022-08-15',,'Total':'1871.13','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Corporate trip - Marketing Analytics Summit conference in Lansing. merger and acquisition discussions over 4 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-11","Item Amount":"354.48"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-11","Item Tax Amount":"17.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-11","Item Amount":"71.58"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-12","Item Amount":"339.35"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-12","Item Tax Amount":"16.79"},{"Item Name":"Entertainment External","Transaction Date":"2022-08-12","Item Amount":"70.39"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-12","Item Amount":"79.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-13","Item Amount":"334.87"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-13","Item Tax Amount":"16.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-13","Item Amount":"59.38"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-08-14","Item Amount":"369.52"},{"Item Name":"Hotel Tax","Transaction Date":"2022-08-14","Item Tax Amount":"18.28"},{"Item Name":"Incidentals","Transaction Date":"2022-08-14","Item Amount":"25.81"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-08-14","Item Amount":"80.35"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-08-15","Item Amount":"16.43"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Lansing Michigan State University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Lansing Michigan State University' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_330(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Cary Crossroads','MerchantAddress':'1313 Flores St, Cary, NC 61319, USA','TransactionDate':'2024-10-10',,'Total':'518.08','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Business trip to Cary for client meetings. Attended Real Estate Investment Summit. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-09","Item Amount":"261.20"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-09","Item Tax Amount":"23.01"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-10-09","Item Amount":"89.81"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-10-09","Item Amount":"12.66"},{"Item Name":"Incidentals","Transaction Date":"2024-10-09","Item Amount":"47.84"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-09","Item Amount":"83.56"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Cary Crossroads' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Cary Crossroads' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_331(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Albuquerque Uptown','MerchantAddress':'9163 Garcia St, Albuquerque, NM 22907, USA','TransactionDate':'2023-03-16',,'Total':'553.45','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NM','Description':'Company travel - Digital Marketing Conference in Albuquerque. 4 business nights for operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-12","Item Amount":"90.36"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-12","Item Tax Amount":"6.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-12","Item Amount":"37.19"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-13","Item Amount":"83.46"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-13","Item Tax Amount":"6.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-13","Item Amount":"40.45"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-14","Item Amount":"105.66"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-14","Item Tax Amount":"7.90"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-03-14","Item Amount":"20.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-14","Item Amount":"28.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-15","Item Amount":"92.80"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-15","Item Tax Amount":"6.94"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-15","Item Amount":"26.25"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Albuquerque Uptown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Albuquerque Uptown' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_332(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Abilene Mall of Abilene','MerchantAddress':'3760 Walker St, Abilene, TX 76588, USA','TransactionDate':'2022-09-07',,'Total':'322.25','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Abilene for Change Management Conference. 2 nights stay for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-05","Item Amount":"72.82"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-05","Item Tax Amount":"1.61"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-05","Item Tax Amount":"4.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-05","Item Amount":"60.87"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-06","Item Amount":"80.97"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-06","Item Tax Amount":"1.78"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-06","Item Tax Amount":"5.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-06","Item Amount":"74.20"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-09-07","Item Amount":"19.83"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Abilene Mall of Abilene' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Abilene Mall of Abilene' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_333(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Murfreesboro Avenue Murfreesboro','MerchantAddress':'697 Howard St, Murfreesboro, TN 64352, USA','TransactionDate':'2021-11-15',,'Total':'417.4','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company business trip - Attended AI & Machine Learning Conference in Murfreesboro. 3 business nights; client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-12","Item Amount":"80.97"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-12","Item Tax Amount":"2.32"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-12","Item Tax Amount":"6.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-12","Item Amount":"61.25"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-13","Item Amount":"73.68"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-13","Item Tax Amount":"2.11"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-13","Item Tax Amount":"6.32"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-13","Item Amount":"51.16"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-14","Item Amount":"69.52"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-14","Item Tax Amount":"1.99"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-14","Item Tax Amount":"1.99"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-14","Item Tax Amount":"5.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-14","Item Amount":"53.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Murfreesboro Avenue Murfreesboro' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Murfreesboro Avenue Murfreesboro' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_334(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Spokane Airport','MerchantAddress':'6611 Franklin Ave, Spokane, WA 47861, USA','TransactionDate':'2023-07-16',,'Total':'1818.72','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Company travel - Customer Experience Summit in Spokane. 4 business nights for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-12","Item Amount":"319.95"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-12","Item Tax Amount":"12.88"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-12","Item Tax Amount":"19.33"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-12","Item Amount":"50.53"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-13","Item Amount":"322.58"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-13","Item Tax Amount":"12.99"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-13","Item Tax Amount":"19.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-13","Item Amount":"66.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-14","Item Amount":"323.32"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-14","Item Tax Amount":"13.02"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-14","Item Tax Amount":"19.53"},{"Item Name":"Incidentals","Transaction Date":"2023-07-14","Item Amount":"46.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-14","Item Amount":"65.64"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-15","Item Amount":"342.59"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-15","Item Tax Amount":"13.80"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-15","Item Tax Amount":"20.69"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-07-15","Item Amount":"80.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-15","Item Amount":"69.07"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Spokane Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Spokane Airport' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_335(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Fremont Mission San Jose','MerchantAddress':'1664 Howard St, Fremont, CA 96340, USA','TransactionDate':'2025-12-29',,'Total':'366.56','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Tech Innovation Conference in Fremont. 2 business nights for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-12-27","Item Amount":"123.15"},{"Item Name":"Hotel Tax","Transaction Date":"2025-12-27","Item Tax Amount":"8.84"},{"Item Name":"Hotel Tax","Transaction Date":"2025-12-27","Item Tax Amount":"2.95"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-12-27","Item Amount":"19.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-12-27","Item Amount":"24.61"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-12-28","Item Amount":"124.21"},{"Item Name":"Hotel Tax","Transaction Date":"2025-12-28","Item Tax Amount":"8.92"},{"Item Name":"Hotel Tax","Transaction Date":"2025-12-28","Item Tax Amount":"2.97"},{"Item Name":"Hotel Tax","Transaction Date":"2025-12-28","Item Tax Amount":"2.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-12-28","Item Amount":"48.16"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Fremont Mission San Jose' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Fremont Mission San Jose' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_336(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Visalia Airport','MerchantAddress':'3235 Taylor Ave, Visalia, CA 83834, USA','TransactionDate':'2020-12-13',,'Total':'663.79','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Visalia for quarterly reviews. Attended E-commerce Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-11","Item Amount":"240.39"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-11","Item Tax Amount":"18.24"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-11","Item Tax Amount":"6.08"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-11","Item Amount":"43.32"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-12","Item Amount":"227.89"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-12","Item Tax Amount":"17.29"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-12","Item Tax Amount":"5.76"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-12","Item Tax Amount":"5.76"},{"Item Name":"Entertainment External","Transaction Date":"2020-12-12","Item Amount":"68.67"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-12","Item Amount":"30.39"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Visalia Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Visalia Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_337(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Abilene Airport','MerchantAddress':'5213 School St, Abilene, TX 75528, USA','TransactionDate':'2023-11-13',,'Total':'1180.66','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Legal Technology Conference in Abilene. 4 business nights; technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-11-09","Item Amount":"238.43"},{"Item Name":"Hotel Tax","Transaction Date":"2023-11-09","Item Tax Amount":"18.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-11-09","Item Amount":"58.27"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-11-10","Item Amount":"220.71"},{"Item Name":"Hotel Tax","Transaction Date":"2023-11-10","Item Tax Amount":"16.84"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-11-10","Item Amount":"38.63"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-11-11","Item Amount":"211.66"},{"Item Name":"Hotel Tax","Transaction Date":"2023-11-11","Item Tax Amount":"16.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-11-11","Item Amount":"53.29"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-11-12","Item Amount":"232.70"},{"Item Name":"Hotel Tax","Transaction Date":"2023-11-12","Item Tax Amount":"17.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-11-12","Item Amount":"58.04"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Abilene Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Abilene Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_338(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Kent SouthCenter','MerchantAddress':'5250 Oak St, Kent, WA 26660, USA','TransactionDate':'2021-12-04',,'Total':'245.22','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Business trip to Kent for vendor negotiations. Attended Blockchain Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-03","Item Amount":"197.49"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-03","Item Tax Amount":"9.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-03","Item Amount":"37.76"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Kent SouthCenter' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Kent SouthCenter' have all 3 required itemizations'?,",
#     )


# def test_expense_hotel_339(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta McKinney Airport','MerchantAddress':'5766 Morris Ave, McKinney, TX 87841, USA','TransactionDate':'2023-04-02',,'Total':'509.28','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - HR Leadership Summit conference in McKinney. partnership development meetings over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-01","Item Amount":"194.28"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-01","Item Tax Amount":"7.51"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-01","Item Tax Amount":"11.27"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-04-01","Item Amount":"185.59"},{"Item Name":"Laundry","Transaction Date":"2023-04-01","Item Amount":"31.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-01","Item Amount":"79.47"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta McKinney Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta McKinney Airport' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_340(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Hayward Airport','MerchantAddress':'3300 Convention Center Dr, Hayward, CA 43086, USA','TransactionDate':'2025-04-20',,'Total':'595.01','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company business trip - Attended Product Management Summit in Hayward. 3 business nights; operational excellence workshops.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-17","Item Amount":"120.44"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-17","Item Tax Amount":"5.92"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-17","Item Amount":"74.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-18","Item Amount":"105.85"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-18","Item Tax Amount":"5.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-18","Item Amount":"70.03"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-19","Item Amount":"127.13"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-19","Item Tax Amount":"6.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-19","Item Amount":"79.83"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Hayward Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Hayward Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_341(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Scranton Dunmore','MerchantAddress':'2353 Market St, Scranton, PA 86724, USA','TransactionDate':'2023-03-09',,'Total':'353.31','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'PA','Description':'Corporate trip - Cybersecurity Conference conference in Scranton. strategic planning sessions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-07","Item Amount":"93.08"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-07","Item Tax Amount":"3.21"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-07","Item Tax Amount":"4.82"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-07","Item Amount":"78.04"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-03-08","Item Amount":"107.27"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-08","Item Tax Amount":"3.70"},{"Item Name":"Hotel Tax","Transaction Date":"2023-03-08","Item Tax Amount":"5.56"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-03-08","Item Amount":"57.63"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Scranton Dunmore' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Scranton Dunmore' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_342(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Charleston Downtown','MerchantAddress':'1860 Bell St, Charleston, SC 74941, USA','TransactionDate':'2023-09-24',,'Total':'223.33','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'SC','Description':'Business travel to Charleston for Corporate Strategy Summit. 1 night stay for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-09-23","Item Amount":"61.90"},{"Item Name":"Hotel Tax","Transaction Date":"2023-09-23","Item Tax Amount":"4.39"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-09-23","Item Amount":"128.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-09-23","Item Amount":"28.63"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Charleston Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Charleston Downtown' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_343(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Comfort Inn Ontario Mills at Ontario','MerchantAddress':'3834 Main St, Ontario, CA 56861, USA','TransactionDate':'2025-02-17',,'Total':'1177.1','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Ontario for Manufacturing Excellence Summit. 4 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-13","Item Amount":"213.07"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-13","Item Tax Amount":"15.03"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-13","Item Tax Amount":"10.02"},{"Item Name":"Entertainment External","Transaction Date":"2025-02-13","Item Amount":"45.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-13","Item Amount":"45.14"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-14","Item Amount":"233.52"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-14","Item Tax Amount":"16.47"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-14","Item Tax Amount":"10.98"},{"Item Name":"Laundry","Transaction Date":"2025-02-14","Item Amount":"36.80"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-14","Item Amount":"34.93"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-15","Item Amount":"203.62"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-15","Item Tax Amount":"14.36"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-15","Item Tax Amount":"9.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-15","Item Amount":"33.28"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-02-16","Item Amount":"204.58"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-16","Item Tax Amount":"14.43"},{"Item Name":"Hotel Tax","Transaction Date":"2025-02-16","Item Tax Amount":"9.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-02-16","Item Amount":"25.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Comfort Inn Ontario Mills at Ontario' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Comfort Inn Ontario Mills at Ontario' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_344(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Newark Downtown','MerchantAddress':'821 Carter St, Newark, NJ 43170, USA','TransactionDate':'2024-09-12',,'Total':'905.9','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Business trip to Newark for client meetings. Attended E-commerce Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-09","Item Amount":"218.15"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-09","Item Tax Amount":"14.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-09","Item Amount":"51.76"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-10","Item Amount":"229.37"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-10","Item Tax Amount":"15.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-10","Item Amount":"66.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-09-11","Item Amount":"245.01"},{"Item Name":"Hotel Tax","Transaction Date":"2024-09-11","Item Tax Amount":"16.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-09-11","Item Amount":"47.94"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Newark Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Newark Downtown' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_345(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Akron University of Akron','MerchantAddress':'9956 Collins St, Akron, OH 72717, USA','TransactionDate':'2022-06-03',,'Total':'420.08','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Company travel - Marketing Analytics Summit in Akron. 2 business nights for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-01","Item Amount":"111.10"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-01","Item Tax Amount":"8.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-01","Item Amount":"84.00"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-02","Item Amount":"110.80"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-02","Item Tax Amount":"8.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-02","Item Amount":"98.16"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Akron University of Akron' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Akron University of Akron' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_346(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'DoubleTree Des Moines East Village','MerchantAddress':'8324 Parker Dr, Des Moines, IA 57360, USA','TransactionDate':'2023-12-10',,'Total':'460.35','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IA','Description':'Corporate trip - IoT Solutions Summit conference in Des Moines. product demos and customer meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-08","Item Amount":"168.07"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-08","Item Tax Amount":"11.20"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-08","Item Tax Amount":"7.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-08","Item Amount":"35.97"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-12-09","Item Amount":"172.79"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-09","Item Tax Amount":"11.52"},{"Item Name":"Hotel Tax","Transaction Date":"2023-12-09","Item Tax Amount":"7.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-12-09","Item Amount":"45.65"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'DoubleTree Des Moines East Village' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'DoubleTree Des Moines East Village' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_347(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Chattanooga Southside','MerchantAddress':'6978 Rivera Ave, Chattanooga, TN 20035, USA','TransactionDate':'2024-04-10',,'Total':'780.99','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company business trip - Attended Sales Leadership Conference in Chattanooga. 4 business nights; market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-06","Item Amount":"117.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-06","Item Tax Amount":"2.95"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-06","Item Tax Amount":"8.84"},{"Item Name":"Laundry","Transaction Date":"2024-04-06","Item Amount":"30.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-06","Item Amount":"36.14"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-07","Item Amount":"123.09"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-07","Item Tax Amount":"3.09"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-07","Item Tax Amount":"3.09"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-07","Item Tax Amount":"9.26"},{"Item Name":"Entertainment External","Transaction Date":"2024-04-07","Item Amount":"92.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-07","Item Amount":"25.13"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-08","Item Amount":"105.86"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-08","Item Tax Amount":"2.66"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-08","Item Tax Amount":"2.66"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-08","Item Tax Amount":"7.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-08","Item Amount":"24.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-04-09","Item Amount":"130.74"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-09","Item Tax Amount":"3.28"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-09","Item Tax Amount":"3.28"},{"Item Name":"Hotel Tax","Transaction Date":"2024-04-09","Item Tax Amount":"9.84"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-04-09","Item Amount":"37.55"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Chattanooga Southside' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Chattanooga Southside' have all 21 required itemizations'?,",
#     )


# def test_expense_hotel_348(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Lubbock Tech Terrace','MerchantAddress':'7467 Howard St, Lubbock, TX 70722, USA','TransactionDate':'2025-11-29',,'Total':'606.18','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Sales Leadership Conference in Lubbock. 4 business nights; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-25","Item Amount":"86.46"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-25","Item Tax Amount":"1.79"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-25","Item Tax Amount":"1.79"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-25","Item Tax Amount":"5.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-25","Item Amount":"61.56"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-26","Item Amount":"82.09"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-26","Item Tax Amount":"1.70"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-26","Item Tax Amount":"5.10"},{"Item Name":"Hotel Telephone","Transaction Date":"2025-11-26","Item Amount":"17.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-26","Item Amount":"50.10"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-27","Item Amount":"92.58"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-27","Item Tax Amount":"1.92"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-27","Item Tax Amount":"1.92"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-27","Item Tax Amount":"5.75"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-27","Item Amount":"43.32"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-11-28","Item Amount":"91.32"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-28","Item Tax Amount":"1.89"},{"Item Name":"Hotel Tax","Transaction Date":"2025-11-28","Item Tax Amount":"5.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-11-28","Item Amount":"48.77"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Lubbock Tech Terrace' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Lubbock Tech Terrace' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_349(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Bakersfield Northeast','MerchantAddress':'6957 King Dr, Bakersfield, CA 23775, USA','TransactionDate':'2024-10-18',,'Total':'640.09','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Digital Marketing Conference in Bakersfield. 3 business nights for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-15","Item Amount":"151.52"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-15","Item Tax Amount":"7.31"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-15","Item Tax Amount":"2.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-15","Item Amount":"36.44"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-16","Item Amount":"145.13"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-16","Item Tax Amount":"7.00"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-16","Item Tax Amount":"2.33"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-10-16","Item Amount":"18.16"},{"Item Name":"Hotel Telephone","Transaction Date":"2024-10-16","Item Amount":"24.26"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-16","Item Amount":"39.96"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-17","Item Amount":"147.24"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-17","Item Tax Amount":"7.10"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-17","Item Tax Amount":"2.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-17","Item Amount":"48.83"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Bakersfield Northeast' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Bakersfield Northeast' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_350(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental Amarillo Airport','MerchantAddress':'6746 Walker St, Amarillo, TX 32738, USA','TransactionDate':'2021-11-18',,'Total':'948.25','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Business travel to Amarillo for Digital Transformation Summit. 4 nights stay for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-14","Item Amount":"191.48"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-14","Item Tax Amount":"12.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-14","Item Amount":"29.63"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-15","Item Amount":"193.37"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-15","Item Tax Amount":"12.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-15","Item Amount":"32.53"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-16","Item Amount":"167.55"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-16","Item Tax Amount":"10.90"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-16","Item Amount":"31.74"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-17","Item Amount":"203.27"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-17","Item Tax Amount":"13.23"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-11-17","Item Amount":"7.31"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-17","Item Amount":"42.20"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental Amarillo Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental Amarillo Airport' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_351(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Elizabeth Jersey Gardens','MerchantAddress':'8159 White St, Elizabeth, NJ 14112, USA','TransactionDate':'2021-02-19',,'Total':'826.14','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NJ','Description':'Business trip to Elizabeth for team training. Attended Digital Marketing Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-15","Item Amount":"109.79"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-15","Item Tax Amount":"9.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-15","Item Tax Amount":"3.25"},{"Item Name":"Entertainment External","Transaction Date":"2021-02-15","Item Amount":"39.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-15","Item Amount":"40.90"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-16","Item Amount":"142.49"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-16","Item Tax Amount":"12.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-16","Item Tax Amount":"4.22"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-02-16","Item Amount":"21.90"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-16","Item Amount":"48.02"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-17","Item Amount":"139.60"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-17","Item Tax Amount":"12.39"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-17","Item Tax Amount":"4.13"},{"Item Name":"Laundry","Transaction Date":"2021-02-17","Item Amount":"19.91"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-17","Item Amount":"45.82"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-02-18","Item Amount":"109.93"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-18","Item Tax Amount":"9.76"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-18","Item Tax Amount":"3.25"},{"Item Name":"Hotel Tax","Transaction Date":"2021-02-18","Item Tax Amount":"3.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-02-18","Item Amount":"45.71"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Elizabeth Jersey Gardens' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Elizabeth Jersey Gardens' have all 20 required itemizations'?,",
#     )


# def test_expense_hotel_352(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Spokane Airport','MerchantAddress':'3099 Business District Way, Spokane, WA 85004, USA','TransactionDate':'2025-01-09',,'Total':'127.3','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WA','Description':'Company business trip - Attended Manufacturing Excellence Summit in Spokane. 1 business night; technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-08","Item Amount":"82.45"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-08","Item Tax Amount":"2.43"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-08","Item Tax Amount":"7.28"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-08","Item Amount":"35.14"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Spokane Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Spokane Airport' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_353(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Scranton University of Scranton','MerchantAddress':'633 Williams Dr, Scranton, PA 46035, USA','TransactionDate':'2023-02-24',,'Total':'494.21','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'PA','Description':'Company travel - Project Management Summit in Scranton. 2 business nights for sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-02-22","Item Amount":"185.69"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-22","Item Tax Amount":"13.42"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-22","Item Tax Amount":"8.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-02-22","Item Amount":"35.87"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-02-23","Item Amount":"189.57"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-23","Item Tax Amount":"13.70"},{"Item Name":"Hotel Tax","Transaction Date":"2023-02-23","Item Tax Amount":"9.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-02-23","Item Amount":"37.88"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Scranton University of Scranton' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Scranton University of Scranton' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_354(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Dayton Airport','MerchantAddress':'2248 Fisher Dr, Dayton, OH 40165, USA','TransactionDate':'2021-04-29',,'Total':'670.45','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business trip to Dayton for market expansion. Attended Corporate Strategy Summit. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-27","Item Amount":"220.54"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-27","Item Tax Amount":"6.47"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-27","Item Tax Amount":"19.40"},{"Item Name":"Entertainment External","Transaction Date":"2021-04-27","Item Amount":"57.14"},{"Item Name":"Laundry","Transaction Date":"2021-04-27","Item Amount":"31.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-27","Item Amount":"18.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-04-28","Item Amount":"229.88"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-28","Item Tax Amount":"6.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-28","Item Tax Amount":"20.22"},{"Item Name":"Hotel Tax","Transaction Date":"2021-04-28","Item Tax Amount":"6.74"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-04-28","Item Amount":"28.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-04-28","Item Amount":"24.83"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Dayton Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Dayton Airport' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_355(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Murfreesboro Middle Tennessee State University','MerchantAddress':'8853 Watson St, Murfreesboro, TN 86855, USA','TransactionDate':'2025-04-25',,'Total':'1296.11','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TN','Description':'Company business trip - Attended AI & Machine Learning Conference in Murfreesboro. 4 business nights; sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-21","Item Amount":"220.51"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-21","Item Tax Amount":"10.05"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-21","Item Tax Amount":"15.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-21","Item Amount":"69.20"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-22","Item Amount":"226.59"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-22","Item Tax Amount":"10.32"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-22","Item Tax Amount":"15.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-22","Item Amount":"48.77"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-23","Item Amount":"220.19"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-23","Item Tax Amount":"10.03"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-23","Item Tax Amount":"15.05"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-04-23","Item Amount":"68.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-23","Item Amount":"49.49"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-24","Item Amount":"229.06"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-24","Item Tax Amount":"10.44"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-24","Item Tax Amount":"15.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-24","Item Amount":"61.97"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Murfreesboro Middle Tennessee State University' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Murfreesboro Middle Tennessee State University' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_356(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Thousand Oaks Janss Marketplace','MerchantAddress':'9763 Moore St, Thousand Oaks, CA 31491, USA','TransactionDate':'2019-04-04',,'Total':'676.93','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Thousand Oaks for Tech Innovation Conference. 3 nights stay for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-01","Item Amount":"156.39"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-01","Item Tax Amount":"10.72"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-01","Item Tax Amount":"3.57"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-01","Item Tax Amount":"3.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-01","Item Amount":"45.89"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-02","Item Amount":"156.73"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-02","Item Tax Amount":"10.74"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-02","Item Tax Amount":"3.58"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-02","Item Amount":"42.99"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-04-03","Item Amount":"174.96"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-03","Item Tax Amount":"11.99"},{"Item Name":"Hotel Tax","Transaction Date":"2019-04-03","Item Tax Amount":"4.00"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-04-03","Item Amount":"51.80"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Thousand Oaks Janss Marketplace' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Thousand Oaks Janss Marketplace' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_357(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Winston-Salem Ardmore','MerchantAddress':'4830 Young St, Winston-Salem, NC 98674, USA','TransactionDate':'2022-05-14',,'Total':'921.11','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Company travel - Data Science Summit in Winston-Salem. 3 business nights for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-11","Item Amount":"248.95"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-11","Item Tax Amount":"21.17"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-11","Item Amount":"46.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-12","Item Amount":"233.11"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-12","Item Tax Amount":"19.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-12","Item Amount":"47.99"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-05-13","Item Amount":"249.04"},{"Item Name":"Hotel Tax","Transaction Date":"2022-05-13","Item Tax Amount":"21.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-05-13","Item Amount":"33.27"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Winston-Salem Ardmore' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Winston-Salem Ardmore' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_358(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Fort Wayne Southwest','MerchantAddress':'3428 Stewart Blvd, Fort Wayne, IN 59802, USA','TransactionDate':'2021-06-25',,'Total':'1480.8','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IN','Description':'Business trip to Fort Wayne for partnership development. Attended Mobile Technology Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-21","Item Amount":"246.59"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-21","Item Tax Amount":"8.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-21","Item Tax Amount":"13.11"},{"Item Name":"Entertainment External","Transaction Date":"2021-06-21","Item Amount":"132.23"},{"Item Name":"Laundry","Transaction Date":"2021-06-21","Item Amount":"15.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-21","Item Amount":"81.22"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-22","Item Amount":"234.94"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-22","Item Tax Amount":"8.33"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-22","Item Tax Amount":"12.50"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-06-22","Item Amount":"19.22"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-22","Item Amount":"57.51"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-23","Item Amount":"237.96"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-23","Item Tax Amount":"8.44"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-23","Item Tax Amount":"12.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-23","Item Amount":"72.28"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-06-24","Item Amount":"237.46"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-24","Item Tax Amount":"8.42"},{"Item Name":"Hotel Tax","Transaction Date":"2021-06-24","Item Tax Amount":"12.63"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-06-24","Item Amount":"60.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Fort Wayne Southwest' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Fort Wayne Southwest' have all 19 required itemizations'?,",
#     )


# def test_expense_hotel_359(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hampton Inn Denver Downtown','MerchantAddress':'5177 Garcia St, Denver, CO 21169, USA','TransactionDate':'2022-06-22',,'Total':'1461.32','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Company travel - Digital Marketing Conference in Denver. 4 business nights for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-18","Item Amount":"266.04"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-18","Item Tax Amount":"16.74"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-18","Item Amount":"60.52"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-19","Item Amount":"254.19"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-19","Item Tax Amount":"15.99"},{"Item Name":"Entertainment External","Transaction Date":"2022-06-19","Item Amount":"88.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-19","Item Amount":"48.61"},{"Item Name":"Incidentals","Transaction Date":"2022-06-19","Item Amount":"37.83"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-20","Item Amount":"264.78"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-20","Item Tax Amount":"16.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-20","Item Amount":"50.29"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-21","Item Amount":"266.72"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-21","Item Tax Amount":"16.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-21","Item Amount":"57.49"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hampton Inn Denver Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hampton Inn Denver Downtown' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_360(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Cape Coral Airport','MerchantAddress':'9592 Commerce St, Cape Coral, FL 80987, USA','TransactionDate':'2021-09-05',,'Total':'605.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Cape Coral for Customer Experience Summit. 3 nights stay for partnership development meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-02","Item Amount":"132.69"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-02","Item Tax Amount":"9.47"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-09-02","Item Amount":"80.14"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-02","Item Amount":"31.18"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-03","Item Amount":"150.74"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-03","Item Tax Amount":"10.76"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-09-03","Item Amount":"13.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-03","Item Amount":"30.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-09-04","Item Amount":"118.66"},{"Item Name":"Hotel Tax","Transaction Date":"2021-09-04","Item Tax Amount":"8.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-09-04","Item Amount":"19.61"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Cape Coral Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Cape Coral Airport' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_361(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Irvine Spectrum Center','MerchantAddress':'267 Carter St, Irvine, CA 90653, USA','TransactionDate':'2022-06-13',,'Total':'1225.09','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Irvine for Legal Technology Conference. 4 nights stay for technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-09","Item Amount":"224.15"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-09","Item Tax Amount":"13.94"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-09","Item Amount":"38.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-10","Item Amount":"259.41"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-10","Item Tax Amount":"16.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-10","Item Amount":"40.97"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-11","Item Amount":"223.02"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-11","Item Tax Amount":"13.87"},{"Item Name":"Entertainment External","Transaction Date":"2022-06-11","Item Amount":"42.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-11","Item Amount":"42.43"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-06-12","Item Amount":"233.18"},{"Item Name":"Hotel Tax","Transaction Date":"2022-06-12","Item Tax Amount":"14.50"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-06-12","Item Amount":"50.52"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-06-13","Item Amount":"12.41"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Irvine Spectrum Center' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Irvine Spectrum Center' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_362(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Denton Airport','MerchantAddress':'8647 Business District Way, Denton, TX 23536, USA','TransactionDate':'2020-10-19',,'Total':'894.03','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Corporate trip - Cybersecurity Conference conference in Denton. quarterly business reviews over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-17","Item Amount":"247.62"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-17","Item Tax Amount":"20.02"},{"Item Name":"Entertainment External","Transaction Date":"2020-10-17","Item Amount":"98.01"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-10-17","Item Amount":"133.62"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-17","Item Amount":"48.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-18","Item Amount":"261.57"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-18","Item Tax Amount":"21.15"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-10-18","Item Amount":"20.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-18","Item Amount":"42.40"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Denton Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Denton Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_363(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Visalia Downtown','MerchantAddress':'6446 Hughes Ave, Visalia, CA 42127, USA','TransactionDate':'2025-04-17',,'Total':'864.37','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Visalia for market expansion. Attended Legal Technology Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-14","Item Amount":"142.50"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-14","Item Tax Amount":"11.81"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-14","Item Tax Amount":"3.94"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-14","Item Tax Amount":"3.94"},{"Item Name":"Hotel Deposit","Transaction Date":"2025-04-14","Item Amount":"142.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-14","Item Amount":"74.19"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-15","Item Amount":"133.73"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-15","Item Tax Amount":"11.08"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-15","Item Tax Amount":"3.69"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-15","Item Tax Amount":"3.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-15","Item Amount":"54.50"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-04-16","Item Amount":"142.22"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-16","Item Tax Amount":"11.78"},{"Item Name":"Hotel Tax","Transaction Date":"2025-04-16","Item Tax Amount":"3.93"},{"Item Name":"Entertainment External","Transaction Date":"2025-04-16","Item Amount":"34.37"},{"Item Name":"Laundry","Transaction Date":"2025-04-16","Item Amount":"35.24"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-04-16","Item Amount":"51.29"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Visalia Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Visalia Downtown' have all 17 required itemizations'?,",
#     )


# def test_expense_hotel_364(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Fullerton Airport','MerchantAddress':'2184 Executive Way, Fullerton, CA 40700, USA','TransactionDate':'2024-10-30',,'Total':'1326.02','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Fullerton for strategic planning. Attended Retail Innovation Conference. 4 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-26","Item Amount":"185.24"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-26","Item Tax Amount":"11.48"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-26","Item Tax Amount":"3.83"},{"Item Name":"Gift and Entertainment","Transaction Date":"2024-10-26","Item Amount":"67.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-26","Item Amount":"73.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-27","Item Amount":"185.54"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-27","Item Tax Amount":"11.50"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-27","Item Tax Amount":"3.83"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-27","Item Tax Amount":"3.83"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-27","Item Amount":"76.26"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-28","Item Amount":"193.44"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-28","Item Tax Amount":"11.99"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-28","Item Tax Amount":"4.00"},{"Item Name":"Hotel Deposit","Transaction Date":"2024-10-28","Item Amount":"177.91"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-28","Item Amount":"70.01"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-10-29","Item Amount":"172.89"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-29","Item Tax Amount":"10.72"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-29","Item Tax Amount":"3.57"},{"Item Name":"Hotel Tax","Transaction Date":"2024-10-29","Item Tax Amount":"3.57"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-10-29","Item Amount":"54.79"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Fullerton Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Fullerton Airport' have all 20 required itemizations'?,",
#     )


# def test_expense_hotel_365(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Sheraton Madison Downtown','MerchantAddress':'9104 Davis St, Madison, WI 85958, USA','TransactionDate':'2023-04-09',,'Total':'980.43','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WI','Description':'Business travel to Madison for Manufacturing Excellence Summit. 3 nights stay for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-06","Item Amount":"174.82"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-06","Item Tax Amount":"13.11"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-06","Item Amount":"93.44"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-07","Item Amount":"152.40"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-07","Item Tax Amount":"11.43"},{"Item Name":"Hotel Deposit","Transaction Date":"2023-04-07","Item Amount":"137.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-07","Item Amount":"80.76"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-04-08","Item Amount":"184.20"},{"Item Name":"Hotel Tax","Transaction Date":"2023-04-08","Item Tax Amount":"13.81"},{"Item Name":"Laundry","Transaction Date":"2023-04-08","Item Amount":"33.71"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-04-08","Item Amount":"85.29"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Sheraton Madison Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Sheraton Madison Downtown' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_366(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Kansas City Strawberry Hill','MerchantAddress':'5602 Young St, Kansas City, KS 28793, USA','TransactionDate':'2022-01-30',,'Total':'980.74','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'KS','Description':'Corporate trip - Product Management Summit conference in Kansas City. vendor negotiations and contract reviews over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-27","Item Amount":"231.29"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-27","Item Tax Amount":"18.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-27","Item Amount":"79.84"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-28","Item Amount":"245.10"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-28","Item Tax Amount":"19.50"},{"Item Name":"Hotel Telephone","Transaction Date":"2022-01-28","Item Amount":"14.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-28","Item Amount":"57.72"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-01-29","Item Amount":"233.75"},{"Item Name":"Hotel Tax","Transaction Date":"2022-01-29","Item Tax Amount":"18.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-01-29","Item Amount":"61.59"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Kansas City Strawberry Hill' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Kansas City Strawberry Hill' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_367(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Scranton Viewmont Mall','MerchantAddress':'6851 Gray St, Scranton, PA 97263, USA','TransactionDate':'2020-10-28',,'Total':'841.04','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'PA','Description':'Business trip to Scranton for partnership development. Attended HR Leadership Summit. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-25","Item Amount":"152.94"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-25","Item Tax Amount":"4.44"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-25","Item Tax Amount":"13.32"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-25","Item Tax Amount":"4.44"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-10-25","Item Amount":"68.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-25","Item Amount":"82.49"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-26","Item Amount":"171.32"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-26","Item Tax Amount":"14.92"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-26","Item Tax Amount":"4.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-26","Item Amount":"77.14"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-10-27","Item Amount":"136.61"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-27","Item Tax Amount":"11.90"},{"Item Name":"Hotel Tax","Transaction Date":"2020-10-27","Item Tax Amount":"3.97"},{"Item Name":"Laundry","Transaction Date":"2020-10-27","Item Amount":"15.06"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-10-27","Item Amount":"78.86"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Scranton Viewmont Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Scranton Viewmont Mall' have all 15 required itemizations'?,",
#     )


# def test_expense_hotel_368(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'InterContinental West Jordan South Valley','MerchantAddress':'5286 Water St, West Jordan, UT 95915, USA','TransactionDate':'2020-11-11',,'Total':'1308.01','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'UT','Description':'Business travel to West Jordan for Analytics Leadership Summit. 4 nights stay for client sessions and project planning.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-07","Item Amount":"250.55"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-07","Item Tax Amount":"12.80"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-07","Item Amount":"55.35"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-08","Item Amount":"286.95"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-08","Item Tax Amount":"14.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-08","Item Amount":"48.88"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-09","Item Amount":"252.44"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-09","Item Tax Amount":"12.90"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-09","Item Amount":"57.27"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-10","Item Amount":"250.26"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-10","Item Tax Amount":"12.78"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-10","Item Amount":"53.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'InterContinental West Jordan South Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'InterContinental West Jordan South Valley' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_369(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Fayetteville Downtown','MerchantAddress':'1441 Diaz St, Fayetteville, NC 82136, USA','TransactionDate':'2020-12-11',,'Total':'599','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Business trip to Fayetteville for vendor negotiations. Attended Change Management Conference. 3 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-08","Item Amount":"131.02"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-08","Item Tax Amount":"11.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-08","Item Amount":"58.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-09","Item Amount":"128.91"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-09","Item Tax Amount":"10.94"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-09","Item Amount":"64.69"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-12-10","Item Amount":"130.76"},{"Item Name":"Hotel Tax","Transaction Date":"2020-12-10","Item Tax Amount":"11.10"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-12-10","Item Amount":"51.84"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Fayetteville Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Fayetteville Downtown' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_370(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Fairmont Pueblo Airport','MerchantAddress':'7542 Martinez Blvd, Pueblo, CO 85475, USA','TransactionDate':'2023-06-10',,'Total':'674.37','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Company business trip - Attended Product Management Summit in Pueblo. 2 business nights; technical workshops and knowledge sharing.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-08","Item Amount":"248.09"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-08","Item Tax Amount":"16.48"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-08","Item Tax Amount":"5.49"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-08","Item Tax Amount":"5.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-08","Item Amount":"72.73"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-06-09","Item Amount":"231.26"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-09","Item Tax Amount":"15.36"},{"Item Name":"Hotel Tax","Transaction Date":"2023-06-09","Item Tax Amount":"5.12"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-06-09","Item Amount":"74.35"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Fairmont Pueblo Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Fairmont Pueblo Airport' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_371(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Surprise Surprise Stadium','MerchantAddress':'7808 Lee Ave, Surprise, AZ 61351, USA','TransactionDate':'2020-01-13',,'Total':'510.83','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Business travel to Surprise for DevOps World. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-11","Item Amount":"188.80"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-11","Item Tax Amount":"9.45"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-11","Item Tax Amount":"6.30"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-11","Item Amount":"50.75"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-01-12","Item Amount":"167.80"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-12","Item Tax Amount":"8.40"},{"Item Name":"Hotel Tax","Transaction Date":"2020-01-12","Item Tax Amount":"5.60"},{"Item Name":"Hotel Breakfast","Transaction Date":"2020-01-12","Item Amount":"13.16"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-01-12","Item Amount":"60.57"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Surprise Surprise Stadium' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Surprise Surprise Stadium' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_372(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Holiday Inn Hialeah Westland Mall','MerchantAddress':'1975 Phillips Ave, Hialeah, FL 57658, USA','TransactionDate':'2024-03-05',,'Total':'527.33','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business travel to Hialeah for Digital Transformation Summit. 2 nights stay for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-03","Item Amount":"169.41"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-03","Item Tax Amount":"7.03"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-03","Item Tax Amount":"10.55"},{"Item Name":"Entertainment External","Transaction Date":"2024-03-03","Item Amount":"50.54"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-03","Item Amount":"45.85"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-03-04","Item Amount":"150.30"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-04","Item Tax Amount":"6.24"},{"Item Name":"Hotel Tax","Transaction Date":"2024-03-04","Item Tax Amount":"9.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-03-04","Item Amount":"40.42"},{"Item Name":"Incidentals","Transaction Date":"2024-03-04","Item Amount":"37.63"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Holiday Inn Hialeah Westland Mall' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Holiday Inn Hialeah Westland Mall' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_373(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Westin Akron Airport','MerchantAddress':'599 Lee Ave, Akron, OH 40387, USA','TransactionDate':'2020-11-18',,'Total':'606.6','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Business travel to Akron for Innovation Leadership Conference. 2 nights stay for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-16","Item Amount":"183.06"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-16","Item Tax Amount":"10.36"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-16","Item Tax Amount":"15.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-16","Item Amount":"22.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-17","Item Amount":"204.43"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-17","Item Tax Amount":"11.56"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-17","Item Tax Amount":"17.35"},{"Item Name":"Hotel Deposit","Transaction Date":"2020-11-17","Item Amount":"73.66"},{"Item Name":"Laundry","Transaction Date":"2020-11-17","Item Amount":"30.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-17","Item Amount":"37.58"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Westin Akron Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Westin Akron Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_374(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hyatt Akron Fairlawn','MerchantAddress':'5778 Hill Ave, Akron, OH 11459, USA','TransactionDate':'2020-02-08',,'Total':'1023.74','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Company business trip - Attended Retail Innovation Conference in Akron. 4 business nights; customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-04","Item Amount":"184.48"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-04","Item Tax Amount":"11.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-04","Item Amount":"55.12"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-05","Item Amount":"172.30"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-05","Item Tax Amount":"10.66"},{"Item Name":"Gift and Entertainment","Transaction Date":"2020-02-05","Item Amount":"32.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-05","Item Amount":"42.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-06","Item Amount":"184.68"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-06","Item Tax Amount":"11.43"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-06","Item Amount":"61.62"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-02-07","Item Amount":"192.75"},{"Item Name":"Hotel Tax","Transaction Date":"2020-02-07","Item Tax Amount":"11.93"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-02-07","Item Amount":"52.67"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hyatt Akron Fairlawn' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hyatt Akron Fairlawn' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_375(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Arlington Downtown','MerchantAddress':'3126 Roberts Dr, Arlington, TX 36418, USA','TransactionDate':'2025-01-14',,'Total':'777.1','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'TX','Description':'Company business trip - Attended Enterprise Software Summit in Arlington. 4 business nights; sales presentations and client onboarding.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-10","Item Amount":"105.48"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-10","Item Tax Amount":"5.08"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-10","Item Tax Amount":"7.62"},{"Item Name":"Incidentals","Transaction Date":"2025-01-10","Item Amount":"18.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-10","Item Amount":"81.09"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-11","Item Amount":"97.03"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-11","Item Tax Amount":"4.67"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-11","Item Tax Amount":"7.01"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-11","Item Amount":"68.27"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-12","Item Amount":"111.96"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-12","Item Tax Amount":"5.39"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-12","Item Tax Amount":"8.09"},{"Item Name":"Hotel Breakfast","Transaction Date":"2025-01-12","Item Amount":"12.37"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-12","Item Amount":"67.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2025-01-13","Item Amount":"95.01"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-13","Item Tax Amount":"4.58"},{"Item Name":"Hotel Tax","Transaction Date":"2025-01-13","Item Tax Amount":"6.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-01-13","Item Amount":"71.12"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Arlington Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Arlington Downtown' have all 18 required itemizations'?,",
#     )


# def test_expense_hotel_376(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Minneapolis Northeast','MerchantAddress':'4669 Monroe Dr, Minneapolis, MN 11820, USA','TransactionDate':'2022-11-08',,'Total':'613.32','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MN','Description':'Company business trip - Attended Blockchain Conference in Minneapolis. 3 business nights; vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-05","Item Amount":"150.20"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-05","Item Tax Amount":"3.46"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-05","Item Tax Amount":"10.38"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-05","Item Tax Amount":"3.46"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-05","Item Amount":"37.73"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-06","Item Amount":"161.37"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-06","Item Tax Amount":"3.72"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-06","Item Tax Amount":"11.15"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-06","Item Amount":"29.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-07","Item Amount":"154.73"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-07","Item Tax Amount":"3.56"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-07","Item Tax Amount":"10.69"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-07","Item Amount":"33.01"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Minneapolis Northeast' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Minneapolis Northeast' have all 13 required itemizations'?,",
#     )


# def test_expense_hotel_377(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Moreno Valley Airport','MerchantAddress':'6889 Collins St, Moreno Valley, CA 48973, USA','TransactionDate':'2022-04-29',,'Total':'716.09','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Moreno Valley for Quality Assurance Conference. 2 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-27","Item Amount":"223.58"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-27","Item Tax Amount":"18.63"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-27","Item Tax Amount":"12.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-27","Item Amount":"67.11"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-04-28","Item Amount":"218.47"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-28","Item Tax Amount":"18.20"},{"Item Name":"Hotel Tax","Transaction Date":"2022-04-28","Item Tax Amount":"12.13"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-04-28","Item Amount":"63.03"},{"Item Name":"Incidentals","Transaction Date":"2022-04-28","Item Amount":"19.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-04-28","Item Amount":"63.25"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Moreno Valley Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Moreno Valley Airport' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_378(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'JW Marriott Victorville Mall of Victor Valley','MerchantAddress':'1236 Powell St, Victorville, CA 57464, USA','TransactionDate':'2021-03-22',,'Total':'605.83','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Victorville for Business Intelligence Summit. 2 nights stay for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-20","Item Amount":"174.07"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-20","Item Tax Amount":"14.17"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-20","Item Tax Amount":"9.44"},{"Item Name":"Laundry","Transaction Date":"2021-03-20","Item Amount":"39.18"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-20","Item Amount":"79.80"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-03-21","Item Amount":"158.41"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-21","Item Tax Amount":"12.89"},{"Item Name":"Hotel Tax","Transaction Date":"2021-03-21","Item Tax Amount":"8.59"},{"Item Name":"Hotel Breakfast","Transaction Date":"2021-03-21","Item Amount":"27.27"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-03-21","Item Amount":"24.84"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-03-21","Item Amount":"57.17"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'JW Marriott Victorville Mall of Victor Valley' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'JW Marriott Victorville Mall of Victor Valley' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_379(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Ann Arbor Downtown','MerchantAddress':'7095 Howard St, Ann Arbor, MI 24689, USA','TransactionDate':'2024-05-15',,'Total':'824.31','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MI','Description':'Business travel to Ann Arbor for Corporate Strategy Summit. 3 nights stay for board meetings and investor presentations.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-12","Item Amount":"203.86"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-12","Item Tax Amount":"10.45"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-12","Item Amount":"38.08"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-13","Item Amount":"208.53"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-13","Item Tax Amount":"10.69"},{"Item Name":"Hotel Breakfast","Transaction Date":"2024-05-13","Item Amount":"14.86"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-13","Item Amount":"44.52"},{"Item Name":"Daily Room Rate","Transaction Date":"2024-05-14","Item Amount":"208.85"},{"Item Name":"Hotel Tax","Transaction Date":"2024-05-14","Item Tax Amount":"10.71"},{"Item Name":"Incidentals","Transaction Date":"2024-05-14","Item Amount":"19.87"},{"Item Name":"Room Service & Meals","Transaction Date":"2024-05-14","Item Amount":"53.89"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Ann Arbor Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Ann Arbor Downtown' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_380(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Torrance Redondo Beach','MerchantAddress':'5202 Foster Dr, Torrance, CA 93806, USA','TransactionDate':'2022-03-17',,'Total':'743.46','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Torrance for Sales Leadership Conference. 2 nights stay for merger and acquisition discussions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-15","Item Amount":"176.58"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-15","Item Tax Amount":"11.98"},{"Item Name":"Hotel Telephone","Transaction Date":"2022-03-15","Item Amount":"14.70"},{"Item Name":"Laundry","Transaction Date":"2022-03-15","Item Amount":"28.60"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-15","Item Amount":"62.57"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-16","Item Amount":"183.64"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-16","Item Tax Amount":"12.46"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-03-16","Item Amount":"181.97"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-16","Item Amount":"70.96"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Torrance Redondo Beach' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Torrance Redondo Beach' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_381(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Marriott Springfield Sangamon','MerchantAddress':'4219 Sanders St, Springfield, IL 32139, USA','TransactionDate':'2020-11-09',,'Total':'845.61','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'IL','Description':'Company travel - Marketing Analytics Summit in Springfield. 4 business nights for customer support and service reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-05","Item Amount":"135.80"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-05","Item Tax Amount":"12.05"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-05","Item Amount":"67.79"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-06","Item Amount":"117.70"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-06","Item Tax Amount":"10.44"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-06","Item Amount":"71.64"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-07","Item Amount":"139.09"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-07","Item Tax Amount":"12.34"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-07","Item Amount":"69.63"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-11-08","Item Amount":"115.14"},{"Item Name":"Hotel Tax","Transaction Date":"2020-11-08","Item Tax Amount":"10.21"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-11-08","Item Amount":"83.78"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Marriott Springfield Sangamon' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Marriott Springfield Sangamon' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_382(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Thornton Airport','MerchantAddress':'5243 Brown Ave, Thornton, CO 21395, USA','TransactionDate':'2022-03-23',,'Total':'995.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Company travel - Mobile Technology Conference in Thornton. 4 business nights for vendor negotiations and contract reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-19","Item Amount":"165.33"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-19","Item Tax Amount":"14.72"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-19","Item Tax Amount":"4.91"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-19","Item Amount":"53.40"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-20","Item Amount":"162.99"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-20","Item Tax Amount":"14.51"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-20","Item Tax Amount":"4.84"},{"Item Name":"Hotel Telephone","Transaction Date":"2022-03-20","Item Amount":"10.40"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-20","Item Amount":"57.59"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-21","Item Amount":"170.82"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-21","Item Tax Amount":"15.21"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-21","Item Tax Amount":"5.07"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-21","Item Tax Amount":"5.07"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-03-21","Item Amount":"26.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-21","Item Amount":"53.69"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-22","Item Amount":"157.82"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-22","Item Tax Amount":"14.05"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-22","Item Tax Amount":"4.68"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-22","Item Tax Amount":"4.68"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-22","Item Amount":"49.32"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Thornton Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Thornton Airport' have all 20 required itemizations'?,",
#     )


# def test_expense_hotel_383(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Rancho Cucamonga Town Square','MerchantAddress':'5910 Rogers St, Rancho Cucamonga, CA 91333, USA','TransactionDate':'2022-03-25',,'Total':'436.07','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Company travel - Data Science Summit in Rancho Cucamonga. 2 business nights for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-23","Item Amount":"80.12"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-23","Item Tax Amount":"7.07"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-23","Item Tax Amount":"4.71"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-23","Item Amount":"39.60"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-03-24","Item Amount":"95.22"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-24","Item Tax Amount":"8.40"},{"Item Name":"Hotel Tax","Transaction Date":"2022-03-24","Item Tax Amount":"5.60"},{"Item Name":"Entertainment External","Transaction Date":"2022-03-24","Item Amount":"96.41"},{"Item Name":"Hotel Breakfast","Transaction Date":"2022-03-24","Item Amount":"28.67"},{"Item Name":"Laundry","Transaction Date":"2022-03-24","Item Amount":"24.59"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-03-24","Item Amount":"45.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Rancho Cucamonga Town Square' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Rancho Cucamonga Town Square' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_384(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Grand Hyatt Thousand Oaks Airport','MerchantAddress':'9296 Roosevelt Way, Thousand Oaks, CA 74330, USA','TransactionDate':'2019-10-24',,'Total':'433.07','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business travel to Thousand Oaks for FinTech Conference. 2 nights stay for stakeholder reviews and partner meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-22","Item Amount":"179.69"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-22","Item Tax Amount":"10.14"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-22","Item Amount":"31.14"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-10-23","Item Amount":"164.66"},{"Item Name":"Hotel Tax","Transaction Date":"2019-10-23","Item Tax Amount":"9.29"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-10-23","Item Amount":"38.15"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Grand Hyatt Thousand Oaks Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Grand Hyatt Thousand Oaks Airport' have all 6 required itemizations'?,",
#     )


# def test_expense_hotel_385(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Pembroke Pines Century Village','MerchantAddress':'7535 Robinson Ave, Pembroke Pines, FL 96695, USA','TransactionDate':'2019-12-08',,'Total':'240.69','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Company travel - Analytics Leadership Summit in Pembroke Pines. 1 business night for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-12-07","Item Amount":"185.88"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-07","Item Tax Amount":"6.33"},{"Item Name":"Hotel Tax","Transaction Date":"2019-12-07","Item Tax Amount":"9.49"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-12-07","Item Amount":"38.99"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Pembroke Pines Century Village' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Pembroke Pines Century Village' have all 4 required itemizations'?,",
#     )


# def test_expense_hotel_386(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Chandler Kyrene','MerchantAddress':'8395 Roosevelt Way, Chandler, AZ 94051, USA','TransactionDate':'2025-06-24',,'Total':'460.58','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AZ','Description':'Business travel to Chandler for Legal Technology Conference. 1 night stay for market research and competitive analysis.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2025-06-23","Item Amount":"197.82"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-23","Item Tax Amount":"9.59"},{"Item Name":"Hotel Tax","Transaction Date":"2025-06-23","Item Tax Amount":"6.39"},{"Item Name":"Entertainment External","Transaction Date":"2025-06-23","Item Amount":"43.50"},{"Item Name":"Gift and Entertainment","Transaction Date":"2025-06-23","Item Amount":"89.10"},{"Item Name":"Laundry","Transaction Date":"2025-06-23","Item Amount":"26.95"},{"Item Name":"Room Service & Meals","Transaction Date":"2025-06-23","Item Amount":"87.23"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Chandler Kyrene' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Chandler Kyrene' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_387(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'La Quinta Huntsville Five Points','MerchantAddress':'6151 Reyes Dr, Huntsville, AL 37786, USA','TransactionDate':'2022-09-12',,'Total':'263.81','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AL','Description':'Corporate trip - Marketing Analytics Summit conference in Huntsville. compliance training and audits over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-11","Item Amount":"172.38"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-11","Item Tax Amount":"10.47"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-11","Item Amount":"80.96"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'La Quinta Huntsville Five Points' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'La Quinta Huntsville Five Points' have all 3 required itemizations'?,",
#     )


# def test_expense_hotel_388(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Hilton Birmingham Highland Park','MerchantAddress':'4900 Ramirez Blvd, Birmingham, AL 24046, USA','TransactionDate':'2019-09-07',,'Total':'396.71','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AL','Description':'Corporate trip - Supply Chain Management Conference conference in Birmingham. client sessions and project planning over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-05","Item Amount":"107.60"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-05","Item Tax Amount":"9.13"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-05","Item Amount":"55.80"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-09-06","Item Amount":"91.26"},{"Item Name":"Hotel Tax","Transaction Date":"2019-09-06","Item Tax Amount":"7.74"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-09-06","Item Amount":"24.19"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-09-06","Item Amount":"52.09"},{"Item Name":"Incidentals","Transaction Date":"2019-09-06","Item Amount":"48.90"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Hilton Birmingham Highland Park' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Hilton Birmingham Highland Park' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_389(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons Little Rock West Little Rock','MerchantAddress':'6812 Fisher Dr, Little Rock, AR 64398, USA','TransactionDate':'2023-07-14',,'Total':'308.39','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'AR','Description':'Business travel to Little Rock for FinTech Conference. 1 night stay for team building and training sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-07-13","Item Amount":"162.81"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-13","Item Tax Amount":"10.93"},{"Item Name":"Hotel Tax","Transaction Date":"2023-07-13","Item Tax Amount":"7.29"},{"Item Name":"Laundry","Transaction Date":"2023-07-13","Item Amount":"39.79"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-07-13","Item Amount":"87.57"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons Little Rock West Little Rock' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons Little Rock West Little Rock' have all 5 required itemizations'?,",
#     )


# def test_expense_hotel_390(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Ritz-Carlton Shreveport Highland','MerchantAddress':'1749 Morgan Ave, Shreveport, LA 79771, USA','TransactionDate':'2020-09-27',,'Total':'715.99','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'LA','Description':'Company travel - Business Intelligence Summit in Shreveport. 3 business nights for product demos and customer meetings.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-24","Item Amount":"169.06"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-24","Item Tax Amount":"9.76"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-24","Item Tax Amount":"3.25"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-24","Item Tax Amount":"3.25"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-24","Item Amount":"47.33"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-25","Item Amount":"177.88"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-25","Item Tax Amount":"10.27"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-25","Item Tax Amount":"3.42"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-25","Item Amount":"51.03"},{"Item Name":"Daily Room Rate","Transaction Date":"2020-09-26","Item Amount":"183.63"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-26","Item Tax Amount":"10.60"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-26","Item Tax Amount":"3.53"},{"Item Name":"Hotel Tax","Transaction Date":"2020-09-26","Item Tax Amount":"3.53"},{"Item Name":"Room Service & Meals","Transaction Date":"2020-09-26","Item Amount":"39.45"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Ritz-Carlton Shreveport Highland' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Ritz-Carlton Shreveport Highland' have all 14 required itemizations'?,",
#     )


# def test_expense_hotel_391(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Best Western Toledo Downtown','MerchantAddress':'6196 Roosevelt Way, Toledo, OH 28453, USA','TransactionDate':'2021-01-29',,'Total':'544.72','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'OH','Description':'Corporate trip - Healthcare IT Summit conference in Toledo. product demos and customer meetings over 3 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-26","Item Amount":"99.65"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-26","Item Tax Amount":"8.88"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-26","Item Amount":"53.49"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-27","Item Amount":"113.03"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-27","Item Tax Amount":"10.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-27","Item Amount":"56.19"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-01-28","Item Amount":"130.89"},{"Item Name":"Hotel Tax","Transaction Date":"2021-01-28","Item Tax Amount":"11.66"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-01-28","Item Amount":"60.86"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Best Western Toledo Downtown' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Best Western Toledo Downtown' have all 9 required itemizations'?,",
#     )


# def test_expense_hotel_392(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Four Seasons St. Petersburg The Pier','MerchantAddress':'3693 Church St, St. Petersburg, FL 71305, USA','TransactionDate':'2022-09-04',,'Total':'494.48','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Business trip to St. Petersburg for quarterly reviews. Attended Change Management Conference. 1 night accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-03","Item Amount":"163.99"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-03","Item Tax Amount":"4.49"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-03","Item Tax Amount":"13.47"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-03","Item Tax Amount":"4.49"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-09-03","Item Amount":"180.47"},{"Item Name":"Hotel Telephone","Transaction Date":"2022-09-03","Item Amount":"18.19"},{"Item Name":"Laundry","Transaction Date":"2022-09-03","Item Amount":"39.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-03","Item Amount":"70.36"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Four Seasons St. Petersburg The Pier' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Four Seasons St. Petersburg The Pier' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_393(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Lancaster The BLVD','MerchantAddress':'4989 White St, Lancaster, CA 54525, USA','TransactionDate':'2019-06-09',,'Total':'870.61','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Legal Technology Conference conference in Lancaster. partnership development meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-07","Item Amount":"330.37"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-07","Item Tax Amount":"21.10"},{"Item Name":"Laundry","Transaction Date":"2019-06-07","Item Amount":"36.51"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-07","Item Amount":"65.76"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-06-08","Item Amount":"340.04"},{"Item Name":"Hotel Tax","Transaction Date":"2019-06-08","Item Tax Amount":"21.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-06-08","Item Amount":"55.11"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Lancaster The BLVD' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Lancaster The BLVD' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_394(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'AC Hotel Lakewood Belmar','MerchantAddress':'7989 Parker Dr, Lakewood, CO 78540, USA','TransactionDate':'2023-01-04',,'Total':'664.59','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CO','Description':'Business travel to Lakewood for Analytics Leadership Summit. 2 nights stay for strategic planning sessions.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-02","Item Amount":"243.62"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-02","Item Tax Amount":"15.82"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-02","Item Tax Amount":"5.27"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-02","Item Tax Amount":"5.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-02","Item Amount":"52.86"},{"Item Name":"Daily Room Rate","Transaction Date":"2023-01-03","Item Amount":"246.47"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-03","Item Tax Amount":"16.00"},{"Item Name":"Hotel Tax","Transaction Date":"2023-01-03","Item Tax Amount":"5.33"},{"Item Name":"Hotel Telephone","Transaction Date":"2023-01-03","Item Amount":"12.27"},{"Item Name":"Room Service & Meals","Transaction Date":"2023-01-03","Item Amount":"61.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'AC Hotel Lakewood Belmar' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'AC Hotel Lakewood Belmar' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_395(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Kimpton Baltimore BWI','MerchantAddress':'4243 Campbell St, Baltimore, MD 39817, USA','TransactionDate':'2019-03-17',,'Total':'536.32','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'MD','Description':'Company travel - Blockchain Conference in Baltimore. 2 business nights for compliance training and audits.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-15","Item Amount":"176.43"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-15","Item Tax Amount":"10.60"},{"Item Name":"Hotel Telephone","Transaction Date":"2019-03-15","Item Amount":"8.65"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-15","Item Amount":"49.81"},{"Item Name":"Daily Room Rate","Transaction Date":"2019-03-16","Item Amount":"195.25"},{"Item Name":"Hotel Tax","Transaction Date":"2019-03-16","Item Tax Amount":"11.73"},{"Item Name":"Room Service & Meals","Transaction Date":"2019-03-16","Item Amount":"56.93"},{"Item Name":"Hotel Breakfast","Transaction Date":"2019-03-17","Item Amount":"26.92"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Kimpton Baltimore BWI' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Kimpton Baltimore BWI' have all 8 required itemizations'?,",
#     )


# def test_expense_hotel_396(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Residence Inn Milwaukee Airport','MerchantAddress':'6934 Torres Ave, Milwaukee, WI 91134, USA','TransactionDate':'2021-12-17',,'Total':'199.1','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'WI','Description':'Corporate trip - Data Science Summit conference in Milwaukee. vendor negotiations and contract reviews over 1 business day.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-12-16","Item Amount":"65.44"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-16","Item Tax Amount":"2.40"},{"Item Name":"Hotel Tax","Transaction Date":"2021-12-16","Item Tax Amount":"3.59"},{"Item Name":"Gift and Entertainment","Transaction Date":"2021-12-16","Item Amount":"53.14"},{"Item Name":"Hotel Telephone","Transaction Date":"2021-12-16","Item Amount":"10.73"},{"Item Name":"Incidentals","Transaction Date":"2021-12-16","Item Amount":"32.41"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-12-16","Item Amount":"31.39"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Residence Inn Milwaukee Airport' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Residence Inn Milwaukee Airport' have all 7 required itemizations'?,",
#     )


# def test_expense_hotel_397(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Aloft Durham Research Triangle','MerchantAddress':'3124 Walker St, Durham, NC 28327, USA','TransactionDate':'2022-11-18',,'Total':'516.34','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'NC','Description':'Company travel - Legal Technology Conference in Durham. 2 business nights for quarterly business reviews.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-16","Item Amount":"126.13"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-16","Item Tax Amount":"3.38"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-16","Item Tax Amount":"10.14"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-16","Item Tax Amount":"3.38"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-16","Item Amount":"57.13"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-11-17","Item Amount":"147.17"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-17","Item Tax Amount":"3.94"},{"Item Name":"Hotel Tax","Transaction Date":"2022-11-17","Item Tax Amount":"11.83"},{"Item Name":"Gift and Entertainment","Transaction Date":"2022-11-17","Item Amount":"71.94"},{"Item Name":"Incidentals","Transaction Date":"2022-11-17","Item Amount":"18.35"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-11-17","Item Amount":"62.95"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Aloft Durham Research Triangle' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Aloft Durham Research Triangle' have all 11 required itemizations'?,",
#     )


# def test_expense_hotel_398(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Renaissance Fullerton Sunny Hills','MerchantAddress':'3752 Rivera Ave, Fullerton, CA 68382, USA','TransactionDate':'2021-07-20',,'Total':'777.05','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Corporate trip - Product Management Summit conference in Fullerton. partnership development meetings over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-18","Item Amount":"215.71"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-18","Item Tax Amount":"18.79"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-18","Item Tax Amount":"6.26"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-18","Item Tax Amount":"6.26"},{"Item Name":"Entertainment External","Transaction Date":"2021-07-18","Item Amount":"103.07"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-18","Item Amount":"93.78"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-07-19","Item Amount":"218.94"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-19","Item Tax Amount":"19.07"},{"Item Name":"Hotel Tax","Transaction Date":"2021-07-19","Item Tax Amount":"6.36"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-07-19","Item Amount":"88.81"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Renaissance Fullerton Sunny Hills' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Renaissance Fullerton Sunny Hills' have all 10 required itemizations'?,",
#     )


# def test_expense_hotel_399(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'Courtyard Hialeah Palmetto','MerchantAddress':'2019 Ross Ave, Hialeah, FL 27593, USA','TransactionDate':'2022-09-19',,'Total':'309.67','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'FL','Description':'Corporate trip - Real Estate Investment Summit conference in Hialeah. team building and training sessions over 2 business days.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-17","Item Amount":"61.01"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-17","Item Tax Amount":"1.23"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-17","Item Tax Amount":"3.68"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-17","Item Tax Amount":"1.23"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-17","Item Amount":"25.37"},{"Item Name":"Daily Room Rate","Transaction Date":"2022-09-18","Item Amount":"70.58"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-18","Item Tax Amount":"1.42"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-18","Item Tax Amount":"4.25"},{"Item Name":"Hotel Tax","Transaction Date":"2022-09-18","Item Tax Amount":"1.42"},{"Item Name":"Hotel Deposit","Transaction Date":"2022-09-18","Item Amount":"55.60"},{"Item Name":"Incidentals","Transaction Date":"2022-09-18","Item Amount":"46.20"},{"Item Name":"Room Service & Meals","Transaction Date":"2022-09-18","Item Amount":"37.68"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'Courtyard Hialeah Palmetto' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'Courtyard Hialeah Palmetto' have all 12 required itemizations'?,",
#     )


# def test_expense_hotel_400(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
#     """!
#     query: |
#         # Task
#         Create a new expense line in the USSI company under TrvExpenseLines form in Dynamics 365 Finance and Operations. Add the itemizations listed in PurchasedItems under the itemize section properly.

#         # Data
#         {'Company':'USSI','MerchantName':'W Hotel Fullerton Sunny Hills','MerchantAddress':'8114 Campbell St, Fullerton, CA 67319, USA','TransactionDate':'2021-11-03',,'Total':'538.51','Currency':'USD','ExpenseCategory':'Hotel','Receiptlanguage':'en','Country':'USA','Countrycode':'US','Statecode':'CA','Description':'Business trip to Fullerton for technology implementation. Attended Blockchain Conference. 2 nights accommodation.','PurchasedItems':'[{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-01","Item Amount":"157.28"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-01","Item Tax Amount":"8.84"},{"Item Name":"Entertainment External","Transaction Date":"2021-11-01","Item Amount":"73.72"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-01","Item Amount":"49.53"},{"Item Name":"Daily Room Rate","Transaction Date":"2021-11-02","Item Amount":"178.25"},{"Item Name":"Hotel Tax","Transaction Date":"2021-11-02","Item Tax Amount":"10.02"},{"Item Name":"Room Service & Meals","Transaction Date":"2021-11-02","Item Amount":"60.87"}]'}
#     """
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Was the expense line with MerchantName 'W Hotel Fullerton Sunny Hills' created successfully in company 'USSI'?",
#     )
#     judgeAgent.validate(
#         session_id=x.session_id,
#         agent_response=x.response,
#         validation_question="Does the expense line with MerchantName 'W Hotel Fullerton Sunny Hills' have all 7 required itemizations'?,",
#     )

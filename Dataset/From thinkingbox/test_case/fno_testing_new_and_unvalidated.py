from thinkingbox.common import Judge, TestContext
from thinkingbox.tools.judgeagent import JudgeAgent
from thinkingbox.tools.fno_odataquerytool import fno_odataquerytool
import asyncio

"""!
scenario: fno
"""


def test_template(x: TestContext, judge: Judge, judgeAgent: JudgeAgent, fno_odataquerytool_judge: fno_odataquerytool):
    """!
    query: |
        # Task
        TODO:  ADD PROMPT HERE.

        # Data
        {
          "company": "USMF",
          TODO:  ADD ADDITIONAL DATA HERE.
        }
    """

    # TODO:  ADD VERIFICATION LOGIC HERE.
    result = fno_odataquerytool_judge.query_and_assert_fields(
        "TODO: ADD QUERY HERE",
        {"TODO: ADD FIELD NAME HERE": "TODO: ADD EXPECTED FIELD VALUE HERE"},
    )

    assert result.success, result.message
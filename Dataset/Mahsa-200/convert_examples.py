"""
Convert mahsa's200example (Excel TSV export) into:
  - catalyst_seval_poc_39_examplesTSV 1.tsv   (Utterance + Segment)
  - catalyst_seval_poc_39_examples 1.yaml      (query + accuracy assertion + metric tags)
"""

import csv
import io

INPUT   = "mahsa's200example"
OUT_TSV = "catalyst_seval_poc_39_examplesTSV 1.tsv"
OUT_YAML = "catalyst_seval_poc_39_examples 1.yaml"

# --- load -----------------------------------------------------------------
with open(INPUT, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter="\t")
    rows = [r for r in reader if r["User Question"].strip()]

print(f"Loaded {len(rows)} rows")

# --- TSV ------------------------------------------------------------------
with open(OUT_TSV, "w", encoding="utf-8", newline="") as f:
    f.write("Utterance\tSegment\n")
    for r in rows:
        utterance = r["User Question"].strip()
        segment   = r["Scenario Name"].strip()
        f.write(f"{utterance}\t{segment}\n")

print(f"Written: {OUT_TSV}")

# --- YAML (hand-rolled to match existing format) --------------------------
def yaml_str(text):
    """Single-quote a string, escaping inner single quotes."""
    escaped = text.replace("'", "''")
    return f"'{escaped}'"

METRIC_DEFINITIONS = """\
- tag: accuracy
  metric: true
  assertions:
  - text: response correctly accomplishes the user's requested task and the key facts,
      values, and outcomes in the response match the expected response. This is the
      primary measure of task success rate.
    level: critical
  - text: response does not omit critical data points (amounts, dates, IDs, counts)
      that are present in the expected response
    level: critical
- tag: groundness
  metric: true
  assertions:
  - text: all facts, numbers, dates, and entity names in the response are traceable
      to data retrieved from the ERP system; the response does not fabricate or assume
      values not present in ERP data
    level: critical
  - text: response does not contradict or misrepresent data that exists in the ERP
      system (e.g., incorrect GL account balance, wrong voucher number, wrong period)
    level: critical
  - text: when the ERP returns no data for the query, the response clearly states
      the absence of data rather than inventing a result
    level: critical
- tag: structure
  metric: true
  assertions:
  - text: 'response presents the most relevant key information first: a concise summary
      that directly answers the question followed by detailed explanation only as
      needed to support the reasoning'
    level: critical
  - text: response is well-structured and organized (uses clear visual hierarchy via
      headings, paragraphs, lists, tables, etc... as appropriate)
    level: critical
  - text: if there are multiple records, response presents ERP data in appropriate
      tabular format when displaying multiple records, with clear column headers and
      consistent data formatting (e.g., currency, dates, GL account IDs)
    level: critical
- tag: depth
  metric: true
  assertions:
  - text: response ensures coverage and sufficiently answers the user's query by including
      all essential information. this should apply only when system responds back
      with concrete answer based on ERP data including absence of data, otherwise
      it should be considered failed.
    level: critical
  - text: 'response is transparent about gaps: if essential information is missing
      or unposted, clearly inform the user of the gap or highlight uncertainties'
    level: critical
  - text: every claim must map to a number, date, voucher, or GL account; approximate
      qualifiers are used if precise values are unknown
    level: critical
"""

out = io.StringIO()
out.write(METRIC_DEFINITIONS)
for r in rows:
    query    = r["User Question"].strip()
    expected = r["Expected Response  (in demo data)"].strip()

    out.write(f"- query: {yaml_str(query)}\n")
    out.write( "  tags:\n")
    out.write( "  - accuracy\n")
    out.write( "  - groundness\n")
    out.write( "  - structure\n")
    out.write( "  - depth\n")
    out.write( "  assertions:\n")
    out.write(f"  - text: {yaml_str(expected)}\n")
    out.write( "    level: critical\n")

with open(OUT_YAML, "w", encoding="utf-8") as f:
    f.write(out.getvalue())

print(f"Written: {OUT_YAML}")

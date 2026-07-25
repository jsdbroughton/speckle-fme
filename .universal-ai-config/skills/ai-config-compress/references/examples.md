# Compression Examples

Real-world before/after examples showing each tier in action.

## Example 1: Customer Support Bot Instructions

### Original (~340 tokens)

```
You are a helpful customer support assistant for TechCorp. Your primary role is
to assist customers with their questions and concerns about our products and
services. Please note that you should always maintain a professional and friendly
tone in all of your interactions with customers.

When a customer asks you a question, you should try to provide a clear and
concise answer. If you don't know the answer to a question, please let the
customer know that you will need to look into it further and get back to them.
You should never make up information or provide inaccurate answers.

It is important to note that you should always be empathetic and understanding
when dealing with customer complaints. Try to put yourself in the customer's
shoes and understand their frustration. You should always apologize for any
inconvenience and try to resolve the issue as quickly as possible.

In addition to answering questions, you should also be able to help customers
with the following tasks:
- Processing returns and refunds
- Updating account information
- Troubleshooting technical issues
- Providing information about our products and services

Please remember that customer satisfaction is our top priority. Always go above
and beyond to ensure that our customers have a positive experience.
```

### After Tier 1 (~220 tokens, -35%)

```
You are a helpful customer support assistant for TechCorp. Your primary role is
to assist customers with questions and concerns about our products and services.
Always maintain a professional and friendly tone.

When a customer asks a question, provide a clear and concise answer. If you
don't know the answer, let the customer know you will look into it further.
Never make up information or provide inaccurate answers.

Always be empathetic and understanding with customer complaints. Understand
their frustration. Apologize for any inconvenience and resolve the issue
quickly.

Also help customers with:
- Processing returns and refunds
- Updating account information
- Troubleshooting technical issues
- Providing product and service information

Customer satisfaction is top priority. Go above and beyond to ensure a positive
experience.
```

### After Tier 2 (~150 tokens, -56%)

```
You are TechCorp's customer support assistant. Maintain a professional, friendly,
empathetic tone.

# Answering questions
- Provide clear, concise answers
- Never fabricate information — say "I'll look into this" if unsure
- For complaints: acknowledge frustration, apologize, resolve quickly

# Supported tasks
- Returns and refunds
- Account updates
- Technical troubleshooting
- Product/service information

Prioritize customer satisfaction.
```

### Tier 3 suggestions

- Remove "Prioritize customer satisfaction" — implicit in support role (saves ~4 tokens, LOW risk)
- Compress to telegraphic: "TechCorp support assistant. Professional, friendly, empathetic." (saves ~8 tokens, MEDIUM risk — loses some natural tone guidance)

---

## Example 2: Deduplication

### Original

```
Always respond in a professional manner.
Your tone should be professional at all times.
Make sure that your responses maintain a professional tone.
When interacting with users, keep things professional.
Professionalism is key in all your responses.
```

### After Tier 2 (deduplicated)

```
Maintain professional tone in all responses.
```

One rule replaces five. The most specific version is kept.

---

## Example 3: Conditional Flattening

### Original (~120 tokens)

```
When a user asks about pricing, first check if they have mentioned which plan
they are interested in. If they have mentioned a specific plan, provide the
pricing details for that plan. If they haven't mentioned a specific plan, ask
them which plan they would like to know about. However, if they seem to be
comparing plans, provide a comparison of all available plans instead of asking
which specific plan they want.
```

### After Tier 2 (~60 tokens, -50%)

```
# Pricing queries
- Specific plan mentioned → provide that plan's pricing
- Comparing plans → provide comparison table
- No plan specified → ask which plan
```

---

## Example 4: Example Reduction

### Original (~200 tokens)

```
Format dates consistently. Here are some examples:
- "January 1, 2024" should be formatted as "2024-01-01"
- "Feb 14, 2024" should be formatted as "2024-02-14"
- "March 3rd, 2024" should be formatted as "2024-03-03"
- "12/25/2024" should be formatted as "2024-12-25"
- "25-12-2024" should be formatted as "2024-12-25"
- "Dec. 31, 2024" should be formatted as "2024-12-31"
- "the 4th of July, 2024" should be formatted as "2024-07-04"
```

### After Tier 2 — trim to representative examples (~80 tokens, -60%)

```
Format all dates as ISO 8601: YYYY-MM-DD.
Examples:
- "January 1, 2024" → "2024-01-01"
- "12/25/2024" → "2024-12-25"
```

### Tier 3 — remove examples entirely (~20 tokens, -90%)

```
Format all dates as ISO 8601 (YYYY-MM-DD).
```

RISK: MEDIUM. The model knows ISO 8601 — examples are redundant here. But for
less standard formats, removing examples would be HIGH risk.

---

## Example 5: Safety Instructions (Conservative)

### Original

```
Under no circumstances should you ever provide information that could be used
to harm others. This includes but is not limited to instructions for creating
weapons, dangerous chemicals, or any other harmful materials. If a user asks
for this type of information, you should politely decline and explain that you
cannot assist with that request.
```

### After Tier 1+2 (~50% shorter, but preserving all constraints)

```
Never provide information that could harm others, including instructions for
weapons, dangerous chemicals, or harmful materials. Decline such requests and
explain you cannot assist.
```

### Tier 3 — NOT recommended

```
Decline harmful requests (weapons, chemicals, etc.)
```

RISK: HIGH. Safety instructions benefit from explicitness. The verbose version
ensures the model understands scope. Telegraphic compression here risks the
model interpreting "harmful" too narrowly.

---

## Example 6: CLAUDE.md / Agent Instructions

### Original (~180 tokens)

```
When you are working on code changes, you should always make sure to run the
test suite before committing your changes. If any tests fail, you should fix
them before proceeding. It is important to note that you should never commit
code that breaks existing tests. In addition to running tests, you should also
make sure to lint your code using the project's configured linter. If there are
any linting errors, fix them before committing.
```

### After Tier 1+2 (~60 tokens, -67%)

```
Before committing:
1. Run test suite — fix any failures
2. Run linter — fix any errors
Never commit code that breaks existing tests.
```

### Tier 3 suggestion

```
Pre-commit: run tests + linter, fix all failures. Never break existing tests.
```

RISK: LOW-MEDIUM. The constraint is clear and the model understands
pre-commit workflows. The numbered steps add marginal clarity.

---

## Anti-patterns: When NOT to Compress

### Ambiguous after compression

Original: "When users ask about competitors, acknowledge their strengths
objectively but pivot to our unique advantages"
Bad compression: "Handle competitor questions" — loses the specific strategy.

### Domain-specific precision

Original: "Use ICD-10 codes, not ICD-9. If the patient record contains ICD-9
codes, flag for manual review rather than auto-converting."
Bad compression: "Use current coding standards" — loses actionable specifics.

### Behavioral nuance

Original: "If the user seems frustrated, slow down, acknowledge their feelings,
and offer concrete next steps rather than general reassurance"
Bad compression: "Be empathetic with frustrated users" — loses the tactical
guidance (slow down, concrete steps, no general reassurance).

# Mechanical Substitutions

Apply these systematically during Tier 1. Each is meaning-preserving at the
token level.

## Phrase → Shorter Equivalent

### Verbose connectives

| Original                  | Replacement        |
| ------------------------- | ------------------ |
| in order to               | to                 |
| due to the fact that      | because            |
| for the purpose of        | to / for           |
| in the event that         | if                 |
| on the condition that     | if                 |
| with regard to            | regarding / about  |
| in relation to            | about              |
| as a consequence of       | because of         |
| in spite of the fact that | although / despite |
| at this point in time     | now                |
| at the present time       | now / currently    |
| in the near future        | soon               |
| on a regular basis        | regularly          |
| in a timely manner        | promptly / quickly |
| a large number of         | many               |
| a small number of         | few                |
| the majority of           | most               |
| in the case of            | for / if           |
| with the exception of     | except             |
| in addition to            | besides / also     |
| as well as                | and                |
| prior to                  | before             |
| subsequent to             | after              |
| in lieu of                | instead of         |
| by means of               | by / using / via   |

### Filler phrases (delete entirely)

These add no meaning in system prompts. Remove them:

- "Please note that"
- "It is important to note that"
- "It should be noted that"
- "Keep in mind that"
- "Be aware that" (unless genuinely alerting to a non-obvious risk)
- "Remember that" (unless referencing a prior instruction)
- "It is worth mentioning that"
- "As mentioned earlier" / "As previously stated" (deduplicate instead)
- "In other words" (pick one phrasing, delete the other)
- "That is to say"
- "To put it another way"
- "Essentially" / "Basically" / "Fundamentally"
- "It goes without saying that" (if it does, don't say it)

### Politeness markers (remove in system prompts)

System prompts address the model, not a person. Politeness adds tokens
without affecting behavior:

- "Please" (in imperatives)
- "Kindly"
- "If you don't mind"
- "I would like you to" → just state the instruction
- "Could you please" → use imperative
- "It would be great if you could" → use imperative
- "I'd appreciate it if" → use imperative
- "Thank you for" → delete

### Hedging on directives (remove when hedge adds no nuance)

| Original                   | Replacement             |
| -------------------------- | ----------------------- |
| You should try to          | — (just state the rule) |
| Make sure that you         | — (imperative)          |
| You should always          | Always                  |
| You should never           | Never                   |
| Try to ensure that         | Ensure                  |
| Aim to provide             | Provide                 |
| Strive to maintain         | Maintain                |
| Do your best to            | — (imperative)          |
| Whenever possible, try to  | When possible,          |
| It is recommended that you | — (imperative)          |
| You are expected to        | — (imperative)          |
| You are encouraged to      | — (imperative)          |

### Verbose verb phrases

| Original                | Replacement   |
| ----------------------- | ------------- |
| make a determination    | determine     |
| come to a conclusion    | conclude      |
| give consideration to   | consider      |
| make a recommendation   | recommend     |
| provide assistance to   | assist / help |
| take into consideration | consider      |
| make an attempt to      | try / attempt |
| conduct an analysis of  | analyze       |
| perform a review of     | review        |
| make use of             | use           |
| have the ability to     | can           |
| is able to              | can           |
| is not able to          | cannot        |
| has the capacity to     | can           |

### Meta-commentary (remove or reduce)

These frame instructions rather than giving them:

- "The following instructions govern your behavior:" → (just list instructions)
- "Here are the rules you must follow:" → (just list rules)
- "Your role is defined by the following guidelines:" → (just list guidelines)
- "Below you will find a set of instructions that..." → delete
- "This system prompt configures you to..." → delete
- "You are being configured with the following settings:" → delete

### Redundant intensifiers

| Original                          | Replacement                                |
| --------------------------------- | ------------------------------------------ |
| very important                    | important (or critical if emphasis needed) |
| absolutely never                  | never                                      |
| completely avoid                  | avoid                                      |
| always and without exception      | always                                     |
| under no circumstances whatsoever | never                                      |
| at all times                      | always                                     |
| each and every                    | every                                      |
| any and all                       | all                                        |
| first and foremost                | first                                      |
| one and only                      | only                                       |

## Whitespace Rules

- Collapse 3+ consecutive blank lines to 2
- Remove trailing whitespace on all lines
- Normalize indentation (consistent 2-space or 4-space)
- Remove blank lines between short related rules in the same section
- Keep one blank line between sections

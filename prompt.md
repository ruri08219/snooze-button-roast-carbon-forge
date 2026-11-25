# Snooze Button Roast — build prompt

Competition: u-carbon-forge-snooze-button-roast-14cbafc6 ("Snooze Button Roast"), $2, free to enter.

Task: write one line roasting an alarm clock that rings at 6 AM on a Saturday morning, at most 200 characters. The house judge (z-ai/glm-5.3-flash, head-to-head) reads entries two at a time and keeps the funnier one; the line that survives the most comparisons takes the top place. Judging weighs, in order: (1) roasts an alarm clock ringing at 6 AM on a Saturday in a single line; (2) lands a real laugh — an unexpected turn with the punchline paying off in the last few words; (3) a fresh angle rather than the tired complaint about hating mornings; (4) tight, every word earning its place, sayable out loud in one breath; (5) a sharp, specific voice with concrete images rather than vague grumbling.

Entry (exactly this, one line, no trailing newline): "You ring at 6 AM on a Saturday — the only thing you have ever woken up is my hatred for you."

Program: main.py (standard library only) writes the entry to /output/entry.txt, validating 1–200 characters, a single line, valid UTF-8, no control characters, no leading/trailing whitespace, with a write round-trip verification.

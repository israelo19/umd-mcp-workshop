# ============================================================
#  CBC x Notion — MCP Workshop
#  UMD CS Student Survival MCP Server
#  March 27, 2026
# ============================================================
#
#  HOW THIS WORKS (the whole thing):
#
#  Step 1 — Create the server
#  Step 2 — Decorate functions with @mcp.tool()
#  Step 3 — Run it
#
#  That's it. Everything else is just Python.
# ============================================================

from mcp.server.fastmcp import FastMCP
import random

# ── STEP 1: Create the server ────────────────────────────────
mcp = FastMCP("UMD CS Student Survival Guide")


# ── STEP 2: Add tools ────────────────────────────────────────

@mcp.tool()
def debug_my_life(error_message: str) -> str:
    """
    Given any error message a CS student is facing (in code OR in life),
    return a Stack Overflow-style diagnosis and a completely unhelpful solution.
    """
    responses = [
        f"StackOverflow (2009): '{error_message}' — marked as duplicate. "
        f"Please see the accepted answer which uses a library that no longer exists.",

        f"This is a known issue with '{error_message}'. "
        f"The fix is to add `sudo` before everything until something works.",

        f"'{error_message}' — have you tried turning it off and on again? "
        f"If that doesn't work, have you considered a different major?",

        f"Closed as off-topic: '{error_message}' does not appear to be a programming question. "
        f"Please rephrase as a programming question. "
        f"(Hint: everything is a programming question if you're brave enough.)",

        f"Top answer (4.2k upvotes): Just use JavaScript. "
        f"Second answer: Never use JavaScript. "
        f"Your issue: '{error_message}'",

        f"The real answer to '{error_message}' is buried in a GitHub issue from 2017 "
        f"where the maintainer said 'won't fix' and closed it.",

        f"'{error_message}' — According to the docs (which haven't been updated since 2019), "
        f"this should not be possible. Congrats, you found an undocumented feature.",
    ]
    return random.choice(responses)


@mcp.tool()
def estimate_project_survival(
    days_until_deadline: int,
    percent_complete: int,
    hours_slept_last_night: float
) -> str:
    """
    Given a student's deadline, how much they've done, and how much they slept,
    calculate their survival probability and give a completely honest assessment.
    """
    # Survival score (lower = more cooked)
    score = (days_until_deadline * 10) + (percent_complete) - ((8 - hours_slept_last_night) * 5)

    if score >= 80:
        verdict = "THRIVING"
        advice = "You're actually fine. This is suspicious. Have you checked the assignment requirements recently?"
    elif score >= 50:
        verdict = "CONCERNING BUT MANAGEABLE"
        advice = (
            f"You have {days_until_deadline} days and {percent_complete}% done. "
            f"The math is giving, but only if you stop watching YouTube."
        )
    elif score >= 20:
        verdict = "CODE RED"
        advice = (
            f"{percent_complete}% done with {days_until_deadline} days left "
            f"on {hours_slept_last_night} hours of sleep. "
            f"You need caffeine, a GitHub Copilot subscription, and a priest."
        )
    else:
        verdict = "COOKED"
        advice = (
            f"With {days_until_deadline} days, {percent_complete}% done, "
            f"and {hours_slept_last_night}hrs of sleep — "
            f"the project isn't the problem anymore, you are. "
            f"Please eat something and submit what you have."
        )

    return (
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"SURVIVAL STATUS: {verdict}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{advice}\n\n"
        f"Recommended next action: {'Keep going!' if score >= 50 else 'Open your laptop. Not Reddit. Your laptop.'}"
    )


# ── STEP 3: Run the server ───────────────────────────────────
if __name__ == "__main__":
    mcp.run()

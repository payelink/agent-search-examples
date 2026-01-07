from typing import List, Dict

from langchain.tools import tool


@tool
def plan_budget(
    monthly_income: float,
    fixed_expenses: float,
    variable_expenses: float,
    savings_goal_percentage: float = 20.0,
) -> Dict[str, float]:
    """
    Plan a simple monthly budget based on income and expenses.

    Args:
        monthly_income: Total income for the month.
        fixed_expenses: Sum of fixed monthly expenses (rent, utilities, etc.).
        variable_expenses: Sum of variable monthly expenses (food, transport, etc.).
        savings_goal_percentage: Target percentage of income to save (default: 20).

    Returns:
        A dictionary with recommended allocations for savings, fixed, and variable expenses.
    """
    if monthly_income <= 0:
        return {"error": "monthly_income must be greater than 0"}

    recommended_savings = monthly_income * (savings_goal_percentage / 100.0)
    remaining_after_savings = monthly_income - recommended_savings

    if remaining_after_savings <= 0:
        return {
            "error": "Savings goal too high for the given income. Reduce savings_goal_percentage."
        }

    # Calculate proportions for fixed vs variable within the remaining budget
    total_expenses_input = fixed_expenses + variable_expenses
    if total_expenses_input <= 0:
        fixed_ratio = 0.6
        variable_ratio = 0.4
    else:
        fixed_ratio = fixed_expenses / total_expenses_input
        variable_ratio = variable_expenses / total_expenses_input

    allocated_fixed = remaining_after_savings * fixed_ratio
    allocated_variable = remaining_after_savings * variable_ratio

    return {
        "monthly_income": monthly_income,
        "recommended_savings": round(recommended_savings, 2),
        "budget_for_fixed_expenses": round(allocated_fixed, 2),
        "budget_for_variable_expenses": round(allocated_variable, 2),
        "savings_goal_percentage": savings_goal_percentage,
    }


@tool
def summarize_expenses(expenses: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Summarize and categorize a list of expenses.

    Args:
        expenses: A list of expense items, each as {"category": str, "amount": float}.

    Returns:
        A dictionary with total spending and totals per category.
    """
    totals: Dict[str, float] = {}
    grand_total = 0.0

    for item in expenses:
        category = str(item.get("category", "uncategorized"))
        amount = float(item.get("amount", 0.0))
        grand_total += amount
        totals[category] = totals.get(category, 0.0) + amount

    # Round for readability
    rounded_totals = {k: round(v, 2) for k, v in totals.items()}

    return {
        "total_spent": round(grand_total, 2),
        "by_category": rounded_totals,
    }



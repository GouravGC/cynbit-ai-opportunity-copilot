
from app.workflows.blueprint import create_blueprint


inquiry = """
A business receives hundreds of customer enquiries each week.
It wants to classify each enquiry, extract important details,
and route it to the appropriate team. It also wants staff to
review uncertain cases before any action is taken.
"""

result = create_blueprint(inquiry)

print("\nCYNBIT OPPORTUNITY BLUEPRINT\n")
print(result)

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
class ActionMath(Action):
     def name(self) -> Text:
        return "action_math"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         num1 = tracker.get_slot("num1")
         num2 = tracker.get_slot("num2")
         operation = tracker.get_slot("operation")

        # Perform math operation
         if operation == "add":
            result = float(num1) + float(num2)
         elif operation == "sub":
            result = float(num1) - float(num2)
         elif operation == "mul":
            result = float(num1) * float(num2)
         elif operation == "div":
            result = float(num1) / float(num2)
         else:
            result = None

        # Send result message
         if result is not None:
            message = f"The result of {num1} {operation} {num2} is {result}."
         else:
            message = "I'm sorry, I didn't understand that math operation."

         dispatcher.utter_message(text="The result is provided")
         return []

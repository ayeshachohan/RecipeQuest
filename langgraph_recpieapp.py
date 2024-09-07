"""# **Testing Api**"""

import requests

def get_meal_details(meal_name):
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        meals = data.get('meals')
        if meals:
            meal = meals[0]
            meal_details = {
                'name': meal.get('strMeal'),
                'category': meal.get('strCategory'),
                'cuisine': meal.get('strArea'),
                'instructions': meal.get('strInstructions'),
                'ingredients': [],
                'image': meal.get('strMealThumb')
            }

            # Collect ingredients and measurements
            for i in range(1, 21):
                ingredient = meal.get(f'strIngredient{i}')
                measurement = meal.get(f'strMeasure{i}')
                if ingredient and ingredient.strip():
                    meal_details['ingredients'].append(f"{measurement} {ingredient}".strip())

            return meal_details
        else:
            return {"error": "Meal not found"}
    else:
        return {"error": "Failed to fetch data"}

# Example usage
meal_name = input("Enter the meal name: ")
details = get_meal_details(meal_name)
if 'error' in details:
    print(details['error'])
else:
    print(f"Name: {details['name']}")
    print(f"Category: {details['category']}")
    print(f"Cuisine: {details['cuisine']}")
    print("Ingredients:")
    for ingredient in details['ingredients']:
        print(f" - {ingredient}")
    print(f"Instructions: {details['instructions']}")
    print(f"Image URL: {details['image']}")

"""# **Loading Model**"""

from langchain_groq import ChatGroq

# Initialize the Groq LLM
llm = ChatGroq(model="llama3-70b-8192")

"""# **Custom Tool**"""

import langchain
langchain.verbose = False
langchain.debug = False
langchain.llm_cache = False

# Test the tool function directly
test_meal_name = 'Biryani'
test_result = get_meal_details(test_meal_name)
print("Direct Tool Result:", test_result)

from langchain_groq import ChatGroq
from langchain_core.tools import tool
import requests
from typing import Dict, Any, Optional

# Define the tool
@tool
def get_meal_details(meal_name: str) -> Dict[str, Any]:
    """Fetch details of a meal by its name from the MealDB API."""
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        meals = data.get('meals')
        if meals:
            meal = meals[0]
            meal_details = {
                'name': meal.get('strMeal'),
                'category': meal.get('strCategory'),
                'cuisine': meal.get('strArea'),
                'instructions': meal.get('strInstructions'),
                'ingredients': [],
                'image': meal.get('strMealThumb')
            }

            # Collect ingredients and measurements
            for i in range(1, 21):
                ingredient = meal.get(f'strIngredient{i}')
                measurement = meal.get(f'strMeasure{i}')
                if ingredient and ingredient.strip():
                    meal_details['ingredients'].append(f"{measurement} {ingredient}".strip())

            return meal_details
        else:
            return {"error": "Meal not found"}
    else:
        return {"error": "Failed to fetch data"}

# Initialize the LLM
llm = ChatGroq(model="llama3-70b-8192")

# Bind the tool to the LLM
tool_model = llm.bind_tools([get_meal_details], tool_choice="auto")

def invoke_tool_model(query: str):
    """
    Invoke the tool model with a specific query.

    Args:
        query (str): The query to be processed by the tool model.

    Returns:
        dict: The result from the tool model.
    """
    try:
        # Invoke the tool model with the query
        result = tool_model.invoke(query)

        # Print the raw result for debugging
        print("Raw Result:", result)

        # Check if the result contains tool calls
        if hasattr(result, 'tool_calls'):
            print("Tool Calls:", result.tool_calls)
            # Process tool calls
            tool_call = result.tool_calls[0]
            # Execute the tool function manually for testing
            if tool_call['name'] == 'get_meal_details':
                args = tool_call['args']
                meal_name = args.get('meal_name')
                # Manually call the tool function
                tool_result = get_meal_details(meal_name)
                print("Manual Tool Call Result:", tool_result)
                return tool_result
            else:
                return {"error": "Unknown tool name"}
        else:
            return {"error": "No tool calls found in the result"}

    except Exception as e:
        return {"error": str(e)}

# Example usage
query = "Can you give me the details of the meal 'biryani'?"
result = invoke_tool_model(query)

# Print the processed result
print("Processed Result:", result)

"""# **Importing Libraries**"""

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain_community.tools import YouTubeSearchTool
from pprint import pprint
import requests
import sqlalchemy as sa
from typing import Dict, Any, List, Optional

llm = ChatGroq(model="llama3-70b-8192")

"""# **tool testing**"""

# Define the tool
@tool
def get_meal_details(meal_name: str) -> Dict[str, Any]:
    """Fetch details of a meal by its name from the MealDB API."""
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        meals = data.get('meals')
        if meals:
            meal = meals[0]
            meal_details = {
                'name': meal.get('strMeal'),
                'category': meal.get('strCategory'),
                'cuisine': meal.get('strArea'),
                'instructions': meal.get('strInstructions'),
                'ingredients': [],
                'image': meal.get('strMealThumb')
            }

            # Collect ingredients and measurements
            for i in range(1, 21):
                ingredient = meal.get(f'strIngredient{i}')
                measurement = meal.get(f'strMeasure{i}')
                if ingredient and ingredient.strip():
                    meal_details['ingredients'].append(f"{measurement} {ingredient}".strip())

            return meal_details
        else:
            return {"error": "Meal not found"}
    else:
        return {"error": "Failed to fetch data"}

# Bind the tool to the LLM
tool_model = llm.bind_tools([get_meal_details], tool_choice="auto")

def invoke_tool_model(query: str) -> Dict[str, Any]:
    """
    Invoke the tool model with a specific query.

    Args:
        query (str): The query to be processed by the tool model.

    Returns:
        dict: The result from the tool model.
    """
    try:
        # Invoke the tool model with the query
        result = tool_model.invoke(query)

        # Print the raw result for debugging
        print("Raw Result:", result)

        # Check if the result contains tool calls
        if hasattr(result, 'tool_calls'):
            print("Tool Calls:", result.tool_calls)
            # Process tool calls
            tool_call = result.tool_calls[0]
            # Execute the tool function manually for testing
            if tool_call['name'] == 'get_meal_details':
                args = tool_call['args']
                meal_name = args.get('meal_name')
                # Manually call the tool function
                tool_result = get_meal_details(meal_name)
                print("Manual Tool Call Result:", tool_result)
                return tool_result
            else:
                return {"error": "Unknown tool name"}
        else:
            return {"error": "No tool calls found in the result"}

    except Exception as e:
        return {"error": str(e)}

# Example usage
query = "Can you give me the details of the meal 'biryani'?"
result = invoke_tool_model(query)

# Print the processed result
print("Processed Result:", result)

"""# **State**"""

from typing_extensions import TypedDict
from typing import List

class RecipeProjectState(TypedDict):
    """
    Represents the state of the recipe recommendation and shopping assistant workflow.

    Attributes:
        user_query: The recipe query entered by the user.
        recipe_details: The details of the recipe obtained from `get_meal_details_tool`.
        ingredients: The list of ingredients required for the recipe.
        available_ingredients: The list of ingredients available in the pantry.
        missing_ingredients: The list of ingredients that are missing.
        shopping_list: The list of items that need to be purchased.
        user_purchased: Whether the user has confirmed purchasing the missing ingredients.
        youtube_tutorials: The list of YouTube video tutorials related to the recipe.
        num_steps: The number of steps completed in the workflow.
    """
    user_query: str
    recipe_details: Dict[str, str]
    ingredients: List[str]
    available_ingredients: List[str]
    missing_ingredients: List[str]
    shopping_list: List[str]
    user_purchased: bool
    youtube_tutorials: List[str]
    num_steps: int

"""# **Node#1**"""

def start_node(state: RecipeProjectState) -> RecipeProjectState:
    """Initialize the workflow by capturing user input."""
    print("---STARTING WORKFLOW---")

    # Prompt user for input
    user_query = input("Which recipe would you like to find? ")

    # Update state with the user's query
    state.update({
        'user_query': user_query,
        'num_steps': state['num_steps'] + 1
    })

    return state

"""# **2nd Node**"""

from typing import List

def research_info_search(state: RecipeProjectState) -> RecipeProjectState:
    """Search for recipe information and extract ingredients."""
    print("---RESEARCH INFO SEARCHING---")

    user_query = state["user_query"]
    num_steps = state['num_steps']
    num_steps += 1

    # Simulate a call to the get_meal_details_tool API
    api_response = get_meal_details.invoke({"meal_name": user_query})

    # Extract information from the API response
    if 'ingredients' in api_response:
        ingredients = api_response['ingredients']
        print(f"Ingredients: {ingredients}")
    else:
        ingredients = []
        print("No ingredients found.")

    # Update state with recipe details and ingredients
    state.update({
        'recipe_details': api_response,
        'ingredients': ingredients,
        'num_steps': num_steps
    })

    return state

"""# **3rd node**"""

import sqlite3
from langchain_community.utilities import SQLDatabase

# Step 1: Create and populate the SQLite database
def setup_database():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pantry (
        ingredient TEXT PRIMARY KEY
    )
    ''')

    ingredients = [
        'Cashew nuts',
        'Cumin seeds',
        'Ghee',
        'Basmati rice',
        'Full fat yogurt',
        'Lamb',
        'Red Chilli powder',
        'Biryani masala'
    ]

    for ingredient in ingredients:
        cursor.execute('''
        INSERT OR IGNORE INTO Pantry (ingredient) VALUES (?)
        ''', (ingredient,))

    conn.commit()
    conn.close()

# Setup the database
setup_database()

# Step 2: Initialize the SQLDatabase object
db = SQLDatabase.from_uri("sqlite:///pantry.db")

# Example query to verify the setup
result = db.run("SELECT * FROM Pantry;", fetch="all")
print(result)

"""# **4rth Node**"""

def check_ingredients_in_pantry(state):
    # Extract pantry ingredients from state
    pantry_ingredients = state.get('pantry_ingredients', [])

    # Print the type and content of pantry_ingredients for debugging
    print("Type of pantry_ingredients:", type(pantry_ingredients))
    print("Content of pantry_ingredients:", pantry_ingredients)

    # Check if the format is a list of tuples or a list of strings
    if isinstance(pantry_ingredients, list):
        if all(isinstance(item, tuple) and len(item) == 1 for item in pantry_ingredients):
            # Extract ingredient names from tuples
            pantry_ingredients = [item[0] for item in pantry_ingredients]
        elif all(isinstance(item, str) for item in pantry_ingredients):
            # If already a list of strings, no further processing needed
            pass
        else:
            # Handle unexpected format
            raise ValueError("The format of pantry_ingredients is not recognized.")
    else:
        # Handle unexpected format
        raise ValueError("The format of pantry_ingredients is not recognized.")

    # Determine which ingredients are missing
    missing_ingredients = [ingredient for ingredient in state['ingredients'] if ingredient not in pantry_ingredients]

    return {
        'missing_ingredients': missing_ingredients
    }

"""# **5rth Node**"""

def handle_user_input(state: RecipeProjectState) -> RecipeProjectState:
    """Prompt the user for additional input or alternative options and manage workflow based on the response."""
    print("---HANDLING USER INPUT---")

    # Extract relevant state variables
    missing_ingredients = state['missing_ingredients']
    pantry_ingredients = state['available_ingredients']
    user_purchased = state['user_purchased']
    num_steps = state['num_steps']

    # Prompt the user for confirmation
    print("Missing ingredients:", missing_ingredients)
    user_response = input("Have you purchased the missing ingredients? (yes/no): ").strip().lower()

    if user_response == 'yes':
        # Update the state to reflect that the ingredients have been purchased
        user_purchased = True
        num_steps += 1

        # Add missing ingredients to pantry
        pantry_ingredients.extend(missing_ingredients)

        print("Great! The missing ingredients have been added to your pantry.")
        print("Updated pantry ingredients:", pantry_ingredients)
    else:
        # Block further workflow until the user confirms ingredient purchase
        print("You need to purchase the ingredients before continuing.")

    state.update({
        'available_ingredients': pantry_ingredients,
        'user_purchased': user_purchased,
        'num_steps': num_steps
    })

    return state

"""# **6th Node**"""

from langchain_community.tools import YouTubeSearchTool
from typing import List, Dict

def fetch_youtube_video_tutorials(state: RecipeProjectState) -> RecipeProjectState:
    """Search for related cooking video tutorials on YouTube."""
    print("---FETCHING YOUTUBE VIDEO TUTORIALS---")

    # Extract relevant state variables
    recipe_details = state.get("recipe_details", {})
    recipe_name = recipe_details.get('name', 'Unknown Recipe')
    num_steps = state['num_steps']

    # Initialize YouTube search tool
    youtube_search_tool = YouTubeSearchTool()

    # Create a search query based on the recipe name
    search_query = f"Cooking tutorial for {recipe_name}"

    # Perform the YouTube search
    youtube_results = youtube_search_tool.run(search_query)
    print("YouTube search results:", youtube_results)

    # Update the state with the results and increment the step count
    state.update({
        'youtube_tutorials': youtube_results,
        'num_steps': num_steps + 1
    })

    return state

"""# **End Node**"""

def end_node(state: RecipeProjectState) -> RecipeProjectState:
    """Conclude the workflow by displaying the results to the user."""
    print("---ENDING WORKFLOW---")

    # Extract the relevant information from the state
    recipe_details = state.get("recipe_details", {})
    youtube_tutorials = state.get("youtube_tutorials", [])
    num_steps = state.get('num_steps', 0)

    # Display results
    print("Recipe Details:", recipe_details)
    print("YouTube Tutorials:", youtube_tutorials)

    # Prepare the final results
    final_results = {
        "recipes": recipe_details,
        "videos": youtube_tutorials
    }

    # Update the state with final results and increment the step count
    state.update({
        'final_results': final_results,
        'num_steps': num_steps + 1
    })

    return state

"""# **state Updation**"""

def state_printer(state: RecipeProjectState) -> None:
    """Print the state of the RecipeQuest workflow."""
    print("---STATE PRINTER---")
    print(f"User Query: {state.get('user_query', 'N/A')} \n")
    print(f"Recipe Details: {state.get('recipe_details', 'N/A')} \n")
    print(f"Ingredients: {state.get('ingredients', [])} \n")
    print(f"Available Ingredients: {state.get('available_ingredients', [])} \n")
    print(f"Missing Ingredients: {state.get('missing_ingredients', [])} \n")
    print(f"Shopping List: {state.get('shopping_list', [])} \n")
    print(f"User Purchased: {state.get('user_purchased', 'N/A')} \n")
    print(f"YouTube Tutorials: {state.get('youtube_tutorials', [])} \n")
    print(f"Num Steps: {state.get('num_steps', 0)} \n")
    print(f"Final Results: {state.get('final_results', {})} \n")

"""# **Conditional Edges**"""

from typing import TypedDict, List, Literal

def route_to_handle_user_input(state: RecipeProjectState) -> Literal["handle_user_input", "__end__"]:
    """Route based on whether ingredients are available or not."""
    if not state.get("available_ingredients"):
        return "__end__"
    return "handle_user_input"

def route_to_youtube_search(state: RecipeProjectState) -> Literal["fetch_youtube_video_tutorials", "__end__"]:
    """Route based on user's response about ingredient purchase."""
    if not state.get("user_purchased"):
        return "__end__"
    return "fetch_youtube_video_tutorials"

"""# **Adding Nodes**"""

from langgraph.graph import StateGraph, START, END

workflow = StateGraph(RecipeProjectState)

workflow.add_node("start_node", start_node)
workflow.add_node("research_info_search", research_info_search)
workflow.add_node("check_ingredients_in_pantry", check_ingredients_in_pantry)
workflow.add_node("handle_user_input", handle_user_input)
workflow.add_node("fetch_youtube_video_tutorials", fetch_youtube_video_tutorials)
workflow.add_node("end_node", end_node)

#workflow.set_entry_point("start_node")

"""# **Adding Edges**"""

# Add edges
workflow.add_edge(START, "start_node")
workflow.add_edge("start_node", "research_info_search")
workflow.add_edge("research_info_search", "check_ingredients_in_pantry")
workflow.add_edge("check_ingredients_in_pantry", "handle_user_input")

# Add conditional edge
workflow.add_conditional_edges(
    "handle_user_input",
    route_to_youtube_search,
    {"fetch_youtube_video_tutorials": "fetch_youtube_video_tutorials", "__end__": "end_node"}
)

workflow.add_edge("fetch_youtube_video_tutorials", "end_node")
workflow.add_edge("end_node", END)

# Compile the workflow
graph = workflow.compile()

print("Nodes:", workflow.nodes)

print(workflow.edges)

"""inshalla

# **Adding edges**

# **Edges**
"""

print("Nodes in the graph:", workflow.nodes)

# Compile the workflow
graph = workflow.compile()

"""# **Graph**"""

from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass

# Define the initial state for the graph
initial_state = {
    "recipe_details": {"recipe_name": "Sample Recipe"},  # Example data
    "ingredients": ["Cashew nuts", "Ghee", "Basmati rice"],  # Example data
    "available_ingredients": [],
    "missing_ingredients": [],
    "shopping_list": [],
    "user_purchased": False,
    "num_steps": 0
}

# Run the graph with the initial state and stream the outputs
for output in graph.stream(initial_state):
    for key, value in output.items():
        pprint(f"Finished running: {key}: {value}")
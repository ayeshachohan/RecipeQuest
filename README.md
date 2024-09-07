# **RecipeQuest 🍲 | Discover Recipes, Manage Ingredients, and Learn Cooking**

Welcome to **RecipeQuest**, your ultimate solution for discovering delicious recipes, managing your pantry, and finding related cooking tutorials! 🍽️ With an easy-to-use interface and powerful integrations, RecipeQuest simplifies your cooking journey.

---

## 🚀 **Purpose**
RecipeQuest is designed to:
- Help users **discover new recipes** based on their preferences.
- **Manage ingredients** and check what's in the pantry.
- Find **related cooking tutorials** to guide you through the process.

---

## 🔧 **Components**
- **SQL Database**: Stores recipe info and user data. Queries recipes and user-specific details.
- **YouTube Search Tool**: Fetches **cooking video tutorials** based on the recipe name using YouTube API.
- **Custom API**: Enhances recipe data and manages your pantry ingredients.
- **LangChain Integration**: Orchestrates workflow between components for a seamless user experience.

---

## 🛠️ **How It Works**
1. **Start**: The user enters a recipe query (e.g., "biryani").  
2. **Check Pantry**: The app checks the pantry for available ingredients using the custom API.
3. **Retrieve Recipe**: Finds the recipe details from the SQL database.
4. **Handle Input**: Allows user interactions (e.g., adjusting ingredients).
5. **Search YouTube**: Fetches relevant **cooking tutorials**.
6. **Display Results**: Presents a detailed recipe, available/missing ingredients, a shopping list, and tutorials.

---

## 🧑‍🍳 **Key Features**
- **Ingredient Checker** 🧺: Compares required recipe ingredients with what's in your pantry.
- **YouTube Tutorials** 🎥: Automatically fetches **video tutorials** to help you cook better.
- **Customizable Shopping List** 🛒: Easily see what you need to buy for your next dish.

---

## 📦 **Data Structures**
- **RecipeProjectState**: Manages the app’s workflow, tracking user queries, recipe details, available/missing ingredients, shopping lists, and tutorials.

---

## 📑 **Functions**
- **`fetch_youtube_video_tutorials`**: Searches for video tutorials related to the recipe.
- **`check_ingredients_in_pantry`**: Checks for available ingredients and updates the shopping list with missing items.

---

## 🛠️ **Challenges & Solutions**
- **Format Issues**: Debugging pantry data to ensure it matches the expected structure.
- **Package Dependencies**: Installing the `youtube_search` module or updating code to use a compatible YouTube search library.

---

## 💡 **Example Workflow**
1. **User Query**: The user asks for a recipe (e.g., "biryani").
2. **Fetch Recipe**: The system retrieves the recipe details.
3. **Check Pantry**: The system checks for available ingredients.
4. **Identify Missing Ingredients**: Updates the shopping list.
5. **Fetch Tutorials**: Finds related YouTube tutorials.
6. **Results**: Displays everything to the user: recipe, ingredients, and tutorials!

---

## 🖼️ **Screenshots of the App**
![App Screenshot 1](https://github.com/ayeshachohan/RecipeQuest/blob/main/screenshots/RecpieQuest%231.png?raw=true)
![App Screenshot 2](https://github.com/ayeshachohan/RecipeQuest/blob/main/screenshots/RecpieQuest%232.png?raw=true)
![App Screenshot 3](https://github.com/ayeshachohan/RecipeQuest/blob/main/screenshots/RecpieQuest%233.png?raw=true)
![App Screenshot 4](https://github.com/ayeshachohan/RecipeQuest/blob/main/screenshots/RecpieQuest%234.png?raw=true)
![App Screenshot 5](https://github.com/ayeshachohan/RecipeQuest/blob/main/screenshots/RecpieQuest%235.png?raw=true)

---

## 🛠️ **Tech Stack**
- **SQL** for recipe storage 📂
- **YouTube API** for video retrieval 🎥
- **LangChain** for workflow orchestration 🔗
- **Custom API** for ingredient management 🍏

---

## ✨ **Get Started**
Clone the repository and explore RecipeQuest! Follow the steps below to install the dependencies and run the project.

```bash
# Clone the repository
git clone https://github.com/your-username/recipequest.git

# Navigate into the project directory
cd recipequest



# Run the app
streamlit run langgraph_recpieapp.py



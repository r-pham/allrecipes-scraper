from bs4 import BeautifulSoup
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

RECIPE_CATEGORY_PAGES = {
    "QUICK AND EASY DINNERS FOR ONE": "",
    "COOKING FOR TWO": "",
    "SHEET PAN DINNERS": "",
    "SLOW COOKER MAIN DISHES": "",
    "VEGETARIAN MAIN DISHES": "",
    "HEALTHY MAIN DISHES": "",
    "MAIN DISHES": "",
    "MEATLOAF": "",
    "PASTA MAIN DISHES": "",
    "PORK CHOPS": "",
    "MAIN DISH SALADS": "",
    "BEEF STEAKS": "",
}


@dataclass_json
@dataclass
class Recipe:
    name: str
    details: str
    ingredients: str
    directions: str


class AllRecipes_Scraper:
    """
    Main class that allows us to scrape recipes and details from AllRecipes website
    """

    HOME_URL = "https://www.allrecipes.com/"

    def get_recipe(url: str) -> Recipe:
        """_summary_

        Args:
            url (str): _description_
        """
        # TODO: Create a dataclass to be returned
        # Scrape contents from URL and consolidate everything into a uniform class
        raise NotImplementedError

    def get_recipes(category: str) -> List[Recipe]:
        """_summary_

        Args:
            category (str): _description_
        """
        # Iterate through all urls from a category's main page
        # For each url, return recipe and details
        raise NotImplementedError

    def get_recipe_images(url: str):
        """
        Return all image links found on a recipe page

        Args:
            url (str): _description_
        """
        raise NotImplementedError

    def _get_all_recipe_urls(url: str):
        """
        Return all recipe urls found on a page

        Args:
            url (str): URL of a page to get other urls
        """
        # Ensure that all urls follow this format: https://www.allrecipes.com/recipe/23891/grilled-cheese-sandwich/
        raise NotImplementedError

    def _html_to_recipe(html: str) -> Recipe:
        """
        Cleans up HTML to be parsed as Recipe object

        Args:
            html (str): HTML to be returned by request
        """
        raise NotImplementedError

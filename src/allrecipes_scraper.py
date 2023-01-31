from bs4 import BeautifulSoup, element
import re
import requests
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

# TODO: Fill these with page url's
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
class RecipeDetail:
    label: str
    value: str


@dataclass_json
@dataclass
class RecipeIngredient:
    quantity: int
    unit: str
    name: str


@dataclass_json
@dataclass
class Recipe:
    name: str
    details: List[RecipeDetail]
    ingredients: List[RecipeIngredient]
    directions: List[str]


class AllRecipes_Scraper:
    """
    Main class that allows us to scrape recipes and details from AllRecipes website
    """

    def get_recipe(self, url: str) -> Recipe:
        """
        Return recipe details from a page

        Args:
            url (str): Recipe URL to parse for details
        """
        if not self._validate_recipe_url(url):
            return
        # Get page HTML
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # Parse recipe details, ingredients, and directions
        recipe_name = soup.find(id="article-heading_2-0")
        recipe_details = self._get_recipe_details(soup.find(id="recipe-details_1-0"))
        ingredients = self._get_recipe_ingredients(
            soup.find(id="mntl-structured-ingredients_1-0")
        )
        directions = self._get_recipe_directions(
            soup.find(id="recipe__steps-content_1-0")
        )
        return Recipe(
            name=recipe_name.text.strip(),
            details=recipe_details,
            ingredients=ingredients,
            directions=directions,
        )

    def get_recipes(category: str) -> List[Recipe]:
        """
        Returns a list of recipes from specified category

        Args:
            category (str): Food category to get recipes from
        """
        # Iterate through all urls from a category's main page
        # For each url, return recipe and details
        raise NotImplementedError

    def get_recipe_images(url: str):
        """
        Return all image links found on a recipe page

        Args:
            url (str): Recipe page URL
        """
        raise NotImplementedError

    @staticmethod
    def _validate_recipe_url(url: str) -> bool:
        """
        Ensure that the specified url is a valid recipe page

        Args:
            url (str): _description_
        """
        # TODO: Look into optimizing this -- I feel like either pattern can be simplified or regex not needed
        return bool(
            re.match("^https:\/\/www\.allrecipes\.com\/recipe\/\d+\/.*\/$", url)
        )

    def _get_all_recipe_urls(self, url: str) -> List[str]:
        """
        Return all recipe urls found on a page

        Args:
            url (str): URL of a page to get other urls
        """
        links = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=True):
            if self._validate_recipe_url(link["href"]):
                links.append(link["href"])
        return links

    @staticmethod
    def _get_recipe_details(recipe_content_html: element.Tag) -> List[RecipeDetail]:
        """
        Get recipe details from a recipe page

        Args:
            recipe_content_html (element.Tag): Recipe page HTML for recipe details
        """
        details = []
        detail_elements = recipe_content_html.find_all(
            "div", class_="mntl-recipe-details__item"
        )
        for e in detail_elements:
            cleaned_element = e.text.strip().split("\n")
            details.append(
                RecipeDetail(
                    label=cleaned_element[0].replace(":", ""), value=cleaned_element[1]
                )
            )
        return details

    @staticmethod
    def _get_recipe_ingredients(ingredients_content_html: element.Tag) -> List[RecipeIngredient]:
        """
        Get recipe ingredients from a recipe page

        Args:
            ingredients_content_html (element.Tag): Recipe page HTML for ingredients
        """
        ingredients = []
        ingredient_elements = ingredients_content_html.find_all(
            "li", class_="mntl-structured-ingredients__list-item"
        )
        for e in ingredient_elements:
            ingredients.append(
                RecipeIngredient(
                    quantity=e.find("span", {"data-ingredient-quantity": "true"}).text.strip(),
                    unit=e.find("span", {"data-ingredient-unit": "true"}).text.strip(),
                    name=e.find("span", {"data-ingredient-name": "true"}).text.strip()
                )
            )
        return ingredients

    @staticmethod
    def _get_recipe_directions(directions_content_html: element.Tag) -> List[str]:
        """
        Get recipe directions from a recipe page

        Args:
            directions_content_html (element.Tag): Recipe page HTML for directions
        """
        # TODO: Get directions in ordered list
        directions = []
        direction_elements = directions_content_html.find_all(
            "p", class_="comp mntl-sc-block mntl-sc-block-html"
        )
        for e in direction_elements:
            cleaned_element = e.text.strip()
            directions.append(cleaned_element)
        return directions

    @staticmethod
    def _get_recipe_ratings(ratings_content_html: element.Tag):
        """
        Get recipe rating and rating count from recipe page

        Args:
            ratings_content_html (element.Tag): Recipe page HTML for ratings
        """
        # TODO: Create ratings object
        raise NotImplementedError

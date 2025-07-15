
# Coffee Machine Simulation

This project is a simple Python application that simulates the core functionalities of a coffee machine. It takes drink orders, checks resources, processes money, handles change, and dispenses coffee.

---

## How It Works

The program operates in a continuous loop, prompting the user for commands. The flow is as follows:

1.  **Order Prompt:** Asks the user "What would you like? (espresso/latte/cappuccino):"
2.  **`off` Command:** Shuts down the machine and ends program execution.
3.  **`report` Command:** Prints a current inventory of water, milk, coffee, and accumulated money.
4.  **Drink Selection:**
    * **Resource Check:** Verifies if enough ingredients are available for the selected drink. If not, it prints a specific "Sorry, there is not enough [ingredient]." message.
    * **Coin Processing:** If resources are sufficient, it prompts the user to insert coins (quarters, dimes, nickels, pennies) and calculates the total amount. Empty inputs for coin counts are treated as zero.
    * **Transaction Check:**
        * If insufficient money is inserted, it prints "Sorry that's not enough money. Money refunded."
        * If sufficient (or excess) money is inserted, it calculates and prints change (if any) and proceeds to make the coffee.
    * **Coffee Making:** Deducts the required ingredients from the machine's `resources` and adds the drink's `cost` to the machine's `money`. Finally, it prints "Here is your [drink_name]. Enjoy!"
5.  **Invalid Choice:** For any unrecognized input, it prints an "Sorry, that's not a valid choice..." message.

---

## Code Structure

* **`resources` (dictionary):** Holds the current quantities of `water`, `milk`, `coffee`, and `money` in the machine.
* **`recipe_book` (dictionary):** Stores the `ingredients` and `cost` for each available drink (`espresso`, `latte`, `cappuccino`).
* **`check_resources(drink_name)` (function):** Checks if there are enough ingredients for the specified `drink_name`.
* **`calculate_coins()` (function):** Prompts for coin input and returns the total monetary value.
* **`make_coffee(drink_name)` (function):** Deducts ingredients, adds profit, and prints the success message.
* **Main `while is_on:` loop:** Manages the overall program flow and user interaction.

---

## Future Enhancements

* **Error Handling:** Implement `try-except` blocks for robust handling of non-integer inputs for coins.
* **Refill Option:** Add a command for maintainers to refill machine resources.
* **More Drinks:** Expand the `recipe_book` with additional coffee options.

---
## Code Challenge from bwgi
To run the methods as modules:

```python -m <module_name>```

or import one by one. Example:

```from reconcile_accounts.module import reconcile_accounts```

### Project Structure
The project contains the following main files:
- reconcile_accounts/__init__.py: Contains the main function to reconcile accounts and runs the module.
- reconcile_accounts/main.py: Contains the reconcile_accounts function.
- computed_property/__init__.py: Contains the main function to demonstrate the usage of the computed_property decorator.
- computed_property/main.py: Contains the computed_property decorator.
- last_lines/__init__.py: Contains the main function to demonstrate the usage of the last_lines function.
- last_lines/main.py: Contains the last_lines function.
- data/: Directory containing CSV files used for reconciliation.


### Example Usage
Reconcile Accounts
To reconcile accounts, run the following command:

```python -m reconcile_accounts```

#### Computed Property
To demonstrate the usage of the computed_property decorator, run the following command:

```python -m computed_property```

This will demonstrate the usage of the Circle and Vector classes with the computed_property decorator.
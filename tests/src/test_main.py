from src import main as module

def test_main():
    """
    Test the main function from the module.
    This test checks if the main function runs without errors.
    """
    module.main()
    assert True  # If no exception is raised, the test passes.

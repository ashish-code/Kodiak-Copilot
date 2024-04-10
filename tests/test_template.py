from brightai.template import main


def test_get_name():
    ret_name = main.get_name()
    assert "brightai.template" in ret_name


def test_main():
    main.main()

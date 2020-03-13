def identify_unique_text(supplier_a: int = 997, supplier_b: int = 987):
    """
    :param supplier_a:
    :param supplier_b:
    :return:
    """
    unique_model_a = UniqueText(supplier_a)
    content_a = unique_model_a.get_content_as_words()
    common_content_a = unique_model_a.get_common_words()
​
    unique_model_b = UniqueText(supplier_b)
    content_b = unique_model_b.get_content_as_words()
    common_content_b = unique_model_b.get_common_words()
​
    removed_common = UniqueText.intersection(common_content_a, common_content_b, True)
    print(removed_common)
​
    lst3 = UniqueText.intersection(content_a, removed_common)
    print(lst3)
​
​
    # flat_list = map(str.strip, flat_list)
​
    return True

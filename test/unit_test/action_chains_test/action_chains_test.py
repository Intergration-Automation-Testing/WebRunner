from sys import stderr

from je_web_runner import webdriver_wrapper, TestObject, Keys


webdriver_wrapper.set_driver("firefox")
webdriver_wrapper.to_url("https://google.com")
google_input = TestObject("q", "name")
google_input_element = webdriver_wrapper.find_element(google_input)
webdriver_wrapper.implicitly_wait(3)
webdriver_wrapper.move_to_element(google_input_element)
webdriver_wrapper.move_to_element_with_offset(google_input_element, 10, 10)
webdriver_wrapper.move_by_offset(10, 10)
webdriver_wrapper.drag_and_drop(google_input_element, google_input_element)
webdriver_wrapper.drag_and_drop_offset(google_input_element, 10, 10)
webdriver_wrapper.perform()
webdriver_wrapper.left_click(google_input_element)
webdriver_wrapper.release(google_input_element)
webdriver_wrapper.left_click()
webdriver_wrapper.release()
webdriver_wrapper.left_double_click()
webdriver_wrapper.release()
webdriver_wrapper.left_click_and_hold()
webdriver_wrapper.release()
webdriver_wrapper.pause(3)
webdriver_wrapper.press_key(Keys.F1)
webdriver_wrapper.release_key(Keys.F1)
webdriver_wrapper.send_keys(Keys.F1)
webdriver_wrapper.send_keys_to_element(google_input_element, Keys.F1)
webdriver_wrapper.perform()
webdriver_wrapper.quit()


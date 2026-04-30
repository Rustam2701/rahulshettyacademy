import os
from playwright.sync_api import expect


# def test_checkboxes(page):
#     page.goto('https://rahulshettyacademy.com/AutomationPractice/')
#     page.locator("input[value='radio2']").check()
#     assert page.locator('input[value="radio2"]').is_checked()
#
#


class LOCATORS:
    DEFAULT_CHECKBOX = "text=Default checkbox"
    CHECKED_CHECKBOX = "text=Checked checkbox"
    CHECKED_SWITCH_CHECKBOX = "text=Checked switch checkbox input"
    DEFAULT_RADIO = "text=Default radio"
    DEFAULT_CHECKED_RADIO = "text=Default checked radio"


def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = [page.locator(LOCATORS.DEFAULT_CHECKBOX),
                  page.locator("text=Checked checkbox"),
                  page.locator("text=Checked switch checkbox input"),
                  page.locator("text=Default radio"),
                  page.locator("text=Default checked radio")]

    for checkbox in checkboxes:
        checkbox.click()
        expect(checkbox).to_be_checked()

def test_form_select(page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    page.select_option("#dropdown-class-example", index=2)
    expect(page.locator("#dropdown-class-example")).to_have_value("option2")

def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()

def test_select_multiple(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files('#formFile', 'hello.txt')
    page.locator('#file-submit').click()

def test_download(page):

    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.locator("#downloadButton").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./tests/"
    download.save_as(os.path.join(destination_folder_path, file_name))



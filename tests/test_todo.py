from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    input_field = page.locator(".new-todo")
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    expect(input_field).to_be_empty()
    input_field.fill("Создать первый сценарий playwright")
    input_field.press('Enter')
    input_field.fill("Добавить в резюме, что умею автоматизировать")
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    todo_item.get_by_role('checkbox').nth(0).check()
    expect(todo_item.nth(0)).to_have_class("completed")

    # page.get_by_placeholder("What needs to be done?").click()
    # page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    # page.get_by_placeholder("What needs to be done?").press("Enter")

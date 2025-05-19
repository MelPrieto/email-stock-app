import yfinance
import pyautogui 
import pyperclip
import webbrowser
import time


ticker = input("Enter the ticker: ")

data = yfinance.Ticker(ticker).history("6mo")
close = data.Close

high = round(close.max(), 2)
low = round(close.min(), 2)
average_price = round(close.mean(), 2)


recipient = input("Enter the recipient's email address: ")
subject = "Stock performance over the past 6 months"
message = f"""
Good afternoon,

I am sharing with you the stock analysis for the past 5 months of {ticker}:

Highest price USD: {high}
Lowest price USD: {low}
Average price USD: {average_price}

Please feel free to reach out if you have any question.
"""

webbrowser.open(input("Enter your email's link: "))

time.sleep(3)

pyautogui.PAUSE = 3

pyautogui.click(141, 228)

pyperclip.copy(recipient)
pyautogui.hotkey("command", "v")
pyautogui.hotkey("tab")

pyperclip.copy(subject)
pyautogui.hotkey("command", "v")
pyautogui.hotkey("tab")

pyperclip.copy(message)
pyautogui.hotkey("command", "v")

pyautogui.click(836, 869)
pyautogui.hotkey("command", "f4")


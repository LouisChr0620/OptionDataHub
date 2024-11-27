import yfinance as yf

# Definiere das Tickersymbol für das zugrunde liegende Asset (z. B. AAPL für Apple)
ticker_symbol = 'AAPL'

# Abrufen des Tickers
ticker = yf.Ticker(ticker_symbol)

# 1. Abrufen der aktuellen Kursdaten (historische und aktuelle Kursdaten)
historical_data = ticker.history(period="1y")  # Daten der letzten 1 Jahr
print("Historical Data:")
print(historical_data)

# 2. Abrufen von Dividenden und Corporate Actions
dividends = ticker.dividends  # Dividenden
actions = ticker.actions  # Corporate Actions
print("\nDividends:")
print(dividends)
print("\nCorporate Actions:")
print(actions)

# 3. Abrufen von Optionsdaten
options = ticker.options  # Liste der Verfallstermine
print("\nAvailable Expiration Dates:")
print(options)

# Abrufen der Optionen-Daten für ein bestimmtes Verfallsdatum (z. B. der erste Verfallstermin)
option_chain = ticker.option_chain(options[0])  # Wählt das erste verfügbare Verfallsdatum
print("\nOption Chain Data for Expiration Date:", options[0])
print("Calls:")
print(option_chain.calls)  # Abrufen der Call-Optionen
print("Puts:")
print(option_chain.puts)  # Abrufen der Put-Optionen

# 4. Abrufen der impliziten Volatilität und anderer Daten aus den Optionspreisen
# Hier extrahierst du spezifische Daten wie Bid, Ask, Last, Strike-Preis, Open Interest, Handelsvolumen
option_data = option_chain.calls  # Du kannst auch die Put-Daten verwenden
print("\nOption Data (Calls):")
print(option_data[['contractSymbol', 'lastPrice', 'ask', 'bid', 'strike', 'impliedVolatility', 'volume', 'openInterest']])

# 5. Abrufen des VIX (Volatility Index)
vix = yf.Ticker('^VIX')  # Ticker für den VIX Index
vix_data = vix.history(period="1y")  # VIX-Daten der letzten 1 Jahr
print("\nVIX Data:")
print(vix_data)

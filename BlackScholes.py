import numpy as np
from scipy.stats import norm

# Define the Black-Scholes function
def black_scholes(S, K, T, r, sigma, option_type='C'):
    """
    S: Current price of the underlying asset (stock)
    K: Strike price of the option
    T: Time to maturity in years (e.g., 240 days / 365)
    r: Risk-free interest rate
    sigma: Volatility of the underlying asset (annualized)
    option_type: 'C' for Call option, 'P' for Put option
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = np.log(S / K) + (r + (sigma ** 2) / 2) * T
    d1 = d1 / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    try:
        # Check option type and calculate option price accordingly
        if option_type.upper() == 'C':  # Call option price
            price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        elif option_type.upper() == 'P':  # Put option price
            price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option type. Please use 'C' for Call or 'P' for Put.")
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    return price

# Define the input parameters for the Black-Scholes model
interest_rate = 0.01  # Risk-free interest rate (1%)
underlying_price = 30  # Current price of the underlying asset (e.g., stock)
strike_price = 40  # Strike price of the option
time = 240 / 365  # Time to maturity in years (240 days)
sigma = 0.30  # Volatility of the underlying asset (30%)

# Test the Black-Scholes function for Call and Put options
call_price = black_scholes(underlying_price, strike_price, time, interest_rate, sigma, option_type='C')
print(f"Call Option Price: {round(call_price, 2)}")

put_price = black_scholes(underlying_price, strike_price, time, interest_rate, sigma, option_type='P')
print(f"Put Option Price: {round(put_price, 2)}")

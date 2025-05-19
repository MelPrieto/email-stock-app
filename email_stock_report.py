import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock Email Generator", page_icon="📈")

st.title("📨 Automated Stock Email Generator")
st.write("This app analyzes the last 6 months of a stock and generates a pre-written email you can copy and send.")

# Entradas del usuario
ticker = st.text_input("Enter the stock ticker (e.g. AAPL, TSLA):")
recipient = st.text_input("Enter the recipient's email address:")
email_url = st.text_input("Enter the URL to your email client (optional):")

# Solo si hay un ticker ingresado
if ticker:
    try:
        data = yf.Ticker(ticker).history("6mo")
        if data.empty:
            st.error("No data found for the given ticker.")
        else:
            close = data.Close
            high = round(close.max(), 2)
            low = round(close.min(), 2)
            average_price = round(close.mean(), 2)

            # Asunto y mensaje
            subject = "Stock performance over the past 6 months"
            message = f"""
Good afternoon,

I am sharing with you the stock analysis for the past 6 months of {ticker.upper()}:

Highest price USD: {high}
Lowest price USD: {low}
Average price USD: {average_price}

Please feel free to reach out if you have any question.
"""

            # Show results
            st.subheader("📊 Stock Summary")
            st.markdown(f"- **Highest Price**: ${high}")
            st.markdown(f"- **Lowest Price**: ${low}")
            st.markdown(f"- **Average Price**: ${average_price}")

            # Show email to copy
            st.subheader("📧 Email Preview")
            st.text_input("Subject", value=subject)
            st.text_area("Body", value=message, height=200)

            # Optional button to open Gmail or any URL
            if email_url:
                if st.button("Open email client"):
                    st.markdown(f"[Click here to open your email client]({email_url})", unsafe_allow_html=True)

            st.success("Copy the content and paste it into your email.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")


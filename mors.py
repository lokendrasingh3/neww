import pandas as pd

# Define Morse code dictionary (reverse of the previous dictionary)
morse_code_dict_reverse = {value: key for key, value in morse_code_dict.items()}

# Function to convert Morse code to text
def morse_to_text(morse_code):
    text = ''
    for code in morse_code.split():
        if code in morse_code_dict_reverse:
            text += morse_code_dict_reverse[code]
    return text.lower()

# Function to decrypt DataFrame with Morse code and make characters lowercase
def decrypt_dataframe(df):
    decrypted_df = df.applymap(lambda x: morse_to_text(str(x)))
    return decrypted_df

# Example Morse code DataFrame



# Decrypt DataFrame and make characters lowercase
decrypted_df = decrypt_dataframe(morse_df)

decrypted_df
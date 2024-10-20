import requests

# Funzione per recuperare le coppie perpetual futures da Bybit
def get_bybit_perpetual_pairs():
    url = "https://api.bybit.com/v5/market/instruments-info"
    params = {
        "category": "linear"  # Richiediamo i contratti perpetual (futures USDT-margined)
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Accediamo alla lista dei contratti in "result" -> "list"
        symbols = data.get("result", {}).get("list", [])
        # Filtriamo solo le coppie perpetual futures, che sono linear perpetual (USDT-margined)
        perpetual_pairs = [
            symbol["symbol"] for symbol in symbols 
            if symbol.get("contractType") == "LinearPerpetual" and "USDT" in symbol["symbol"]
        ]
        return perpetual_pairs
    else:
        print("Errore nel recupero delle coppie da Bybit:", response.status_code)
        return []

# Funzione per inserire le coppie su TradingView
def add_to_tradingview_watchlist(pairs):
    for pair in pairs:
        # Converti il simbolo di Bybit nel formato corretto per TradingView
        tv_symbol = f"BYBIT:{pair}"
        print(f"{tv_symbol}.P")
        # Qui puoi aggiungere il simbolo alla watchlist

# Main
if __name__ == "__main__":
    perpetual_pairs = get_bybit_perpetual_pairs()
    
    if perpetual_pairs:
        print(f"Recuperate {len(perpetual_pairs)} coppie perpetual.")
        add_to_tradingview_watchlist(perpetual_pairs)
    else:
        print("Nessuna coppia perpetual trovata.")

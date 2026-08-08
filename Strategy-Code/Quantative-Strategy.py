import pandas as pd
import yfinance as yf

stockUniverse = [
    "ACN",
    "ADBE",
    "AMD",
    "AKAM",
    "APH",
    "ADI",
    "AAPL",
    "AMAT",
    "ANET",
    "ADSK",
    "ADP",
    "XYZ",
    "AVGO",
    "BR",
    "CDNS",
    "CDW",
    "CIEN",
    "CSCO",
    "CTSH",
    "COHR",
    "GLW",
    "CPAY",
    "CRWD",
    "DDOG",
    "DELL",
    "FFIV",
    "FICO",
    "FIS",
    "FSLR",
    "FLEX",
    "FTNT",
    "FTV",
    "GRMN",
    "IT",
    "GEN",
    "GDDY",
    "HPE",
    "HPQ",
    "IBM",
    "INTC",
    "INTU",
    "JBL",
    "JKHY",
    "KEYS",
    "KLAC",
    "LRCX",
    "LDOS",
    "LITE",
    "MRVL",
    "MCHP",
    "MU",
    "MSFT",
    "MPWR",
    "MSI",
    "NTAP",
    "NVDA",
    "NXPI",
    "ON",
    "ORCL",
    "PLTR",
    "PANW",
    "PAYX",
    "PTC",
    "QCOM",
    "Q",
    "ROP",
    "CRM",
    "SNDK",
    "STX",
    "NOW",
    "SWKS",
    "SMCI",
    "SNPS",
    "TEL",
    "TDY",
    "TER",
    "TXN",
    "TRMB",
    "TYL",
    "UBER",
    "VRSN",
    "WDC",
    "WDAY",
    "ZBRA",
    "AFL",
    "ALL",
    "AXP",
    "AIG",
    "AMP",
    "AON",
    "ACGL",
    "ARES",
    "AJG",
    "AIZ",
    "BAC",
    "BLK",
    "BX",
    "BNY",
    "BRO",
    "COF",
    "CBOE",
    "SCHW",
    "CB",
    "CINF",
    "C",
    "CFG",
    "CME",
    "COIN",
    "ERIE",
    "EG",
    "FDS",
    "FITB",
    "BEN",
    "GL",
    "GS",
    "HIG",
    "HBAN",
    "IBKR",
    "ICE",
    "IVZ",
    "JPM",
    "KEY",
    "KKR",
    "L",
    "MTB",
    "MRSH",
    "MA",
    "MET",
    "MCO",
    "MS",
    "MSCI",
    "NDAQ",
    "NTRS",
    "PYPL",
    "PNC",
    "PFG",
    "PGR",
    "PRU",
    "RJF",
    "RF",
    "HOOD",
    "SPGI",
    "STT",
    "SYF",
    "TROW",
    "TRV",
    "TFC",
    "USB",
    "V",
    "WRB",
    "WFC",
    "WTW",
    "ABT",
    "ABBV",
    "A",
    "ALGN",
    "AMGN",
    "BAX",
    "BDX",
    "TECH",
    "BIIB",
    "BSX",
    "BMY",
    "CAH",
    "COR",
    "CNC",
    "CRL",
    "CI",
    "COO",
    "CVS",
    "DHR",
    "DVA",
    "DXCM",
    "EW",
    "ELV",
    "GEHC",
    "GILD",
    "HCA",
    "HSIC",
    "HUM",
    "IDXX",
    "INCY",
    "PODD",
    "ISRG",
    "IQV",
    "JNJ",
    "LH",
    "LLY",
    "MCK",
    "MDT",
    "MRK",
    "MTD",
    "MRNA",
    # "PFE",
    "DGX",
    "REGN",
    "RMD",
    "RVTY",
    "SOLV",
    "STE",
    "SYK",
    "TMO",
    "UNH",
    "UHS",
    "VEEV",
    "VRTX",
    "VTRS",
    "WAT",
    "WST",
    "ZBH",
    "ZTS",
    "ABNB",
    "AMZN",
    "AMCR",
    "APTV",
    "AZO",
    "AVY",
    "BALL",
    "BBY",
    "BKNG",
    "CCL",
    "CVNA",
    "CASY",
    "CMG",
    "DRI",
    "DECK",
    "DPZ",
    "DASH",
    "DHI",
    "EBAY",
    "EXPE",
    "F",
    "GM",
    "GPC",
    "HAS",
    "HLT",
    "HD",
    "IP",
    "LVS",
    "LEN",
    "LOW",
    "LULU",
    "MAR",
    "MCD",
    "MGM",
    "NKE",
    "NCLH",
    "NVR",
    "ORLY",
    "PKG",
    "PHM",
    "RL",
    "ROL",
    "ROST",
    "RCL",
    "SW",
    "SBUX",
    "TPR",
    "TSLA",
    "TJX",
    "TSCO",
    "ULTA",
    "WSM",
    "WYNN",
    "YUM",
    "MO",
    "ADM",
    "BG",
    "CHD",
    "CLX",
    "KO",
    "CL",
    "STZ",
    "COST",
    "DG",
    "DLTR",
    "EL",
    "GIS",
    "HSY",
    "HRL",
    "KVUE",
    "KDP",
    "KMB",
    "KHC",
    "KR",
    "MKC",
    "TAP",
    "MDLZ",
    "MNST",
    "PEP",
    "PM",
    "PG",
    "SJM",
    "SYY",
    "TGT",
    "TSN",
    "WMT",
    "GOOGL",
    "GOOG",
    "APP",
    "T",
    "CHTR",
    "CMCSA",
    "ECHO",
    "EA",
    "FOXA",
    "FOX",
    "LYV",
    "META",
    "NFLX",
    "NWSA",
    "NWS",
    "OMC",
    "PSKY",
    "TMUS",
    "TTWO",
    "TKO",
    "TTD",
    "VZ",
    "DIS",
    "WBD",
    "MMM",
    "AOS",
    "ALLE",
    "AME",
    "AXON",
    "BA",
    "BLDR",
    "CHRW",
    "CARR",
    "CAT",
    "CTAS",
    "FIX",
    "CPRT",
    "CSX",
    "CMI",
    "DE",
    "DAL",
    "DOV",
    "ETN",
    "EME",
    "EMR",
    "EFX",
    "EXPD",
    "FAST",
    "FDX",
    "FDXF",
    "GE",
    "GEV",
    "GNRC",
    "GD",
    "GPN",
    "HONA",
    "HON",
    "HWM",
    "HUBB",
    "HII",
    "IEX",
    "ITW",
    "IR",
    "JBHT",
    "J",
    "JCI",
    "LHX",
    "LII",
    "LMT",
    "MAS",
    "NDSN",
    "NSC",
    "NOC",
    "ODFL",
    "OTIS",
    "PCAR",
    "PH",
    "PNR",
    "PWR",
    "RTX",
    "RSG",
    "ROK",
    "SNA",
    "LUV",
    "SWK",
    "TXT",
    "TT",
    "TDG",
    "UNP",
    "UAL",
    "UPS",
    "URI",
    "VLTO",
    "VRSK",
    "VRT",
    "GWW",
    "WAB",
    "WM",
    "XYL",
    "APA",
    "BKR",
    "CVX",
    "COP",
    "DVN",
    "FANG",
    "EOG",
    "EQT",
    "EXE",
    "XOM",
    "HAL",
    "KMI",
    "MPC",
    "OXY",
    "OKE",
    "PSX",
    "SLB",
    "TRGP",
    "TPL",
    "VLO",
    "WMB",
    "AES",
    "LNT",
    "AEE",
    "AEP",
    "AWK",
    "ATO",
    "CNP",
    "CMS",
    "ED",
    "CEG",
    "D",
    "DTE",
    "DUK",
    "EIX",
    "ETR",
    "EVRG",
    "ES",
    "EXC",
    "FE",
    "NEE",
    "NI",
    "NRG",
    "PCG",
    "PNW",
    "PPL",
    "PEG",
    "SRE",
    "SO",
    "VST",
    "WEC",
    "APD",
    "ALB",
    "CF",
    "CTVA",
    "CRH",
    "DOW",
    "DD",
    "ECL",
    "IFF",
    "LIN",
    "LYB",
    "MLM",
    "MOS",
    "NEM",
    "NUE",
    "PPG",
    "SHW",
    "STLD",
    "VMC",
    "ARE",
    "AMT",
    "AVB",
    "BXP",
    "CPT",
    "CBRE",
    "CSGP",
    "CCI",
    "DLR",
    "EQIX",
    "EQR",
    "ESS",
    "EXR",
    "FRT",
    "DOC",
    "HST",
    "INVH",
    "IRM",
    "KIM",
    "MAA",
    "PLD",
    "PSA",
    "O",
    "REG",
    "SBAC",
    "SPG",
    "UDR",
    "VTR",
    "VICI",
    "WELL",
    "WY",
]
swingers = []

dfSPY = yf.download(
    "SPY",
    period="2y",
    interval="1d",
    auto_adjust=True,
    progress=False,
    multi_level_index=False,
)


def strategy(stock, dfSPY):
    dfMA = yf.download(
        stock,
        period="2y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        multi_level_index=False,
    )
    if dfMA.empty:
        return swingers

    if len(dfMA) < 400:
        return swingers

    # Live
    price = float(dfMA["Close"].iloc[-1])
    averageLine = float(dfMA["Close"].rolling(window=20).mean().iloc[-1])
    lowestLine = float(dfMA["Close"].iloc[-(64):-1].min())
    activateLine = float(((averageLine - lowestLine) * 0.7) + lowestLine)

    # Conditionals

    ma200 = float(dfMA["Close"].rolling(window=200).mean().iloc[-1])
    ma50 = float(dfMA["Close"].rolling(50).mean().iloc[-1])
    ma20Today = dfMA["Close"].rolling(20).mean()
    volume = dfMA["Volume"].rolling(20).mean().iloc[-1]
    distance = (activateLine - price) / activateLine

    delta = dfMA["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / 14, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / 14, adjust=False).mean()
    rs = avg_gain / avg_loss
    rsi = float((100 - (100 / (1 + rs))).iloc[-1])
    expectedReturn = (averageLine - price) / price

    yesterday = dfMA["Close"].iloc[-2]
    today = dfMA["Close"].iloc[-1]

    high = dfMA["High"]
    low = dfMA["Low"]
    close = dfMA["Close"]

    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))

    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    tr14 = true_range.rolling(14).mean()

    atr = float(tr14.iloc[-1])

    atrPercent = atr / price * 100

    if today <= yesterday * 0.94:
        return swingers
    if atrPercent > 6:
        return swingers
    if price >= averageLine:
        return swingers
    if ma50 <= ma200:
        return swingers
    if ma20Today.iloc[-1] <= ma20Today.iloc[-6]:
        return swingers
    if rsi >= 72.5 or rsi <= 27.5:
        return swingers
    if price <= ma200:
        return swingers
    if volume * price < 5000000:
        return swingers
    if expectedReturn < 0.02:
        return swingers
    if distance > 0.25:
        return swingers
    if price < activateLine and price > (lowestLine * 1.1):
        swingers.append(stock)
        return swingers
    if price >= activateLine or price <= (lowestLine * 1.1):
        return swingers


def trades():
    spy20 = dfSPY["Close"].rolling(20).mean()
    spy50 = dfSPY["Close"].rolling(50).mean()

    spy50Slope = spy50.iloc[-1] - spy50.iloc[-11]

    if dfSPY.empty:
        print("NO SPY DATA")
        return

    if spy20.iloc[-1] < spy50.iloc[-1] or spy50Slope < 0:
        print("SPY Bearish")
        return

    for i in range(len(stockUniverse)):
        strategy(stockUniverse[i], dfSPY)
    
    if len(swingers) == 0:
        print("NO STOCKS FIT CONDITIONS")
        print()
    for i in range(len(swingers)):
        dMA = yf.download(
            swingers[i],
            period="2y",
            interval="1d",
            auto_adjust=True,
            progress=False,
            multi_level_index=False,
        )

        price = float(dMA["Close"].iloc[-1])
        averageLine = float(dMA["Close"].rolling(window=20).mean().iloc[-1])

        stopLoss = 0.92 * price
        takeProfit = averageLine * 1.02

        print()
        print(swingers[i])
        print(str(round(price, 2)))
        print(
            "Stop-Loss : Take-Profit - "
            + str(round(stopLoss, 2))
            + " : "
            + str(round(takeProfit, 2))
        )
        print()


trades()


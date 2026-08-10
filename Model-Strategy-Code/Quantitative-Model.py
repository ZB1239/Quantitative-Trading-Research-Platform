import pandas as pd
import yfinance as yf
from stockScreener import stockScreener
from stockUniverse import stockUniverse

def SPYCheck():
    dfSPY = yf.download(
        "SPY",
        period="2y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        multi_level_index=False,
    )

    spy20 = dfSPY["Close"].rolling(20).mean()
    spy50 = dfSPY["Close"].rolling(50).mean()
    spy50Slope = spy50.iloc[-1] - spy50.iloc[-11]

    if dfSPY.empty or spy20.iloc[-1] < spy50.iloc[-1] or spy50Slope < 0:
        SPYCheck = False
        return SPYCheck


def downloadStockData(stock):
    dfStockData = yf.download(
        stock,
        period="2y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        multi_level_index=False,
    )
    if dfStockData.empty or len(dfStockData) < 400:
        print("[" + str(stock) + "] - Download Fail/Incomplete Dataset")
        return None
    return dfStockData


def tradeEquity(tradingEquity, dfStockData):
    prevClose = dfStockData["Close"].shift(1)
    tr1 = dfStockData["High"] - dfStockData["Low"]
    tr2 = (dfStockData["High"] - prevClose).abs()
    tr3 = (dfStockData["Low"] - prevClose).abs()
    dfStockData["TR"] = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    dfStockData["ATR"] = dfStockData["TR"].rolling(14).mean()
    atr = float(dfStockData["ATR"].iloc[-1])

    marketClosurePrice = float(dfStockData["Close"].iloc[-1])
    averageLine = float(dfStockData["Close"].rolling(window=20).mean().iloc[-1])

    stopLoss = round(marketClosurePrice - (2 * atr), 2)
    takeProfit = round(averageLine * 1.02, 2)

    takeProfitWeekTwo = round(marketClosurePrice * 1.0655, 2)
    stopLossWeekTwo = round(marketClosurePrice - (1.75 * atr), 2)

    takeProfitWeekThree = round(marketClosurePrice * 1.0455, 2)
    stopLossWeekThree = round(marketClosurePrice - (1.5 * atr), 2)

    print(tradingEquity)
    print("Market Closure Price: " + str(round(marketClosurePrice, 2)))
    print(
        "Stop-Loss : Take-Profit - "
        + str(round(stopLoss, 2))
        + " : "
        + str(round(takeProfit, 2))
    )
    print(
        "Stop-Loss(Week 2) : Take-Profit(Week 2) - "
        + str(round(stopLossWeekTwo, 2))
        + " : "
        + str(round(takeProfitWeekTwo, 2))
    )
    print(
        "Stop-Loss(Week 3) : Take-Profit(Week 3) -"
        + str(round(stopLossWeekThree, 2))
        + " : "
        + str(round(takeProfitWeekThree, 2))
    )


def quantitativeTradingModel():
    market = SPYCheck()

    if market == False:
        print("Market Condition Failure: SPY Bearish or Data Failure")

    for i in range(len(stockUniverse)):
        stock = stockUniverse[i]
        dfStockData = downloadStockData(stock)
        tradingEquity = stockScreener(stock, dfStockData)[0]
        dfTradingStockData = stockScreener(stock, dfStockData)[1]

        if dfStockData is None:
            continue

        if tradeEquity == False or dfTradingStockData is None:
            continue

        tradeEquity(tradingEquity, dfTradingStockData)
quantitativeTradingModel()
quantitativeTradingMo

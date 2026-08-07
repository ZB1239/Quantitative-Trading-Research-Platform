# Quantitative-Trading-Research-Platform
Python-built proprietary quantitative swing trading platform with research and automated signal-generation capabilities, leveraging mathematical models and technical analysis of historical and real-time S&amp;P 500 market data.


## Overview
This project is a proprietary quantitative trading research platform to design, backtest, and evaluate systematic swing-trading strategies on S&P 500 equities.

The platform integrates historical market data, quantitative signal generation, portfolio simulation, risk management, and statistical performance analysis into a single research workflow. It is designed to assess whether a systematic trading strategy can generate consistent risk-adjusted returns while accounting for factors such as position sizing, stop-losses, take-profits, holding periods, and market conditions.

The research process includes parameter optimisation, historical backtesting, benchmark comparison against the S&P 500, and detailed trade-level analysis. The platform records individual trade characteristics including entry and exit prices, realised returns, holding periods, maximum favourable movement, and maximum adverse movement, allowing the strategy to be evaluated beyond headline returns.

The current research has been evaluated across one year of historical market data following parameter optimisation over approximately 50 trading days. Performance is assessed using metrics including total return, CAGR, maximum drawdown, Sharpe ratio, Sortino ratio, Calmar ratio, profit factor, expectancy, and annualised volatility.

The strategy and its underlying methodology are proprietary and therefore the core trading logic and parameters are not publicly disclosed.


## Strategy
The platform implements a systematic quantitative swing-trading strategy designed to identify short-to-medium-term opportunities within S&P 500 equities.

The strategy evaluates historical and current market data to generate objective entry and exit signals based on a combination of quantitative indicators, price behaviour, market trends, and predefined risk-management rules. Rather than relying on discretionary decision-making, each trade is evaluated according to a consistent set of rules.

The strategy incorporates:

Market regime filtering — evaluates broader market conditions before allowing individual equity positions to be considered.
Quantitative signal generation — identifies equities that satisfy the strategy's predefined entry conditions.
Dynamic entry levels — determines an appropriate entry price based on the underlying market data and strategy conditions.
Risk management — applies systematic stop-loss and take-profit levels to control downside risk and manage exits.
Position sizing — determines exposure according to predefined portfolio allocation rules.
Trade management — monitors positions until an exit condition is reached.
Benchmark comparison — evaluates strategy performance against the S&P 500 through the SPY ETF.

The underlying mathematical formulation, parameter values, signal thresholds, and proprietary decision rules are intentionally not disclosed.


## Performance
The strategy was evaluated using one year of historical S&P 500 market data following parameter optimisation over approximately 50 trading days. The resulting parameters were then held fixed throughout the evaluation period.

Strategy vs SPY
                  
Initial Capital - £10,000 : £10,000

Final Portfolio Value -	£14,200.76 : £11,877.40

Net Profit - £4,200.76 : £1,877.40

Total Return- 42.01% : 18.77%

Maximum Drawdown- -9.12% : -6.70%

Annualised Sharpe Ratio- 1.90 : 1.20

Sortino Ratio-	2.67 : 1.80

Calmar Ratio-	4.61	: 2.80

Annualised Volatility-	28.10%	: 15.50%

----------------------------

Trade Statistics for Strategy

Total Trades	79

Win Rate	68.35%

Average Winning Trade	6.23%

Average Losing Trade	-5.92%

Largest Winner	12.87%

Largest Loser	-9.82%

Median Trade Return	4.50%

Average Holding Period	11.43 trading days

Profit Factor	2.27

Expectancy	2.39%


The strategy generated a 42.01% total return over the evaluation period compared with 18.77% for SPY. While the strategy experienced greater volatility and a somewhat larger maximum drawdown, it produced stronger risk-adjusted performance across the Sharpe, Sortino, and Calmar ratios.

These results represent historical backtest performance and should not be interpreted as an indication of future returns. Further out-of-sample, walk-forward, transaction-cost, and robustness testing is required before drawing conclusions regarding live trading performance.


## Disclaimer
This project is intended for quantitative research, educational, and experimental purposes only. The performance figures presented are based on historical backtesting and do not represent actual live trading results.

Backtested performance may differ materially from real-world performance due to factors including market conditions, transaction costs, slippage, liquidity, data quality, execution constraints, and model overfitting. Past performance does not guarantee future results.

The strategy's parameters and underlying methodology are proprietary and are not intended to constitute financial advice or a recommendation to buy or sell any security.

Furthermore, this research project was produced my an un-experienced junior in terms of the stock market and wider-financial world so some metrics or statements may unintentionally be incorrect. Thank you,
Zach Barber. 

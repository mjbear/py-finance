import quantstats_lumi as qs

# extend pandas functionality with metrics, etc.
qs.extend_pandas()

# fetch the daily returns for a stock
stock = qs.utils.download_returns('META')

print("sharpe" + str(stock.sharpe()))
print("sortino" + str(stock.sortino()))
print("smart_sortino" + str(stock.smart_sortino()))
print("best" + str(stock.best()*100))
print("avg_win" + str(stock.avg_win()*100))
print(".worst" + str(stock.worst()*100))
print("avg_loss" + str(stock.avg_loss()*100))
print("ytd" + str(stock.ytd()*100))
print("CAGR" + str(stock.cagr()))
print("volatility" + str(stock.volatility()))
print("profit_ratio(" + str(stock.profit_ratio()))
print("ulcer_index" + str(stock.ulcer_index()))
print("risk_return_ratio" + str(stock.risk_return_ratio()))
print("expected_return" + str(stock.expected_return()))
print("consecutive_losses" + str(stock.consecutive_losses()))
print("onsecutive_wins" + str(stock.consecutive_wins()))
print("" + str(stock.tail()))

#qs.plots.snapshot(stock, title='Facebook Performance', show=False)

print("END")
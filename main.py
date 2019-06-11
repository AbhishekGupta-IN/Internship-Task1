from trade import get_trades, plot_graph, get_bands, get_csticks, get_close_price_n_time
import trading_strategy as ts

trade_data = get_trades('BNBUSDT','4h','1000','sasda','asas')
csticks = get_csticks(trade_data)
t_list, t_time = get_close_price_n_time(trade_data)
bands = get_bands(t_list)

markers = ts.backtest_()
plot_graph(bands, csticks, t_time)

import logging
import sys
sys.dont_write_bytecode = True

N = 2
PERIODS = 100
TREND_BIAS = 0.05
START = '1/1/2000'
FREQ = 'H'
START_PRICE = 200
RESAMPLE_FREQ = '1H'

STREAM_HISTORY_LEN = 4
DELAYED_EXECUTION = False
PRINT_PNL = False
PRINT_TRADES = False
PLOT_PERFORMANCE = False
LOG_LEVEL = logging.INFO
LOG_TO_FILE = True
PRINT_OPTIMIZATION_RUN = False
CALC_ROLLING_STATS = True
INITIAL_CASH = 100000
LOG_FREQUENCY = 100
LOG_TRADES = True
TRADES_FILE = 'results/test_trades.dat'
LOG_TRADES_TO_FILE = False
DELAY_CYCLES = 1
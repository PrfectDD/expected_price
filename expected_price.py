# 一个用于计算穿透回报率和预期价格的小工具（带Tkinter界面）
import tkinter as tk
from tkinter import ttk

# 计算函数
def calc_penetrating_return(discount, payout_ratio, required_yield, market_cap, total_shares, net_profit):
    """
    参数：
        discount: 折价（百分数，如80表示80%）
        payout_ratio: 股息支付率（百分数，如70表示70%）
        required_yield: 要求股息率（百分数，如4表示4%）
        market_cap: 总市值（单位：亿）
        total_shares: 总股本（单位：亿）
        net_profit: 净利润（单位：亿）
    返回：
        当前穿透回报率、预期穿透回报率价格、每股价格
    """
    try:
        # 百分数转小数
        discount = float(discount) / 100
        payout_ratio = float(payout_ratio) / 100
        required_yield = float(required_yield) / 100
        market_cap = float(market_cap)
        total_shares = float(total_shares)
        net_profit = float(net_profit)
        # 当前穿透回报率 = 净利润 * 折价 * 股息率 / 总市值
        current_yield = net_profit * discount * payout_ratio / market_cap
        # 预期穿透回报率价格 = 净利润 * 折价 * 股息率 / 要求股息率
        expected_price = net_profit * discount * payout_ratio / required_yield
        # 每股价格 = 预期穿透回报率价格 / 总股本
        price_per_share = expected_price / total_shares
        return current_yield, expected_price, price_per_share
    except Exception:
        return None, None, None

# 实时更新结果
def update_result(*args):
    current_yield, expected_price, price_per_share = calc_penetrating_return(
        discount_var.get(), payout_ratio_var.get(), required_yield_var.get(),
        market_cap_var.get(), total_shares_var.get(), net_profit_var.get()
    )
    if None in (current_yield, expected_price, price_per_share):
        result_var.set("请完整输入所有参数且为数字")
    else:
        result_var.set(f"当前穿透回报率：{current_yield*100:.2f}%\n预期穿透回报率总市值：{expected_price:.2f}亿\n每股价格：{price_per_share:.2f}")

# 创建主窗口
root = tk.Tk()
root.title("穿透回报率与预期价格计算器")

# 定义变量
discount_var = tk.StringVar()
payout_ratio_var = tk.StringVar()
required_yield_var = tk.StringVar()
market_cap_var = tk.StringVar()
total_shares_var = tk.StringVar()
net_profit_var = tk.StringVar()
result_var = tk.StringVar()

# 绑定变量变化事件
for var in [discount_var, payout_ratio_var, required_yield_var, market_cap_var, total_shares_var, net_profit_var]:
    var.trace_add('write', update_result)

# 布局
fields = [
    ("折价（如80表示80%）", discount_var),
    ("股息支付率（如70表示70%）", payout_ratio_var),
    ("要求股息率（如4表示4%）", required_yield_var),
    ("总市值（单位：亿）", market_cap_var),
    ("总股本（单位：亿）", total_shares_var),
    ("净利润（单位：亿）", net_profit_var),
]

for i, (label, var) in enumerate(fields):
    ttk.Label(root, text=label).grid(row=i, column=0, sticky='e', padx=5, pady=5)
    ttk.Entry(root, textvariable=var, width=20).grid(row=i, column=1, padx=5, pady=5)

# 结果显示
result_label = ttk.Label(root, textvariable=result_var, foreground='blue', font=("微软雅黑", 12))
result_label.grid(row=len(fields), column=0, columnspan=2, pady=15)

# 启动主循环
root.mainloop()
1

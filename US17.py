import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

# =========================
# 1. ĐỌC DỮ LIỆU
# =========================
df = pd.read_csv("orders.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

today = pd.Timestamp.today().normalize()

# =========================
# 2. LỌC DỮ LIỆU THEO THỜI GIAN
# =========================
def filter_by_time(option):
    if option == "today":
        return df[df["order_date"] == today]

    elif option == "yesterday":
        return df[df["order_date"] == today - timedelta(days=1)]

    elif option == "this_week":
        start_week = today - timedelta(days=today.weekday())
        return df[df["order_date"] >= start_week]

    elif option == "this_month":
        start_month = today.replace(day=1)
        return df[df["order_date"] >= start_month]

    else:
        return df

# =========================
# 3. BÁO CÁO DOANH THU
# =========================

# 3.1 Tổng doanh thu thuần
def total_net_sales(data):
    return data["net_sales"].sum()

# 3.2 Doanh thu theo ngày
def net_sales_by_day(data):
    return data.groupby("order_date")["net_sales"].sum()

# 3.3 Doanh thu theo tuần
def net_sales_by_week():
    df["week"] = df["order_date"].dt.to_period("W")
    return df.groupby("week")["net_sales"].sum()

# 3.4 Doanh thu theo tháng
def net_sales_by_month():
    df["month"] = df["order_date"].dt.to_period("M")
    return df.groupby("month")["net_sales"].sum()

# =========================
# 4. BIỂU ĐỒ XU HƯỚNG DOANH THU
# =========================
def plot_revenue_trend(data):
    daily_sales = data.groupby("order_date")["net_sales"].sum()

    plt.figure()
    plt.plot(daily_sales.index, daily_sales.values)
    plt.xlabel("Ngày")
    plt.ylabel("Doanh thu thuần")
    plt.title("Xu hướng Doanh thu thuần (Net Sales)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# =========================
# 5. CHẠY BÁO CÁO
# =========================
option = "this_month"  # today | yesterday | this_week | this_month
data = filter_by_time(option)

print("TỔNG DOANH THU THUẦN:", total_net_sales(data))
print("\nDOANH THU THEO NGÀY:\n", net_sales_by_day(data))

plot_revenue_trend(data)

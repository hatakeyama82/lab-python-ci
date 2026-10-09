# Decimal：小数の計算で、浮動小数点による誤差を避けるために使う。
from decimal import Decimal, ROUND_HALF_UP


# price：税抜き金額。
# rate：税率。指定しなければ10%。
def calculate_total(
    price: Decimal,
    rate: Decimal = Decimal("0.10"),
) -> Decimal:
    # 負の金額・税率は受け付けない。
    if price < 0 or rate < 0:
        raise ValueError("Price and tax rate must not be negative.")

    # 税込金額を計算する。
    total = price * (Decimal("1") + rate)

    # 1円単位に四捨五入する。
    return total.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


# このファイルを直接実行したときだけ、サンプル計算を行う。
if __name__ == "__main__":
    print(calculate_total(Decimal("1000")))
    
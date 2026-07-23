import streamlit as st

st.title("🛒 แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")

# รับราคาสินค้า
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

# คำนวณ VAT และราคาสุทธิ
vat = price * 0.07
net_price = price - vat

# แสดงผล
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): {vat:.2f} บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.write("นายแสงเฮอ เลขที่ 28 ม.4/15")

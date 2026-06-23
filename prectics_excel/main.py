import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setting ko wide mode me karein taaki dashboard khula-khula dikhe
st.set_page_config(page_title="Car Sales Dashboard", layout="wide")

# Custom CSS lagakar background aur cards ko professional look dein
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1E3A8A; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: 700; text-align: center; margin-bottom: 30px; }
    .card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

df = pd.read_csv('car_clean_dataset')

st.markdown('<h1>🚗 Modern Car Sales Dashboard</h1>', unsafe_allow_html=True)

# --- Data Aggregations (Aapka pure data logic) ---
group_transmission = df.groupby(['Transmission'])['Transmission'].count()
group_Fuel_Type = df.groupby(['Fuel_Type'])['Fuel_Type'].count()
group_Owner_Type = df.groupby(['Owner_Type'])['Owner_Type'].count()
df=df[df['Owner_Type']=='First']
group_car = df.groupby(['Name'])['Name'].count()
group_car_sort = group_car.sort_values(ascending=False).head(30)

# ==================== ROW 1: KEY METRICS CORNER (PIE CHARTS) ====================
# Streamlit ke columns banakar charts ko alag-alag compartments me set kiya
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>⚙️ Transmission Distribution</h3>', unsafe_allow_html=True)
    fig1, ax1 = plt.subplots(figsize=(5, 4))
    colors = sns.color_palette('pastel')[0:len(group_transmission)]
    ax1.pie(group_transmission, labels=group_transmission.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'white'})
    ax1.axis('equal')
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>⛽ Fuel Type Distribution</h3>', unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    colors = sns.color_palette('muted')[0:len(group_Fuel_Type)]
    ax2.pie(group_Fuel_Type, labels=group_Fuel_Type.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'white'})
    ax2.axis('equal')
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>👤 Owner Type Distribution</h3>', unsafe_allow_html=True)
    fig3, ax3 = plt.subplots(figsize=(5, 4))
    colors = sns.color_palette('deep')[0:len(group_Owner_Type)]
    ax3.pie(group_Owner_Type, labels=group_Owner_Type.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'white'})
    ax3.axis('equal')
    st.pyplot(fig3)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== ROW 2: MAIN SALES CORNER (BAR CHART) ====================
st.markdown('<div class="card"><h3>🏆 Top 30 Highest Sales Cars</h3>', unsafe_allow_html=True)

# Is chart ko bada aur khula banane ke liye alag se space di gayi hai
fig4, ax4 = plt.subplots(figsize=(15, 5))

# Seaborn barplot se smooth, professional color gradient bar chart banaya
sns.barplot(x=group_car_sort.values, y=group_car_sort.index, ax=ax4, palette="Blues_r")

# Chart styling ki taaki grid lines clean dikhein
ax4.set_xlabel('Number of Cars Sold', fontsize=12)
ax4.set_ylabel('Car Model Name', fontsize=12)
sns.despine(left=True, bottom=True) # Faltu border lines hatane ke liye
ax4.grid(axis='x', linestyle='--', alpha=0.5)

st.pyplot(fig4, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<br>',unsafe_allow_html=True)
st.markdown(' ## FIRST HAND CAR SALES DATA')
#top 30 cars properties price range
price_lis=[]
for i in group_car_sort.index:
    index_value=df[df['Name']==i].index[0]
    price=df['Price'].iloc[index_value]
    price_lis.append(price)
#top 30 car  mileage range
mileage_range=[]
for i in group_car_sort.index:
    index_value=df[df['Name']==i].index[0]
    mileage=df['Mileage'].iloc[index_value]
    mileage_range.append(mileage)
#top 30 car power range
car_power=[]
for i in group_car_sort.index:
    index_value=df[df['Name']==i].index[0]
    power=df['Power'].iloc[index_value]
    car_power.append(power)
col1,col2,col3,col4=st.columns(4)
#top seliing car cites
cites_count=df[df['Name'].isin(group_car_sort.index)]['Location'].value_counts()
with col1:
    st.markdown('<div class="card"><h3> $ top 30 selling  cars price range in Lakh',unsafe_allow_html=True)
    fig5,ax5=plt.subplots(figsize=(5,4))
    colors=sns.color_palette('muted')[0]
    ax5.hist(price_lis,bins=60,color=colors ,edgecolor='white')
    ax5.set_xlabel('distrbution of prize range in Lakh')
    ax5.set_ylabel('number of car sales')
    st.pyplot(fig5)
    st.markdown('</div>',unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h3> $ top 30 selling cars mileage range',unsafe_allow_html=True)
    fig6,ax6=plt.subplots(figsize=(5,4))
    colors = sns.color_palette('pastel')[0]
    ax6.hist(mileage_range,bins=60,color=colors ,edgecolor='white')
    ax6.set_xlabel('distrbution of mileage in km/L')
    ax6.set_ylabel('number of car sales')
    st.pyplot(fig6)
    st.markdown('</div>',unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><h3> $ top 30 selling cars power range',unsafe_allow_html=True)
    fig7,ax7=plt.subplots(figsize=(5,4))
    colors = sns.color_palette('Blues_r')[0]
    ax7.hist(car_power,bins=60,color=colors ,edgecolor='white')
    ax7.set_xlabel('distrbution of power in CC')
    ax7.set_ylabel('number of car sales')
    st.pyplot(fig7)
    st.markdown('</div>',unsafe_allow_html=True)
with col4:
    st.markdown('<div class="card"><h3>top cites</h3>', unsafe_allow_html=True)
    fig8, ax8 = plt.subplots(figsize=(5, 4))
    colors = sns.color_palette('pastel')[0:len(cites_count)]
    ax8.pie(cites_count, labels=cites_count.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'white'})
    ax8.axis('equal')
    st.pyplot(fig8)
    st.markdown('</div>', unsafe_allow_html=True)    
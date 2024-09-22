import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px




st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)



tab1, tab2 = st.tabs(["Penelusuran Literatur", "Lain-Lain"])












with tab1:
   col1, col2, col3 = st.columns(3)
   with col1:
     st.image("https://statkomat.com/gambar/ugi.png", caption='', width = 350)
   with col1:
     st.markdown("<h5 style='text-align: justify; color: blue;'>Hadirnya website ini sebagai media untuk sharing terkait penelusuran literatur. Topik yang disajikan di sini merupakan topik yang sedang saya tekuni.</h5><br><br><center><a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>STATKOMAT</b></font></a> | <a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>YOUTUBE</b></font></a></center>", unsafe_allow_html=True)





      
   st.header(":blue[Penelusuran Literatur]")
   
   pilih_topik = st.radio(
    "Pilih Topik: ",
    ["Pengaruh Kinerja Keuangan Perusahaan (Firm Financial Performance) terhadap Kapitalisasi Pasar (Market Capitalization)", "Pengaruh Kinerja Keuangan Perusahaan (Firm Financial Performance) terhadap Harga Saham", "Bankruptcy, Financial Distress, Financial Health on Stock Price"],)
   
   if pilih_topik == "Pengaruh Kinerja Keuangan Perusahaan (Firm Financial Performance) terhadap Kapitalisasi Pasar (Market Capitalization)":
    st.markdown("<br><br><br><center><h2 style='text-align: justify; color: blue;'>Tabel Ringkasan Literatur</h2></center>", unsafe_allow_html=True)
    data_market_cap = pd.read_excel('Ringkasan Hasil Paper Market Capitalization.xlsx', index_col=0) 
    st.dataframe(data_market_cap)

    tab1.markdown("<h3 style='text-align: justify; color: #39ff14;'><center>Penelusuran Literatur berdasarkan Pengaruh Kinerja Keuangan Perusahaan (<i>Firm Financial Performance</i>) terhadap Kapitalisasi Pasar (<i>Market Capitalization</i>)</center></h5>", unsafe_allow_html=True)
    st.write('''

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] <a href = "https://www.mdpi.com/1996-1073/16/3/1398" target = "_blank" style = "text-decoration:none">Judul: Examining the Causality between Integrated Reporting and Stock Market Capitalization. The Case of the European Renewable Energy Equipment and Services Industry | <font color = "#ff1493">Jurnal: energies</font> | <font color = "#32cd32">Publisher: MDPI</font></a>
             <br><br><br>


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2022</b></font><br>  
             [1] <a href = "https://journal.unimma.ac.id/index.php/bisnisekonomi/article/view/7835" target = "_blank" style = "text-decoration:none">Judul: Market Capitalization and Financial Performance: Evidence from Banking Listed Company in Indonesia | <font color = "#ff1493">Jurnal: Jurnal Analisis Bisnis Ekonomi</font> | <font color = "#32cd32">Publisher: Fakultas Ekonomi Universitas Muhammadiyah Magelang</font></a><br><br><br>
             

             
<font color = "#ff00ff" size = 5><b>Tahun Terbit 2020</b></font><br>  
             [1] <a href = "https://www.ijicc.net/images/vol_13/Iss_7/13700v_Hermawan_2020_E_R1.pdf" target = "_blank" style = "text-decoration:none">Judul: Intellectual Capital Disclosure and Company Financial Performance : Market Capitalization | <font color = "#ff1493">Jurnal: International Journal of Innovation, Creativity and Change</font> | <font color = "#32cd32">Publisher: </font></a><br>
             [2] <a href = "https://scipg.com/index.php/103/article/view/359" target = "_blank" style = "text-decoration:none">Judul: Evaluation of Return on Assets on Market Capitalization of Quoted Construction/Real Estate and Conglomerate Companies in Nigeria | <font color = "#ff1493">Jurnal: International Journal of Emerging Trends in Social Sciences</font> | <font color = "#32cd32">Publisher: Scientific Publishing Institute</font></a><br>
             [3] <a href = "https://www.tandfonline.com/doi/full/10.1080/23311975.2020.1750332" target = "_blank" style = "text-decoration:none">Judul: Corporate governance on intellectual capital disclosure and market capitalization | <font color = "#ff1493">Jurnal: Cogent Business & Management</font> | <font color = "#32cd32">Publisher: Taylor & Francis</font></a><br><br><br>
             

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2019</b></font><br>  
             [1] <a href = "https://www.anrec.it/wp-content/uploads/2019/06/Market_Capitalization_and_Financial_Variables.pdf" target = "_blank" style = "text-decoration:none">Judul: Market Capitalization and Financial Variables: Evidence from Italian Listed Companies | <font color = "#ff1493">Jurnal: International Journal of Academic Research Business and Social Sciences</font> | <font color = "#32cd32">Publisher: </font></a><br><br><br>

             
<font color = "#ff00ff" size = 5><b>Tahun Terbit 2018</b></font><br>  
             [1] <a href = "https://www.ijbssnet.com/journal/index/3997" target = "_blank" style = "text-decoration:none">Judul: An Empirical Study on Effect of Profitability Ratios & Market Value Ratios on Market Capitalization of Commercial Banks in Jordan | <font color = "#ff1493">Jurnal: International Journal of Business and Social Science</font> | <font color = "#32cd32">Publisher: The Brooklyn Research and Publishing Institute</font></a><br><br><br>


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2017</b></font><br>  
             [1] <a href = "https://www.shs-conferences.org/articles/shsconf/abs/2017/02/shsconf_four2017_07001/shsconf_four2017_07001.html" target = "_blank" style = "text-decoration:none">Judul: Intellectual capital disclosure determinants and its effects on the market capitalization: evidence from Indonesian listed companies | <font color = "#ff1493">Jurnal: SHS Web of Conferences</font> | <font color = "#32cd32">Publisher: EDP Sciences</font></a><br><br><br>


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2016</b></font><br>  
             [1] <a href = "https://ijbmi.org/papers/Vol(5)11/version-2/E051102056062.pdf" target = "_blank" style = "text-decoration:none">Judul: Impact of profitability, bank and macroeconomic factors on the market capitalization of the Middle Eastern banks | <font color = "#ff1493">Jurnal: International Journal of Business and Management Invention</font> | <font color = "#32cd32">Publisher: </font></a><br><br><br>

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2015</b></font><br>  
             [1] <a href = "https://www.iiste.org/Journals/index.php/JEDS/article/view/21061" target = "_blank" style = "text-decoration:none">Judul: The Effect of Profitability Ratios on Market Capitalization in Jordanian Insurance Companies Listed in Amman Stock Exchange | <font color = "#ff1493">Jurnal: Journal of Economics and Sustainable Development</font> | <font color = "#32cd32">Publisher: The International Institute for Science, Technology and Education (IISTE)</font></a>








                  ''', unsafe_allow_html=True)


if pilih_topik == "Pengaruh Kinerja Keuangan Perusahaan (Firm Financial Performance) terhadap Harga Saham":
    tab1.markdown("<h3 style='text-align: justify; color: #39ff14;'><center>Penelusuran Literatur berdasarkan Pengaruh Kinerja Keuangan Perusahaan (<i>Firm Financial Performance</i>) terhadap Harga Saham (<i>Stock Price</i>)</center></h5>", unsafe_allow_html=True)
    st.write('''

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2024</b></font><br>  
             [1] <a href = "https://ejournal.uigm.ac.id/index.php/EGMK/article/view/3905" target = "_blank" style = "text-decoration:none">Judul: Correlation Analysis Between Financial Ratios and Stock Prices of Real Estate Companies Listed on the Indonesia Stock Exchange | <font color = "#ff1493">Jurnal: Jurnal Ilmiah Ekonomi Global Masa Kini</font> | <font color = "#32cd32">Publisher: </font></a>
             <br>
             [2] <a href = "https://ip2i.org/jip/index.php/ema/article/view/177" target = "_blank" style = "text-decoration:none">Judul: The effect of return on asset and net profit margin on stock price | <font color = "#ff1493">Jurnal: Jurnal Ekonomi, Manajemen dan Akuntansi</font> | <font color = "#32cd32">Publisher: </font></a>
             <br>
             [3] <a href = "https://ip2i.org/jip/index.php/ema/article/view/155" target = "_blank" style = "text-decoration:none">Judul: The effect of market value added and dividend payout ratio on stock prices | <font color = "#ff1493">Jurnal: Jurnal Ekonomi, Manajemen dan Akuntansi</font> | <font color = "#32cd32">Publisher: </font></a>
             <br>
             [4] <a href = "https://ip2i.org/jip/index.php/ema/article/view/100" target = "_blank" style = "text-decoration:none">Judul: The effect of cash flow changes on stock prices | <font color = "#ff1493">Jurnal: Jurnal Ekonomi, Manajemen dan Akuntansi</font> | <font color = "#32cd32">Publisher: </font></a>
             <br>
             [5] <a href = "https://ip2i.org/jip/index.php/ema/article/view/129" target = "_blank" style = "text-decoration:none">Judul: The effect of earning per share and debt to equity ratio on the share price | <font color = "#ff1493">Jurnal: Jurnal Ekonomi, Manajemen dan Akuntansi</font> | <font color = "#32cd32">Publisher: </font></a>
             <br><br><br>




<font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] <a href = "https://sloap.org/journal/index.php/ijbem/article/view/2058" target = "_blank" style = "text-decoration:none">Judul: The effect of financial ratio on stock price in telecommunications sector companies listed on the Indonesia stock exchange | <font color = "#ff1493">Jurnal: International Journal of Business, Economics & Management</font> | <font color = "#32cd32">Publisher: </font></a>
             <br>
             [2] <a href = "http://journalfeb.unla.ac.id/index.php/almana/article/view/2071" target = "_blank" style = "text-decoration:none">Judul: Analysis of Financial Ratio to Stock Price | <font color = "#ff1493">Jurnal: Almana : Jurnal Manajemen dan Bisnis</font> | <font color = "#32cd32">Publisher: </font></a>
             <br>
             [3] <a href = "https://journal.unnes.ac.id/nju/jda/article/view/40072/14223" target = "_blank" style = "text-decoration:none">Judul: Fundamental Analysis of Financial Ratios in Stock Price: Do Loss and Firm Size Matter? | <font color = "#ff1493">Jurnal: Almana : Jurnal Dinamika Akuntansi</font> | <font color = "#32cd32">Publisher: </font></a>
             <br><br><br>


 <font color = "#ff00ff" size = 5><b>Tahun Terbit 2019</b></font><br>  
             [1] <a href = "https://journal.uinjkt.ac.id/index.php/etikonomi/article/view/10987/pdf" target = "_blank" style = "text-decoration:none">Judul: The Determinant of Stock Prices: Evidence on Food and Beverage Companies in Indonesia | <font color = "#ff1493">Jurnal: Etikonomi</font> | <font color = "#32cd32">Publisher: </font></a>
            <br><br><br>

            


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2018</b></font><br>  
             [1] <a href = "https://www.econjournals.com.tr/index.php/ijeep/article/view/5964" target = "_blank" style = "text-decoration:none">Judul: Impact of Accounting Information on Financial Statements to the Stock Price of the Energy Enterprises Listed on Vietnam's Stock Market | <font color = "#ff1493">Jurnal: International Journal of Energy Economics and Policy</font> | <font color = "#32cd32">Publisher: </font></a>
            <br><br><br>













<font color = "#ff00ff" size = 5><b>Tahun Terbit 2017</b></font><br>  
             [1] <a href = "https://journal.unpak.ac.id/index.php/jiafe/article/view/778/0" target = "_blank" style = "text-decoration:none">Judul: THE EFFECT OF FINANCIAL PERFORMANCE ON STOCK PRICE AT PHARMACEUTICAL SUB-SECTOR COMPANY LISTED IN INDONESIA STOCK EXCHANGE | <font color = "#ff1493">Jurnal: JIAFE (Jurnal Ilmiah Akuntansi Fakultas Ekonomi)</font> | <font color = "#32cd32">Publisher: </font></a>
             <br>
             [2] <a href = "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3542011" target = "_blank" style = "text-decoration:none">Judul: The Effect of Financial Performance and Corporate Governance to Stock Price in Non-Bank Financial Industry | <font color = "#ff1493">Jurnal: Corporate Ownership & Control</font> | <font color = "#32cd32">Publisher: </font></a>             
             [3] <a href = "https://www.atlantis-press.com/proceedings/icame-17/25885676" target = "_blank" style = "text-decoration:none">Judul: Is Financial Performance Reflected in Stock Prices? | <font color = "#ff1493">Jurnal: Proceedings of the 2nd International Conference on Accounting, Management, and Economics 2017 (ICAME 2017): Advances in Economics, Business and Management Research</font> | <font color = "#32cd32">Publisher: </font></a>             
             <br><br><br>


             




<font color = "#ff00ff" size = 5><b>Tahun Terbit 2016</b></font><br>  
             [1] <a href = "https://journal.perbanas.ac.id/index.php/tiar/article/view/853" target = "_blank" style = "text-decoration:none">Judul: The influence of profitability ratio, market ratio, and solvency ratio on the share prices of companies listed on LQ 45 Index | <font color = "#ff1493">Jurnal: The Indonesian Accounting Review</font> | <font color = "#32cd32">Publisher: </font></a>
            <br><br><br>










<font color = "#ff00ff" size = 5><b>Tahun Terbit 2014</b></font><br>  
             [1] <a href = "https://journal.perbanas.ac.id/index.php/jebav/article/view/356" target = "_blank" style = "text-decoration:none">Judul: The effect of fundamental and technical variables on stock price (Study on manufacturing companies listed in Indonesia Stock Exchange) | <font color = "#ff1493">Jurnal: Journal of Economics, Business, and Accountancy Ventura</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>






             





















             ''', unsafe_allow_html = True)




if pilih_topik == "Bankruptcy, Financial Distress, Financial Health on Stock Price":
    tab1.markdown("<h3 style='text-align: justify; color: #39ff14;'><center>Penelusuran Literatur berdasarkan Pengaruh Kinerja Keuangan Perusahaan (<i>Firm Financial Performance</i>) terhadap Harga Saham (<i>Stock Price</i>)</center></h5>", unsafe_allow_html=True)
    st.write('''
             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2018</b></font><br>  
             [1] <a href = "https://journal.uinjkt.ac.id/index.php/etikonomi/article/view/6559/pdf" target = "_blank" style = "text-decoration:none">Judul: Bankruptcy Prediction Models and Stock Prices of the Coal Mining Industry in Indonesia | <font color = "#ff1493">Jurnal: Etikonomi</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>



             ''', unsafe_allow_html = True)





with tab2:
   st.header(":blue[Lain-Lain]")
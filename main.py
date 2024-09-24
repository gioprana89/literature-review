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
    [":rainbow[Pengaruh Kinerja Keuangan Perusahaan (***Firm Financial Performance***) atau Rasio Finansial (***Financial Ratios***) terhadap Kapitalisasi Pasar (***Market Capitalization***)]", ":rainbow[Pengaruh Kinerja Keuangan Perusahaan (***Firm Financial Performance***) atau Rasio Finansial (***Financial Ratios***) terhadap Harga Saham (***Stock Price***)]", ":rainbow[Pengaruh Kebangkrutan (***Bankruptcy***) atau Kesulitan Keuangan (***Financial Distress***) atau Kesehatan Keuangan (***Financial Health***) Perusahaan terhadap Harga Saham (***Stock Price***)]", ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Harga Saham (***Stock Price***)]", ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Resiko Jatuhnya Harga Saham (***Stock Price Crash Risk***)]", ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Kinerja Perusahaan (***Firm Performance***) atau Kinerja Keuangan (***Financial Performance***)]", ":rainbow[Definisi Kinerja Keuangan (***Financial Performance***) Perusahaan atau Kinerja Perusahaan (***Firm Performance***)]", ":rainbow[Definisi ***Market Capitalization***]", ":rainbow[Definisi ***Stock Price Crash Risk***]", ":rainbow[Definisi ***Intellectual Capital***]",     ":rainbow[Bursa Efek Indonesia (***Indonesia Stock Exchange)***]",         ":rainbow[PT Kustodian Sentral Efek Indonesia ]"         ],)
   
   if pilih_topik == ":rainbow[Pengaruh Kinerja Keuangan Perusahaan (***Firm Financial Performance***) atau Rasio Finansial (***Financial Ratios***) terhadap Kapitalisasi Pasar (***Market Capitalization***)]":

    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Pengaruh Kinerja Keuangan Perusahaan (<i>Firm Financial Performance</i>) atau Rasio Finansial (<i>Financial Ratios</i>) terhadap Kapitalisasi Pasar (<i>Market Capitalization</i>)</center></h5>", unsafe_allow_html=True)
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
    

    st.markdown("<br><br><br><center><h2 style='text-align: justify; color: blue;'>Tabel Ringkasan Literatur</h2></center>", unsafe_allow_html=True)
    data_market_cap = pd.read_excel('Ringkasan Hasil Paper Market Capitalization.xlsx', index_col=0) 
    st.dataframe(data_market_cap)














if pilih_topik == ":rainbow[Pengaruh Kinerja Keuangan Perusahaan (***Firm Financial Performance***) atau Rasio Finansial (***Financial Ratios***) terhadap Harga Saham (***Stock Price***)]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Pengaruh Kinerja Keuangan Perusahaan (<i>Firm Financial Performance</i>) atau Rasio Finansial (<i>Financial Ratios</i>) terhadap Harga Saham (<i>Stock Price</i>)</center></h5>", unsafe_allow_html=True)
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




if pilih_topik == ":rainbow[Pengaruh Kebangkrutan (***Bankruptcy***) atau Kesulitan Keuangan (***Financial Distress***) atau Kesehatan Keuangan (***Financial Health***) Perusahaan terhadap Harga Saham (***Stock Price***)]":
    tab1.markdown("<h3 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Pengaruh Kebangkrutan (<i>Bankruptcy</i>) atau Kesulitan Keuangan (<i>Financial Distress</i>) atau Kesehatan Keuangan (<i>Financial Health</i>) Perusahaan terhadap Harga Saham (<i>Stock Price</i>)</center></h5>", unsafe_allow_html=True)
    st.write('''
             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2018</b></font><br>  
             [1] <a href = "https://journal.uinjkt.ac.id/index.php/etikonomi/article/view/6559/pdf" target = "_blank" style = "text-decoration:none">Judul: Bankruptcy Prediction Models and Stock Prices of the Coal Mining Industry in Indonesia | <font color = "#ff1493">Jurnal: Etikonomi</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>



             ''', unsafe_allow_html = True)












if pilih_topik == ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Harga Saham (***Stock Price***)]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Pengaruh <i>Intellectual Capital</i> terhadap Harga Saham (<i>Stock Price</i>)</center></h5>", unsafe_allow_html=True)
    st.write('''
             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2014</b></font><br>  
             [1] <a href = "https://register-jobfair.perbanas.ac.id/index.php/tiar/article/view/284" target = "_blank" style = "text-decoration:none">Judul: The impact of intellectual capital on stock price with financial performance as intervening variable of manufacturing listed in Indonesia Stock Exchange period 2008 – 2012 | <font color = "#ff1493">Jurnal: The Indonesian Accounting Review</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br>
             [2] <a href = "https://journal.perbanas.ac.id/index.php/tiar/article/view/331" target = "_blank" style = "text-decoration:none">Judul: The effect of intellectual capital on stock price and company value in manufacturing companies listed in Indonesia Stock Exchange 2008-2012 with size and leverage as moderating variables | <font color = "#ff1493">Jurnal: The Indonesian Accounting Review</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>


             ''', unsafe_allow_html = True)
    















if pilih_topik == ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Resiko Jatuhnya Harga Saham (***Stock Price Crash Risk***)]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Pengaruh <i>Intellectual Capital</i> terhadap Resiko Jatuhnya Harga Saham (<i>Stock Price Crash Risk</i>)</center></h5>", unsafe_allow_html=True)
    st.write('''
             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2022</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/JIC-09-2020-0306/full/html" target = "_blank" style = "text-decoration:none">Judul: Does intellectual capital have any influence on stock price crash risk? | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a>       
             <br><br><br>



             ''', unsafe_allow_html = True)
    







































if pilih_topik == ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Kinerja Perusahaan (***Firm Performance***) atau Kinerja Keuangan (***Financial Performance***)]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Pengaruh <i>Intellectual Capital</i> terhadap Kinerja Perusahaan (<i>Firm Performance</i>) atau Kinerja Keuangan (<i>Financial Performance</i>)</center></h5>", unsafe_allow_html=True)
    st.write('''
             


             



  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] <a href = "https://link.springer.com/article/10.1186/s43093-023-00208-1" target = "_blank" style = "text-decoration:none">Judul: The influence of intellectual capital on organizational performance | <font color = "#ff1493">Jurnal: Future Business Journal</font> | <font color = "#32cd32">Publisher: Springer</font></a>
             <br><br><br>




<font color = "#ff00ff" size = 5><b>Tahun Terbit 2020</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/JIC-09-2019-0225/full/html" target = "_blank" style = "text-decoration:none">Judul: Measures that matter: an empirical investigation of intellectual capital and financial performance of banking firms in Indonesia | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a>       
             [2] <a href = "https://journals.sagepub.com/doi/abs/10.1177/0972262920914108" target = "_blank" style = "text-decoration:none">Judul: Intellectual Capital and Profitability: Evidence from Indian Pharmaceutical Sector | <font color = "#ff1493">Jurnal: Vision: The Journal of Business Perspective</font> | <font color = "#32cd32">Publisher: SAGE Journals</font></a>       
             <br>


             

  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2017</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/JIC-01-2017-0014/full/html" target = "_blank" style = "text-decoration:none">Judul: Impact of intellectual capital on corporate performance: evidence from the Arab region | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a>
             <br><br><br>


             
  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2016</b></font><br>  
             [1] <a href = "https://journals.sagepub.com/doi/abs/10.1177/0972150916645703" target = "_blank" style = "text-decoration:none">Judul: Measuring Intellectual Capital and Its Impact on Financial Performance: Empirical Evidence from CNX Nifty Companies | <font color = "#ff1493">Jurnal: Global Business Review</font> | <font color = "#32cd32">Publisher: SAGE Journal</font></a>
             <br><br><br>




  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2015</b></font><br>  
             [1] <a href = "https://www.semanticscholar.org/reader/7a200641b5bb5f4d71067d5121528571e106bb4e" target = "_blank" style = "text-decoration:none">Judul: Impact of Intellectual capital on Financial Performance and Market Valuation of Firms in India | <font color = "#ff1493">Jurnal: International Letters of Social and Humanistic Sciences</font> | <font color = "#32cd32">Publisher: </font></a>
             <br><br><br>







  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2013</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/14691931311323887/full/html" target = "_blank" style = "text-decoration:none">Judul: Intellectual capital and financial performance: an evaluation of the Australian financial sector | <font color = "#ff1493">Jurnal: Measuring Business Excellence</font> | <font color = "#32cd32">Publisher: Emerald</font></a>
             <br><br><br>



  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2012</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/13683041211204671/full/html" target = "_blank" style = "text-decoration:none">Judul: The effect of intellectual capital on firm performance: an investigation of Iran insurance companies | <font color = "#ff1493">Jurnal: Measuring Business Excellence</font> | <font color = "#32cd32">Publisher: Emerald</font></a>
             <br><br><br>

             


  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2011</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/14691931111097944/full/html" target = "_blank" style = "text-decoration:none">Judul: The impact of intellectual capital on firms' market value and financial performance | <font color = "#ff1493">Jurnal: Measuring Business Excellence</font> | <font color = "#32cd32">Publisher: Emerald</font></a>
             <br><br><br>
















  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2009</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/14691930910977798/full/html" target = "_blank" style = "text-decoration:none">Judul: Indian software and pharmaceutical sector IC and financial performance | <font color = "#ff1493">Jurnal: Measuring Business Excellence</font> | <font color = "#32cd32">Publisher: Emerald</font></a>
             <br><br><br>





  <font color = "#ff00ff" size = 5><b>Tahun Terbit 2007</b></font><br>  
             [1] <a href = "http://americanscholarspress.us/journals/IMR/pdf/IMR-2-2007/v3n207-art2.pdf" target = "_blank" style = "text-decoration:none">Judul: The Impact of Intellectual Capital on Investors’ Capital Gains on Shares: An Empirical Investigation of Thai Banking, Finance & Insurance Sector | <font color = "#ff1493">Jurnal: International Management Review</font> | <font color = "#32cd32">Publisher: </font></a><br><br><br>  











<font color = "#ff00ff" size = 5><b>Tahun Terbit 2005</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/14691930510592771/full/html" target = "_blank" style = "text-decoration:none">Judul: An empirical investigation of the relationship between intellectual capital and firms’ market value and financial performance | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a><br><br><br>  


             

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2003</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/14691930310487806/full/html" target = "_blank" style = "text-decoration:none">Judul: Intellectual capital and traditional measures of corporate performance | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a><br>
             [2] <a href = "https://www.emerald.com/insight/content/doi/10.1108/10222529200300003/full/html" target = "_blank" style = "text-decoration:none">Judul: Testing the relationship between intellectual capital and a company’s performance: Evidence from South Africa | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a><br><br><br>  













             ''', unsafe_allow_html = True)
    




























































if pilih_topik == ":rainbow[Definisi Kinerja Keuangan (***Financial Performance***) Perusahaan atau Kinerja Perusahaan (***Firm Performance***)]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Definisi Kinerja Keuangan (<i>Financial Performance</i>) Perusahaan atau Kinerja Perusahaan (<i>Firm Performance</i>)</center></h5>", unsafe_allow_html=True)


























































if pilih_topik == ":rainbow[Definisi ***Market Capitalization***]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Definisi <i>Market Capitalization</i>", unsafe_allow_html=True)

    st.write('''
             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] <a href = "https://www.tandfonline.com/doi/full/10.1080/23322039.2023.2252652" target = "_blank" style = "text-decoration:none">Judul: Six-factor plus intellectual capital in the capital asset pricing model and excess stock return: Empirical evidence in emerging stock markets | <font color = "#ff1493">Jurnal: Cogent Economics & Finance</font> | <font color = "#32cd32">Publisher: Taylor & Francis</font></a>       
             <br><br><br>

             

             














<font color = "#ff00ff" size = 5><b>Tahun Terbit 2022</b></font><br>  
             [1] <a href = "https://link.springer.com/article/10.1007/s42521-022-00066-6" target = "_blank" style = "text-decoration:none">Judul: Persistence in daily returns of stocks with highest market capitalization in the Indian market | <font color = "#ff1493">Jurnal:  Digital Finance</font> | <font color = "#32cd32">Publisher: Springer</font></a>       
            

             
<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

         The choice of stocks in our analysis is under the assumption that, for any stock to be included in the index, it has to have the market power to influence public opinion, credibility amongst stakeholders, higher and steady returns, therefore making it the top performer amongst the sector to which it belongs (Gompers & Metrick, 2001). Within the NIFTY index, we have chosen ten stocks with highest market capitalisation as they are perceived to possess the aforementioned characteristics. This will be useful to understand market dynamics and investor behaviour. The asset returns of stocks in NIFTY index used in this study are: ICICI BANK LTD., BHARTI AIRTEL LTD., WIPRO LTD., HERO MOTO CORP LTD., NMDC LTD., CIPLA LTD., CAIRN INDIA LTD., UNITED SPIRITS LTD., POWER FINANCE CORPN. LTD. and OIL INDIA LTD. The daily returns of stocks over a period of ten years from 2005 to 2015 are used in the study. The returns are calculated as the differences in log price and are used for the following analyses
       

</font>
</font>
</p>	





























<font color = "#ff00ff" size = 5><b>Tahun Terbit 2020</b></font><br>  
             [1] <a href = "https://www.tandfonline.com/doi/full/10.1080/23311975.2020.1750332" target = "_blank" style = "text-decoration:none">Judul: Corporate governance on intellectual capital disclosure and market capitalization | <font color = "#ff1493">Jurnal: Cogent Business & Management</font> | <font color = "#32cd32">Publisher: Taylor & Francis</font></a>       
            

             
<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

             Market capitalization in a company refers to the number of shares outstanding multiplied by the market price per share (Abdelkarim & Almumani, 2018). In general, the benchmark to measure the value of a company is market capitalization or more generally, wealth is created by a company that represents the collective value of a company or stock. Now, market capitalization has become a universally accepted indicator of business valuation (Abdelkarim & Almumani, 2018). It represents the aggregate value of the company or stock. Capital formation is an integral part of economic growth and development and plays an important role in economic theory of production and distribution (Abraham & Ofosu, 2018). Capital accumulation is assumed to facilitate faster economic growth. Stock market growth is measured by market capitalization.

       

</font>
</font>
</p>	


<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

        
           
             Market capitalization is the value of a company traded on the stock market and this makes it one of the factors considered by investors in making investment decisions. There are, however, several variables influencing the high or low market capitalization and an example is the information published concerning the implementation of corporate governance. The basic framework to predict the reaction of the stock market to this information is explained through the use of signaling theory (Woudstra et al., 2017). Several existing studies have confirmed that stock market rewards companies with more comprehensive corporate governance with high values but there are limited studies on the reasons for this action (Pae & Choi, 2011).


</font>
</font>
</p>	






             

 [2] <a href = "https://www.tandfonline.com/doi/full/10.1080/1540496X.2018.1509790" target = "_blank" style = "text-decoration:none">Judul: The Influences of Book-to-Price Ratio and Stock Capitalization on Value-at-Risk Estimation in Taiwan Stock Market | <font color = "#ff1493">Jurnal: Cogent Business & Management</font> | <font color = "#32cd32">Publisher: Taylor & Francis</font></a>       
            

             
<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

       In general, a company with smaller market cap has higher bankruptcy risk than the company with larger market cap. Additionally, the smaller cap companies generally has less stable earnings than the larger cap ones. Consequently, for sustaining these risks, the smaller cap stocks should require higher expected returns than the larger cap ones

</font>
</font>
</p>	








             



<br><br>

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2009</b></font><br>  
             [1] <a href = "https://journals.sagepub.com/doi/abs/10.1509/jmkg.73.6.119" target = "_blank" style = "text-decoration:none">Judul: Expanding the Role of Marketing: From Customer Equity to Market Capitalization | <font color = "#ff1493">Jurnal: Journal of Marketing</font> | <font color = "#32cd32">Publisher: SAGE Journal</font></a>       
            

             
<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

       Calculating MC (Market Capitalization). A popular measure of firm valuation is MC, which is based on the stock price of the firm. Under this approach, firm value is computed as the product of the stock price of the firm and the number of outstanding shares in the market. According to the efficient market theory, stock prices incorporate all information about the expected future earnings (Fama 1970). Thus, measures based on stock price can be assumed to be a good proxy for the longterm performance of the firm.

</font>
</font>
</p>	






















             ''', unsafe_allow_html = True)

































if pilih_topik == ":rainbow[Definisi ***Stock Price Crash Risk***]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Definisi <i>Stock Price Crash Risk</i>", unsafe_allow_html=True)
































if pilih_topik == ":rainbow[Definisi ***Intellectual Capital***]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Definisi <i>Intellectual Capital</i>", unsafe_allow_html=True)

    
    st.write('''
             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] <a href = "https://www.tandfonline.com/doi/full/10.1080/23322039.2023.2252652" target = "_blank" style = "text-decoration:none">Judul: Six-factor plus intellectual capital in the capital asset pricing model and excess stock return: Empirical evidence in emerging stock markets | <font color = "#ff1493">Jurnal: Cogent Economics & Finance</font> | <font color = "#32cd32">Publisher: Taylor & Francis</font></a>       
             <br><br><br>


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2018</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/JIC-09-2016-0091/full/html" target = "_blank" style = "text-decoration:none">Judul: Intellectual capital efficiency and corporate book value: evidence from Nigerian economy | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a>       
             <br><br><br>

             




<font color = "#ff00ff" size = 5><b>Tahun Terbit 2007</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/14691930710715088/full/html" target = "_blank" style = "text-decoration:none">Judul: The intellectual capital performance of the Indian banking sector | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a>       
             <br><br><br>

             
<font color = "#ff00ff" size = 5><b>Tahun Terbit 2005</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/00251740510626254/full/html" target = "_blank" style = "text-decoration:none">Judul: Linking intellectual capital and intellectual property to company performance | <font color = "#ff1493">Jurnal: Journal of Intellectual Capital</font> | <font color = "#32cd32">Publisher: Emerald</font></a>       
             <br><br><br>

             










             ''', unsafe_allow_html = True)














if pilih_topik == ":rainbow[Bursa Efek Indonesia (***Indonesia Stock Exchange)***]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur di Bursa Efek Indonesia (<i>Indonesia Stock Exchange</i>)", unsafe_allow_html=True)

    




if pilih_topik == ":rainbow[PT Kustodian Sentral Efek Indonesia ]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur di PT Kustodian Sentral Efek Indonesia", unsafe_allow_html=True)

    




































with tab2:
   st.header(":blue[Lain-Lain]")
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
     st.markdown("<a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>STATKOMAT</b></font></a> | <a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>YOUTUBE</b></font></a> | <a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>LITERATURE REVIEW</b></font></a> | <a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>LIST OF PAPERS</b></font></a> | <a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>PUBLICATION</b></font></a> | <a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>PLS-SEM</b></font></a> | <a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>MY SOFTWARE</b></font></a> | <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>MY BOOK</b></font></a> | <a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>UGI</b></font></a> | <a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>SHINY</b></font></a> | <a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>INDCOMP</b></font></a> | <a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>FIGSHARE</b></font></a> | <a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>GITHUB</b></font></a>", unsafe_allow_html=True)





      
   st.header(":blue[Penelusuran Literatur]")
   
   pilih_topik = st.radio(
    "Pilih Topik: ",
    [":rainbow[Pengaruh Kinerja Keuangan Perusahaan (***Firm Financial Performance***) atau Rasio Finansial (***Financial Ratios***) terhadap Kapitalisasi Pasar (***Market Capitalization***)]", ":rainbow[Pengaruh Kinerja Keuangan Perusahaan (***Firm Financial Performance***) atau Rasio Finansial (***Financial Ratios***) terhadap Harga Saham (***Stock Price***)]", ":rainbow[Pengaruh Kebangkrutan (***Bankruptcy***) atau Kesulitan Keuangan (***Financial Distress***) atau Kesehatan Keuangan (***Financial Health***) Perusahaan terhadap Harga Saham (***Stock Price***)]", ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Harga Saham (***Stock Price***)]", ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Resiko Jatuhnya Harga Saham (***Stock Price Crash Risk***)]", ":rainbow[Pengaruh ***Intellectual Capital*** terhadap Kinerja Perusahaan (***Firm Performance***) atau Kinerja Keuangan (***Financial Performance***)]", ":rainbow[Pengaruh ***Financial Ratio*** terhadap ***Stock Trading Volume***]", ":rainbow[Pengaruh ***Stock Trading Volume*** terhadap Harga Saham (***Stock Price***)]", ":rainbow[Definisi Kinerja Keuangan (***Financial Performance***) Perusahaan atau Kinerja Perusahaan (***Firm Performance***)]", ":rainbow[Definisi ***Market Capitalization***]", ":rainbow[Definisi ***Stock Price Crash Risk***]", ":rainbow[Definisi ***Intellectual Capital***]",  ":rainbow[Definisi ***Stock Trading Volume***]",     ":rainbow[Bursa Efek Indonesia (***Indonesia Stock Exchange)***]",         ":rainbow[PT Kustodian Sentral Efek Indonesia ]" , ":rainbow[Katadata]"        ],)
   
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


             

 <font color = "#ff00ff" size = 5><b>Tahun Terbit 2020</b></font><br>  
             [1] <a href = "https://journal.jis-institute.org/index.php/ijfr/article/view/280" target = "_blank" style = "text-decoration:none">Judul: The Effect Of Return On Assets, Return On Equity, Net Profit Margin, Earning Per Share, And Operating Profit Margin On Stock Prices Of Banking Companies In Indonesia Stock Exchange | <font color = "#ff1493">Jurnal: International Journal of Finance Research</font> | <font color = "#32cd32">Publisher: </font></a>
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
             


             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2024</b></font><br>  
             [1] <a href = "https://link.springer.com/article/10.1007/s11294-024-09885-2" target = "_blank" style = "text-decoration:none">Judul: Investor Attention and Stock Liquidity in the Chinese Market | <font color = "#ff1493">Jurnal:   International Advances in Economic Research </font> | <font color = "#32cd32">Publisher: Springer</font></a>       
            

             
<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

        Control variables encompass stock market capitalization (MktCap), calculated as the product of stock price and outstanding shares
      

</font>
</font>
</p>	












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






[2] <a href = "https://www.sciencedirect.com/science/article/pii/S2214845022000199" target = "_blank" style = "text-decoration:none">Judul: How do market capitalization and intellectual capital determine industrial investment? | <font color = "#ff1493">Jurnal:  Borsa Istanbul Review</font> | <font color = "#32cd32">Publisher: Elsevier</font></a>       
            


<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

        Market capitalization and intellectual capital can be understood as two main that can play a dynamic role in multiple organizational decisions. Given that, the current study examines the role of market capitalization and intellectual capital in determining corporate investment decisions. The statistical analysis first reveals the positive significant effect of market capitalization on investment decisions because of the availability of sufficient funds for investment. It then substantiates the significant role of human capital, structural capital, and capital employed efficiency in protecting industrial investment. The empirical findings offer policy implications on how market capitalization (MC) and intellectual capital (IC) promote investment decisions. Among others, the volume of market capitalization by firms is a vital financial factor that allows them to deliberately make some investments (Armstrong & Vashishtha, 2012). Therefore, this study explores the impact of market capitalization (MC) and IC on industrial investment. To measure industrial investment, this study uses the ratio of a firm's total expenses to acquire capital assets to total assets (Chen et al., 2019). This ratio further indicates the firm's intention to expand its existing business operations by acquiring these assets. The main explanatory variables include MC, the cumulative market worth of a firm, which demonstrates the total monetary value of a firm's stocks. Consequently, we make the following contributions to the existing literature. First, this study supplements empirical evidence regarding the importance of MC in industrial investment. Industrial enterprises that have higher market capitalization enjoy positive investment growth. In addition, the empirical analysis demonstrates the investment behavior of firms that invest more in the development of their intellectual capital (IC). These firms have a positive attitude toward capital investment. Among other things, market capitalization shows that the market value of a company can help to enhance the volume of business by establishing more PPE activities. A company with more market capitalization has few financial problems and has enough financial resources for investment (Kuvshinov & Zimmermann, 2021). Additionally, these enterprises can collect more funds through the issuance of more stocks due to a good market reputation. When a company has high market capital, it can obtain funds more easily, which has positive spillover on engaging in physical projects. In addition to financing, market capitalization shows the market reputation of enterprises and helps in obtaining other benefits, for example, low information asymmetry between shareholders and firm managers, ease in trade activities (both purchasing and selling), and a first preference of wise brains (Mukherjee et al., 2018). In view of the cumulative benefits of market capital, high market capitalization provides important stimulus for capital investment.

       

</font>
</font>
</p>	
	







<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

        Using financial resources, firms make investments to expand their existing productive operations (Kumar & Ranjani, 2018). Greater availability of funds enables industries to invest in new ventures. These notions show the importance of finance in the expansion of industrial investment. Market capitalization is an important financial source through which enterprises finance their multiple operations (Buchuk et al., 2014). It also indicates the value of a company in the financial market and typically plays a vital role in multiple business decisions. In this regard, Polk and Sapienza (2009) studied the relationship between stock exchange performance and corporate investment. Testing the catering theory, they documented a positive relationship between discretionary accruals and abnormal investment, indicating the significance of the stock market in investmentrelated decisions. Bakke and Whited (2010) also confirm the role of the stock market in industrial investment. Despite the large number of studies that describe the potential role of funds in determining industrial investment (Hugonnier et al., 2015; Nnadi et al., 2021; Shiau et al., 2018; Yang et al., 2017), no study has clearly illustrated the linkages between market capitalization and firm investment decisions. Thus, our study is an early attempt to explore this relationship.

       

</font>
</font>
</p>	


<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

        H1. There exists a positive and significant connection between high market capitalization and industrial investment.

        H2a. HCE is positively and significantly related to industrial investment decisions.

        H2b. There exists a positive significant correlation between SCE and investment decisions.

        H2c. : CEE has a significant positive impact on corporate investment decisions.

       

</font>
</font>
</p>	



<p style="text-align:justify">
<font style="color:#DAA520; text-align: justify; font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', sans-serif;">
        <font size = 4>

        Market capitalization (MC) is an explanatory variable, calculated by multiplying the total shares outstanding by the market value per share. It shows the financial wealth of a company in an open market. MC further shows the total funds available to a company to finance its business operations. Dias (2013) is based on a similar calculation of MC

       

</font>
</font>
</p>	







<font color = "#ff00ff" size = 5><b>Tahun Terbit 2021</b></font><br>  
             [1] <a href = "https://www.sciencedirect.com/science/article/pii/S2214785320363756" target = "_blank" style = "text-decoration:none">Judul: Market capitalization: Pre and post COVID-19 analysis | <font color = "#ff1493">Jurnal: Materials Today: Proceedings</font> | <font color = "#32cd32">Publisher: Elsevier</font></a>       
             <br><br><br>

             

















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














































if pilih_topik == ":rainbow[Pengaruh ***Financial Ratio*** terhadap ***Stock Trading Volume***]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Pengaruh <i>Financial Ratio</i> terhadap <i>Stock Trading Volume</i>", unsafe_allow_html=True)


    st.write('''
             

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] <a href = "https://www.inovatus.es/index.php/ejbsos/article/view/1867" target = "_blank" style = "text-decoration:none">Judul: The Influence of Fundamental Factors on Stock Trading Volume and Share Prices of Conventional Finance Companies Listed on the Indonesian Stock Exchange | <font color = "#ff1493">Jurnal: European Journal of Business Startups and Open Society</font> | <font color = "#32cd32">Publisher: </font></a>       
             [2] <a href = "https://journal.um-surabaya.ac.id/index.php/balance/article/view/17671" target = "_blank" style = "text-decoration:none">Judul: The Effect Of Retained Earnings On Trading Volume Activity (TVA) With Return On Assets As A Moderation Variable | <font color = "#ff1493">Jurnal: BALANCE : Economic, Business, Management, and Accounting Journal</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>
             





<font color = "#ff00ff" size = 5><b>Tahun Terbit 2022</b></font><br>  
             [1] <a href = "https://www.e-journal.trisakti.ac.id/index.php/ijca/article/view/15155/8898" target = "_blank" style = "text-decoration:none">Judul: FACTORS THAT DETERMINE STOCK RETURNS MODERATED BY STOCK TRADING VOLUME IN MANUFACTURING COMPANIES LISTED ON THE INDONESIAN STOCK EXCHANGEFOR THE 2017-2021 PERIOD | <font color = "#ff1493">Jurnal: International Journal of Contemporary Accounting</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>




<font color = "#ff00ff" size = 5><b>Tahun Terbit 2020</b></font><br>  
             [1] <a href = "https://jurnal.unimed.ac.id/2012/index.php/jcrs/article/view/18530/13574" target = "_blank" style = "text-decoration:none">Judul: THE XBRL TECHNOLOGYAND MARKET EFFICIENCY IN BANKING COMPANIES LISTED ON THE INDONESIA STOCK EXCHANGE (IDX) | <font color = "#ff1493">Jurnal: Journal of Community Research and Service</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>









<font color = "#ff00ff" size = 5><b>Tahun Terbit 2019</b></font><br>  
             [1] <a href = "https://d1wqtxts1xzle7.cloudfront.net/65025226/Jurnal_Trading_Volume_Activity-libre.pdf?1606281161=&response-content-disposition=inline%3B+filename%3DFactors_Affecting_Trading_Volume_Activit.pdf&Expires=1727179817&Signature=F-2kexVh2Hjbfb6bgVnb9~Tq66jhvTTsU7UXtdunI9w4FSMY~U1x8Iu3HpkBtNdDvTY7eM7HRWV~oetgOrdl0qTujtcvlZXkVryCPDRoqGW8wL1cBTHrNuYWbKU76bZzY5IZ-SlhgaJ2N-MLwGD20uQE-wWCnR9IYLjIb2Q1ISp5YhnkMlxmsZhhdCClo5PTGJo~MD8dvOByTvp2Ibm-xHY4G5Wl32OMo0iY7jErJAMiNUKj3jzI0S-TpREnKUirXP0Ic6tJu2Nc0hTzncLSjfFf7KjY5SCdOLxqn39nyY8BF2T~LZxggMMbuM7WCoI1YUEgCvdflTjD1MW36jJ7JQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA" target = "_blank" style = "text-decoration:none">Judul: Factors Affecting Trading Volume Activity with Tobin’s Q as an Intervening Variable LQ45 Company in Indonesia Stock Exchange | <font color = "#ff1493">Jurnal: IOSR Journal of Business and Management (IOSR-JBM)</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>




<font color = "#ff00ff" size = 5><b>Tahun Terbit 2017</b></font><br>  
             [1] <a href = "https://www.tandfonline.com/doi/abs/10.1080/10599231.2017.1346408" target = "_blank" style = "text-decoration:none">Judul: The Role of Financial Ratios in the Variance of Stock Trading Volume in Emerging Stock Markets | <font color = "#ff1493">Jurnal: Journal of Asia-Pacific Business</font> | <font color = "#32cd32">Publisher: Taylor & Francis</font></a>       
             [2] <a href = "http://www.jbrc.pk/volumes/Paper5-7.pdf" target = "_blank" style = "text-decoration:none">Judul: Determinants of Trading Volume in Karachi Stock Market | <font color = "#ff1493">Jurnal: Jinnah Business Review</font> | <font color = "#32cd32">Publisher: </font></a>       
             [3] <a href = "https://ojs.unud.ac.id/index.php/akuntansi/article/view/29958/21555" target = "_blank" style = "text-decoration:none">Judul: Pengaruh Informasi Arus Kas, Laba Bersih dan Pengungkapan Corporate Social Responsibility Pada Volume Perdagangan Saham  | <font color = "#ff1493">Jurnal: E-Jurnal Akuntansi Universitas Udayana</font> | <font color = "#32cd32">Publisher: </font></a>       
                    





<font color = "#ff00ff" size = 5><b>Tahun Terbit 2015</b></font><br>  
             [1] <a href = "https://www.ccsenet.org/journal/index.php/ibr/article/view/48011" target = "_blank" style = "text-decoration:none">Judul: The Effect of Financial Indicators on Trading Volume of the Listed Companies on the Tehran Stock Exchange | <font color = "#ff1493">Jurnal: International Business Research</font> | <font color = "#32cd32">Publisher: </font></a>                  
             [2] <a href = "https://www.sciencedirect.com/science/article/pii/S1877042815054580" target = "_blank" style = "text-decoration:none">Judul: The Effect of Return on Equity (ROE) and Return on Investment (ROI) on Trading Volume | <font color = "#ff1493">Jurnal: Procedia - Social and Behavioral Sciences</font> | <font color = "#32cd32">Publisher: Elsevier</font></a>       
             <br><br><br>








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




























if pilih_topik == ":rainbow[Definisi ***Stock Trading Volume***]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Definisi <i>Stock Trading Volume</i>", unsafe_allow_html=True)


    st.write('''
             





<font color = "#ff00ff" size = 5><b>Tahun Terbit 2021</b></font><br>  
             [1] <a href = "https://www.emerald.com/insight/content/doi/10.1108/JDQS-01-2021-0003/full/html" target = "_blank" style = "text-decoration:none">Judul: The short-term mean reversion of stock price and the change in trading volume | <font color = "#ff1493">Jurnal: Journal of Derivatives and Quantitative Studies</font> | <font color = "#32cd32">Publisher: Emerald</font></a>       
             [2] <a href = "https://www.igbr.org/wp-content/Journals/2021/GJAF_Vol_5_No_2_2021.pdf#page=27" target = "_blank" style = "text-decoration:none">Judul: RELATIONSHIPS BETWEEN STOCK PRICE, TRADING VOLUME, AND BID-ASK SPREAD ON THE US STOCK EXCHANGE: AN EMPIRICAL INVESTIGATION | <font color = "#ff1493">Jurnal: Global Journal of Accounting and Finance</font> | <font color = "#32cd32">Publisher: </font></a>       
             <br><br><br>

<font color = "#ff00ff" size = 5><b>Tahun Terbit 2011</b></font><br>  
             [1] <a href = "https://onlinelibrary.wiley.com/doi/10.1111/j.1475-6803.2010.01285.x" target = "_blank" style = "text-decoration:none">Judul: THE FUNDAMENTAL DETERMINANTS OF TRADING VOLUME REACTION TO FINANCIAL INFORMATION: EVIDENCE AND IMPLICATIONS FOR EMPIRICAL CAPITAL MARKET RESEARCH | <font color = "#ff1493">Jurnal: The Journal of Financial Research</font> | <font color = "#32cd32">Publisher: WILEY</font></a>       
             <br><br><br>











             ''', unsafe_allow_html = True)






































































if pilih_topik == ":rainbow[Pengaruh ***Stock Trading Volume*** terhadap Harga Saham (***Stock Price***)]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur berdasarkan Pengaruh <i>Stock Trading Volume</i> terhadap Harga Saham (<i>Stock Price</i>)", unsafe_allow_html=True)


    st.write('''
             


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2024</b></font><br>  
             [1] <a href = "https://www.researchgate.net/publication/380553674_Fundamental_Analysis_and_Trading_Volume_on_Stock_Prices_with_Company_Size_as_a_Control_Variable#fullTextFileContent" target = "_blank" style = "text-decoration:none">Judul: Fundamental Analysis and Trading Volume on Stock Prices with Company Size as a Control Variable | <font color = "#ff1493">Jurnal: East Asian Journal of Multidisciplinary Research (EAJMR)</font> | <font color = "#32cd32">Publisher: </font></a>     


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] <a href = "http://journal.unmasmataram.ac.id/index.php/GARA/article/view/560" target = "_blank" style = "text-decoration:none">Judul: PENGARUH FAKTOR TEKNIKAL DAN FUNDAMENTAL TERHADAP HARGA SAHAM (STUDI KASUS PERUSAHAAN FOOD AND BEVERAGE DI BEI TAHUN 2019-2021) | <font color = "#ff1493">Jurnal: Jurnal Ganec Swara</font> | <font color = "#32cd32">Publisher: </font></a>       
             [2] <a href = "https://ictmt.stiepari.org/index.php/journal/article/view/117" target = "_blank" style = "text-decoration:none">Judul: The Effect Of Technical And Fundamental Analysis On Stock Prices | <font color = "#ff1493">Jurnal: Proceeding of International Conference on Digital Advance Tourism, Management and Technology 2023</font> | <font color = "#32cd32">Publisher: </font></a>  
             [3] <a href = "https://www.inovatus.es/index.php/ejbsos/article/view/1867" target = "_blank" style = "text-decoration:none">Judul: The Influence of Fundamental Factors on Stock Trading Volume and Share Prices of Conventional Finance Companies Listed on the Indonesian Stock Exchange | <font color = "#ff1493">Jurnal: EUROPEAN JOURNAL OF BUSINESS STARTUPS AND OPEN SOCIETY</font> | <font color = "#32cd32">Publisher: </font></a>  


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2018</b></font><br>  
             [1] <a href = "https://www.ijtef.org/index.php?m=content&c=index&a=show&catid=96&id=977" target = "_blank" style = "text-decoration:none">Judul: How Fundamental Analysis and Technical Analysis Determining the Stock Price: Case Study of Mining Company Listed on the Indonesia Stock Exchange | <font color = "#ff1493">Jurnal: International Journal of Trade, Economics and Finance</font> | <font color = "#32cd32">Publisher: </font></a>       









             ''', unsafe_allow_html = True)

















































if pilih_topik == ":rainbow[Bursa Efek Indonesia (***Indonesia Stock Exchange)***]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur di Bursa Efek Indonesia (<i>Indonesia Stock Exchange</i>)", unsafe_allow_html=True)

    
    st.write('''
             

             



<font color = "#ff00ff" size = 5><b>Tahun Terbit 2023</b></font><br>  
             [1] Judul: IDX Statistics 2023 | <a href = "https://www.idx.co.id/Media/e3ppd3kq/idx_4th-quarter_2023.pdf" target = "_blank" style = "text-decoration:none">Link IDX</a> | <a href = "https://drive.google.com/file/d/1UugU78sMNF5RE_Beppwj9WEq-rA9Xr3d/view?usp=sharing" target = "_blank" style = "text-decoration:none">Link Drive</a>








<font color = "#ff00ff" size = 5><b>Tahun Terbit 2022</b></font><br>  
             [1] Judul: IDX Statistics 2022 | <a href = "https://www.idx.co.id/Media/5pfnt4gg/idx_yearly_statistics_2022.pdf" target = "_blank" style = "text-decoration:none">Link IDX</a> | <a href = "https://drive.google.com/file/d/1otJPxPA4WwHujmrxoGN7gE_MJOkxB3cd/view?usp=sharing" target = "_blank" style = "text-decoration:none">Link Drive</a>

             
<font color = "#ff00ff" size = 5><b>Tahun Terbit 2021</b></font><br>  
             [1] Judul: IDX Statistics 2021 | <a href = "https://www.idx.co.id/Media/11330/idx_annually-statistic_2021.pdf" target = "_blank" style = "text-decoration:none">Link IDX</a> | <a href = "https://drive.google.com/file/d/1FeiWncTwp2h1ptvgTNEMSQ-UeLG3GxiU/view?usp=sharing" target = "_blank" style = "text-decoration:none">Link Drive</a>


<font color = "#ff00ff" size = 5><b>Tahun Terbit 2020</b></font><br>  
             [1] Judul: IDX Statistics 2020 | <a href = "" target = "_blank" style = "text-decoration:none">Link IDX</a> | <a href = "https://drive.google.com/file/d/1cqGdUvqILtWKuU4qnyHKrf5j9ZJXqFtQ/view?usp=sharing" target = "_blank" style = "text-decoration:none">Link Drive</a>






             ''', unsafe_allow_html = True)

























if pilih_topik == ":rainbow[PT Kustodian Sentral Efek Indonesia ]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur di PT Kustodian Sentral Efek Indonesia", unsafe_allow_html=True)

    





















if pilih_topik == ":rainbow[Katadata]":
    tab1.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Penelusuran Literatur di Katadata", unsafe_allow_html=True)

    














with tab2:
   st.header(":blue[Lain-Lain]")

d1 = "The stock market is a dynamic and complex financial system where investors buy and sell securities, such as stocks and bonds, representing ownership in companies. It serves as a platform for businesses to raise capital and for individuals and institutions to invest and grow their wealth. The stock market plays a significant role in the global economy, providing liquidity, facilitating price discovery, and enabling the allocation of resources to productive enterprises."
d2 = "Investing in the stock market involves assessing the financial health, performance, and growth potential of companies. Investors analyze various factors, including earnings reports, industry trends, macroeconomic indicators, and management strategies, to make informed decisions. They aim to buy stocks at favorable prices and benefit from capital appreciation or receive dividends as the company's profitability improves. However, the stock market is also subject to volatility and fluctuations influenced by economic conditions, investor sentiment, geopolitical events, and market psychology."
d3 = "The stock market operates through exchanges, such as the New York Stock Exchange (NYSE) and the NASDAQ, where buyers and sellers come together to trade securities. These exchanges provide a transparent and regulated marketplace where transactions are executed electronically. Stock market participants include individual retail investors, institutional investors such as mutual funds and pension funds, as well as high-frequency traders and market makers. The stock market also facilitates trading through brokerage firms, online trading platforms, and investment vehicles like exchange-traded funds (ETFs)."
d4 = "Market indices, such as the S&P 500, Dow Jones Industrial Average (DJIA), and NASDAQ Composite, track the performance of specific groups of stocks and serve as benchmarks for overall market performance. These indices provide insights into the health of the stock market and are often used to evaluate investment strategies and compare portfolio returns. Market participants and analysts closely monitor stock market indices, economic indicators, and financial news to anticipate market trends and make informed investment decisions."
d5 = "The stock market plays a crucial role in capital formation, facilitating the flow of funds from savers to companies seeking investment capital. It allows companies to raise funds for research and development, expansion, and innovation, driving economic growth and job creation. The stock market also offers individuals an opportunity to participate in the growth and success of companies and build long-term wealth. However, investing in the stock market carries risks, and individuals should consider their financial goals, risk tolerance, and seek professional advice before making investment decisions."

d6 = "An IP lawyer, also known as an Intellectual Property lawyer, plays a crucial role in protecting and enforcing intellectual property rights. These legal professionals specialize in areas such as patents, trademarks, copyrights, and trade secrets. With the rapid advancements in technology and the global marketplace, the need for skilled IP lawyers has become more critical than ever. IP lawyers assist individuals, businesses, and organizations in navigating the complex landscape of intellectual property laws, ensuring that their innovations and creative works are safeguarded from unauthorized use and infringement."
d7 = "IP lawyers often work closely with inventors, artists, entrepreneurs, and corporate entities to identify, secure, and enforce their intellectual property rights. They help clients file patent applications to protect novel inventions, trademarks to safeguard brand identities, and copyrights to secure original artistic and literary works. These professionals also provide counsel on licensing agreements, technology transfers, and intellectual property disputes. Their expertise extends to conducting comprehensive searches and due diligence to assess the viability and potential risks associated with intellectual property assets."
d8 = "In addition to protecting intellectual property rights, IP lawyers also play an essential role in defending their clients against infringement claims. They analyze complex legal issues, assess the validity of patents and trademarks, and formulate effective strategies to respond to allegations of intellectual property violations. IP lawyers may engage in litigation, negotiation, or alternative dispute resolution methods to resolve conflicts and protect their clients' interests. Their knowledge of intellectual property laws, combined with their litigation skills, allows them to advocate for their clients in courtrooms and help secure favorable outcomes."
d9 = "Furthermore, IP lawyers are at the forefront of emerging issues and challenges in intellectual property law. They stay abreast of new legislation, international treaties, and court decisions that shape the legal landscape surrounding intellectual property. This continuous learning and adaptation are crucial in an ever-evolving digital age where issues such as online piracy, software patents, and data privacy pose unique challenges. IP lawyers also provide guidance on the proper use and protection of intellectual property assets in the digital realm, including social media, e-commerce platforms, and online content distribution."
d10 = "The role of an IP lawyer extends beyond legal expertise; they are also advisors, strategists, and advocates for innovation and creativity. By fostering an environment that values and protects intellectual property, these professionals contribute to economic growth, technological advancement, and the promotion of arts and culture. Whether it's helping startups secure their ideas or assisting established corporations in protecting their brands, IP lawyers play a vital role in shaping the future of intellectual property rights and fostering a climate of innovation and respect for creativity."

# d1 = d1.split(". ")
# d2 = d2.split(". ")
# d3 = d3.split(". ")
# d4 = d4.split(". ")
# d5 = d5.split(". ")
# d6 = d6.split(". ")
# d7 = d7.split(". ")
# d8 = d8.split(". ")
# d9 = d9.split(". ")
# d10 = d10.split(". ")

# documents = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10
# print(len(documents))

delimiter = "."
# Open the file in read mode
with open("dataset.txt", "r") as file:
    # Read the contents of the file
    lines = file.read()

# Print the data
documents = lines.split(delimiter)
print(documents[10])

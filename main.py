from requests import Request, Session
import json
import pprint


#----------------------------------------------------------------------------------

from tkinter import *

lst = [
        'BTC', 'ETH', 'USDT', 'USDC', 'BNB', 'XRP', 'ADA', 'BUSD', 'SOL',
    'DOGE', 'DOT', 'AVAX', 'TRX', 'SHIB', 'DAI', 'MATIC', 'CRO', 'LEO',
    'LTC', 'NEAR', 'FTT', 'BCH', 'UNI', 'LINK', 'XLM', 'ATOM', 'ALGO',
    'XMR', 'FLOW', 'ETC', 'APE', 'MANA', 'HBAR', 'EGLD', 'VET', 'ICP',
    'FIL', 'SAND', 'XTZ', 'MKR', 'ZEC', 'KCS', 'THETA', 'CAKE', 'EOS',
    'AXS', 'TUSD', 'GRT', 'UST', 'AAVE', 'KLAY', 'HT', 'RUNE', 'HNT',
    'BTT', 'BSV', 'MIOTA', 'USDP', 'XEC', 'FTM', 'GMT', 'USDN', 'QNT',
    'NEXO', 'STX', 'OKB', 'NEO', 'WAVES', 'CHZ', 'CVX', 'KSM', 'ZIL',
    'ENJ', 'DASH', 'CELO', 'CRV', 'LRC', 'GALA', 'PAXG', 'BAT', 'GNO',
    'AMP', 'ONE', 'XDC', 'AR', 'XEM', 'MINA', 'DCR', 'KDA', 'COMP',
    'HOT', 'KAVA', 'LDO', 'GT', 'FEI', 'QTUM', 'BNT', '1INCH', 'XYM'
    ]


def check_input(_event=None):
    value = entry.get().lower()

    if value == '':
        listbox_values.set(lst)
    else:
        data = []
        for item in lst:
            if value.lower() in item.lower():
                data.append(item)

        listbox_values.set(data)


root = Tk()

root.title('fcefv')
root.geometry('500x400')
root['background']


entry_text = StringVar()
entry = Entry(root, textvariable=entry_text)
entry.bind('<KeyRelease>', check_input)
entry.pack()


def on_change_selection(event):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters1 = {'slug': 'bitcoin'}  # 1
    parameters2 = {'slug': 'ethereum'}  # 1027
    parameters3 = {'slug': 'tether'}  # 825
    parameters4 = {'slug': 'usd-coin'}  # 3408
    parameters5 = {'slug': 'bnb'}  # 1839
    parameters6 = {'slug': 'xrp'}  # 52
    parameters7 = {'slug': 'cardano'}  # 2010
    parameters8 = {'slug': 'binance-usd'}  # 4687
    parameters9 = {'slug': 'solana'}  # 5426
    parameters10 = {'slug': 'dogecoin'}  # 74

    parameters11 = {'slug': 'polkadot-new'}  # 6636
    parameters12 = {'slug': 'avalanche'}  # 5805
    parameters13 = {'slug': 'tron'}  # 1958
    parameters14 = {'slug': 'shiba-inu'}  # 5994
    parameters15 = {'slug': 'multi-collateral-dai'}  # 4943
    parameters16 = {'slug': 'polygon'}  # 3890
    parameters17 = {'slug': 'cronos'}  # 3635
    parameters18 = {'slug': 'unus-sed-leo'}  # 3957
    parameters19 = {'slug': 'litecoin'}  # 2
    parameters20 = {'slug': 'near-protocol'}  # 6535

    parameters21 = {'slug': 'ftx-token'}  # 4195
    parameters22 = {'slug': 'bitcoin-cash'}  # 1831
    parameters23 = {'slug': 'uniswap'}  # 7083
    parameters24 = {'slug': 'chainlink'}  # 1975
    parameters25 = {'slug': 'stellar'}  # 512
    parameters26 = {'slug': 'cosmos'}  # 3794
    parameters27 = {'slug': 'algorand'}  # 4030
    parameters28 = {'slug': 'monero'}  # 328
    parameters29 = {'slug': 'flow'}  # 4558
    parameters30 = {'slug': 'ethereum-classic'}  # 1321

    parameters31 = {'slug': 'apecoin-ape'}  # 18876
    parameters32 = {'slug': 'decentraland'}  # 1966
    parameters33 = {'slug': 'hedera'}  # 4642
    parameters34 = {'slug': 'elrond-egld'}  # 6892
    parameters35 = {'slug': 'vechain'}  # 3077
    parameters36 = {'slug': 'internet-computer'}  # 8916
    parameters37 = {'slug': 'filecoin'}  # 2280
    parameters38 = {'slug': 'the-sandbox'}  # 6210
    parameters39 = {'slug': 'tezos'}  # 2011
    parameters40 = {'slug': 'maker'}  # 1518

    parameters41 = {'slug': 'zcash'}  # 1437
    parameters42 = {'slug': 'kucoin-token'}  # 2087
    parameters43 = {'slug': 'theta-network'}  # 2416
    parameters44 = {'slug': 'pancakeswap'}  # 7186
    parameters45 = {'slug': 'eos'}  # 1765
    parameters46 = {'slug': 'axie-infinity'}  # 6783
    parameters47 = {'slug': 'trueusd'}  # 2563
    parameters48 = {'slug': 'the-graph'}  # 6719
    parameters49 = {'slug': 'terrausd'}  # 7129
    parameters50 = {'slug': 'aave'}  # 7278

    parameters51 = {'slug': 'klaytn'}  # 4256
    parameters52 = {'slug': 'huobi-token'}  # 2502
    parameters53 = {'slug': 'thorchain'}  # 4157
    parameters54 = {'slug': 'helium'}  # 5665
    parameters55 = {'slug': 'bittorrent-new'}  # 16086
    parameters56 = {'slug': 'bitcoin-sv'}  # 3602
    parameters57 = {'slug': 'iota'}  # 1720
    parameters58 = {'slug': 'paxos-standard'}  # 3330
    parameters59 = {'slug': 'ecash'}  # 10791
    parameters60 = {'slug': 'fantom'}  # 3513

    parameters61 = {'slug': 'green-metaverse-token'}  # 18069
    parameters62 = {'slug': 'neutrino-usd'}  # 5068
    parameters63 = {'slug': 'quant'}  # 3155
    parameters64 = {'slug': 'nexo'}  # 2694
    parameters65 = {'slug': 'stacks'}  # 4847
    parameters66 = {'slug': 'okb'}  # 3897
    parameters67 = {'slug': 'neo'}  # 1376
    parameters68 = {'slug': 'waves'}  # 1274
    parameters69 = {'slug': 'chiliz'}  # 4066
    parameters70 = {'slug': 'convex-finance'}  # 9903

    parameters71 = {'slug': 'kusama'}  # 5034
    parameters72 = {'slug': 'zilliqa'}  # 2469
    parameters73 = {'slug': 'enjin-coin'}  # 2130
    parameters74 = {'slug': 'dash'}  # 131
    parameters75 = {'slug': 'celo'}  # 5567
    parameters76 = {'slug': 'curve-dao-token'}  # 6538
    parameters77 = {'slug': 'loopring'}  # 1934
    parameters78 = {'slug': 'gala'}  # 7080
    parameters79 = {'slug': 'pax-gold'}  # 4705
    parameters80 = {'slug': 'basic-attention-token'}  # 1697

    parameters81 = {'slug': 'gnosis-gno'}  # 1659
    parameters82 = {'slug': 'amp'}  # 6945
    parameters83 = {'slug': 'harmony'}  # 3945
    parameters84 = {'slug': 'xinfin'}  # 2634
    parameters85 = {'slug': 'arweave'}  # 5632
    parameters86 = {'slug': 'nem'}  # 873
    parameters87 = {'slug': 'mina'}  # 8646
    parameters88 = {'slug': 'decred'}  # 1168
    parameters89 = {'slug': 'kadena'}  # 5647
    parameters90 = {'slug': 'compound'}  # 5692

    parameters91 = {'slug': 'holo'}  # 2682
    parameters92 = {'slug': 'kava'}  # 4846
    parameters93 = {'slug': 'lido-dao'}  # 8000
    parameters94 = {'slug': 'gatetoken'}  # 4269
    parameters95 = {'slug': 'fei-usd'}  # 8642
    parameters96 = {'slug': 'qtum'}  # 1684
    parameters97 = {'slug': 'bancor'}  # 1727
    parameters98 = {'slug': '1inch'}  # 8104
    parameters99 = {'slug': 'symbol'}  # 8677

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '556ed841-e4a9-4693-9ec2-88ab62aeff6e'
    }

    session = Session()
    session.headers.update(headers)

    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        dataa = event.widget.get(index)
        entry_text.set(dataa)
        check_input()

    if dataa == 'BTC':
        response = session.get(url, params=parameters1)
        lbl.configure(text="BTC")
        lbl2.configure(text = str(json.loads(response.text)['data']['1']['quote']['USD']['price'])[:-10])
        color_change = json.loads(response.text)['data']['1']['quote']['USD']['percent_change_1h']
        if color_change > 0:
            lbl2.configure(fg = 'green')
        else:
            lbl2.configure(fg = 'red')

    elif dataa == 'ETH':
        response = session.get(url, params=parameters2)
        lbl.configure(text="ETH")
        lbl2.configure(text = str(json.loads(response.text)['data']['1027']['quote']['USD']['price'])[:-10])
        color_change = json.loads(response.text)['data']['1027']['quote']['USD']['percent_change_1h']
        if color_change > 0:
            lbl2.configure(fg = 'green')
        else:
            lbl2.configure(fg = 'red')

    elif dataa == 'USDT':
        response = session.get(url, params=parameters3)
        lbl.configure(text="USDT")
        lbl2.configure(text = str(json.loads(response.text)['data']['825']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['825']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'USDC':
        response = session.get(url, params=parameters4)
        lbl.configure(text="USDC")
        lbl2.configure(text = str(json.loads(response.text)['data']['3408']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['3408']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'BNB':
        response = session.get(url, params=parameters5)
        lbl.configure(text="BNB")
        lbl2.configure(text = str(json.loads(response.text)['data']['1839']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1839']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'XRP':
        response = session.get(url, params=parameters6)
        lbl.configure(text="XRP")
        lbl2.configure(text = str(json.loads(response.text)['data']['52']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['52']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'ADA':
        response = session.get(url, params=parameters7)
        lbl.configure(text="ADA")
        lbl2.configure(text = str(json.loads(response.text)['data']['2010']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['2010']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'BUSD':
        response = session.get(url, params=parameters8)
        lbl.configure(text="BUSD")
        lbl2.configure(text = str(json.loads(response.text)['data']['4687']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['4687']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'SOL':
        response = session.get(url, params=parameters9)
        lbl.configure(text="SOL")
        lbl2.configure(text = str(json.loads(response.text)['data']['5426']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['5426']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'DOGE':
        response = session.get(url, params=parameters10)
        lbl.configure(text="DOGE")
        lbl2.configure(text = str(json.loads(response.text)['data']['74']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['74']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'DOT':
        response = session.get(url, params=parameters11)
        lbl.configure(text="DOT")
        lbl2.configure(text = str(json.loads(response.text)['data']['6636']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['6636']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'AVAX':
        response = session.get(url, params=parameters12)
        lbl.configure(text="AVAX")
        lbl2.configure(text = str(json.loads(response.text)['data']['5805']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['5805']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'TRX':
        response = session.get(url, params=parameters13)
        lbl.configure(text="TRX")
        lbl2.configure(text = str(json.loads(response.text)['data']['1958']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1958']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'SHIB':
        response = session.get(url, params=parameters14)
        lbl.configure(text="SHIB")
        lbl2.configure(text = str(json.loads(response.text)['data']['5994']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['5994']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'DAI':
        response = session.get(url, params=parameters15)
        lbl.configure(text="DAI")
        lbl2.configure(text = str(json.loads(response.text)['data']['4943']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['4943']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'MATIC':
        response = session.get(url, params=parameters16)
        lbl.configure(text="MATIC")
        lbl2.configure(text = str(json.loads(response.text)['data']['3890']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['3890']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'CRO':
        response = session.get(url, params=parameters17)
        lbl.configure(text="CRO")
        lbl2.configure(text = str(json.loads(response.text)['data']['3635']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['3635']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'LEO':
        response = session.get(url, params=parameters18)
        lbl.configure(text="LEO")
        lbl2.configure(text = str(json.loads(response.text)['data']['3957']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['3957']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'LTC':
        response = session.get(url, params=parameters19)
        lbl.configure(text="LTC")
        lbl2.configure(text = str(json.loads(response.text)['data']['2']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['2']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'NEAR':
        response = session.get(url, params=parameters20)
        lbl.configure(text="NEAR")
        lbl2.configure(text = str(json.loads(response.text)['data']['6535']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['6535']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'FTT':
        response = session.get(url, params=parameters21)
        lbl.configure(text="FTT")
        lbl2.configure(text = str(json.loads(response.text)['data']['4195']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['4195']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'BCH':
        response = session.get(url, params=parameters22)
        lbl.configure(text="BCH")
        lbl2.configure(text = str(json.loads(response.text)['data']['1831']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1831']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'UNI':
        response = session.get(url, params=parameters23)
        lbl.configure(text="UNI")
        lbl2.configure(text = str(json.loads(response.text)['data']['7083']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['7083']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'LINK':
        response = session.get(url, params=parameters24)
        lbl.configure(text="LINK")
        lbl2.configure(text = str(json.loads(response.text)['data']['1975']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1975']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'XLM':
        response = session.get(url, params=parameters25)
        lbl.configure(text="XLM")
        lbl2.configure(text = str(json.loads(response.text)['data']['512']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['512']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'ATOM':
        response = session.get(url, params=parameters26)
        lbl.configure(text="ATOM")
        lbl2.configure(text = str(json.loads(response.text)['data']['3794']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['3794']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'ALGO':
        response = session.get(url, params=parameters27)
        lbl.configure(text="ALGO")
        lbl2.configure(text = str(json.loads(response.text)['data']['4030']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['4030']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'XMR':
        response = session.get(url, params=parameters28)
        lbl.configure(text="XMR")
        lbl2.configure(text = str(json.loads(response.text)['data']['328']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['328']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'FLOW':
        response = session.get(url, params=parameters29)
        lbl.configure(text="FLOW")
        lbl2.configure(text = str(json.loads(response.text)['data']['4558']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['4558']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'ETC':
        response = session.get(url, params=parameters30)
        lbl.configure(text="ETC")
        lbl2.configure(text = str(json.loads(response.text)['data']['1321']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1321']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'APE':
        response = session.get(url, params=parameters31)
        lbl.configure(text="APE")
        lbl2.configure(text=str(json.loads(response.text)['data']['18876']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['18876']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'MANA':
        response = session.get(url, params=parameters32)
        lbl.configure(text="MANA")
        lbl2.configure(text=str(json.loads(response.text)['data']['1321']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1321']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'HBAR':
        response = session.get(url, params=parameters33)
        lbl.configure(text="HBAR")
        lbl2.configure(text=str(json.loads(response.text)['data']['4642']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['4642']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'EGLD':
        response = session.get(url, params=parameters34)
        lbl.configure(text="EGLD")
        lbl2.configure(text=str(json.loads(response.text)['data']['6892']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['6892']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'VET':
        response = session.get(url, params=parameters35)
        lbl.configure(text="VET")
        lbl2.configure(text=str(json.loads(response.text)['data']['3077']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['3077']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'ICP':
        response = session.get(url, params=parameters36)
        lbl.configure(text="ICP")
        lbl2.configure(text=str(json.loads(response.text)['data']['8916']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['8916']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'FIL':
        response = session.get(url, params=parameters37)
        lbl.configure(text="FIL")
        lbl2.configure(text=str(json.loads(response.text)['data']['2280']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['2280']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'SAND':
        response = session.get(url, params=parameters38)
        lbl.configure(text="SAND")
        lbl2.configure(text=str(json.loads(response.text)['data']['6210']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['6210']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'XTZ':
        response = session.get(url, params=parameters39)
        lbl.configure(text="XTZ")
        lbl2.configure(text=str(json.loads(response.text)['data']['2011']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['2011']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'MKR':
        response = session.get(url, params=parameters40)
        lbl.configure(text="MKR")
        lbl2.configure(text=str(json.loads(response.text)['data']['1518']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1518']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'ZEC':
        response = session.get(url, params=parameters41)
        lbl.configure(text="ZEC")
        lbl2.configure(text=str(json.loads(response.text)['data']['1437']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1437']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'KCS':
        response = session.get(url, params=parameters42)
        lbl.configure(text="KCS")
        lbl2.configure(text=str(json.loads(response.text)['data']['2087']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['2087']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'THETA':
        response = session.get(url, params=parameters43)
        lbl.configure(text="THETA")
        lbl2.configure(text=str(json.loads(response.text)['data']['2416']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['2416']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'CAKE':
        response = session.get(url, params=parameters44)
        lbl.configure(text="CAKE")
        lbl2.configure(text=str(json.loads(response.text)['data']['7186']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['7186']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'EOS':
        response = session.get(url, params=parameters45)
        lbl.configure(text="EOS")
        lbl2.configure(text=str(json.loads(response.text)['data']['1765']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['1765']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'AXS':
        response = session.get(url, params=parameters46)
        lbl.configure(text="AXS")
        lbl2.configure(text=str(json.loads(response.text)['data']['6783']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['6783']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'TUSD':
        response = session.get(url, params=parameters47)
        lbl.configure(text="TUSD")
        lbl2.configure(text=str(json.loads(response.text)['data']['15']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['15']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'GRT':
        response = session.get(url, params=parameters48)
        lbl.configure(text="GRT")
        lbl2.configure(text=str(json.loads(response.text)['data']['6719']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['6719']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'UST':
        response = session.get(url, params=parameters49)
        lbl.configure(text="UST")
        lbl2.configure(text=str(json.loads(response.text)['data']['7129']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['7129']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

    elif dataa == 'AAVE':
        response = session.get(url, params=parameters50)
        lbl.configure(text="AAVE")
        lbl2.configure(text=str(json.loads(response.text)['data']['7278']['quote']['USD']['price'])[:-10])
        color_change = (json.loads(response.text)['data']['7278']['quote']['USD']['percent_change_1h'])
        col_ch(color_change)

def col_ch(color_change):
    if color_change > 0:
        lbl2.configure(fg='green')
    else:
        lbl2.configure(fg='red')

my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame)

listbox_values = Variable()
listbox = Listbox(my_frame, listvariable=listbox_values, height=5, yscrollcommand=my_scrollbar.set)
listbox.bind('<<ListboxSelect>>', on_change_selection)
listbox.pack()
listbox_values.set(lst)

my_scrollbar.config(command=listbox.yview)
my_scrollbar.pack(side = RIGHT, fill =Y)
my_frame.pack()


lbl = Label(root, text=" ", font=("Arial Bold", 30))
lbl.place(x=130,y=230)

lbl2 = Label(root, text=" ", font=("Arial Bold", 30))
lbl2.place(x=130,y=270)

root.mainloop()
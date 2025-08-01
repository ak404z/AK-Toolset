import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import requests
import base64 as b64
import binascii as ba
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

class AKToolsetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AK Toolset GUI - OSINT Suite")
        self.root.geometry("1000x700")
        self.root.configure(bg="black")

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background='black', foreground='lime', padding=10)
        style.map("TNotebook.Tab", background=[("selected", "green")])

        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(fill='both', expand=True)

        self.create_instagram_osint_tab()
        self.create_phone_tab()
        self.create_darkweb_tab()
        self.create_about_tab()

    def create_instagram_osint_tab(self):
        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text='🔍 Instagram OSINT')

        frame = tk.Frame(tab, bg='black')
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        label = tk.Label(frame, text="Enter Instagram Username:", fg='lime', bg='black')
        label.pack()

        self.ig_entry = tk.Entry(frame, width=50)
        self.ig_entry.pack(pady=5)

        run_button = tk.Button(frame, text="Run OSINT", command=self.run_osint_thread, bg='green', fg='black')
        run_button.pack()

        self.ig_output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=110, height=30, bg='black', fg='lime')
        self.ig_output.pack(pady=10)

    def run_osint_thread(self):
        threading.Thread(target=self.instagram_osint, daemon=True).start()

    def instagram_osint(self):
        username = self.ig_entry.get()
        self.ig_output.delete(1.0, tk.END)
        if not username:
            self.ig_output.insert(tk.END, "[!] Username cannot be empty!\n")
            return

        headers = {
            'accept-language': 'en-US;q=1.0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-agent': 'Instagram 337.0.3.23.54 (...) AppleWebKit/420+',
        }

        data = { "q": username }

        def uwnrevj(uhevwcnje):
            return ba.unhexlify(uhevwcnje)

        hex_data = ''.join([
            '61','48','52','30','63','48','4D','36','4C','79','39','70','4C','6D','6C','75',
            '63','33','52','68','5A','33','4A','68','62','53','35','6A','62','32','30','76',
            '59','58','42','70','4C','33','59','78','4C','33','56','7A','5A','58','4A','7A',
            '4C','32','78','76','62','32','74','31','63','43','38','3D'
        ])
        decoded_url = b64.b64decode(uwnrevj(hex_data)).decode('utf-8')

        try:
            response = requests.post(decoded_url, headers=headers, data=data)
            response.raise_for_status()
            response_json = response.json()
        except Exception as e:
            self.ig_output.insert(tk.END, f"[!] Request failed: {e}\n")
            return

        if response_json:
            for key, value in response_json.items():
                if isinstance(value, dict):
                    self.ig_output.insert(tk.END, f"\n[{key}]\n")
                    for subk, subv in value.items():
                        self.ig_output.insert(tk.END, f"  {subk}: {subv}\n")
                else:
                    self.ig_output.insert(tk.END, f"{key}: {value}\n")

    def create_phone_tab(self):
        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text='📞 Phone Lookup')

        frame = tk.Frame(tab, bg='black')
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        label = tk.Label(frame, text="Enter Phone Number:", fg='lime', bg='black')
        label.pack()

        self.phone_entry = tk.Entry(frame, width=50)
        self.phone_entry.pack(pady=5)

        run_button = tk.Button(frame, text="Locate", command=self.run_phone_thread, bg='green', fg='black')
        run_button.pack()

        self.phone_output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=110, height=30, bg='black', fg='lime')
        self.phone_output.pack(pady=10)

    def run_phone_thread(self):
        threading.Thread(target=self.phone_lookup, daemon=True).start()

    def phone_lookup(self):
        number = self.phone_entry.get()
        self.phone_output.delete(1.0, tk.END)
        self.phone_output.insert(tk.END, f"[+] Looking up: {number}\n")

        try:
            parsed = phonenumbers.parse(number, None)
            status = "Valid" if phonenumbers.is_valid_number(parsed) else "Invalid"
            carrier_name = carrier.name_for_number(parsed, "en")
            tz = timezone.time_zones_for_number(parsed)
            country = geocoder.region_code_for_number(parsed)
            region = geocoder.description_for_number(parsed, "en")
            formatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

            result = f"""
[+] Phone        : {number}
[+] Formatted    : {formatted}
[+] Status       : {status}
[+] Country      : {country}
[+] Region       : {region}
[+] Timezone     : {tz[0] if tz else 'Unknown'}
[+] Carrier      : {carrier_name}
"""
            self.phone_output.insert(tk.END, result)
        except Exception as e:
            self.phone_output.insert(tk.END, f"[!] Error: {e}\n")

    def create_darkweb_tab(self):
        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text='🌐 Dark Web Sites')
        frame = tk.Frame(tab, bg='black')
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        label = tk.Label(frame, text="Click to Load Dark Web Sites", fg='lime', bg='black')
        label.pack(pady=5)

        run_button = tk.Button(frame, text="Load", command=self.load_darkweb, bg='green', fg='black')
        run_button.pack()

        self.darkweb_output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=110, height=30, bg='black', fg='lime')
        self.darkweb_output.pack(pady=10)

    def load_darkweb(self):
        self.darkweb_output.delete(1.0, tk.END)
        self.darkweb_output.insert(tk.END, "🌐 Dark Web Links:\n")
        darkweb_sites = [
            ("Hidden Wiki", "http://wikitjerrta4qgz4.onion/"),
            ("Torch", "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/"),
            ("Danex", "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/"),
            ("Sentor", "http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/"),
            ("Hidden Answers", "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/"),
            ("riseup searx", "http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/"),
            ("Dark Mixer", "http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/"),
            ("Mixabit", "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/"),
            ("EasyCoin", "http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/"),
            ("Onionwallet", "http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/"),
            ("VirginBitcoin", "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/"),
            ("Cryptostamps", "http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion/"),
            ("Stresser", "http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/"),
            ("Deep Market", "http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/"),
            ("DrChronic", "http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/"),
            ("TomAndJerry", "http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/"),
            ("420prime", "http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/"),
            ("DeDope", "http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/"),
            ("AccMarket", "http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/"),
            ("Cardshop", "http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/"),
            ("Darkmining", "http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/"),
            ("MobileStore", "http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/"),
            ("EuroGuns", "http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/"),
            ("UKpassports", "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/"),
            ("ccPal", "http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/"),
            ("Webuybitcoins", "http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/"),
            ("ASAP Market 1", "http://asap4u7rq4tyakf5gdahmj2c77blwc4noxnsppp5lzlhk7x34x2e22yd.onion/"),
            ("ASAP Market 2", "http://asap2u4pvplnkzl7ecle45wajojnftja45wvovl3jrvhangeyq67ziid.onion/"),
            ("ASAP Market 3", "http://asap4u2ihsunfdsumm66pmado3mt3lemdiu3fbx5b7wj5hb3xpgmwkqd.onion/"),
            ("Hydra", "http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/"),
            ("Versus Project", "http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/"),
            ("Tor Market", "http://rrlm2f22lpqgfhyydqkxxzv6snwo5qvc2krjt2q557l7z4te7fsvhbid.onion/"),
            ("The Pirate Bay", "http://uj3wazyk5kz5rzs.onion/"),
            ("1337x", "http://1337xwlc2c8sf3d7.onion/"),
            ("Foxy", "http://foxy6vayr5g5hwwx.onion/"),
            ("Deep Web Wiki", "http://wikicbtbf7rgjjbqe.onion/"),
            ("EDU", "http://edu.onion/")
        ]

        for name, url in darkweb_sites:
            self.darkweb_output.insert(tk.END, f"{name}: {url}\n")
        self.darkweb_output.insert(tk.END, "[✓] Done\n")

    def create_about_tab(self):
        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text='💀 About Me')

        frame = tk.Frame(tab, bg='black')
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        about_text = """[🔥] AK Toolset - Developed by AK 👑

[💻] OS: Kali Linux
[🌐] GitHub : github.com/ak404z
[📽️] Youtube : youtube.com/@ak404z
[🎵] TikTok : tiktok.com/@wak404z
[📷] Instagram : instagram.com/ak404z
[💡] Twitter/X : twitter.com/ak404z
[💬] Telegram : https://t.me/AKHacking1

[⚔] This tool is for educational and red teaming purposes only.
"""

        label = tk.Label(frame, text="About Developer", fg='lime', bg='black', font=('Arial', 14, 'bold'))
        label.pack(pady=10)

        output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=110, height=25, bg='black', fg='lime')
        output.insert(tk.END, about_text)
        output.configure(state='disabled')
        output.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AKToolsetGUI(root)
    root.mainloop()

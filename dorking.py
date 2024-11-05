import requests
from bs4 import BeautifulSoup
import os
import time  # Untuk jeda antar permintaan, jika diperlukan

# Definisikan kode warna secara global
R = "\033[91m"  # Merah
w = "\033[97m"  # Putih
u = "\033[94m"  # Biru
x = "\033[0m"   # Reset

def clear():
    """Fungsi untuk membersihkan layar konsol."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    # Menampilkan header dengan tulisan "DorkSM"
    print(rf"""{R}
 ____             _     
|  _ \  ___  _ __| | __ ____  __  __
| | | |/ _ \| '__| |/ // ___||  \/  |
| |_| | (_) | |  |   < \___ \| |\/| |
|____/ \___/|_|  |_|\_\ ___) | |  | |
{w}>>>>>>>> {u}BY{x} {u}@msxsec1337{x} {R}|____/|_|  |_|{x}
 
""")

def google_search(query, max_results=100):  # Default max results to 100
    results = []
    pages = min((max_results // 10), 10)  # Calculate the number of pages needed, limit to 10

    for page in range(pages):
        start = page * 10
        url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"{R}Terjadi kesalahan saat melakukan pencarian: {e}{x}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.select('div.tF2Cxc')
        
        if search_results:  # Pastikan ada hasil
            for g in search_results:  # Loop melalui semua hasil
                title_tag = g.select_one('h3')
                link_tag = g.select_one('a')
                if title_tag and link_tag:
                    title = title_tag.get_text()
                    link = link_tag['href']
                    results.append((title, link))

        # Tambahkan jeda untuk menghindari batasan permintaan berlebihan
        time.sleep(2)
        
        if len(results) >= max_results:  # Stop if we reached the max results
            break
        
    return results[:max_results]  # Kembalikan hasil yang terbatas

def dorking_tool():
    clear()  # Membersihkan layar sebelum memulai
    print_header()
    
    print(f"{u} [!] Tidak Support Dork SQL{x}")  # Menampilkan informasi tambahan
    print(f"{u} [?] Ketik Keluar Jika Mau Keluar Dari Tools{x}")

    query = input(f"{w}Dork: {x}")
    if query.lower() == 'keluar':
        print("Terima kasih telah menggunakan alat ini.")
        return
        
    results = google_search(query)  # Call with default max results of 100
    
    if results:
        print("\nHasil Dorking:")
        print("=" * 50)
        for i, (title, link) in enumerate(results, start=1):
            print(f"[{i}] {title}")
            print(f"   Link: {link}\n")
        print("=" * 50)
    else:
        print(f"{R}Tidak ada hasil yang ditemukan untuk kueri ini.{x}")
        print("=" * 50)

if __name__ == "__main__":
    dorking_tool()

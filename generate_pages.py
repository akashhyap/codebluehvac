#!/usr/bin/env python3
"""Generate all pages for Code Blue HVAC website."""
import os

BASE = "/home/claude/codebluehvac/src/pages"

# ============================================================
# CONSTANTS
# ============================================================

PHONE = "(702) 887-1656"
PHONE_RAW = "+17028871656"
BIZ = "Code Blue HVAC"

SVG_PATTERN = '''<div class="absolute inset-0 opacity-5" style="background-image: url(&quot;data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E&quot;);"></div>'''

GRID_BG = 'style="background-image: linear-gradient(rgba(255,255,255,.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.1) 1px, transparent 1px); background-size: 60px 60px;"'

PHONE_SVG = '<svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>'
ARROW_SVG = '<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
CHEVRON_SVG = '<svg class="w-4 h-4 transition-transform duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>'

# SVG Icons for service cards
ICONS = {
    "wrench": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>',
    "snowflake": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3v18M5.63 5.63l12.74 12.74M3 12h18M5.63 18.37l12.74-12.74"/><circle cx="12" cy="12" r="3"/></svg>',
    "flame": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2c-5 7-8 11-8 14a8 8 0 1016 0c0-3-3-7-8-14z"/></svg>',
    "building": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M9 6h.01M15 6h.01M9 10h.01M15 10h.01M9 14h.01M15 14h.01"/></svg>',
    "wind": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9.59 4.59A2 2 0 1111 8H2m10.59 11.41A2 2 0 1014 16H2m15.73-8.27A2.5 2.5 0 1119.5 12H2"/></svg>',
    "shield": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "clock": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "home": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M9 22V12h6v10"/></svg>',
    "download": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3v12M8 11l4 4 4-4"/><path d="M20 21H4"/></svg>',
    "refresh": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 4v6h6"/><path d="M3.51 15a9 9 0 102.13-9.36L1 10"/></svg>',
    "settings": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>',
    "zap": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
    "filter": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>',
    "mappin": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "check": '<svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>',
}

FAQ_SCRIPT = """<script>
document.querySelectorAll('.faq-trigger').forEach((trigger) => {
trigger.addEventListener('click', () => {
const item = trigger.closest('.faq-item');
const content = item?.querySelector('.faq-content');
const icon = item?.querySelector('.faq-icon svg');
const isOpen = trigger.getAttribute('aria-expanded') === 'true';
document.querySelectorAll('.faq-item').forEach((o) => { if (o !== item) { const c = o.querySelector('.faq-content'); const t = o.querySelector('.faq-trigger'); const ic = o.querySelector('.faq-icon svg'); if (c) c.style.maxHeight='0'; if (t) t.setAttribute('aria-expanded','false'); if (ic) ic.style.transform='rotate(0deg)'; } });
if (isOpen) { content.style.maxHeight='0'; trigger.setAttribute('aria-expanded','false'); icon.style.transform='rotate(0deg)'; }
else { content.style.maxHeight=content.scrollHeight+'px'; trigger.setAttribute('aria-expanded','true'); icon.style.transform='rotate(180deg)'; }
});
});
</script>"""


# ============================================================
# SECTION BUILDERS
# ============================================================

def hero_section(breadcrumbs, title, subtitle):
    crumbs = ""
    for i, (label, url) in enumerate(breadcrumbs):
        if i > 0: crumbs += '<li>/</li>'
        if url:
            crumbs += f'<li><a href="{url}" class="hover:text-white transition-colors">{label}</a></li>'
        else:
            crumbs += f'<li class="text-accent">{label}</li>'
    return f'''<section class="relative bg-dark pt-32 pb-16 lg:pt-40 lg:pb-20 overflow-hidden">
{SVG_PATTERN}
<div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<nav class="mb-4"><ol class="flex items-center gap-2 text-sm text-white/40">{crumbs}</ol></nav>
<h1 class="font-heading text-5xl sm:text-6xl lg:text-8xl uppercase tracking-wide text-white leading-[0.85] animate-fade-in-up">{title}</h1>
<p class="mt-4 text-white/50 text-lg max-w-2xl animate-fade-in-up delay-100">{subtitle}</p>
<div class="mt-8 flex flex-wrap gap-4 animate-fade-in-up delay-200">
<a href="tel:{PHONE_RAW}" class="inline-flex items-center gap-2 bg-accent text-white px-7 py-4 rounded-card font-accent font-semibold uppercase tracking-wide text-sm hover:bg-accent-dark transition-all">{PHONE_SVG}{PHONE}</a>
<a href="/contact" class="inline-flex items-center gap-2 bg-white/10 text-white px-7 py-4 rounded-card font-accent font-semibold uppercase tracking-wide text-sm hover:bg-white/20 transition-all">Schedule Service {ARROW_SVG}</a>
</div></div></section>'''


def content_section(label, h2_line1, h2_line2, paragraphs, bg="white"):
    paras = "".join([f"<p>{p}</p>" for p in paragraphs])
    return f'''<section class="py-20 lg:py-28 bg-{bg}">
<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">{label}</p>
<h2 class="font-heading text-4xl sm:text-5xl uppercase tracking-wide text-dark leading-[0.9] mb-6">{h2_line1}<br /><span class="text-accent">{h2_line2}</span></h2>
<div class="space-y-4 text-dark/60 leading-relaxed">{paras}</div>
</div></section>'''


def intro_2col(label, h2_line1, h2_line2, paragraphs, icon_key="snowflake"):
    paras = "".join([f"<p>{p}</p>" for p in paragraphs])
    icon = ICONS.get(icon_key, ICONS["snowflake"])
    return f'''<section class="py-20 lg:py-28 bg-white">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
<div>
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">{label}</p>
<h2 class="font-heading text-5xl sm:text-6xl uppercase tracking-wide text-dark leading-[0.9] mb-6">{h2_line1}<br /><span class="text-accent">{h2_line2}</span></h2>
<div class="space-y-4 text-dark/60 leading-relaxed">{paras}</div>
</div>
<div class="big-top bg-light aspect-[4/5] flex items-center justify-center">
<div class="text-center p-8">
<div class="w-20 h-20 mx-auto text-accent/15 mb-3">{icon}</div>
<p class="text-dark/25 font-accent text-sm uppercase tracking-wider">{label}</p>
</div></div></div></div></section>'''


def service_grid(cards):
    """cards: list of (title, desc, href, icon_key)"""
    items = ""
    for title, desc, href, icon_key in cards:
        icon = ICONS.get(icon_key, ICONS["wrench"])
        items += f'''<a href="{href}" class="group bg-white/5 hover:bg-white/10 border border-white/10 hover:border-accent/30 rounded-card p-7 lg:p-8 transition-all duration-300 block">
<div class="w-14 h-14 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-5 group-hover:bg-accent group-hover:text-white transition-all duration-300">
<Fragment set:html={{'{icon}'}}>
</Fragment></div>
<h3 class="font-heading text-xl uppercase tracking-wide text-white mb-3">{title}</h3>
<p class="text-white/50 text-sm leading-relaxed">{desc}</p>
<div class="mt-5 flex items-center gap-2 text-accent text-sm font-accent font-medium opacity-0 group-hover:opacity-100 transition-opacity duration-300">Learn More {ARROW_SVG}</div>
</a>\n'''
    return f'''<section class="py-20 lg:py-28 bg-dark relative overflow-hidden">
<div class="absolute inset-0 opacity-5" {GRID_BG}></div>
<div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="mb-16">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">Our Services</p>
<h2 class="font-heading text-5xl sm:text-6xl lg:text-7xl uppercase tracking-wide text-white leading-[0.9]">What We<br /><span class="text-accent">Offer</span></h2>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
{items}
</div></div></section>'''


def service_grid_hub(label, h2_line1, h2_line2, cards):
    """Hub-specific service grid with custom heading. cards: list of (title, desc, href, icon_key)"""
    items = ""
    for title, desc, href, icon_key in cards:
        icon_svg = ICONS.get(icon_key, ICONS["wrench"]).replace("'", "\\'").replace('"', '\\"')
        # Use a simpler approach - just hardcode the SVG directly
        icon_html = ICONS.get(icon_key, ICONS["wrench"])
        items += f'''<a href="{href}" class="group bg-white/5 hover:bg-white/10 border border-white/10 hover:border-accent/30 rounded-card p-7 lg:p-8 transition-all duration-300 block">
<div class="w-14 h-14 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-5 group-hover:bg-accent group-hover:text-white transition-all duration-300">
''' + "<Fragment set:html={'" + icon_html.replace("'", "\\'") + "'} />" + f'''
</div>
<h3 class="font-heading text-xl uppercase tracking-wide text-white mb-3">{title}</h3>
<p class="text-white/50 text-sm leading-relaxed">{desc}</p>
<div class="mt-5 flex items-center gap-2 text-accent text-sm font-accent font-medium opacity-0 group-hover:opacity-100 transition-opacity duration-300">Learn More {ARROW_SVG}</div>
</a>\n'''
    return f'''<section class="py-20 lg:py-28 bg-dark relative overflow-hidden">
<div class="absolute inset-0 opacity-5" {GRID_BG}></div>
<div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="mb-16">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">{label}</p>
<h2 class="font-heading text-5xl sm:text-6xl lg:text-7xl uppercase tracking-wide text-white leading-[0.9]">{h2_line1}<br /><span class="text-accent">{h2_line2}</span></h2>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
{items}
</div></div></section>'''


def faq_section(faqs):
    items = ""
    for i, (q, a) in enumerate(faqs):
        items += f'''<div class="faq-item border-b border-border" data-faq-index="{i}">
<button class="faq-trigger w-full flex items-center justify-between py-6 text-left group" aria-expanded="false">
<span class="font-accent font-semibold text-dark text-base lg:text-lg pr-4 group-hover:text-accent transition-colors">{q}</span>
<span class="faq-icon w-10 h-10 bg-warm rounded-card flex-shrink-0 flex items-center justify-center transition-all duration-300 group-hover:bg-accent group-hover:text-white">{CHEVRON_SVG}</span>
</button>
<div class="faq-content overflow-hidden transition-all duration-300 max-h-0">
<p class="pb-6 text-dark/60 leading-relaxed pr-14">{a}</p>
</div></div>\n'''
    return f'''<section class="py-20 lg:py-28 bg-light">
<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-16">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">FAQ</p>
<h2 class="font-heading text-5xl sm:text-6xl uppercase tracking-wide text-dark leading-[0.9]">Common<br /><span class="text-accent">Questions</span></h2>
</div>
<div class="space-y-0">{items}</div>
</div></section>'''


def related_links(links):
    lh = ""
    for label, url in links:
        lh += f'<a href="{url}" class="text-accent hover:text-accent-dark text-sm font-accent font-medium transition-colors">{label} &rarr;</a>\n'
    return f'''<section class="py-12 bg-white border-t border-border">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<p class="font-accent font-semibold text-dark text-sm uppercase tracking-wider mb-4">Related</p>
<div class="flex flex-wrap gap-4">{lh}</div>
</div></section>'''


def build_page(filepath, title, description, sections, cta_heading):
    if "/blog/" in filepath or "/services/" in filepath or "/service-areas/" in filepath:
        prefix = "../../"
    else:
        prefix = "../"
    imports = f'''---
import Layout from '{prefix}layouts/Layout.astro';
import Header from '{prefix}components/Header.astro';
import CTA from '{prefix}components/CTA.astro';
import Footer from '{prefix}components/Footer.astro';
---'''
    body = "\n".join(sections)
    page = f'''{imports}
<Layout title="{title}" description="{description}">
<Header />
<main>
{body}
<CTA heading="{cta_heading}" />
</main>
<Footer />
</Layout>
{FAQ_SCRIPT}'''
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(page)
    print(f"  ✓ {filepath.replace(BASE, '')}")


# ============================================================
# HOMEPAGE
# ============================================================
print("\\n=== Building Homepage ===")

homepage = f'''---
import Layout from '../layouts/Layout.astro';
import Header from '../components/Header.astro';
import Hero from '../components/Hero.astro';
import CTA from '../components/CTA.astro';
import Footer from '../components/Footer.astro';
---
<Layout title="Code Blue HVAC | 24/7 HVAC Contractor in North Las Vegas, NV" description="Code Blue HVAC – Family-owned HVAC contractor in North Las Vegas. Commercial & residential AC repair, heating, ductwork & mini-splits. BBB A+ accredited. Call (702) 887-1656.">
<Header />
<main>
<Hero />

<!-- Services Overview -->
<section class="py-20 lg:py-28 bg-white">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-16">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">Full-Service HVAC</p>
<h2 class="font-heading text-5xl sm:text-6xl lg:text-7xl uppercase tracking-wide text-dark leading-[0.9]">Our HVAC<br /><span class="text-accent">Services</span></h2>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
<a href="/services/ac-cooling" class="group p-8 bg-light rounded-card hover:shadow-lg transition-all duration-300">
<div class="w-14 h-14 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-5 group-hover:bg-accent group-hover:text-white transition-all">
<svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3v18M5.63 5.63l12.74 12.74M3 12h18M5.63 18.37l12.74-12.74"/><circle cx="12" cy="12" r="3"/></svg>
</div>
<h3 class="font-heading text-2xl uppercase tracking-wide text-dark mb-2">AC & Cooling</h3>
<p class="text-dark/50 text-sm leading-relaxed">Expert AC repair, installation, replacement, and maintenance to beat the Las Vegas heat.</p>
</a>
<a href="/services/heating" class="group p-8 bg-light rounded-card hover:shadow-lg transition-all duration-300">
<div class="w-14 h-14 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-5 group-hover:bg-accent group-hover:text-white transition-all">
<svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2c-5 7-8 11-8 14a8 8 0 1016 0c0-3-3-7-8-14z"/></svg>
</div>
<h3 class="font-heading text-2xl uppercase tracking-wide text-dark mb-2">Heating</h3>
<p class="text-dark/50 text-sm leading-relaxed">Furnace repair, installation, and maintenance to keep your home warm through desert winters.</p>
</a>
<a href="/services/commercial-hvac" class="group p-8 bg-light rounded-card hover:shadow-lg transition-all duration-300">
<div class="w-14 h-14 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-5 group-hover:bg-accent group-hover:text-white transition-all">
<svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M9 6h.01M15 6h.01M9 10h.01M15 10h.01M9 14h.01M15 14h.01"/></svg>
</div>
<h3 class="font-heading text-2xl uppercase tracking-wide text-dark mb-2">Commercial HVAC</h3>
<p class="text-dark/50 text-sm leading-relaxed">Full commercial HVAC solutions for businesses across the Las Vegas Valley.</p>
</a>
<a href="/services/ductwork-air-quality" class="group p-8 bg-light rounded-card hover:shadow-lg transition-all duration-300">
<div class="w-14 h-14 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-5 group-hover:bg-accent group-hover:text-white transition-all">
<svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9.59 4.59A2 2 0 1111 8H2m10.59 11.41A2 2 0 1014 16H2m15.73-8.27A2.5 2.5 0 1119.5 12H2"/></svg>
</div>
<h3 class="font-heading text-2xl uppercase tracking-wide text-dark mb-2">Ductwork & Air Quality</h3>
<p class="text-dark/50 text-sm leading-relaxed">Duct installation, repair, cleaning, and air purification for cleaner, healthier indoor air.</p>
</a>
<a href="/services/ductless-mini-splits" class="group p-8 bg-light rounded-card hover:shadow-lg transition-all duration-300">
<div class="w-14 h-14 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-5 group-hover:bg-accent group-hover:text-white transition-all">
<svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
</div>
<h3 class="font-heading text-2xl uppercase tracking-wide text-dark mb-2">Ductless Mini-Splits</h3>
<p class="text-dark/50 text-sm leading-relaxed">Efficient zone-by-zone cooling and heating without the need for ductwork.</p>
</a>
<a href="/contact" class="group p-8 bg-accent rounded-card hover:bg-accent-dark transition-all duration-300">
<div class="w-14 h-14 bg-white/20 rounded-card flex items-center justify-center text-white mb-5">
<svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
</div>
<h3 class="font-heading text-2xl uppercase tracking-wide text-white mb-2">Get a Free Quote</h3>
<p class="text-white/70 text-sm leading-relaxed">Contact us today for a free consultation on any HVAC service you need.</p>
</a>
</div>
</div>
</section>

<!-- Why Choose Us -->
<section class="py-20 lg:py-28 bg-dark relative overflow-hidden">
<div class="absolute inset-0 opacity-5" {GRID_BG}></div>
<div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-16">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">Why Code Blue</p>
<h2 class="font-heading text-5xl sm:text-6xl lg:text-7xl uppercase tracking-wide text-white leading-[0.9]">Why Choose<br /><span class="text-accent">Code Blue HVAC</span></h2>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
<div class="bg-white/5 border border-white/10 rounded-card p-7">
<div class="w-12 h-12 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-4">
<svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M9 22V12h6v10"/></svg>
</div>
<h3 class="font-heading text-xl uppercase tracking-wide text-white mb-2">Family Owned</h3>
<p class="text-white/40 text-sm leading-relaxed">Owned and operated by Chris and Connie Montague. We treat every customer like family.</p>
</div>
<div class="bg-white/5 border border-white/10 rounded-card p-7">
<div class="w-12 h-12 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-4">
<svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
</div>
<h3 class="font-heading text-xl uppercase tracking-wide text-white mb-2">BBB A+ Rated</h3>
<p class="text-white/40 text-sm leading-relaxed">BBB accredited with an A+ rating. Licensed, bonded, and insured for your protection.</p>
</div>
<div class="bg-white/5 border border-white/10 rounded-card p-7">
<div class="w-12 h-12 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-4">
<svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
</div>
<h3 class="font-heading text-xl uppercase tracking-wide text-white mb-2">24/7 Service</h3>
<p class="text-white/40 text-sm leading-relaxed">HVAC emergencies don&rsquo;t wait, and neither do we. Available around the clock, 365 days a year.</p>
</div>
<div class="bg-white/5 border border-white/10 rounded-card p-7">
<div class="w-12 h-12 bg-accent/10 rounded-card flex items-center justify-center text-accent mb-4">
<svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</div>
<h3 class="font-heading text-xl uppercase tracking-wide text-white mb-2">15% Off</h3>
<p class="text-white/40 text-sm leading-relaxed">Seniors, veterans, and first responders receive 15% off parts and labor on all services.</p>
</div>
</div>
</div>
</section>

<!-- Testimonials -->
<section class="py-20 lg:py-28 bg-light">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-16">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">Testimonials</p>
<h2 class="font-heading text-5xl sm:text-6xl uppercase tracking-wide text-dark leading-[0.9]">What Our<br /><span class="text-accent">Customers Say</span></h2>
</div>
<div class="grid md:grid-cols-3 gap-8">
<div class="bg-white rounded-card p-8 shadow-sm">
<div class="flex gap-1 mb-4">
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</div>
<p class="text-dark/60 text-sm leading-relaxed mb-4">&ldquo;Chris and his team have always taken care of my HVAC needs for the past three years. Professional, honest, and always on time.&rdquo;</p>
<p class="font-accent font-semibold text-dark text-sm">Larry C.</p>
</div>
<div class="bg-white rounded-card p-8 shadow-sm">
<div class="flex gap-1 mb-4">
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</div>
<p class="text-dark/60 text-sm leading-relaxed mb-4">&ldquo;Prompt, professional service with A/C system repair during intense summer heat. So grateful for their quick response and expertise!&rdquo;</p>
<p class="font-accent font-semibold text-dark text-sm">O. Cruey</p>
</div>
<div class="bg-white rounded-card p-8 shadow-sm">
<div class="flex gap-1 mb-4">
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<svg class="w-4 h-4 text-accent" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</div>
<p class="text-dark/60 text-sm leading-relaxed mb-4">&ldquo;Very professional, competitive prices, helped me with all the setup and answered my questions. I would definitely call this company again!&rdquo;</p>
<p class="font-accent font-semibold text-dark text-sm">Lisa A.</p>
</div>
</div>
<div class="text-center mt-12">
<a href="/reviews" class="inline-flex items-center gap-2 font-accent font-semibold text-accent hover:text-accent-dark text-sm uppercase tracking-wide transition-colors">Read All Reviews {ARROW_SVG}</a>
</div>
</div>
</section>

<!-- Service Areas -->
<section class="py-20 lg:py-28 bg-white">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-16">
<p class="text-accent font-accent font-semibold text-sm uppercase tracking-widest mb-3">Serving Clark County</p>
<h2 class="font-heading text-5xl sm:text-6xl uppercase tracking-wide text-dark leading-[0.9]">Areas We<br /><span class="text-accent">Serve</span></h2>
</div>
<div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
<a href="/service-areas/north-las-vegas" class="group text-center p-6 bg-light rounded-card hover:bg-accent hover:text-white transition-all duration-200">
<p class="font-accent font-semibold text-sm uppercase tracking-wide text-dark/70 group-hover:text-white transition-colors">North Las Vegas</p>
</a>
<a href="/service-areas/las-vegas" class="group text-center p-6 bg-light rounded-card hover:bg-accent hover:text-white transition-all duration-200">
<p class="font-accent font-semibold text-sm uppercase tracking-wide text-dark/70 group-hover:text-white transition-colors">Las Vegas</p>
</a>
<a href="/service-areas/henderson" class="group text-center p-6 bg-light rounded-card hover:bg-accent hover:text-white transition-all duration-200">
<p class="font-accent font-semibold text-sm uppercase tracking-wide text-dark/70 group-hover:text-white transition-colors">Henderson</p>
</a>
<a href="/service-areas/summerlin" class="group text-center p-6 bg-light rounded-card hover:bg-accent hover:text-white transition-all duration-200">
<p class="font-accent font-semibold text-sm uppercase tracking-wide text-dark/70 group-hover:text-white transition-colors">Summerlin</p>
</a>
<a href="/service-areas/boulder-city" class="group text-center p-6 bg-light rounded-card hover:bg-accent hover:text-white transition-all duration-200">
<p class="font-accent font-semibold text-sm uppercase tracking-wide text-dark/70 group-hover:text-white transition-colors">Boulder City</p>
</a>
<a href="/service-areas/paradise" class="group text-center p-6 bg-light rounded-card hover:bg-accent hover:text-white transition-all duration-200">
<p class="font-accent font-semibold text-sm uppercase tracking-wide text-dark/70 group-hover:text-white transition-colors">Paradise</p>
</a>
</div>
</div>
</section>

<CTA />
</main>
<Footer />
</Layout>
'''

with open(f"{BASE}/index.astro", 'w') as f:
    f.write(homepage)
print("  ✓ /index.astro")


# ============================================================
# HUB PAGES
# ============================================================
print("\\n=== Building Hub Pages ===")

# Hub 1: AC & Cooling
build_page(f"{BASE}/services/ac-cooling.astro",
    "AC & Cooling Services North Las Vegas | Code Blue HVAC",
    "Complete AC and cooling services in North Las Vegas and the Las Vegas Valley. Expert AC repair, installation, replacement, maintenance and 24/7 emergency service. Call (702) 887-1656.",
    [
        hero_section([("Home","/"),("Services","/services/ac-cooling"),("AC & Cooling",None)], "AC & Cooling", "Complete AC and cooling services for homes and businesses across the Las Vegas Valley. From emergency repairs to full system installations."),
        intro_2col("AC & Cooling Experts","Beat the Las Vegas","Heat",["Las Vegas summers push air conditioning systems to their absolute limits. With temperatures regularly exceeding 115°F, your AC is essential life support for your home and family. Code Blue HVAC specializes in keeping North Las Vegas homes and businesses cool, comfortable, and energy-efficient year-round.","Our licensed technicians are trained on all major brands—including Ruud, Rheem, Carrier, Trane, Lennox, and more—and understand the unique challenges of desert climate HVAC. From emergency repairs when your system goes down to complete new installations with the latest high-efficiency equipment, we deliver fast, honest service every time.","Whether you need a quick fix, a full system replacement, or a maintenance plan to prevent breakdowns during peak season, Code Blue HVAC responds fast with transparent pricing and expert workmanship."],"snowflake"),
        service_grid_hub("Our AC Services","AC & Cooling","Services",[
            ("AC Repair","Fast, reliable AC repair in Las Vegas. We diagnose and fix all makes and models—often same day.","/services/ac-repair","wrench"),
            ("AC Installation","New AC system installation sized and designed for your Las Vegas home. Energy-efficient options.","/services/ac-installation","download"),
            ("AC Replacement","Upgrade your old, inefficient AC to a modern high-SEER system. We handle everything.","/services/ac-replacement","refresh"),
            ("AC Maintenance","Preventative maintenance plans to keep your system running efficiently and prevent breakdowns.","/services/ac-maintenance","settings"),
            ("Emergency AC Repair","24/7 emergency AC repair when you need it most. No extra charge for after-hours service.","/services/emergency-ac-repair","zap"),
        ]),
        faq_section([
            ("How quickly can you respond to an AC emergency?","We offer 24/7 emergency AC repair across the Las Vegas Valley. In most cases, a technician can be at your door within a few hours of your call, even on weekends and holidays."),
            ("How often should I service my AC in Las Vegas?","We recommend twice-yearly service—once in spring before cooling season and once in fall. In Las Vegas, your AC runs 6-8 months per year and needs more frequent attention than in milder climates."),
            ("What SEER rating should I choose for my new AC?","For Las Vegas, we recommend at least 16 SEER for solid efficiency. Higher SEER ratings (18-26) provide greater savings on NV Energy bills but cost more upfront. We help you calculate the ROI based on your usage."),
            ("Do you service all AC brands?","Yes. As a Ruud Pro-Partner, we specialize in Ruud and Rheem systems, but our technicians are trained to repair and maintain all major brands including Carrier, Trane, Lennox, York, Bryant, Amana, and more."),
        ]),
        related_links([("Heating Services","/services/heating"),("Commercial HVAC","/services/commercial-hvac"),("Ductless Mini-Splits","/services/ductless-mini-splits"),("Ductwork & Air Quality","/services/ductwork-air-quality")]),
    ], "Need AC Service?\\nCall Code Blue")

# Hub 2: Heating
build_page(f"{BASE}/services/heating.astro",
    "Heating Services North Las Vegas | Furnace Repair & Installation | Code Blue HVAC",
    "Expert heating and furnace services in North Las Vegas. Furnace repair, installation, replacement, and maintenance. 24/7 emergency service. Call (702) 887-1656.",
    [
        hero_section([("Home","/"),("Services","/services/heating"),("Heating",None)], "Heating Services", "Expert furnace and heating system repair, installation, and maintenance for Las Vegas homes and businesses."),
        intro_2col("Heating Experts","Stay Warm Through","Desert Winters",["While Las Vegas is known for scorching summers, winter temperatures can drop into the 30s and 40s overnight. A reliable heating system is essential for keeping your family comfortable from November through March.","Code Blue HVAC provides complete heating services including furnace repair, new furnace installation, heating system replacement, and preventative maintenance. Our technicians are trained on gas furnaces, electric furnaces, heat pumps, and hydronic systems.","As a family-owned company, we understand budget concerns and always provide upfront pricing with no hidden fees. We also offer financing options to make heating system upgrades accessible to every homeowner."],"flame"),
        service_grid_hub("Heating Services","Heating","Services",[
            ("Furnace Repair","Fast furnace diagnosis and repair for all makes and models. Get your heat back fast.","/services/furnace-repair","wrench"),
            ("Furnace Installation","New furnace installation with proper sizing for your home. Energy-efficient options available.","/services/furnace-installation","download"),
            ("Heating Maintenance","Keep your furnace running safely and efficiently with our seasonal maintenance plans.","/services/heating-maintenance","settings"),
        ]),
        faq_section([
            ("How do I know if my furnace needs repair or replacement?","If your furnace is over 15 years old, requires frequent repairs, has uneven heating, or your energy bills are climbing, it may be time for a replacement. Our technicians provide honest assessments to help you decide."),
            ("How long does a furnace installation take?","A standard furnace replacement typically takes one day. If ductwork modifications are needed, it may take an additional day. We always provide a timeline upfront."),
            ("Do you service gas and electric furnaces?","Yes, our technicians are trained on both gas and electric furnaces, as well as heat pumps and dual-fuel systems. We service all major brands."),
        ]),
        related_links([("AC & Cooling","/services/ac-cooling"),("Ductless Mini-Splits","/services/ductless-mini-splits"),("Commercial HVAC","/services/commercial-hvac")]),
    ], "Need Heating Service?\\nCall Code Blue")

# Hub 3: Commercial HVAC
build_page(f"{BASE}/services/commercial-hvac.astro",
    "Commercial HVAC Services North Las Vegas | Code Blue HVAC",
    "Full-service commercial HVAC for businesses in North Las Vegas and Clark County. Installation, repair, and maintenance. Call (702) 887-1656.",
    [
        hero_section([("Home","/"),("Services","/services/commercial-hvac"),("Commercial HVAC",None)], "Commercial HVAC", "Full-service commercial HVAC solutions for businesses across the Las Vegas Valley and Clark County."),
        intro_2col("Commercial HVAC Experts","Keep Your Business","Comfortable",["Las Vegas businesses depend on reliable HVAC to maintain comfortable environments for employees and customers alike. Code Blue HVAC provides comprehensive commercial HVAC services tailored to the unique demands of commercial spaces.","From office buildings and retail spaces to restaurants and warehouses, our experienced technicians handle installations, repairs, and preventative maintenance for commercial systems of all sizes. We work with rooftop units, split systems, VRF/VRV systems, and more.","We understand that downtime costs money, which is why we offer priority commercial service with rapid response times and flexible scheduling to minimize disruption to your operations."],"building"),
        service_grid_hub("Commercial Services","Commercial","Services",[
            ("Commercial AC Repair","Fast commercial AC repair to minimize downtime and keep your business comfortable.","/services/commercial-ac-repair","wrench"),
            ("Commercial Installation","New commercial HVAC installations designed for efficiency and your specific space requirements.","/services/commercial-installation","download"),
            ("Commercial Maintenance","Preventative maintenance programs to keep your commercial systems running reliably year-round.","/services/commercial-maintenance","settings"),
        ]),
        faq_section([
            ("Do you work on rooftop commercial units?","Absolutely. Our technicians are experienced with all types of commercial equipment including rooftop units (RTUs), split systems, VRF/VRV systems, and package units."),
            ("Can you set up a commercial maintenance contract?","Yes. We offer customized commercial maintenance plans that include regular inspections, filter changes, and preventative service to keep your systems running at peak efficiency."),
            ("Are you available for emergency commercial HVAC repair?","Yes. We provide 24/7 emergency service for commercial customers. We understand that a broken HVAC system can impact your business operations and customer experience."),
        ]),
        related_links([("AC & Cooling","/services/ac-cooling"),("Heating Services","/services/heating"),("Ductwork & Air Quality","/services/ductwork-air-quality")]),
    ], "Commercial HVAC Needs?\\nCall Code Blue")

# Hub 4: Ductwork & Air Quality
build_page(f"{BASE}/services/ductwork-air-quality.astro",
    "Ductwork & Indoor Air Quality Services | Code Blue HVAC | North Las Vegas",
    "Professional ductwork installation, repair, cleaning, and air purification services in North Las Vegas. Improve your indoor air quality. Call (702) 887-1656.",
    [
        hero_section([("Home","/"),("Services","/services/ductwork-air-quality"),("Ductwork & Air Quality",None)], "Ductwork &<br />Air Quality", "Professional ductwork solutions and indoor air quality services for healthier, more comfortable living."),
        intro_2col("Air Quality Experts","Breathe Cleaner","Indoor Air",["Your ductwork is the circulatory system of your home. When ducts are damaged, dirty, or improperly installed, your HVAC system works harder, your energy bills climb, and the air you breathe suffers.","Code Blue HVAC provides complete ductwork services—from new installations and repairs to thorough duct cleaning—along with advanced air purification solutions. We help Las Vegas homeowners improve indoor air quality, reduce allergens, and maximize HVAC efficiency.","With the Las Vegas desert environment bringing dust, allergens, and dry air into your home, proper ductwork and air quality solutions are more important here than almost anywhere else in the country."],"wind"),
        service_grid_hub("Ductwork & IAQ Services","Ductwork &","Air Quality",[
            ("Ductwork Installation","Custom ductwork design and installation for optimal airflow and efficiency.","/services/ductwork-installation","download"),
            ("Ductwork Repair","Seal leaks, fix damage, and restore your duct system to peak performance.","/services/ductwork-repair","wrench"),
            ("Duct Cleaning","Professional duct cleaning to remove dust, allergens, and debris from your system.","/services/duct-cleaning","wind"),
            ("Air Purification","Advanced air purification systems to eliminate contaminants and improve indoor air quality.","/services/air-purification","filter"),
        ]),
        faq_section([
            ("How often should air ducts be cleaned?","We recommend duct cleaning every 3-5 years, or sooner if you notice excessive dust, musty odors, visible mold, or if anyone in your household has allergies or respiratory issues."),
            ("Can leaky ducts affect my energy bills?","Absolutely. Leaky ductwork can waste 20-30% of the air your HVAC system produces. Sealing and repairing ducts can significantly reduce your energy bills and improve comfort."),
            ("What air purification systems do you install?","We install a range of air purification solutions including UV germicidal lights, HEPA filtration systems, whole-home air purifiers, and humidity control systems."),
        ]),
        related_links([("AC & Cooling","/services/ac-cooling"),("Heating Services","/services/heating"),("Ductless Mini-Splits","/services/ductless-mini-splits")]),
    ], "Improve Your Air Quality\\nCall Code Blue")

# Hub 5: Ductless Mini-Splits
build_page(f"{BASE}/services/ductless-mini-splits.astro",
    "Ductless Mini-Split Installation & Repair | Code Blue HVAC | North Las Vegas",
    "Expert ductless mini-split installation and repair in North Las Vegas. Energy-efficient zone cooling and heating. Call (702) 887-1656.",
    [
        hero_section([("Home","/"),("Services","/services/ductless-mini-splits"),("Ductless Mini-Splits",None)], "Ductless<br />Mini-Splits", "Efficient zone-by-zone cooling and heating without the need for traditional ductwork."),
        intro_2col("Mini-Split Experts","Zone Comfort","Without Ducts",["Ductless mini-split systems offer a versatile, energy-efficient alternative to traditional central HVAC. They are ideal for room additions, converted garages, home offices, and older homes without existing ductwork.","Code Blue HVAC installs and services ductless systems from leading brands including Fujitsu, Bosch, LG, and others. Mini-splits deliver exceptional efficiency with individual zone control, letting you cool or heat only the rooms you use.","With no ductwork required, installation is faster and less invasive than traditional systems. Plus, many mini-split systems qualify for energy rebates and tax incentives, making them a smart investment for Las Vegas homeowners."],"zap"),
        service_grid_hub("Mini-Split Services","Ductless","Services",[
            ("Ductless Installation","Professional mini-split installation with custom placement for optimal comfort and efficiency.","/services/ductless-installation","download"),
            ("Ductless Repair","Expert mini-split diagnosis and repair to keep your ductless system running smoothly.","/services/ductless-repair","wrench"),
        ]),
        faq_section([
            ("How much does a ductless mini-split system cost?","Costs vary based on the number of zones, system capacity, and installation complexity. A single-zone system typically starts around $3,000-$5,000 installed. We provide free estimates for every project."),
            ("Are mini-splits energy efficient?","Yes. Ductless mini-splits are among the most energy-efficient HVAC options available, with SEER ratings often exceeding 20. They also eliminate the energy losses associated with ductwork."),
            ("Can a mini-split heat and cool?","Yes. Most modern mini-split systems are heat pumps that provide both cooling and heating. They work efficiently even in cooler weather, making them a great year-round solution."),
        ]),
        related_links([("AC & Cooling","/services/ac-cooling"),("Heating Services","/services/heating"),("Ductwork & Air Quality","/services/ductwork-air-quality")]),
    ], "Interested in Mini-Splits?\\nCall Code Blue")


# ============================================================
# SPOKE PAGES
# ============================================================
print("\\n=== Building Spoke Pages ===")

spokes = [
    # AC Spokes
    ("ac-repair", "AC Repair", "AC & Cooling", "/services/ac-cooling", "Fast, reliable AC repair in North Las Vegas and the Las Vegas Valley. Same-day service available, all brands serviced.", "Expert AC Repair", "Fast, Reliable", "AC Repair",
     ["When your AC stops working in the Las Vegas heat, you need a solution fast. Code Blue HVAC provides expert AC repair with same-day service availability and 24/7 emergency response.","Our licensed technicians diagnose the problem quickly and accurately, using state-of-the-art diagnostic tools to identify the root cause—not just the symptoms. We repair all makes and models and carry common parts on our trucks for faster repairs.","From refrigerant leaks and compressor failures to thermostat issues and electrical problems, we handle it all with upfront pricing and no surprise charges."],
     "Our AC Repair Process", "What to", "Expect",
     ["When you call Code Blue HVAC for AC repair, we dispatch a technician as quickly as possible—often within hours. Upon arrival, your technician performs a thorough diagnostic of your entire system, identifies the issue, and provides a clear, upfront estimate before any work begins.","We carry common replacement parts on our service trucks so many repairs can be completed in a single visit. For parts that need to be ordered, we expedite delivery and schedule your follow-up at a time that works for you. Every repair is backed by our satisfaction guarantee."],
     [("How much does AC repair cost in Las Vegas?","AC repair costs vary based on the issue. Simple fixes like capacitor replacements may cost $150-$300, while more complex repairs like compressor replacements can range from $800-$2,500. We always provide an upfront estimate before beginning work."),("My AC is blowing warm air. What could be wrong?","Common causes include low refrigerant, a dirty air filter, a malfunctioning compressor, or a faulty thermostat. Our technicians can diagnose the exact issue and recommend the most cost-effective solution."),("Do you charge extra for weekend or evening repairs?","No. Code Blue HVAC does not charge extra for after-hours, weekend, or holiday service calls. Our pricing is the same 24/7.")],
     [("AC Installation","/services/ac-installation"),("AC Replacement","/services/ac-replacement"),("AC Maintenance","/services/ac-maintenance"),("Emergency AC Repair","/services/emergency-ac-repair")]),

    ("ac-installation", "AC Installation", "AC & Cooling", "/services/ac-cooling", "Professional AC installation in North Las Vegas. New systems sized for your home with top brands. Free estimates. Call (702) 887-1656.", "New System Installation", "Professional AC", "Installation",
     ["A properly sized and installed air conditioning system is essential for comfort and efficiency in the Las Vegas desert climate. Code Blue HVAC provides expert AC installation services using top-quality equipment from Ruud, Rheem, Carrier, Trane, and other leading brands.","Our comfort advisors start with a thorough evaluation of your home, considering square footage, insulation, window orientation, ceiling height, and your familys comfort preferences. This ensures your new system is perfectly sized—not too big, not too small.","We handle everything from equipment selection and permit pulling to professional installation and system commissioning. Every installation includes a full warranty and our satisfaction guarantee."],
     "Installation Process", "How We", "Install",
     ["Our installation process begins with a free in-home consultation where we assess your needs and recommend the right system. We present options at different price points so you can make an informed decision. Once you approve the estimate, we schedule installation at your convenience—often within days.","On installation day, our team handles everything professionally, including removing and disposing of your old equipment, installing the new system, connecting electrical and refrigerant lines, and performing a complete system commissioning to ensure everything runs perfectly."],
     [("What size AC system do I need?","Sizing depends on your homes square footage, insulation levels, window exposure, and other factors. We perform a Manual J load calculation to determine the exact capacity needed for optimal performance."),("How long does AC installation take?","A standard replacement typically takes one day. If ductwork modifications are needed, it may take 2-3 days. We always provide an accurate timeline during your free estimate."),("Do you offer financing for new AC systems?","Yes. We offer flexible financing options to make a new AC system affordable. Visit our financing page or call us for details.")],
     [("AC Repair","/services/ac-repair"),("AC Replacement","/services/ac-replacement"),("AC Maintenance","/services/ac-maintenance")]),

    ("ac-replacement", "AC Replacement", "AC & Cooling", "/services/ac-cooling", "AC replacement services in North Las Vegas. Upgrade to a high-efficiency system. Free estimates, financing available. Call (702) 887-1656.", "System Replacement", "Time for an", "AC Upgrade",
     ["If your AC system is over 10-15 years old, requires frequent repairs, or struggles to keep your home cool, it may be time for a replacement. Upgrading to a modern high-efficiency system can dramatically reduce your energy bills while providing better, more consistent comfort.","Code Blue HVAC makes the replacement process seamless. We help you select the right system for your home and budget, handle professional removal of your old equipment, and install your new system with precision and care.","Modern AC systems offer significantly higher SEER ratings, meaning they use less energy to produce the same cooling output. In the Las Vegas climate where AC runs 6-8 months per year, the energy savings from a high-efficiency upgrade can be substantial."],
     "Signs You Need Replacement", "When to", "Replace",
     ["Several signs indicate your AC may need replacement rather than repair: the system is over 15 years old, requires repairs costing more than 50% of a new systems value, uses R-22 refrigerant (which is being phased out), or your energy bills are climbing despite regular maintenance.","Our technicians provide honest assessments. If a repair makes more sense financially, well tell you. We want to earn your trust for the long term, not just a single sale."],
     [("How much does AC replacement cost in Las Vegas?","A full AC replacement typically ranges from $5,000-$15,000 depending on system size, efficiency rating, and installation requirements. We provide free estimates and offer financing options."),("Should I replace just the AC or the whole system?","If your furnace or air handler is also aging, replacing both at the same time ensures optimal compatibility and efficiency. We can advise on the best approach during your consultation."),("What brands do you install?","We install systems from Ruud, Rheem, Carrier, Trane, Lennox, York, Bryant, Amana, Bosch, Fujitsu, LG, and other top brands.")],
     [("AC Repair","/services/ac-repair"),("AC Installation","/services/ac-installation"),("AC Maintenance","/services/ac-maintenance")]),

    ("ac-maintenance", "AC Maintenance", "AC & Cooling", "/services/ac-cooling", "AC maintenance and tune-up services in North Las Vegas. Prevent breakdowns and extend system life. Call (702) 887-1656.", "Preventative Maintenance", "Keep Your AC", "Running Strong",
     ["Regular AC maintenance is the single most important thing you can do to prevent unexpected breakdowns, extend the life of your system, and keep your energy bills in check. In the Las Vegas climate, where your AC works harder and longer than almost anywhere else, preventative maintenance is essential.","Code Blue HVACs maintenance plans include thorough system inspections, coil cleaning, refrigerant level checks, electrical connection testing, thermostat calibration, and more. We catch small problems before they become expensive emergencies.","Our affordable maintenance plans provide priority scheduling, discounted service rates, and the peace of mind that comes from knowing your system is professionally maintained."],
     "What We Inspect", "Comprehensive", "Tune-Up",
     ["During each maintenance visit, our technicians perform a comprehensive inspection covering all critical components: refrigerant levels, electrical connections, capacitors, contactors, compressor amperage, condenser and evaporator coils, blower motor, air filter, thermostat calibration, and drain line.","We also provide recommendations for any issues we find and prioritize them by urgency so you can make informed decisions about repairs or upgrades."],
     [("How often should I get AC maintenance?","In Las Vegas, we recommend twice-yearly maintenance—a spring tune-up before cooling season and a fall inspection before heating season. This keeps your system running efficiently year-round."),("Does maintenance really save money?","Yes. Regular maintenance can reduce your energy bills by 15-25% and extends your systems lifespan by several years. It also catches small issues before they become major, expensive repairs."),("Do you offer maintenance plans?","Yes. We offer affordable maintenance plans that include two annual visits, priority scheduling, and discounted service rates. Call us for plan details and pricing.")],
     [("AC Repair","/services/ac-repair"),("AC Installation","/services/ac-installation"),("Emergency AC Repair","/services/emergency-ac-repair")]),

    ("emergency-ac-repair", "Emergency AC Repair", "AC & Cooling", "/services/ac-cooling", "24/7 emergency AC repair in North Las Vegas. No extra charge for nights, weekends, or holidays. Call (702) 887-1656 now.", "Emergency Service", "24/7 Emergency", "AC Repair",
     ["When your AC fails in the middle of a Las Vegas summer, it is more than an inconvenience—it can be dangerous, especially for young children, elderly family members, and pets. Code Blue HVAC provides 24/7 emergency AC repair with no extra charges for nights, weekends, or holidays.","Our emergency technicians carry common replacement parts on their trucks and are equipped to handle most repairs on the spot. We prioritize emergency calls and strive to have a technician at your door as quickly as possible.","Whether your AC stopped working at 2 AM on a Sunday or during a holiday weekend, you can count on Code Blue HVAC to respond quickly and get your system running again."],
     "Emergency Response", "When to Call", "For Help",
     ["Call us immediately if your AC has completely stopped working during extreme heat, if you hear unusual grinding or screeching noises, if you smell burning or electrical odors, if your system is leaking refrigerant, or if your home temperature is rising rapidly.","Our dispatcher will assess your situation over the phone and send the nearest available technician to your location. We keep you informed throughout the process so you know when to expect help."],
     [("Do you charge extra for emergency calls?","No. Code Blue HVAC does not charge extra for emergency, after-hours, weekend, or holiday service calls. Our pricing is the same 24/7."),("How quickly can you respond to an emergency?","Response times vary based on demand and location, but we strive to have a technician at your door within a few hours of your call. We prioritize emergencies based on severity."),("What should I do while waiting for the technician?","Turn off your AC system to prevent further damage. Close blinds and curtains to keep heat out. If safe to do so, check your thermostat batteries and air filter. Stay hydrated and move to the coolest area of your home.")],
     [("AC Repair","/services/ac-repair"),("AC Maintenance","/services/ac-maintenance"),("AC Replacement","/services/ac-replacement")]),

    # Heating Spokes
    ("furnace-repair", "Furnace Repair", "Heating", "/services/heating", "Expert furnace repair in North Las Vegas. Gas and electric furnaces, all brands. 24/7 emergency service. Call (702) 887-1656.", "Furnace Repair Experts", "Fast, Expert", "Furnace Repair",
     ["When your furnace stops working on a cold Las Vegas night, you need a reliable repair service you can trust. Code Blue HVAC provides fast furnace repair for all makes and models, including gas furnaces, electric furnaces, and heat pump systems.","Our technicians arrive with the diagnostic tools and common parts needed to complete most repairs in a single visit. We diagnose the problem accurately, explain your options clearly, and provide upfront pricing before beginning any work.","From ignitor failures and thermocouple issues to blower motor problems and gas valve malfunctions, we handle all furnace repairs with expertise and professionalism."],
     "Common Furnace Issues", "Signs Your Furnace", "Needs Repair",
     ["Warning signs that your furnace needs professional attention include: no heat output, weak airflow, unusual noises such as banging or squealing, frequent cycling on and off, yellow pilot light instead of blue, higher than normal energy bills, and cold spots in your home.","If you notice any of these symptoms, dont wait for a complete breakdown. Call Code Blue HVAC for a prompt diagnosis and repair. Early intervention often prevents more costly repairs down the line."],
     [("How much does furnace repair cost?","Furnace repair costs vary based on the issue. Minor repairs like ignitor replacement may cost $150-$300, while major repairs can range from $500-$1,500. We always provide upfront pricing."),("Can you repair both gas and electric furnaces?","Yes. Our technicians are trained on gas, electric, and dual-fuel heating systems from all major brands."),("Is it worth repairing an old furnace?","If your furnace is under 15 years old and the repair cost is less than 50% of replacement cost, repair usually makes sense. For older units, we can help you weigh the costs and benefits of repair vs. replacement.")],
     [("Furnace Installation","/services/furnace-installation"),("Heating Maintenance","/services/heating-maintenance"),("AC Repair","/services/ac-repair")]),

    ("furnace-installation", "Furnace Installation", "Heating", "/services/heating", "New furnace installation in North Las Vegas. Energy-efficient systems, professional installation. Free estimates. Call (702) 887-1656.", "New Furnace Installation", "Professional", "Furnace Installation",
     ["A new furnace is a significant investment in your homes comfort and efficiency. Code Blue HVAC provides expert furnace installation with proper sizing, professional setup, and full warranty coverage.","We offer a range of furnace options from top brands, from high-efficiency 95%+ AFUE gas furnaces to reliable electric models. Our comfort advisors help you select the right system based on your homes heating needs, your budget, and your long-term energy savings goals.","Every installation includes proper equipment sizing, professional ductwork connections, electrical and gas line hookups, thermostat setup, and a complete system test to ensure perfect operation from day one."],
     "Our Process", "Installation", "Steps",
     ["Our furnace installation process starts with a free in-home evaluation. We assess your current system, measure your home, and discuss your comfort goals. We then present options at different efficiency levels and price points so you can choose with confidence.","On installation day, our team arrives on time with all necessary equipment. We remove your old furnace, install the new system, make all necessary connections, and perform thorough testing. We also walk you through your new systems operation and answer any questions."],
     [("What size furnace do I need?","Furnace sizing depends on your homes square footage, insulation, window quality, and ceiling height. We perform a load calculation to determine the right capacity for your home."),("How long does furnace installation take?","A standard furnace installation typically takes 4-8 hours. If additional work is needed such as ductwork modifications, it may extend to two days."),("Do you offer financing for new furnaces?","Yes. We offer flexible financing options to make a new furnace affordable. Contact us for current rates and terms.")],
     [("Furnace Repair","/services/furnace-repair"),("Heating Maintenance","/services/heating-maintenance"),("AC Installation","/services/ac-installation")]),

    ("heating-maintenance", "Heating Maintenance", "Heating", "/services/heating", "Heating and furnace maintenance in North Las Vegas. Keep your system safe, efficient, and reliable. Call (702) 887-1656.", "Heating Maintenance", "Keep Your Heating", "System Safe",
     ["Annual heating maintenance is critical for safety, efficiency, and longevity. Gas furnaces in particular require regular inspection to ensure safe operation and prevent carbon monoxide risks.","Code Blue HVACs heating maintenance service includes a comprehensive inspection of all heating components, cleaning of burners and heat exchangers, testing of safety controls, thermostat calibration, and airflow verification.","Our maintenance plans are designed for Las Vegas homeowners who want reliable heating without unexpected breakdowns or safety concerns. Prevention is always less expensive than emergency repair."],
     "Maintenance Checklist", "What We", "Inspect",
     ["Our comprehensive heating maintenance includes: heat exchanger inspection for cracks, burner cleaning and adjustment, ignition system testing, safety control verification, gas pressure checks, blower motor lubrication, air filter replacement, thermostat calibration, and carbon monoxide testing.","We document our findings and provide a detailed report of your systems condition along with any recommendations for repairs or improvements."],
     [("How often should I have my furnace maintained?","We recommend annual heating maintenance, ideally in the fall before heating season begins. This ensures your system is safe and ready for winter."),("Does heating maintenance prevent carbon monoxide leaks?","Yes. One of the most important aspects of heating maintenance is inspecting the heat exchanger for cracks that could allow carbon monoxide to enter your home. Regular maintenance helps catch these issues early."),("What does a heating tune-up include?","Our tune-up includes a complete system inspection, cleaning, lubrication, calibration, safety testing, and filter replacement. Its a thorough service that keeps your system running safely and efficiently.")],
     [("Furnace Repair","/services/furnace-repair"),("Furnace Installation","/services/furnace-installation"),("AC Maintenance","/services/ac-maintenance")]),

    # Commercial Spokes
    ("commercial-ac-repair", "Commercial AC Repair", "Commercial HVAC", "/services/commercial-hvac", "Fast commercial AC repair in North Las Vegas. Minimize downtime for your business. 24/7 emergency service. Call (702) 887-1656.", "Commercial AC Repair", "Fast Commercial", "AC Repair",
     ["A broken AC system can cost your business customers, productivity, and revenue. Code Blue HVAC provides rapid commercial AC repair to minimize downtime and keep your business environment comfortable.","Our technicians have extensive experience with commercial equipment including rooftop units, split systems, VRF/VRV systems, and package units. We service all brands and carry common commercial parts for faster repairs.","We offer priority service for commercial customers with service agreements and 24/7 emergency response for critical failures."],
     "Our Commercial Approach", "Minimizing", "Downtime",
     ["We understand that every hour of HVAC downtime affects your bottom line. Our commercial repair process emphasizes speed without sacrificing quality. We dispatch experienced technicians who arrive prepared with diagnostic equipment and common parts.","For businesses with service agreements, we offer priority scheduling and guaranteed response times to ensure your operations are disrupted as little as possible."],
     [("How quickly can you respond to a commercial AC emergency?","We provide 24/7 emergency commercial service. Response times depend on demand and location, but we prioritize commercial emergencies to minimize business impact."),("Do you service rooftop units?","Yes. Our technicians are experienced with all types of commercial rooftop units from leading manufacturers."),("Can you set up a commercial service agreement?","Absolutely. Our commercial maintenance agreements include priority service, scheduled maintenance visits, and discounted repair rates.")],
     [("Commercial Installation","/services/commercial-installation"),("Commercial Maintenance","/services/commercial-maintenance"),("AC Repair","/services/ac-repair")]),

    ("commercial-installation", "Commercial HVAC Installation", "Commercial HVAC", "/services/commercial-hvac", "Commercial HVAC installation in North Las Vegas. New systems designed for your business. Free estimates. Call (702) 887-1656.", "Commercial Installation", "Commercial HVAC", "Installation",
     ["Whether you are building a new commercial space or upgrading an existing system, Code Blue HVAC provides professional commercial HVAC installation tailored to your business requirements.","We work with architects, general contractors, and property managers to design and install commercial systems that deliver optimal comfort, efficiency, and reliability. From single-zone retail spaces to multi-zone office complexes, we have the experience and expertise to deliver.","Our commercial installation services include equipment selection, load calculation, ductwork design, installation, commissioning, and staff training on system operation."],
     "Our Process", "Professional", "Approach",
     ["Every commercial installation begins with a detailed assessment of your space, occupancy patterns, and comfort requirements. We design a system that balances performance with energy efficiency, and we present options at multiple price points.","Our installation teams work efficiently to minimize disruption to your business, often completing installations during off-hours when possible. Every system is thoroughly tested and commissioned before handoff."],
     [("What types of commercial systems do you install?","We install all types of commercial HVAC equipment including rooftop units, split systems, VRF/VRV systems, package units, and make-up air units."),("Do you handle permits and inspections?","Yes. We handle all necessary permits, inspections, and code compliance for commercial installations in Clark County."),("Can you work around our business hours?","Absolutely. We offer flexible scheduling including evenings and weekends to minimize disruption to your business operations.")],
     [("Commercial AC Repair","/services/commercial-ac-repair"),("Commercial Maintenance","/services/commercial-maintenance")]),

    ("commercial-maintenance", "Commercial HVAC Maintenance", "Commercial HVAC", "/services/commercial-hvac", "Commercial HVAC maintenance programs in North Las Vegas. Prevent breakdowns and optimize efficiency. Call (702) 887-1656.", "Commercial Maintenance", "Preventative", "Commercial Maintenance",
     ["A well-maintained commercial HVAC system operates more efficiently, lasts longer, and breaks down less often. Code Blue HVACs commercial maintenance programs are designed to keep your business systems running reliably while controlling operating costs.","Our customized maintenance plans include regular inspections, filter changes, coil cleaning, refrigerant checks, electrical testing, and detailed documentation for your records.","We work with you to develop a maintenance schedule that minimizes disruption to your operations while ensuring your systems receive the attention they need to perform at their best."],
     "Program Benefits", "Why Commercial", "Maintenance Matters",
     ["Regular commercial maintenance delivers measurable benefits: reduced energy costs of 15-30%, fewer emergency repairs, extended equipment lifespan, better indoor air quality for employees and customers, and compliance with manufacturer warranty requirements.","Our maintenance reports provide detailed documentation that can help with budgeting, insurance, and property management decisions."],
     [("What does a commercial maintenance plan include?","Our plans are customized to your equipment and needs but typically include quarterly inspections, filter changes, coil cleaning, refrigerant checks, electrical testing, and priority emergency service."),("How much can maintenance save on energy costs?","Well-maintained commercial systems typically operate 15-30% more efficiently than neglected ones. For businesses with significant HVAC loads, this can translate to thousands of dollars in annual savings."),("Do you provide maintenance documentation?","Yes. We provide detailed reports after every maintenance visit, documenting system condition, work performed, and any recommendations.")],
     [("Commercial AC Repair","/services/commercial-ac-repair"),("Commercial Installation","/services/commercial-installation")]),

    # Ductwork & IAQ Spokes
    ("ductwork-installation", "Ductwork Installation", "Ductwork & Air Quality", "/services/ductwork-air-quality", "Custom ductwork installation in North Las Vegas. Optimize airflow and HVAC efficiency. Call (702) 887-1656.", "Ductwork Installation", "Professional", "Ductwork Installation",
     ["Properly designed and installed ductwork is essential for efficient HVAC operation and consistent comfort throughout your home. Code Blue HVAC provides custom ductwork solutions tailored to your space.","Whether you are building new, renovating, or replacing aging ductwork, our technicians design and install duct systems that maximize airflow, minimize energy waste, and deliver even temperatures to every room.","We use high-quality materials and follow industry best practices for sizing, sealing, and insulating ductwork to ensure long-lasting performance."],
     "Custom Design", "Engineered for", "Your Home",
     ["Every ductwork installation begins with a detailed assessment of your home layout, HVAC system requirements, and comfort goals. We design a duct system that delivers the right amount of airflow to every room while minimizing energy losses.","Our installations include proper sealing at all joints, adequate insulation for unconditioned spaces, and smooth transitions to minimize air turbulence and noise."],
     [("How long does ductwork installation take?","A complete ductwork installation typically takes 2-5 days depending on the size and complexity of your home. Replacements in existing homes may take less time."),("Can new ductwork improve my comfort?","Absolutely. Properly designed ductwork eliminates hot and cold spots, reduces noise, and can improve your HVAC systems efficiency by 20-30%."),("Do you install ductwork for new construction?","Yes. We work with builders and homeowners on new construction ductwork installations, ensuring optimal design from the start.")],
     [("Ductwork Repair","/services/ductwork-repair"),("Duct Cleaning","/services/duct-cleaning"),("AC Installation","/services/ac-installation")]),

    ("ductwork-repair", "Ductwork Repair", "Ductwork & Air Quality", "/services/ductwork-air-quality", "Ductwork repair and sealing in North Las Vegas. Fix leaks, restore efficiency. Call (702) 887-1656.", "Ductwork Repair", "Seal Leaks &", "Restore Efficiency",
     ["Damaged or leaky ductwork is one of the most common—and most overlooked—causes of HVAC inefficiency, uneven temperatures, and high energy bills. Code Blue HVAC provides professional ductwork repair and sealing to restore your systems performance.","Common ductwork issues include disconnected joints, crushed or kinked flex ducts, deteriorated sealing tape, pest damage, and corrosion. These problems allow conditioned air to escape into attics, crawl spaces, and wall cavities.","Our technicians inspect your entire duct system, identify all problem areas, and perform professional repairs using industry-approved materials and methods."],
     "Common Issues", "Signs of Duct", "Problems",
     ["Warning signs of ductwork problems include rooms that are consistently too hot or too cold, excessive dust in your home, higher than normal energy bills, and whistling or rattling sounds from your vents.","Our duct repair services include leak sealing with mastic and foil tape, reconnecting separated joints, replacing damaged sections, and re-insulating exposed ducts. We also test airflow before and after repairs to verify improvement."],
     [("How do I know if my ducts are leaking?","Signs include uneven temperatures between rooms, excessive dust, high energy bills, and rooms that never seem to get comfortable. A professional duct inspection can identify leaks and measure their impact."),("Can duct sealing reduce my energy bills?","Yes. Sealing leaky ducts can reduce your HVAC energy consumption by 20-30%, which translates to significant savings on your NV Energy bills."),("Do you use mastic or duct tape for sealing?","We use professional-grade mastic sealant and UL-listed foil tape for all duct sealing work. Standard duct tape is not appropriate for HVAC ductwork and will fail over time.")],
     [("Ductwork Installation","/services/ductwork-installation"),("Duct Cleaning","/services/duct-cleaning"),("Air Purification","/services/air-purification")]),

    ("duct-cleaning", "Duct Cleaning", "Ductwork & Air Quality", "/services/ductwork-air-quality", "Professional duct cleaning in North Las Vegas. Remove dust, allergens, and debris. Breathe cleaner air. Call (702) 887-1656.", "Duct Cleaning", "Professional", "Duct Cleaning",
     ["Over time, your ductwork accumulates dust, pet dander, pollen, mold spores, and other contaminants that circulate through your home every time your HVAC system runs. Professional duct cleaning removes these pollutants and improves your indoor air quality.","In the Las Vegas desert environment, dust accumulation is particularly aggressive. Sand, construction dust, and desert particulates find their way into your home and HVAC system, making regular duct cleaning even more important.","Code Blue HVAC uses professional-grade equipment including high-powered vacuums and rotary brush systems to thoroughly clean your entire duct system, from supply and return ducts to registers and grilles."],
     "Our Cleaning Process", "Thorough &", "Professional",
     ["Our duct cleaning process begins with a visual inspection of your duct system using cameras to assess the level of contamination. We then seal all registers except the one being cleaned and use high-powered vacuum equipment to create negative pressure in the system.","Our technicians clean each duct run individually using rotary brushes and compressed air to dislodge debris, which is then captured by our vacuum system. We also clean registers, grilles, and the area around your air handler."],
     [("How often should I have my ducts cleaned?","We recommend duct cleaning every 3-5 years, or more frequently if you have pets, allergies, recent construction or renovation, or visible mold growth in your ducts."),("Will duct cleaning reduce dust in my home?","Yes. Clean ducts mean less dust being circulated through your home. Many customers notice a significant reduction in household dust after professional duct cleaning."),("How long does duct cleaning take?","A typical residential duct cleaning takes 2-4 hours depending on the size of your home and the number of duct runs. We work efficiently to minimize disruption.")],
     [("Air Purification","/services/air-purification"),("Ductwork Repair","/services/ductwork-repair"),("AC Maintenance","/services/ac-maintenance")]),

    ("air-purification", "Air Purification", "Ductwork & Air Quality", "/services/ductwork-air-quality", "Whole-home air purification systems in North Las Vegas. UV lights, HEPA filters, and more. Call (702) 887-1656.", "Air Purification", "Breathe Cleaner", "Indoor Air",
     ["Indoor air quality is a growing concern for Las Vegas homeowners. Between desert dust, allergens, and the sealed nature of modern homes, the air inside your home can be significantly more polluted than outdoor air.","Code Blue HVAC installs a range of air purification solutions that integrate with your existing HVAC system to filter, sanitize, and purify the air throughout your entire home. Options include UV germicidal lights, whole-home HEPA filtration, electronic air cleaners, and advanced air scrubber systems.","These systems work continuously with your HVAC to remove airborne particles, neutralize bacteria and viruses, eliminate odors, and reduce allergens—creating a healthier environment for your family."],
     "Solutions We Offer", "Air Quality", "Options",
     ["We offer multiple air purification technologies to match your needs and budget: UV germicidal lights installed in your ductwork to kill biological contaminants, whole-home HEPA filters that capture 99.97% of particles, electronic air cleaners for enhanced filtration, and advanced air scrubber systems that actively purify air throughout your home.","During your consultation, we assess your specific air quality concerns and recommend the most effective solution. Many systems can be installed in a single visit with minimal disruption."],
     [("What is the best air purification system for allergies?","For allergy sufferers, we typically recommend a combination of a whole-home HEPA filter and UV germicidal lights. This combination captures airborne particles while neutralizing biological contaminants."),("Can air purification help with Las Vegas dust?","Absolutely. Whole-home filtration systems are particularly effective at capturing the fine desert dust that is prevalent in the Las Vegas Valley."),("How much does a whole-home air purifier cost?","Costs vary by system type. UV germicidal lights start around $500-$800 installed, while comprehensive whole-home purification systems can range from $1,000-$3,000.")],
     [("Duct Cleaning","/services/duct-cleaning"),("AC Maintenance","/services/ac-maintenance"),("Ductwork Repair","/services/ductwork-repair")]),

    # Ductless Spokes
    ("ductless-installation", "Ductless Installation", "Ductless Mini-Splits", "/services/ductless-mini-splits", "Ductless mini-split installation in North Las Vegas. Zone cooling and heating. Free estimates. Call (702) 887-1656.", "Ductless Installation", "Professional", "Ductless Installation",
     ["Ductless mini-split systems offer the ultimate in flexible, efficient climate control. Code Blue HVAC provides professional ductless installation for homes and businesses throughout the Las Vegas Valley.","Mini-splits are perfect for room additions, converted garages, home offices, sunrooms, and older homes without existing ductwork. They provide individualized zone control, allowing you to heat or cool specific areas without conditioning your entire home.","We install systems from top brands including Fujitsu, Bosch, LG, and Daikin. Whether you need a single-zone system for one room or a multi-zone system for your entire home, we design and install solutions that maximize comfort and efficiency."],
     "Why Go Ductless", "Benefits of", "Mini-Splits",
     ["Ductless mini-splits offer several advantages over traditional systems: no ductwork required, individual zone control, higher energy efficiency (SEER ratings often exceeding 20), quiet operation, and easy installation with minimal construction.","For Las Vegas homeowners, the efficiency benefits are particularly significant. Zone control means you only cool or heat the rooms you are using, which can dramatically reduce energy costs compared to whole-home central systems."],
     [("How many zones do I need?","The number of zones depends on your homes layout and your comfort goals. A single-zone system handles one room, while multi-zone systems can serve 2-5 or more rooms from a single outdoor unit. We help you determine the right configuration during your free consultation."),("Is ductless installation invasive?","No. Ductless installation requires only a small hole (about 3 inches) through an exterior wall for the refrigerant lines. There is no need for major construction or ductwork installation."),("Are ductless systems energy efficient?","Very. Ductless mini-splits are among the most efficient HVAC systems available, with SEER ratings often exceeding 20. They also eliminate the 20-30% energy losses typically associated with ductwork.")],
     [("Ductless Repair","/services/ductless-repair"),("AC Installation","/services/ac-installation"),("Ductwork Installation","/services/ductwork-installation")]),

    ("ductless-repair", "Ductless Repair", "Ductless Mini-Splits", "/services/ductless-mini-splits", "Ductless mini-split repair in North Las Vegas. Expert diagnosis and repair for all brands. Call (702) 887-1656.", "Ductless Repair", "Expert", "Ductless Repair",
     ["Ductless mini-split systems are reliable, but like any mechanical system, they can develop issues over time. Code Blue HVAC provides expert ductless repair services for all brands and models.","Common mini-split issues include refrigerant leaks, drainage problems, sensor malfunctions, compressor issues, and electrical faults. Our technicians are trained on the specific diagnostic procedures for ductless systems and carry common replacement parts for faster repairs.","Whether your mini-split is not cooling, making unusual noises, leaking water, or displaying error codes, we diagnose the problem quickly and provide an upfront repair estimate."],
     "Common Issues", "Ductless System", "Problems",
     ["Mini-split systems may exhibit several warning signs that indicate a need for repair: reduced cooling or heating output, water leaking from the indoor unit, unusual noises, ice formation on coils, error codes on the display, or the system failing to turn on.","If you notice any of these issues, contact Code Blue HVAC for a professional diagnosis. Early repair often prevents more extensive and costly damage to your mini-split system."],
     [("Why is my mini-split leaking water?","The most common cause of indoor unit water leaks is a clogged condensate drain line. This is typically an easy fix for our technicians. Other causes can include frozen coils or improper installation."),("My mini-split is showing an error code. What should I do?","Error codes indicate specific system faults. While some issues may resolve with a simple reset, its best to have a professional diagnose the underlying cause. Note the error code and call us for a diagnosis."),("Do you repair all mini-split brands?","Yes. Our technicians are trained on all major ductless brands including Fujitsu, Bosch, LG, Daikin, Mitsubishi, and others.")],
     [("Ductless Installation","/services/ductless-installation"),("AC Repair","/services/ac-repair"),("Ductwork Repair","/services/ductwork-repair")]),
]

for slug, name, hub_name, hub_url, meta_desc, label, h2_l1, h2_l2, intro_paras, label2, h2b_l1, h2b_l2, process_paras, faqs, rel_links in spokes:
    build_page(f"{BASE}/services/{slug}.astro",
        f"{name} North Las Vegas | {BIZ}",
        meta_desc,
        [
            hero_section([("Home","/"), (hub_name, hub_url), (name, None)], name, meta_desc.split(". Call")[0] + "."),
            content_section(label, h2_l1, h2_l2, intro_paras),
            content_section(label2, h2b_l1, h2b_l2, process_paras, "light"),
            faq_section(faqs),
            related_links(rel_links),
        ], f"Need {name}?\\nCall Code Blue")


# ============================================================
# SERVICE AREA PAGES
# ============================================================
print("\\n=== Building Service Area Pages ===")

# Service Areas Hub
build_page(f"{BASE}/service-areas/index.astro",
    "HVAC Service Areas | North Las Vegas & Clark County | Code Blue HVAC",
    "Code Blue HVAC serves North Las Vegas, Las Vegas, Henderson, Summerlin, Boulder City, Paradise, and surrounding Clark County areas. Call (702) 887-1656.",
    [
        hero_section([("Home","/"),("Service Areas",None)], "Areas We Serve", "Providing expert HVAC services across the Las Vegas Valley and Clark County."),
        content_section("Service Areas","Serving the","Las Vegas Valley",["Code Blue HVAC is proud to serve homeowners and businesses throughout the greater Las Vegas area. Based in North Las Vegas, our service vehicles cover the entire Las Vegas Valley, ensuring fast response times and reliable service no matter where you are in Clark County.","Whether you need emergency AC repair, a new furnace installation, duct cleaning, or a ductless mini-split system, our licensed technicians are available 24/7 to serve you. We offer the same fair pricing and expert workmanship to every community we serve."]),
        service_grid_hub("Our Coverage","Service","Areas",[
            ("North Las Vegas","Our home base. Fast response times and deep knowledge of local HVAC needs.","/service-areas/north-las-vegas","mappin"),
            ("Las Vegas","Serving homes and businesses throughout the Las Vegas metro area.","/service-areas/las-vegas","mappin"),
            ("Henderson","Expert HVAC services for the Henderson community.","/service-areas/henderson","mappin"),
            ("Summerlin","Reliable HVAC solutions for Summerlin residents and businesses.","/service-areas/summerlin","mappin"),
            ("Boulder City","Professional HVAC services extending to Boulder City.","/service-areas/boulder-city","mappin"),
            ("Paradise","Serving the Paradise area with full HVAC capabilities.","/service-areas/paradise","mappin"),
        ]),
        faq_section([
            ("Do you charge extra for service outside North Las Vegas?","No. We charge the same rates across our entire service area. There are no additional travel fees for any location within our coverage zone."),
            ("What is your typical response time?","Response times depend on demand and your location, but we typically arrive within a few hours for standard service calls and prioritize emergencies for the fastest possible response."),
            ("Do you serve commercial properties in all these areas?","Yes. We provide both residential and commercial HVAC services throughout our entire service area."),
        ]),
        related_links([("AC & Cooling","/services/ac-cooling"),("Heating","/services/heating"),("Commercial HVAC","/services/commercial-hvac")]),
    ], "Need HVAC Service?\\nCall Code Blue")

areas = [
    ("north-las-vegas","North Las Vegas","home base","North Las Vegas is where Code Blue HVAC calls home. We know the neighborhoods, the housing styles, and the unique HVAC challenges that residents face. From the established neighborhoods near Cheyenne and Craig to the newer developments in Aliante and Centennial Hills, we provide fast, reliable service to our neighbors."),
    ("las-vegas","Las Vegas","the heart of our service area","From the Strip-adjacent neighborhoods to the residential communities throughout the city, Code Blue HVAC provides comprehensive HVAC services to Las Vegas homeowners and businesses. We understand the demands that Las Vegas extreme climate places on HVAC systems and deliver solutions built to last."),
    ("henderson","Henderson","a key part of our coverage","Henderson residents trust Code Blue HVAC for reliable heating and cooling services. From Green Valley to Anthem and everything in between, our technicians provide the same expert service and fair pricing that has earned us an A+ BBB rating."),
    ("summerlin","Summerlin","an important community we serve","Summerlin homes range from cozy single-family residences to expansive luxury properties, each with unique HVAC requirements. Code Blue HVAC provides tailored solutions for every home size and style in the Summerlin community."),
    ("boulder-city","Boulder City","part of our extended service area","Boulder City homeowners can count on Code Blue HVAC for professional HVAC services. While we are based in North Las Vegas, our service vehicles regularly cover Boulder City to ensure residents have access to quality heating and cooling solutions."),
    ("paradise","Paradise","a neighborhood we proudly serve","The Paradise area encompasses a diverse mix of residential and commercial properties, all of which need reliable HVAC service in the Las Vegas climate. Code Blue HVAC provides expert installation, repair, and maintenance throughout Paradise."),
]

for slug, name, desc_phrase, detail in areas:
    build_page(f"{BASE}/service-areas/{slug}.astro",
        f"HVAC Services in {name}, NV | {BIZ}",
        f"Code Blue HVAC provides expert AC repair, heating, ductwork, and mini-split services in {name}, NV. 24/7 emergency service. Call (702) 887-1656.",
        [
            hero_section([("Home","/"),("Service Areas","/service-areas"),(name,None)], f"{name}<br />HVAC Services", f"Expert residential and commercial HVAC services in {name}, NV and surrounding areas."),
            content_section(f"Serving {name}",f"HVAC Experts in",name,[f"{name} is {desc_phrase} for Code Blue HVAC. {detail}",f"Our full range of services is available to {name} residents and businesses, including AC repair, AC installation, furnace repair, furnace installation, duct cleaning, ductwork services, ductless mini-splits, and commercial HVAC. We offer 24/7 emergency service and 15% discounts for seniors, veterans, and first responders."]),
            content_section("Our Services",f"What We Offer in",name,[f"As a family-owned HVAC contractor with over a decade of experience, Code Blue HVAC delivers professional service to every home and business in {name}. Our technicians arrive fully equipped to handle repairs, installations, maintenance, and emergency situations.","We are a Ruud Pro-Partner and service all major HVAC brands including Rheem, Carrier, Trane, Lennox, York, Bryant, Amana, Bosch, Fujitsu, and LG. Whether you need a simple repair or a complete system replacement, we provide honest assessments and transparent pricing."],"light"),
            faq_section([(f"Do you charge extra for service in {name}?",f"No. {name} is within our standard service area and there are no additional travel or service fees."),(f"How fast can you respond to an emergency in {name}?","We offer 24/7 emergency service and strive to have a technician at your door as quickly as possible, typically within a few hours of your call."),(f"What HVAC services do you offer in {name}?","We offer the full range of HVAC services including AC repair, AC installation, furnace repair, furnace installation, duct cleaning, ductwork repair, ductless mini-splits, air purification, and commercial HVAC services.")]),
            related_links([("AC Repair","/services/ac-repair"),("Heating Services","/services/heating"),("Commercial HVAC","/services/commercial-hvac"),("All Service Areas","/service-areas")]),
        ], f"Need HVAC in {name}?\\nCall Code Blue")


# ============================================================
# TRUST / CONVERSION PAGES
# ============================================================
print("\\n=== Building Trust Pages ===")

# About
build_page(f"{BASE}/about.astro",
    "About Code Blue HVAC | Family-Owned HVAC Contractor | North Las Vegas",
    "Learn about Code Blue HVAC, a family-owned HVAC contractor in North Las Vegas. Owner Chris Montague and team provide expert commercial and residential HVAC service. BBB A+ accredited.",
    [
        hero_section([("Home","/"),("About",None)], "About Us", "Family-owned and operated HVAC contractor proudly serving the Las Vegas Valley since 2020."),
        intro_2col("Our Story","Family-Owned","HVAC Experts",["Code Blue HVAC was founded by Chris Montague with a simple mission: provide honest, reliable HVAC services to the Las Vegas community at fair prices. What started as a small operation has grown into a trusted name in commercial and residential HVAC across Clark County.","As a family-owned and operated business, Chris and his partner Connie bring a personal touch to every interaction. When you call Code Blue HVAC, you are not just another ticket number—you are a neighbor. We treat every home and business with the same care and attention we would give our own.","Our team of licensed, bonded, and insured technicians carries over a decade of combined HVAC experience. We are a Ruud Pro-Partner and service all major brands. Our BBB A+ accreditation reflects our commitment to integrity, transparency, and customer satisfaction."],"shield"),
        content_section("What Sets Us Apart","Why Choose","Code Blue",["Code Blue HVAC is not the biggest HVAC company in Las Vegas, and we are proud of that. Being family-owned means we can focus on what matters most: quality work, honest pricing, and genuine customer relationships.","We offer 24/7 emergency service with no extra charges for nights, weekends, or holidays. We provide 15% discounts for seniors, veterans, and first responders because we believe in honoring those who serve our community. And we back every job with our satisfaction guarantee.","Our name—Code Blue—reflects our commitment to treating every HVAC emergency with urgency and professionalism. When your comfort is on the line, we respond like it matters, because it does."],"light"),
        faq_section([("How long has Code Blue HVAC been in business?","Code Blue HVAC (Chiller Tech Industrial Inc.) was established in June 2020 and has been serving the Las Vegas Valley ever since. Our owner Chris Montague brings over a decade of hands-on HVAC experience."),("Are you licensed and insured?","Yes. Code Blue HVAC is fully licensed, bonded, and insured in the state of Nevada. We are also BBB A+ accredited and a Ruud Pro-Partner."),("Do you serve both residential and commercial customers?","Absolutely. We provide comprehensive HVAC services for both homeowners and businesses throughout the Las Vegas Valley and Clark County.")]),
        related_links([("Our Services","/services/ac-cooling"),("Reviews","/reviews"),("Contact Us","/contact"),("Financing","/financing")]),
    ], "Ready to Work Together?\\nCall Code Blue")

# Reviews
build_page(f"{BASE}/reviews.astro",
    "Customer Reviews | Code Blue HVAC | North Las Vegas",
    "Read what customers say about Code Blue HVAC. BBB A+ accredited with hundreds of positive reviews. Serving North Las Vegas and the Las Vegas Valley.",
    [
        hero_section([("Home","/"),("Reviews",None)], "Reviews", "Hear from our satisfied customers across the Las Vegas Valley."),
        content_section("Customer Feedback","What Our","Customers Say",["At Code Blue HVAC, we measure our success by the satisfaction of our customers. We are proud to maintain a BBB A+ rating and hundreds of positive reviews across Google, Yelp, and other platforms.","Here is what some of our customers have said about their experience with Code Blue HVAC."]),
        content_section("Testimonials","Real Reviews From","Real Customers",['"Hello, my name is Larry. I have been a customer of Code Blue HVAC for three years. The owner, Chris, and his wonderful companion Connie have always taken care of my HVAC needs." — Larry C.','"They really know what they are doing and did a professional job. Very friendly staff." — Dean E.','"Very professional, competitive prices, helped me with all the setup and answered my questions. I would definitely call this company again!" — Lisa A.','"They came on time and acted very quickly and were very reliable. We had a great experience with this company and will definitely use them again." — Cheryl R.','"Prompt, professional service with A/C system repair during intense summer heat — so grateful!" — O. Cruey','"Made it very quick on such short notice." — Robert C.'],"light"),
        related_links([("About Us","/about"),("Contact Us","/contact"),("Our Services","/services/ac-cooling")]),
    ], "Experience the Difference\\nCall Code Blue")

# Financing
build_page(f"{BASE}/financing.astro",
    "HVAC Financing Options | Code Blue HVAC | North Las Vegas",
    "Flexible HVAC financing options from Code Blue HVAC. Make AC and heating system upgrades affordable. Call (702) 887-1656 for details.",
    [
        hero_section([("Home","/"),("Financing",None)], "Financing", "Flexible financing options to make your HVAC upgrades affordable."),
        content_section("Affordable Comfort","Flexible HVAC","Financing",["We believe every family deserves a comfortable home, regardless of budget. That is why Code Blue HVAC offers flexible financing options for qualifying customers on new HVAC system installations and replacements.","Our financing plans feature competitive rates, low monthly payments, and quick approval. Whether you need a new AC system, furnace, ductless mini-split, or complete HVAC overhaul, we can help you find a payment plan that fits your budget.","Contact us today to learn more about available financing options and see if you qualify. Our team will walk you through the process and help you find the best plan for your situation."]),
        content_section("How It Works","Simple","Application Process",["Getting financing for your HVAC project is easy with Code Blue HVAC. Start by scheduling a free consultation where we assess your needs and provide a detailed estimate. Once you have your estimate, we can walk you through available financing options and help you apply.","The application process is quick—most approvals come within minutes. Once approved, we can schedule your installation right away, often within days. You enjoy immediate comfort while making manageable monthly payments."],"light"),
        faq_section([("What can be financed?","We offer financing on new HVAC system installations and replacements, including air conditioning systems, furnaces, heat pumps, ductless mini-splits, and complete system upgrades."),("How do I apply for financing?","Contact us for a free estimate, and we will walk you through available financing options during the consultation process."),("Is there a minimum credit score required?","Qualification requirements vary by financing provider. We work with multiple lenders to offer options for various credit profiles. Contact us to learn more about available programs.")]),
        related_links([("AC Installation","/services/ac-installation"),("Furnace Installation","/services/furnace-installation"),("Specials","/specials"),("Contact Us","/contact")]),
    ], "Ready to Get Started?\\nCall Code Blue")

# Specials
build_page(f"{BASE}/specials.astro",
    "HVAC Specials & Discounts | Code Blue HVAC | North Las Vegas",
    "Current HVAC specials and discounts from Code Blue HVAC. 15% off for seniors, veterans, and first responders. Call (702) 887-1656.",
    [
        hero_section([("Home","/"),("Specials",None)], "Specials", "Current promotions and discounts for our valued customers."),
        content_section("Current Offers","Specials &","Discounts",["Code Blue HVAC is committed to providing exceptional value. In addition to our already competitive pricing, we offer the following specials and discounts to help you save on your HVAC services.","15% Off for Seniors, Veterans & First Responders — We honor those who serve our community with a 15% discount on parts and labor for all services (unit replacements excluded). Just mention this discount when you call to schedule.","Free Estimates on New Installations — Considering a new AC system, furnace, or ductless mini-split? We provide free in-home consultations and estimates with no obligation.","Seasonal Maintenance Plans — Our affordable maintenance plans include twice-yearly system inspections, priority scheduling, and discounted repair rates. Ask about our current plan pricing when you call."]),
        content_section("Savings Tips","Maximize","Your Savings",["Beyond our specials, there are additional ways to save on HVAC costs. Regular maintenance prevents expensive emergency repairs and keeps your system running efficiently. Upgrading to a high-efficiency system can reduce your energy bills by 30% or more. And taking advantage of manufacturer rebates and utility incentives can offset the cost of new equipment.","Our team can help you identify all available savings opportunities and make informed decisions about your HVAC investments. Call us today to discuss how we can help you save."],"light"),
        related_links([("AC & Cooling","/services/ac-cooling"),("Financing","/financing"),("Contact Us","/contact")]),
    ], "Take Advantage of Our Specials\\nCall Code Blue")

# Gallery
build_page(f"{BASE}/gallery.astro",
    "HVAC Project Gallery | Code Blue HVAC | North Las Vegas",
    "View our HVAC installation and repair projects in North Las Vegas and the Las Vegas Valley. See the quality of Code Blue HVAC workmanship.",
    [
        hero_section([("Home","/"),("Gallery",None)], "Gallery", "See examples of our professional HVAC installations and projects across the Las Vegas Valley."),
        content_section("Our Work","Project","Gallery",["At Code Blue HVAC, we take pride in every installation, repair, and maintenance project we complete. Our gallery showcases the quality of workmanship you can expect when you choose Code Blue HVAC.","From residential AC installations and furnace replacements to commercial rooftop units and ductless mini-split systems, our portfolio demonstrates the range and quality of our work across the Las Vegas Valley.","Want to see more examples or discuss your specific project? Contact us today for a free consultation."]),
        content_section("Project Types","Work We","Are Proud Of",["Our project gallery includes residential AC system installations and replacements, commercial HVAC installations for offices and retail spaces, ductless mini-split system installations, ductwork replacement and repair projects, and custom HVAC solutions for unique spaces.","Each project represents our commitment to quality materials, professional installation, and customer satisfaction. We approach every job—big or small—with the same level of care and attention to detail."],"light"),
        related_links([("About Us","/about"),("Reviews","/reviews"),("Contact Us","/contact")]),
    ], "Start Your Project\\nCall Code Blue")

# Contact
build_page(f"{BASE}/contact.astro",
    "Contact Code Blue HVAC | Schedule Service | North Las Vegas",
    "Contact Code Blue HVAC for HVAC service in North Las Vegas and the Las Vegas Valley. Call (702) 887-1656 or fill out our contact form.",
    [
        hero_section([("Home","/"),("Contact",None)], "Contact Us", "Get in touch for a free estimate or to schedule HVAC service."),
        content_section("Get in Touch","Contact","Code Blue HVAC",["We are here to help with all your heating, cooling, and air quality needs. Whether you need emergency service, want to schedule maintenance, or are interested in a free estimate for a new system, our friendly team is ready to assist.","Phone: (702) 887-1656 — Available 24/7 for emergencies.","Email: info@codebluehvac.com","Address: 3612 Sandy Brown Ave, North Las Vegas, NV 89031","Facebook: facebook.com/Chris.codebluehvac"]),
        content_section("Visit or Call","Business","Information",["Code Blue HVAC is available 24 hours a day, 7 days a week for emergency HVAC service. For non-emergency consultations and estimates, we are happy to schedule at a time that works for you.","We serve all of Clark County including North Las Vegas, Las Vegas, Henderson, Summerlin, Boulder City, and Paradise. There are no extra charges for service anywhere within our coverage area.","Remember: Seniors, veterans, and first responders receive 15% off parts and labor on all services (excluding unit replacements)."],"light"),
        related_links([("AC & Cooling","/services/ac-cooling"),("Heating","/services/heating"),("Financing","/financing"),("Service Areas","/service-areas")]),
    ], "Ready to Get Comfortable?\\nCall Code Blue")


# ============================================================
# BLOG POSTS
# ============================================================
print("\\n=== Building Blog Pages ===")

# Blog Index
build_page(f"{BASE}/blog/index.astro",
    "HVAC Tips & Blog | Code Blue HVAC | North Las Vegas",
    "HVAC tips, maintenance guides, and industry insights from Code Blue HVAC. Stay informed about keeping your Las Vegas home comfortable.",
    [
        hero_section([("Home","/"),("Blog",None)], "Blog", "HVAC tips, guides, and industry insights for Las Vegas homeowners."),
        content_section("Latest Articles","HVAC Tips &","Insights",["Stay informed with the latest HVAC tips, maintenance guides, and industry updates from the Code Blue HVAC team. Our blog covers everything Las Vegas homeowners need to know about keeping their homes comfortable and energy-efficient year-round."]),
        related_links([("5 Common AC Problems","/blog/common-ac-problems"),("HVAC Maintenance Tips","/blog/hvac-maintenance-tips-las-vegas"),("When to Replace Your AC","/blog/when-to-replace-your-ac"),("AC & Cooling Services","/services/ac-cooling"),("Heating Services","/services/heating")]),
    ], "Have Questions?\\nCall Code Blue")

build_page(f"{BASE}/blog/common-ac-problems.astro",
    "5 Common AC Problems You Shouldn't Ignore | Code Blue HVAC Blog",
    "Learn about the 5 most common AC problems Las Vegas homeowners face and when to call a professional. Tips from Code Blue HVAC.",
    [
        hero_section([("Home","/"),("Blog","/blog"),("5 Common AC Problems",None)], "5 Common AC<br />Problems", "Warning signs that your air conditioner needs professional attention."),
        content_section("AC Troubles","5 AC Problems","To Watch For",["Your air conditioning system gives you warning signs before a complete breakdown. Recognizing these signs early can save you money and prevent uncomfortable situations, especially during the brutal Las Vegas summers.","1. AC Blowing Warm Air — If your AC is running but producing warm air, the cause could be low refrigerant, a dirty air filter, a faulty compressor, or a thermostat issue. Check your filter first. If that does not solve it, call a professional.","2. Unusual Noises — Grinding, squealing, banging, or rattling sounds indicate mechanical problems that will worsen over time. Do not ignore these—they often signal failing bearings, loose components, or compressor issues.","3. Frequent Cycling — If your AC turns on and off frequently without maintaining the set temperature, it could be oversized, have a refrigerant issue, or a failing thermostat. This wastes energy and puts unnecessary wear on your system.","4. Water Leaks — Water pooling around your indoor unit typically indicates a clogged condensate drain line. While this is usually an easy fix, ignoring it can lead to water damage and mold growth.","5. High Energy Bills — If your electricity bills are climbing without changes in usage, your AC may be losing efficiency due to age, lack of maintenance, or developing mechanical issues."]),
        content_section("What to Do","When to Call","A Professional",["While some issues like a dirty air filter can be handled yourself, most AC problems require professional diagnosis and repair. Attempting DIY repairs on refrigerant, electrical, or mechanical components can be dangerous and may void your warranty.","If you notice any of these warning signs, call Code Blue HVAC at (702) 887-1656 for a professional diagnosis. Our technicians provide honest assessments and upfront pricing, so you always know exactly what you are paying for."],"light"),
        related_links([("AC Repair","/services/ac-repair"),("AC Maintenance","/services/ac-maintenance"),("Emergency AC Repair","/services/emergency-ac-repair"),("When to Replace Your AC","/blog/when-to-replace-your-ac")]),
    ], "AC Acting Up?\\nCall Code Blue")

build_page(f"{BASE}/blog/hvac-maintenance-tips-las-vegas.astro",
    "HVAC Maintenance Tips for Las Vegas Homeowners | Code Blue HVAC Blog",
    "Essential HVAC maintenance tips for Las Vegas homeowners. Keep your system running efficiently in the desert climate. Tips from Code Blue HVAC.",
    [
        hero_section([("Home","/"),("Blog","/blog"),("Maintenance Tips",None)], "HVAC Maintenance<br />Tips", "Essential maintenance advice for Las Vegas homeowners."),
        content_section("Desert HVAC Care","Maintenance Tips for","Las Vegas Homes",["Living in Las Vegas puts unique demands on your HVAC system. With extreme summer heat, dusty conditions, and hard water, your heating and cooling equipment needs extra attention to perform reliably. Here are our top maintenance tips.","Change your air filter monthly during peak cooling season (May through October). Las Vegas desert dust clogs filters faster than in other climates, reducing efficiency and airflow.","Keep your outdoor condenser unit clear of debris, landscaping, and obstructions. Maintain at least 2 feet of clearance on all sides for proper airflow.","Schedule professional maintenance twice a year—spring for AC and fall for heating. A professional tune-up catches small problems before they become expensive emergencies.","Monitor your energy bills for unexpected increases, which can signal declining system efficiency or developing problems."]),
        content_section("DIY vs Professional","What You Can Do","At Home",["Some maintenance tasks are safe and easy for homeowners: changing air filters, keeping the outdoor unit clear, ensuring vents are open and unobstructed, and keeping your thermostat programmed efficiently.","However, tasks involving refrigerant, electrical components, gas connections, and internal system cleaning should always be left to licensed professionals. Improper maintenance can damage your system, void warranties, and create safety hazards."],"light"),
        related_links([("AC Maintenance","/services/ac-maintenance"),("Heating Maintenance","/services/heating-maintenance"),("Duct Cleaning","/services/duct-cleaning"),("5 Common AC Problems","/blog/common-ac-problems")]),
    ], "Schedule Maintenance\\nCall Code Blue")

build_page(f"{BASE}/blog/when-to-replace-your-ac.astro",
    "When to Replace Your AC System | Code Blue HVAC Blog",
    "How to know when it's time to replace your AC in Las Vegas. Signs, costs, and what to expect. Guide from Code Blue HVAC.",
    [
        hero_section([("Home","/"),("Blog","/blog"),("When to Replace Your AC",None)], "When to Replace<br />Your AC", "How to know when repair is no longer enough."),
        content_section("Replacement Guide","Signs It Is Time for","A New AC",["No homeowner wants to hear that their AC needs to be replaced, but continuing to repair an aging, inefficient system can cost more in the long run than investing in a new one. Here are the key signs that replacement may be the smarter choice.","Your system is over 15 years old. The average lifespan of an AC system in Las Vegas is 12-15 years due to the extreme operating conditions. If your system is approaching or exceeding this age, it is living on borrowed time.","Repair costs are adding up. A good rule of thumb: if a repair costs more than 50% of what a new system would cost, replacement usually makes better financial sense.","Your system uses R-22 refrigerant. R-22 (Freon) has been phased out and is increasingly expensive. If your system uses R-22, upgrading to a modern system with R-410A is strongly recommended.","Your energy bills keep climbing. Older systems lose efficiency over time. A new high-SEER system can reduce your cooling costs by 30-50% compared to an aging unit."]),
        content_section("Making the Decision","Repair vs","Replace",["The decision between repair and replacement is not always clear-cut, and a good HVAC contractor will give you an honest assessment rather than pushing for the most expensive option.","At Code Blue HVAC, we always explain your options clearly and let you make the decision. If a repair makes more financial sense, we will tell you. If replacement is the smarter long-term investment, we will explain why and present options at multiple price points.","We also offer financing to make new system purchases more affordable, and we can help you identify any available manufacturer rebates or energy incentives."],"light"),
        related_links([("AC Replacement","/services/ac-replacement"),("AC Installation","/services/ac-installation"),("Financing","/financing"),("5 Common AC Problems","/blog/common-ac-problems")]),
    ], "Need an AC Assessment?\\nCall Code Blue")


# ============================================================
# LEGAL PAGES
# ============================================================
print("\\n=== Building Legal Pages ===")

build_page(f"{BASE}/privacy-policy.astro",
    "Privacy Policy | Code Blue HVAC",
    "Privacy policy for Code Blue HVAC website. Learn how we collect, use, and protect your personal information.",
    [
        hero_section([("Home","/"),("Privacy Policy",None)], "Privacy Policy", "How we collect, use, and protect your personal information."),
        content_section("Privacy Policy","Your Privacy","Matters",["Code Blue HVAC (Chiller Tech Industrial Inc.) respects your privacy and is committed to protecting your personal information. This policy explains how we collect, use, and safeguard information when you visit our website or use our services.","We may collect personal information such as your name, email address, phone number, and service address when you contact us, request a consultation, or schedule service. This information is used solely to provide the services you request and to communicate with you about your HVAC needs.","We do not sell, trade, or rent your personal information to third parties. We may share information with trusted service partners only as necessary to fulfill your service requests.","Our website may use cookies and analytics tools to improve user experience and understand how visitors use our site. You can control cookie settings through your browser preferences.","If you have questions about our privacy practices, please contact us at info@codebluehvac.com or call (702) 887-1656."]),
    ], "Questions?\\nCall Code Blue")

build_page(f"{BASE}/terms-of-service.astro",
    "Terms of Service | Code Blue HVAC",
    "Terms of service for Code Blue HVAC. Read our service terms, warranty information, and policies.",
    [
        hero_section([("Home","/"),("Terms of Service",None)], "Terms of Service", "Please review our terms of service carefully."),
        content_section("Terms of Service","Service","Terms",["By using the Code Blue HVAC website and services, you agree to these terms. Code Blue HVAC (Chiller Tech Industrial Inc.) provides HVAC installation, repair, maintenance, and related services in the Las Vegas Valley area.","All services are subject to availability and scheduling. Emergency services are provided on a first-come, first-served basis with prioritization based on urgency. Estimates are provided free of charge and are valid for 30 days unless otherwise noted.","Payment is due upon completion of service unless financing has been arranged. We accept all major credit cards and offer financing options for qualifying installations.","Work performed by Code Blue HVAC is warranted according to the specific terms provided with each service or installation. Manufacturer warranties apply to equipment as specified by the manufacturer.","Code Blue HVAC is licensed, bonded, and insured in the state of Nevada. Our BBB A+ accreditation reflects our commitment to business integrity and customer satisfaction.","For questions about these terms, contact us at info@codebluehvac.com or call (702) 887-1656."]),
    ], "Questions?\\nCall Code Blue")


print("\\n=== DONE! All pages generated. ===")

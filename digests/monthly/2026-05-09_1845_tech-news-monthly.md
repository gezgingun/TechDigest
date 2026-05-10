# Tech News — Monthly Rollup
*Generated: 2026-05-09 18:45*
*Window: 2026-04-09 → 2026-05-09 (30 days, including all available daily digests)*
*Sources (local files): 2026-04-30_1745, 2026-05-02_1819, 2026-05-07_1905, 2026-05-08_1200, 2026-05-09_1200, 2026-05-09_1800*

> Note: this is the first monthly rollup for this project. No weekly digest existed at the time of generation, so the monthly is built directly from daily digests. Going forward, the agent will prefer existing weekly rollups for fully-covered weeks.

## Month at a Glance
- **The AI infrastructure map got rebuilt in real time.** Microsoft–OpenAI exclusivity ended; OpenAI landed on AWS Bedrock, then publicly retreated from first-party Stargate. Anthropic took effectively all of SpaceX Colossus 1, signed a $1.8B Akamai deal, and was simultaneously excluded from Pentagon classified-network AI as a "supply-chain risk." Hyperscaler 2026 capex guides cleared $180–190B per company; Amazon's in-house silicon hit a $20B run rate.
- **Two universal Linux root LPEs in ten days.** "Copy Fail" (Apr 29–30) and "Dirty Frag" (May 8) both grant root with public exploits, the latter unpatched at disclosure. cPanel/WHM zero-day (Apr 29) and a separate cPanel "Black Week" (May 9) bracketed the month.
- **The biggest single breach was educational, not enterprise.** ShinyHunters' Canvas/Instructure intrusion ended the month claiming data on ~275 million students at ~9,000 institutions, with a May 12 negotiation deadline.
- **GPT-5.5 shipped and immediately got more expensive.** Default model in ChatGPT on May 5; per-call costs landing 49–92% higher in the wild by May 8. Anthropic Opus 4.7 trended the same way.
- **AI is now publicly named as the reason for layoffs.** Cloudflare's 20% cut (1,100 staff) was the canonical example; Akamai surged 26% on its Anthropic deal the same day. Truecaller, Porsche, and Oracle layoffs followed different logic but compounded the narrative.
- **Policy whiplashed in both directions.** EU pushed AI Act high-risk enforcement back to Dec 2027 after industry pressure. The Trump administration began drafting an executive order requiring federal pre-release vetting of frontier AI models — a sharp reversal of earlier deregulation.
- **The cloud kept catching fire.** AWS US-EAST-1 thermal/power outage; IBM Cloud Amsterdam offline 4+ hours after a NorthC datacenter fire; Canonical DDoSed during Ubuntu 26 launch; TomTom sync wipe; Discord API outage; Iran war driving datacenter build costs +20% globally.
- **Hardware tightening.** SK hynix customers are reportedly offering hundreds of millions to fund new fab lines; motherboard sales projected -25%+ in 2026 as wafers divert to AI; HDD prices high enough to threaten the Internet Archive; Intel reportedly to fab some Apple silicon.

## Top 10 Stories of the Month
1. **Microsoft–OpenAI exclusivity ends; OpenAI lands on AWS Bedrock (4/28).** Restructured the entire AI cloud-infra landscape — Bedrock joint managed agent service, Nadella ready to "exploit" the new arrangement.
2. **Pentagon classified-network AI deals close — Anthropic excluded as a "supply-chain risk" (5/1).** Sets the procurement template for federal AI for years.
3. **"Copy Fail" + "Dirty Frag" — two universal Linux root LPEs in ten days (4/29–4/30, 5/8).** Both with public exploits; Dirty Frag unpatched at disclosure.
4. **Anthropic + SpaceX Colossus 1 deal: 220K+ GPUs, 300+ MW (5/6) → Akamai $1.8B inference deal (5/9).** Anthropic effectively re-architected its compute supply in one week.
5. **GPT-5.5 ships as ChatGPT default (5/5); pricing reality check (5/8).** 52% fewer hallucinations claimed; per-call cost up 49–92% in real workloads.
6. **ShinyHunters / Canvas — ~275M students, ~9,000 institutions (5/7–5/8).** Largest disclosed compromise of the month; May 12 negotiation deadline; multi-school individual ransom dealings reported.
7. **EU AI Act high-risk rules pushed to Dec 2027 (5/7).** Annex III enforcement delayed 16 months; Annex I to Aug 2028; deepfake/AI-content transparency *cut* from 6 to 3 months grace.
8. **Cloudflare cuts 20%, framed as the "AI replaces these jobs" moment (5/8).** Stock -19% same day; Akamai +26% on the Anthropic deal — clean ledger of who's winning the AI labor reshuffle.
9. **Trump pivots from deregulation to mandatory federal AI vetting EO (5/8).** Reversal traceable to concern over Anthropic's Mythos and the broader AI "patch tsunami."
10. **Intel reportedly to fab some Apple silicon (5/8); Intel stock +490% YoY.** The most striking semis dynamic shift in years; Apple-Intel reverse from the post-Apple-Silicon era.

## AI

### Microsoft–OpenAI restructuring; OpenAI on AWS Bedrock; Stargate retreat
The AI structural story of the month. OpenAI's models, Codex, and a jointly-built managed agent service launched on AWS Bedrock in limited preview; Satya Nadella publicly said Microsoft is ready to "exploit" the new arrangement. Tom's Hardware reported OpenAI has effectively abandoned first-party Stargate datacenters in favor of leasing — "Stargate" now an umbrella term.
**Sources:** [The Register — OpenAI on Bedrock](https://www.theregister.com/2026/04/28/openai_climbs_into_amazons_bedrock/) · [TechCrunch — Nadella](https://techcrunch.com/2026/04/29/satya-nadella-says-hes-ready-to-exploit-the-new-openai-deal/) · [Tom's Hardware — Stargate retreat](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-has-effectively-abandoned-first-party-stargate-data-centers-in-favor-of-more-flexible-deals-company-now-prefers-to-lease-compute-and-says-stargate-is-an-umbrella-term)
*Arc:* 2026-04-28 → 2026-04-30: Bedrock launch, Nadella commentary, Stargate framing shift.

### Anthropic: $50B raise rumor → 10 financial agents → SpaceX Colossus → Akamai $1.8B
A month-long arc that re-cast Anthropic's posture from "alignment-first lab" to compute and enterprise heavyweight. Pentagon's "supply-chain risk" exclusion in early May was the only material setback.
**Sources:** [TechCrunch — $50B / $900B raise rumor](https://techcrunch.com/2026/04/29/sources-anthropic-could-raise-a-new-50b-round-at-a-valuation-of-900b/) · [Anthropic — finance agents](https://www.anthropic.com/news/finance-agents) · [Anthropic — SpaceX deal](https://www.anthropic.com/news/higher-limits-spacex) · [The Register — Akamai surge](https://www.theregister.com/networks/2026/05/09/akamai-surges-on-big-llm-deal-as-cloudflare-dims/5237552)
*Arc:*
- 2026-04-29: $50B raise at $900B valuation reportedly in talks
- 2026-05-01: Pentagon excludes Anthropic from classified-network AI deals as "supply-chain risk"
- 2026-05-05: 10 vertical agents for finance (Goldman/Citi/Visa/AIG; Microsoft 365 + Moody's data)
- 2026-05-06: SpaceX Colossus 1 deal — 220K+ Nvidia GPUs, 300+ MW; Code rate limits doubled
- 2026-05-07: Mozilla credits Anthropic Mythos with finding "a wealth" of high-severity Firefox bugs
- 2026-05-08: 423-bug Firefox sweep tied to Mythos; Claude Code 1-click RCE disclosed (Anthropic disputes scope)
- 2026-05-09: Akamai signs $1.8B Anthropic inference contract; Akamai +26%

### GPT-5.5 launches, then the cost story
GPT-5.5 Instant became the default in ChatGPT and `chat-latest` in the API on May 5; Anthropic Opus 4.7 trended on similar pricing. Three days later, The Register documented 49–92% higher per-call costs in real workloads despite token-efficiency claims.
**Sources:** [OpenAI](https://openai.com/index/gpt-5-5-instant/) · [The Register — pricing](https://www.theregister.com/ai-and-ml/2026/05/08/gpt-55-may-burn-fewer-tokens-but-it-always-burns-more-cash/5237498)
*Arc:* 2026-05-05: launch · 2026-05-08: cost reality check.

### Pentagon classified-network AI deals (Anthropic excluded)
DoD signed AI-on-classified-networks deals with AWS, Microsoft, Nvidia, OpenAI, Google, SpaceX, and Reflection (Oracle added shortly after). Anthropic was excluded as a "supply-chain risk" after refusing to remove guardrails on autonomous weapons / surveillance.
**Source:** TechCrunch · [Read original](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/) · 2026-05-01

### Hyperscaler AI capex ceiling moved up — again
Q1/Q2 earnings: Alphabet raised 2026 capex to $180–190B; Microsoft pushed past $190B (with $25B attributed to component price rises rather than new builds); Amazon and Meta also lifted plans. Microsoft disclosed 20M+ paid Copilot users with engagement data; Amazon's silicon business hit a $20B run rate; Google Cloud crossed $20B but called itself capacity-constrained.
**Sources:** [TechCrunch — Google Cloud](https://techcrunch.com/2026/04/29/google-cloud-surpasses-20b-but-says-growth-was-capacity-constrained/) · [The Register — Microsoft +$25B](https://www.theregister.com/2026/04/30/microsoft_q3_2026/) · [TechCrunch — Copilot 20M](https://techcrunch.com/2026/04/29/microsoft-says-it-has-over-20m-paid-copilot-users-and-they-really-are-using-it/) · [The Register — Amazon $20B silicon](https://www.theregister.com/2026/04/29/amazon_chips_20b_business/)
*Arc:* 2026-04-28 → 2026-04-30 earnings cycle.

### Musk v. Altman trial weeks 1–2
Week 1 (5/1): Musk testified he was "duped" into funding OpenAI, warned AI "could kill us all," and admitted xAI uses model distillation from OpenAI for Grok. Week 2 (5/8): Brockman testified that Musk himself pushed OpenAI to go for-profit; Zilis testified Musk tried to poach Altman to a Tesla AI lab.
**Sources:** [MIT Tech Review — week 1](https://www.technologyreview.com/2026/05/01/1136800/musk-v-altman-week-1-musk-says-he-was-duped-warns-ai-could-kill-us-all-and-admits-that-xai-distills-openais-models/) · [MIT Tech Review — week 2](https://www.technologyreview.com/2026/05/08/1137008/musk-v-altman-week-2-openai-fires-back-and-shivon-zilis-reveals-that-musk-tried-to-poach-sam-altman/)

### Mozilla "Mythos" sweep: 423 Firefox bugs in April
Mozilla's preview integration of Anthropic's Mythos vulnerability-finding model was credited with a ~5x jump in monthly Firefox security fixes. Concrete evidence for NCSC's earlier "patch tsunami" warning.
**Sources:** [Mozilla Hacks](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/) · [The Register](https://www.theregister.com/security/2026/05/08/mozilla-says-ai-helped-squash-423-firefox-security-bugs/5235438)

### Other AI items in window
- **OpenAI shipped voice-API features, Codex Chrome plugin, and "Trusted Contact" safety** in a single week (5/7–8).
- **Perplexity Personal Computer** went free for Mac (5/7); **Bumble** killed the swipe in favor of an AI matchmaker codenamed "Bee" (5/7).
- **Google DeepMind AlphaEvolve** detailed across math/algorithms/engineering; minority stake in Eve Online's owner to train AI on player behavior (5/7–8).
- **Spotify** opened up to AI-generated personal podcasts; AI DJ added 4 languages across 75+ markets (5/7).
- **Sony + Bandai Namco** announced gen-AI in PlayStation/games pipelines (5/8).
- **Airbnb** disclosed AI now writes ~60% of new code; ~40% of customer-support tickets handled autonomously (5/8).
- **Goodfire / Silico** mechanistic-interpretability tool launched (4/30).
- **IBM** open-sourced Granite 4.1 (8B claimed competitive with 32B MoE, 4/30); shipped "Bob" coding partner to GA (4/28).
- **Meta** acquired Assured Robot Intelligence for humanoids (5/2); reportedly weighing delay of its 100% renewables 2030 goal due to AI demand (5/6).
- **Moonshot AI** raised $2B at $20B (5/7); **Pit (Voi founders)** raised $16M seed (5/7); **Coatue** launched a vehicle to buy data-center land, reportedly for Anthropic (5/1); **KKR** raised $10B for Helix data-center fund (5/1).
- **Mistral** Workflows entered public preview (4/29).
- **DeepSeek V4** near-frontier performance at fractional cost (surfaced 5/1); **ZAYA1-8B** open-weights MoE matched DeepSeek-R1 (5/7).
- **DAIMON Robotics** released the largest tactile-manipulation dataset (4/30).
- **Mozilla** formally opposed Chrome's Prompt API (4/30).
- **Snap–Perplexity $400M deal** terminated (5/6).
- **Chrome** silently installs a 4 GB on-device LLM unless users opt out (5/7).
- **Anthropic** publishes Natural Language Autoencoders (5/7) and "Teaching Claude Why" (5/8).
- **Researchers poison an LLM with a $12 domain and one Wikipedia edit** (4/29). **"Alignment whack-a-mole"** — fine-tuning re-activates copyrighted-book recall (4/30). **LLMs prefer résumés they generated** (5/2).
- **Google** $9.99/mo Gemini health coach + Fitbit Air launch slated for May 19 (5/7).

## Security

### Two universal Linux root LPEs ten days apart
**Copy Fail** (4/29–4/30): a Linux LPE chain in cryptographic code grants root with a 732-byte exploit on every major distro; patches rolling out across distros. **Dirty Frag** (5/8): a separate two-bug chain (initial analyses point at GNU IFUNC) hits Ubuntu/RHEL/Fedora/etc., with a working PoC and embargo broken before vendors could patch.
**Sources:**
- Copy Fail: [xint.io](https://xint.io/blog/copy-fail-linux-distributions) · [The Register](https://www.theregister.com/2026/04/30/linux_cryptographic_code_flaw/)
- Dirty Frag: [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/) · [The Register](https://www.theregister.com/security/2026/05/08/dirty-frag-linux-flaw-one-ups-copyfail-with-no-patches-and-public-root-exploit/5237230)

### ShinyHunters — Canvas / Instructure (~275M students)
Started as Instructure's brief "cyber incident" disclosure on May 1, escalated to mass login-portal defacement during exam week on May 7, and ended the month with KrebsOnSecurity reporting ~275M-student / ~9,000-institution scope and a May 12 deadline — with multiple universities reportedly negotiating individually.
**Source:** [KrebsOnSecurity](https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/)
*Arc:* 2026-05-01 → 2026-05-08: from quiet disclosure to the largest disclosed breach of the month.

### cPanel/WHM zero-days bracket the month
- **CVE-2026-41940** (cPanel/WHM authentication bypass) exploited in the wild since late February; PoC public; emergency patch end of April. **Patch state: action required.**
- **cPanel "Black Week"** at month's end: three new vulnerabilities patched after a ransomware-led campaign hit ~44,000 servers (5/9).
**Sources:** [BleepingComputer — Apr CVE](https://www.bleepingcomputer.com/news/security/critical-cpanel-and-whm-bug-exploited-as-a-zero-day-poc-now-available/) · [The Register — bug-of-the-year framing](https://www.theregister.com/2026/04/30/cpanel_whn_cves/) · [Copahost via HN — Black Week](https://www.copahost.com/blog/cpanels-black-week-three-new-vulnerabilities-patched-after-ransomware-attack-on-44000-servers/)

### Active enterprise zero-days: Palo Alto, Ivanti, GitHub, Windows
- **Palo Alto PAN-OS Captive Portal RCE (CVE-2026-0300)** exploited by suspected state actors for ~one month before patch (5/7).
- **Ivanti EPMM RCE** under active exploitation; CISA gave feds 4 days to patch (5/7–5/8).
- **GitHub RCE (CVE-2026-3854)** patched after Wiz disclosure — could have given attackers read/write to millions of private repos (4/29).
- **Windows zero-click info-disclosure** under active attack; CISA fed-wide patch directive (4/29).

### Supply-chain & loader compromises (this month)
- **DAEMON Tools** confirmed compromise; clean rebuild (5/6).
- **Official SAP npm packages** trojanized for credential theft (4/29; tied to TeamPCP).
- **WordPress Quick Page/Post Redirect plugin** dormant backdoor on ~70,000 sites for ~5 years (4/29).
- **Fake Claude AI site** drops new "Beagle" Windows backdoor (5/7).
- **Fake "OpenAI Privacy Filter" repo** trends on Hugging Face, drops infostealer (5/9).
- **JDownloader site compromised**, Python RAT distributed via swapped installers (5/9).

### Other notable security in window
- **vm2 sandbox** critical RCE (5/6).
- **PCPJack worm** removes rival TeamPCP malware while harvesting credentials (5/7).
- **TCLBanker malware** (Logitech installer trojan; 59 banking/crypto platforms; WhatsApp/Outlook propagation) (5/7).
- **NVIDIA GeForce NOW breach** (Armenian users) (5/8).
- **RansomHouse claims Trellix source-code theft** (5/8).
- **Zara** breach indexed on HIBP (~197K customers) (5/8).
- **Sohaib Akhter** convicted of wiping 96 federal databases minutes after firing (5/8).
- **US defense contractor Peter Williams** ordered to pay $10M for selling tools to Russia-linked broker (5/8).
- **Poland: Russian-attributed water-utility intrusions**; US warned of same TTPs (5/8).
- **Two Americans sentenced** for North-Korean "laptop farm" scheme (5/7).
- **$250M crypto-heist gang member** sentenced to 78 months (5/7).
- **Hungarian arrest** of alleged 2024 RI swatter (5/7).
- **Taiwan high-speed rail student hack** via SDR + 19 years of unrotated keys (5/7).
- **MD5 password hashes** ~60% crackable in <1 hour on a single GPU (Kaspersky, 5/7).
- **CISA flags data-theft bug in NSA-built OT tool GrassMarlin** (4/29).
- **Pitney Bowes** 8.2M-record leak (ShinyHunters) (4/28).
- **Vimeo** confirms breach via Anodot (4/28).
- **LiteLLM critical pre-auth SQLi (CVE-2026-42208)** under active exploitation (4/28).
- **"VECT 2.0" "ransomware"** is actually a wiper — encryption-nonce bug irreversibly destroys files >128 KB (4/28).
- **"30 ClawHub skills" abuse AI agents to crypto-mine** (4/29).
- **Canonical DDoS** during Ubuntu 26 launch (5/1).
- **Two transnational crypto-fraud takedowns** (US/China and Austria/Albania) (4/29–4/30).
- **3 arrested over 610,000 hijacked Roblox accounts** (4/29).
- **Sri Lanka** discloses second cyber-loss days after $2.5M finance-ministry theft (4/29).
- **Met Police's Palantir deployment** used to investigate its own officers (~600 officers) (4/30).
- **MuddyWater (Iran)** uses Chaos ransomware as a decoy (5/6).
- **Fake IT workers / North Korean laptop farm** scheme: 18-month sentences for two Americans (5/7).
- **CISA gives feds 4 days to patch Ivanti** (5/8).
- **Meta drops E2E encryption from Instagram DMs** (5/8).
- **io_uring ZCRX freelist LPE** write-up (5/8).
- **.de domain DNSSEC outage** (5/5).

## Cloud / Infra Incidents
- **AWS US-EAST-1** thermal/power event impairs EC2/EBS; FanDuel, Coinbase among casualties (5/8).
- **IBM Cloud AMS3** offline 4+ hours after a NorthC datacenter fire; status page reportedly silent during the outage (5/7).
- **Canonical** under sustained DDoS during Ubuntu 26 launch ("313 Team," Iranian hacktivists) (5/1).
- **TomTom** cloud sync wipe erases routes/locations across devices (5/7).
- **Discord** multi-hour partial API outage (5/8).
- **Iran war disrupts datacenter supply chains** — material costs +20%, availability ~25% of orders, transformer/chiller delays (5/8).
- **UK kills £35M Police National Database cloud move** after discovering only ~20% of legacy code is reusable (5/8).
- **Cloudflare Q1 internet-disruption report** notes unusually heavy disruptions (4/29).

## Hardware

### AI infrastructure stacking
- **AMD MI350P PCIe** AI accelerator: 144 GB HBM3e, 4.6 PFLOPS FP4 (5/7).
- **PCIe 8.0 draft 0.5** — 1 TB/s bidirectional, new connector, ratification 2028 (5/7).
- **Tenstorrent's RISC-V "Galaxy Blackhole"** AI servers ship — 32 accelerators in 6U for $110K (4/28).
- **Cambricon Q1 $423M** as Chinese domestic AI silicon takes share (4/30).
- **First Chinese GPU to clear Microsoft WHQL** — Lisuan Tech LX 7G100 (4/29).
- **TSMC SoIC 3D-stacking roadmap** to 4.5-micron pitch by 2029 (4/29).
- **Nvidia $300M Corning investment** (3 new US fiber plants, +50% capacity) (5/6).
- **Arm**: datacenter to be biggest segment "soon"; $2B+ committed customer demand for new AGI CPU (5/7).
- **HDD roadmap to 100 TB+** — Toshiba/Seagate/WD on three distinct paths (5/7).
- **HPE 723H** first Juniper-Aruba "self-driving" Wi-Fi 7 AP (5/8).
- **Intel reportedly to fab some Apple silicon** — preliminary deal, +490% YoY stock (5/8).
- **Sony + TSMC image-sensor JV**, including new fab (5/8).
- **SK hynix customers** offering hundreds of millions to fund new fab lines amid HBM scarcity (5/8).

### Consumer / enthusiast PC under pressure
- **Motherboard sales** projected to "collapse" 25%+ in 2026 as wafer/substrate capacity diverts to AI accelerators (5/7).
- **Framework RTX 5070 12GB module** is 72% pricier than the 8GB version due to memory crunch (4/29).
- **Sony PS5 Slim** refurb prices +$100; $399 bundles sold out — end of new $399 consoles (5/2).
- **Toto** invests in NAND-grade ceramics as an unlikely beneficiary of the memory crunch (5/1).
- **French retailer** sells transport-damaged RTX 5090s from $1,760 (5/2).
- **Nintendo Switch 2** to $499 starting September; Switch Online subs also up (5/8).
- **Internet Archive / Wayback Machine** struggling under AI-driven HDD prices (5/8).

### Other hardware in window
- **Tesla Model Y** first car to clear NHTSA's new driver-assist benchmark (5/7).
- **Lexus TZ** debuts as upscale three-row EV SUV (5/7).
- **Qualcomm Snapdragon 6 Gen 5 / 4 Gen 5** for budget phones (5/7).
- **Samsung Galaxy Watch** can predict fainting "with high accuracy" (5/7).
- **3D-printed solid rocket fuel** tested at 1,800 PSI (Chromatic 3D Materials) (5/7).
- **Valve** opens Steam Controller wave-2 reservations (5/8); CAD files released CC BY-NC-SA (5/6).
- **DJI Osmo Pocket 4P** (dual-camera) teased; **Boox Tappy** wireless page-turner; **Blackmagic Camera** Apple Watch remote (5/8).
- **LG 2026 Gram lineup** from $1,150 (5/1).
- **Apple Q2 FY26**: $111.2B revenue (+17% YoY), $100B buyback; iPhone 17 driving services to a record (5/1). Mac mini/Studio shortages tied to local-AI demand. Cheapest Mac mini appears discontinued (5/1).
- **Oura** adds birth-control side-effect tracking on Series 3/4 (5/1).
- **Light Phone III** to support a curated third-party app SDK (4/30).
- **Microsoft begins Xbox-mode rollout** to Windows 11 (5/1); CTO publicly acknowledges Win32 anchors Windows 11 (5/8).
- **Japan trials humanoid baggage handlers** at Tokyo airports (4/29).
- **Texas housing delayed 2 months** as electricians migrate to AI data centers (4/30).
- **EPFL: nanoscale device** generates continuous power from evaporating water (4/29).
- **Meta to "beam sunlight from space"** via Overview Energy (1 GW orbital reservation) (4/29).
- **Oracle 2.45 GW fuel-cell farm** for New Mexico DC (4/28).
- **Intel** reduces wafer-yield variability — more sellable dies per wafer (4/29).
- **US blocks chip-tool exports to Hua Hong** (4/29).
- **FCC permits banned drones/routers** to receive security updates through Jan 2029 (5/9).
- **Nvidia RTX Mega Geometry** tested — VRAM reduction for path-traced rendering (5/9).
- **TheA1200 retro Amiga emulator** delayed ~6 months by chip shortage (5/9).
- **Maingear MG-1 (2026)** review: clean build with personalisation (5/8).
- **Lenovo G02** retro handheld surfaces on AliExpress at ~$63 (5/8).

## Big Tech & Business

### Layoffs & restructuring
- **Cloudflare**: 20% / 1,100 staff, framed as the "agentic AI era" (5/8).
- **Oracle**: refuses severance negotiations, many laid-off staff outside WARN protections (5/8).
- **Porsche**: shutters e-bike, V4Drive battery, Porsche Digital subsidiaries; 500+ staff (5/8–5/9).
- **Truecaller**: cuts 70 jobs after 44% ad-revenue drop (5/8).
- **Xbox**: new CEO Asha Sharma kills Copilot for Gaming, restructures with CoreAI veterans (5/6).

### Other big-tech / business in window
- **Apple** loses bid to pause App Store fee changes; case heads to SCOTUS (4/29).
- **Apple Q2 FY26** earnings: $111.2B revenue, $100B buyback (5/1).
- **Uber** to convert driver fleet into a sensor grid for AV companies (5/2); adds hotel booking (4/29).
- **Reddit** reports 30% YoY jump in search engagement (5/1).
- **Atlassian** wins ITSM share at ServiceNow's expense (5/1).
- **Roku** $3 streaming "Howdy" hits 1M subs (4/29).
- **Disney** plans a unified "super-app" under new CEO Josh D'Amaro (5/7).
- **Twitch** announces viewbotting penalties (5/7).
- **Bezos rep** leaves Slate Auto's board (5/7).
- **Samsung chip workers** reject $340K bonus, threaten 18-day strike (5/7).
- **Nvidia** copyright suit over 197K pirated books survives motion to dismiss (5/7); pays $300M for three Corning US optical-fiber plants (5/6).
- **SpaceX** files for $55B semiconductor fab in rural Texas (originally announced as $20B) (5/6).
- **Lime** files for Nasdaq IPO under "LIME" (5/8).
- **InMusic acquires Native Instruments** (consolidates with Akai/Moog/M-Audio) (5/8).
- **Prime Video** adds a TikTok-like "Clips" feed (5/8).
- **Avride** (Uber AV partner) under NHTSA investigation after >12 self-driving crashes (5/8).
- **Meta** challenges Ofcom on UK fine math (UK revenue vs. global turnover) (5/8); AR/VR losses still large (4/29); buys Assured Robot Intelligence for humanoid push (5/2); reportedly weighing delay of 2030 100% renewables goal (5/6); reportedly building OpenClaw competitor that can shop on Instagram (5/7); threatened to pull apps from New Mexico over judge's pending ruling (4/30).
- **GameStop CEO eBay** account briefly banned, then restored mid-takeover stunt (5/8).
- **Bumble** drops the swipe in favor of an AI matchmaker (5/7).
- **Maryland** files complaint over a $2B grid-upgrade bill caused by out-of-state AI data centers (5/9).

## Policy & Regulation

### EU
- **AI Act high-risk rules pushed to Dec 2027** (5/7).
- **Preliminary DSA finding: Meta failed to keep under-13s off its platforms** (4/29).
- **EU ordering Google to share Android's AI sandbox** with rival assistants (4/28).
- **Open-source age-verification tool** moves forward (4/29).
- **VPNs labelled an "age-verification loophole"** (5/9).

### US
- **White House drafting EO** to require federal vetting of frontier AI models pre-release (5/7–5/8).
- **Pentagon "Department of War" UFO files site** launches (5/8).
- **Apple Epic Games App Store** changes case heads to SCOTUS (4/29).
- **Trump admin** paying offshore-wind developers up to $885M to pivot to fossil fuels (4/28).
- **Trump fires all 22 members of the National Science Board** (5/1).
- **FCC bans Chinese certification labs** from certifying US-bound electronics (5/2).
- **Maryland** files complaint over $2B grid-upgrade bill (5/9).
- **AI data-center bans:** 50 active moratoriums, 69 jurisdictions; Michigan post-Stargate; Utah senator slaps reporter's phone (5/7–5/8).
- **Pentagon classified-network AI deals** (Anthropic excluded) (5/1).
- **Cloudera charged by DoJ** over fake-email hiring scheme (4/28).
- **Academy** rules AI performances/screenplays Oscar-ineligible (5/1).
- **Radiant Mobile** launches Christian-themed US carrier with permanent network-level content blocks (5/1).

### UK / India / Other
- **NHS** restricts open-source code repos over AI vuln-discovery fears; FSF Europe pushes back (5/7).
- **UK minister** defends £330M Palantir NHS analytics contract (5/7).
- **UK Home Office** kills £35M Police National Database cloud move (5/8).
- **UK Home Office** seeking three CTOs for borders, passports, core IT (5/7).
- **UK DWP** accidentally discloses vendor doc tied to £370M procurement litigation (4/28).
- **UK breach data**: phishing still the top vector — not "AI attacks" (4/30).
- **UK NCSC**: brace for an AI-driven "patch tsunami" (5/2).
- **India**: Amazon/Meta lobby against Google Pay / PhonePe ~80% UPI duopoly (4/29).
- **Canadian regulators** allege OpenAI broke federal/provincial privacy law (5/6).
- **Databricks copyright class action** survives motion to dismiss (4/29).

## Funding & Startups
- **KKR Helix Digital Infrastructure** raises $10B+ for AI DC build/operate (5/1).
- **Coatue** launches a vehicle to buy DC land, reportedly for Anthropic (5/1).
- **SoftBank** reportedly planning $100B "Roze" AI/robotics IPO (5/1) and a separate robotics-builds-DCs spinout aiming at a $100B IPO (4/30).
- **Anthropic** reportedly raising $50B at $900B valuation (4/29).
- **Akamai signs $1.8B Anthropic inference deal**; +26% same-day stock move (5/9).
- **Moonshot AI** raises $2B at $20B (5/7).
- **Kalshi** raises $1B at $22B, doubled in 5 months (5/7).
- **Ramp** in talks at $40B+ (5/7).
- **Pit (Voi founders)** raises $16M seed (5/7).
- **Kodiak AI** raises $100M at a discount; -37% same-day (5/7).
- **Gusto** crosses $1B revenue, eyeing IPO (5/7).
- **Mother Ventures** launches with a $10M debut fund targeting moms-as-consumers (5/8).
- **Lime** files for Nasdaq IPO (5/8).
- **InMusic acquires Native Instruments** (5/8).
- **IREN buys Mirantis** (5/7).
- **Skyroot** becomes India's first space-tech unicorn (5/7).
- **QuantWare** raises $178M for superconducting QPUs (5/6).
- **Lovable** institutes automatic 10% annual raises (5/7).
- **Pursuit (gov-sales tooling)** raises $22M Series A (Bill Gurley + Jack Altman) (4/29).
- **Parallel Web Systems** hits $2B in 5 months (4/29).
- **Musely** raises $360M non-dilutive from General Catalyst (5/1).
- **Pronto (India)** closes a round after a 20-minute Lachy Groom pitch (5/6).
- **Zap Energy** adds nuclear fission to its fusion roadmap (4/29).
- **Earth AI** vertically integrates critical-mineral exploration (4/29).
- **Replit's Amjad Masad** publicly addresses the ~$60B Cursor/SpaceX deal rumor and explains why he won't sell (5/1).
- **TechCrunch's "21 European startups beyond Lovable and Mistral"** reading list (5/2).

## Open Source / Developer
- **Zed 1.0** ships (4/29).
- **Fedora 44** released (4/29).
- **Mojo 1.0 Beta** released (5/8).
- **jj 0.41** released (5/6).
- **Go 1.x FIPS 140-3** certified (surfaced 5/6).
- **Microsoft open-sources 86-DOS / PC-DOS 1.00** (4/29; 45th anniversary, 5/2).
- **Modder ships PS5-to-Linux loader** (4/30).
- **Stripe's rubyfmt** overnight-formatting writeup (5/6).
- **GitHub** apologises after the "GitHub is sinking" cycle and Hashimoto moves Ghostty off (4/29).
- **Mozilla Mythos / "Teaching Claude Why" / NLAE** (Anthropic) — interpretability/research surge in window.
- **Bambu Lab vs. OrcaSlicer-BambuLab** legal threat → fork shutdown (4/29).
- **FastCGI vs. HTTP for reverse proxies** opinion piece (4/29).
- **Zig** project anti-AI contribution policy gets attention (4/30).
- **IBM Granite 4.1** open-sourced (4/30).
- **ZAYA1-8B** open-weights MoE (5/7).
- **Raspberry Pi Connect on Windows** in limited test (5/8).
- **Simon Willison**: "vibe coding and agentic engineering are getting closer than I'd like" (5/6).

## Science
- **MIT TR**: balcony solar boom in the US (5/7); IVF tech feature pair (5/7–5/8); cruise-ship Andes virus outbreak (5/8); seafloor-hopping autonomous submersibles (5/1); Arctic seabed drilling expedition (4/30); "make a plan for nuclear waste" (4/29).
- **IEEE Spectrum**: bionic tech needs to leave the lab (5/5); Sardinia clean-energy resistance (5/7); Ana Inês Inácio profile on RF-sensor IC design (5/8).
- **DAIMON Robotics** Vision-Tactile-Language-Action dataset (4/30).
- **Anaesthetised hippocampus** still processes language — Baylor (5/7).
- **NASA Curiosity** drill stuck; Arctic seafloor recordings (5/9).
- **Craig Venter** dies at 79 (4/30).
- **NASA admin "Make Pluto A Planet Again"** (4/29).

## Consumer Apps & Services
- **YouTube** picture-in-picture rolls out worldwide for free tier (4/30).
- **Sony** clarifies no PlayStation 30-day DRM check after backlash (4/28–4/30).
- **Gemini** can now generate Word and LaTeX files directly (4/29).
- **Google Photos "Wardrobe"** auto-cataloging (4/29).
- **Motorola** unveils its first book-style foldable Razr (4/29).
- **Uber** adds hotel booking (4/29).
- **"Divine"** Vine reboot launches with a no-AI-slop policy (4/29).
- **YouTube TV** customizable multiview (4/29).
- **Microsoft tests modern Run dialog with dark mode** (5/1).

---

## Notes
- Source-list issues persisted across the month: **The Verge / Ars Technica / Wired / CNET / Reuters Tech / FT** continued to fail WebFetch — recommend pruning or replacing. **VentureBeat AI feed** has not had fresh items since January 2026 — replace. **Bloomberg / The Information** paywalled (no public RSS). **Krebs on Security / IEEE Spectrum / Import AI** publish slowly — expected silence.
- Stories flagged unconfirmed/leaked across the month: SoftBank "Roze" / robotics-DC IPO; Microsoft 2030 renewables retreat; Cursor/SpaceX acquisition referenced in the Replit interview; White House AI vetting EO; Intel-Apple fab deal — all paywalled or single-source at the time.
- This rollup is built directly from daily digests; the weekly digest agent had not yet produced a file at generation time. Future monthly runs will prefer weekly digests where they cover full weeks.

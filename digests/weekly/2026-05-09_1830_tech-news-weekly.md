# Tech News — Weekly Rollup
*Generated: 2026-05-09 18:30*
*Window: 2026-05-02 → 2026-05-09 (7 days)*
*Sources (local files): 2026-05-02_1819, 2026-05-07_1905, 2026-05-08_1200, 2026-05-09_1200, 2026-05-09_1800*

## Themes of the Week
- **Anthropic vs. the rest of the AI infra map.** Anthropic took effectively all of SpaceX Colossus 1 (220K+ GPUs, 300+ MW), signed a $1.8B Akamai inference deal, shipped 10 vertical agents for finance, but was excluded from the Pentagon's classified-network AI deals as a "supply-chain risk."
- **Two unpatched Linux root LPEs and a textbook supply-chain week.** Dirty Frag drops with a working PoC and no patches; ShinyHunters' Canvas/Instructure breach now claims data on ~275M students at ~9,000 schools; PAN-OS, Ivanti EPMM, vm2 sandbox, and DAEMON Tools all under active exploitation or post-incident.
- **OpenAI's product week + a pricing reality check.** GPT-5.5 Instant becomes ChatGPT's default; voice intelligence, Codex Chrome plugin, and "Trusted Contact" safeguard ship — but realised per-call costs land 49–92% higher than 5.x for many users.
- **AI is now the named reason for layoffs.** Cloudflare cuts 20% (~1,100) framed as the "agentic AI era," sending its stock down ~19% even on record revenue. Akamai surges 26% on the same day on the Anthropic deal. Truecaller cuts 70 on a 44% ad-revenue drop.
- **Policy whiplash.** EU pushes high-risk AI Act enforcement back to Dec 2027; the Trump administration pivots from "anything goes" to a likely EO requiring federal vetting of AI models pre-release.
- **Cloud incident streak.** AWS US-EAST-1 thermal event (FanDuel, Coinbase among casualties), IBM Cloud Amsterdam offline 4+ hours after a NorthC fire, TomTom sync wipes saved routes, Discord API outage, plus the Iran war driving datacenter build costs up ~20%.

## AI

### Anthropic + SpaceX Colossus 1 deal — and follow-ons
Anthropic took effectively all capacity at SpaceX's Colossus 1 — 220,000+ Nvidia GPUs and 300+ MW. The two parties also said they'll "explore" multi-gigawatt orbital AI compute. Anthropic doubled Claude Code's 5-hour rate limits on Pro/Max/Team/Enterprise the same day and lifted Opus API limits.
**Source:** Anthropic · [Read original](https://www.anthropic.com/news/higher-limits-spacex) · 2026-05-06
*Timeline:*
- 2026-05-06: deal announced; Code rate limits doubled
- 2026-05-07: cross-coverage at Tom's, Register, CNBC, Axios
- 2026-05-09: Akamai signs separate $1.8B Anthropic inference contract; shares jump 26%

### GPT-5.5 ships, then the cost story emerges
GPT-5.5 Instant became ChatGPT's default and `chat-latest` in the API. OpenAI claimed 52% fewer hallucinations on high-stakes prompts and ~30% shorter responses. Two days later, The Register documented per-call costs running 49–92% higher than 5.x for many real workloads. Anthropic's Opus 4.7 is showing similar increases.
**Sources:** [OpenAI announcement](https://openai.com/index/gpt-5-5-instant/) · [The Register pricing analysis](https://www.theregister.com/ai-and-ml/2026/05/08/gpt-55-may-burn-fewer-tokens-but-it-always-burns-more-cash/5237498) · 2026-05-05 → 2026-05-08

### Anthropic launches 10 vertical AI agents for banks and insurers
Pre-built agents covering pitchbooks, earnings analysis, credit memos, KYC, month-end close, statement audits and insurance claims. Co-developed with Goldman Sachs, Citi, Visa, AIG, others; FIS building AML on top; Microsoft 365 + Moody's data integrations.
**Source:** Anthropic · [Read original](https://www.anthropic.com/news/finance-agents) · 2026-05-05

### OpenAI ships voice intelligence API + Codex Chrome plugin + Trusted Contact safety
A wave of consumer/dev surface launches: voice-intelligence features in the API, a Chrome extension for Codex, and a "Trusted Contact" feature that can reach out to a designated human if conversations indicate possible self-harm.
**Source:** TechCrunch · [Voice API](https://techcrunch.com/2026/05/07/openai-launches-new-voice-intelligence-features-in-its-api/) · [Trusted Contact](https://techcrunch.com/2026/05/07/openai-introduces-new-trusted-contact-safeguard-for-cases-of-possible-self-harm/) · [Codex Chrome](https://www.engadget.com/2167480/openai-debuts-a-codex-plugin-for-chrome/) · 2026-05-07–08

### Mozilla "Mythos" boost: 423 Firefox security bugs squashed in April
Mozilla's preview integration of Anthropic's Mythos vulnerability-finding model is being credited with a ~5x jump in monthly Firefox security fixes. Researchers debate how much credit goes to Mythos vs. Mozilla's improved AI harness. Concrete evidence for NCSC's "patch tsunami" warning.
**Sources:** [Mozilla Hacks](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/) · [The Register](https://www.theregister.com/security/2026/05/08/mozilla-says-ai-helped-squash-423-firefox-security-bugs/5235438) · 2026-05-06–08

### Pentagon classified-network AI deals close — Anthropic excluded
DoD signed AI-on-classified-networks contracts with AWS, Microsoft, Nvidia, OpenAI, Google, SpaceX, and Reflection (Oracle added shortly after). Anthropic was tagged a "supply-chain risk" after refusing to remove guardrails on autonomous weapons / surveillance. The Pentagon CTO said Mythos is still being separately evaluated despite the broader exclusion.
**Source:** TechCrunch · [Read original](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/) · 2026-05-01

### AI labor shockwaves: Cloudflare -20%, Akamai +26%, Airbnb says AI writes 60% of new code
Cloudflare laid off ~1,100 (20%) framing it as restructuring for the "agentic AI era," even with 34% YoY revenue growth; stock fell ~19%. Akamai's $1.8B Anthropic deal sent it up 26% the same day. Airbnb disclosed AI now generates ~60% of new code and handles ~40% of customer-support tickets autonomously.
**Sources:** [The Register — Cloudflare](https://www.theregister.com/off-prem/2026/05/08/cloudflare-to-fire-1100-staff-whose-jobs-just-arent-ai-enough/5235536) · [The Register — Akamai surge](https://www.theregister.com/networks/2026/05/09/akamai-surges-on-big-llm-deal-as-cloudflare-dims/5237552) · [TechCrunch — Airbnb](https://techcrunch.com/2026/05/08/airbnb-says-ai-now-writes-60-of-its-new-code/) · 2026-05-08–09

### Anthropic publishes "Natural Language Autoencoders" and "Teaching Claude Why"
Two interpretability/reasoning research posts in the same week: NLAE translates internal representations into readable text; "Teaching Claude Why" trains the model to explain *why* it produces a given answer.
**Sources:** [NLAE](https://www.anthropic.com/research/natural-language-autoencoders) · [Teaching Claude Why](https://www.anthropic.com/research/teaching-claude-why) · 2026-05-07–08

### Google DeepMind: AlphaEvolve + Eve Online stake for behavior training
DeepMind detailed AlphaEvolve, a Gemini-powered coding agent applied across math/algorithms/engineering — and took a minority stake in Fenris Creations, the new owner of Eve Online, to train AI on the MMORPG's ~250K-player multi-agent economy.
**Sources:** [DeepMind / AlphaEvolve](https://deepmind.google/blog/alphaevolve-impact/) · [Tom's Hardware — Eve Online](https://www.tomshardware.com/tech-industry/artificial-intelligence/googles-deepmind-to-train-ai-on-player-actions-in-quarter-million-player-mmorpg-eve-online-google-bought-in-by-purchasing-a-minority-stake-in-the-newly-independent-fenris-creations) · 2026-05-07–08

### Perplexity Personal Computer goes free for Mac; Bumble drops the swipe for an AI matchmaker
Perplexity removed its Max-tier paywall on its desktop agent. Bumble confirmed it's killing the swipe in favor of an AI assistant codenamed "Bee."
**Sources:** [TechCrunch — Perplexity](https://techcrunch.com/2026/05/07/perplexitys-personal-computer-is-now-available-everyone-on-mac/) · [TechCrunch — Bumble](https://techcrunch.com/2026/05/07/bumble-is-getting-rid-of-the-swipe-ceo-says/) · 2026-05-07

### Spotify opens up to AI-generated personal podcasts; AI DJ goes multilingual
Users can generate personal podcasts in tools like Codex/Claude/OpenClaw and import into Spotify; AI DJ added French, German, Italian, Brazilian Portuguese across 75+ markets.
**Source:** TechCrunch · [Read original](https://techcrunch.com/2026/05/07/spotify-wants-to-become-the-home-for-ai-generated-personal-audio/) · 2026-05-07

### Other AI items in window
- **Moonshot AI** raises $2B at $20B valuation (China open-source) — 2026-05-07
- **Snap-Perplexity $400M deal** "amicably" terminated — 2026-05-06
- **Chrome silently installs a 4 GB on-device LLM** unless users opt out — 2026-05-07
- **Vision-based AI agents burn 45× more tokens than API-driven flows** — 2026-05-07
- **Pit (Voi founders' new AI startup)** raises $16M seed led by a16z — 2026-05-07
- **Musk v. Altman week 2:** Brockman testifies that Musk himself pushed OpenAI to go for-profit; Zilis says Musk tried to poach Altman to a Tesla AI lab — 2026-05-08
- **Airbnb / Spotify / Sony+Bandai** all leaning further into generative AI in their respective stacks

## Security

### "Dirty Frag" — universal Linux LPE goes public unpatched
A two-bug chain in the Linux kernel grants immediate root on Ubuntu, RHEL, Fedora, and most major distros, with a working PoC. Embargo broke before vendors could ship patches. Initial analyses point at GNU IFUNC as the underlying mechanism (drawing comparisons to xz/CVE-2024-3094).
**Source:** BleepingComputer · [Read original](https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/) · 2026-05-08
*Timeline:*
- 2026-05-08 early: oss-security advisory and Tom's Hardware coverage emerge
- 2026-05-08: BleepingComputer + The Register cross-coverage; defenders should assume widespread exploitation
- 2026-05-09: distros still rolling out patches; no CVE assigned at original disclosure

### ShinyHunters / Canvas (Instructure) — ~275M students claimed
ShinyHunters claims it pulled data from ~9,000 institutions in a fresh Instructure breach, defacing Canvas login portals during exam week. KrebsOnSecurity reports the dataset spans roughly 275 million students. Some universities are reportedly negotiating individually; ShinyHunters set a May 12 deadline.
**Source:** KrebsOnSecurity · [Read original](https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/) · 2026-05-08
*Timeline:*
- 2026-05-01: Instructure discloses initial cyber incident
- 2026-05-07: ShinyHunters defaces Canvas login pages with extortion messages
- 2026-05-08: Krebs reports dataset scope (~275M / ~9,000 schools); Engadget reports May 12 deadline

### Palo Alto PAN-OS firewall zero-day exploited ~one month before patch
CVE-2026-0300 (PAN-OS Captive Portal RCE, CVSS 9.3) abused by suspected state-sponsored actors since around April 9. No patch initially; mitigations only.
**Source:** BleepingComputer · [Read original](https://www.bleepingcomputer.com/news/security/pan-os-firewall-rce-zero-day-exploited-in-attacks-since-april-9/) · 2026-05-07

### Ivanti EPMM zero-day; CISA gives feds 4 days to patch
Ivanti disclosed an actively exploited high-severity RCE in Endpoint Manager Mobile on 5/7. CISA followed 5/8 with an emergency directive requiring federal patching within 4 days.
**Sources:** [BleepingComputer — disclosure](https://www.bleepingcomputer.com/news/security/ivanti-warns-of-new-epmm-flaw-exploited-in-zero-day-attacks/) · [BleepingComputer — CISA directive](https://www.bleepingcomputer.com/news/security/cisa-gives-feds-four-days-to-patch-ivanti-flaw-exploited-as-zero-day/) · 2026-05-07–08

### Other notable security in window
- **vm2 sandbox critical bug** allows host RCE; widely embedded library — 2026-05-06
- **DAEMON Tools** confirmed supply-chain compromise; clean rebuild shipped — 2026-05-06
- **PCPJack worm** removes rival TeamPCP malware while harvesting credentials and self-propagating across cloud infra — 2026-05-07
- **TCLBanker malware** self-propagates over WhatsApp/Outlook via a trojanised Logitech installer; targets 59 banking/crypto platforms — 2026-05-07
- **NVIDIA GeForce NOW breach** affecting Armenian users — 2026-05-08
- **RansomHouse claims Trellix source-code theft** — 2026-05-08
- **Zara breach** (~197K customers) indexed on HIBP — 2026-05-08
- **Sohaib Akhter convicted** of wiping 96 federal databases minutes after being fired — 2026-05-08
- **US defense contractor Peter Williams** ordered to pay $10M for selling tools to a Russia-linked broker — 2026-05-08
- **Poland: Russian-attributed water-utility intrusions**, US warned of same TTPs — 2026-05-08
- **Fake Claude AI site / "Beagle" Windows backdoor** — 2026-05-07
- **Fake "OpenAI Privacy Filter" repo** trends on Hugging Face, drops infostealer — 2026-05-09
- **JDownloader site compromised**, Python RAT distributed via swapped installers — 2026-05-09
- **cPanel "Black Week"** — three new vulnerabilities patched after a ransomware-led campaign hit ~44,000 servers — 2026-05-09
- **Meta drops E2E encryption from Instagram DMs**, citing low adoption, steers users to WhatsApp — 2026-05-08
- **io_uring ZCRX freelist LPE** — new write-up of a Linux kernel privesc — 2026-05-08
- **Two Americans sentenced** for running North-Korean "laptop farm" remote-IT scheme — 2026-05-07
- **$250M crypto-heist gang member** sentenced to 6.5 years — 2026-05-07
- **Hungarian arrest** of alleged 2024 Rhode Island swatter — 2026-05-07
- **Taiwan high-speed rail student hack** via SDR + 19 years of unrotated keys — 2026-05-07
- **MD5 password hashes** — Kaspersky finds ~60% crackable in <1 hour on a single GPU — 2026-05-07

## Cloud / Infra Incidents

### AWS US-EAST-1 thermal event takes hours to clear
Power loss in AWS's most-troubled region impaired EC2 and EBS. FanDuel, Coinbase, and many other services took knock-on hits.
**Source:** The Register · [Read original](https://www.theregister.com/off-prem/2026/05/08/aws-warns-of-ec2-impairment-as-power-loss-hits-notorious-us-east-1-region/5235509) · 2026-05-08

### IBM Cloud AMS3 down 4+ hours after NorthC datacenter fire
Building evacuated, status page reportedly silent during the outage. No injuries.
**Source:** The Register · [Read original](https://www.theregister.com/off-prem/2026/05/07/ibm-cloud-evaporates-as-datacenter-loses-power/5234835) · 2026-05-07

### Iran war disrupts datacenter supply chains; build costs +20%
Strait of Hormuz closure has driven build-material costs up ~20% with availability down to ~25% of orders. Critical equipment (transformers, chillers) is delayed by months — Middle East buildouts hit hardest.
**Source:** The Register · [Read original](https://www.theregister.com/on-prem/2026/05/08/iran-war-disrupts-datacenter-construction-supply-chains-raises-material-costs/5235852) · 2026-05-08

### TomTom cloud sync wipes saved routes; Discord API outage
TomTom backend issue (reportedly AWS-linked) erased synced routes, locations, and favourites across user devices. Discord had a separate multi-hour partial outage tied to API systems.
**Sources:** [The Register — TomTom](https://www.theregister.com/personal-tech/2026/05/07/tomtoms-route-planner-takes-an-unplanned-detour-into-oblivion/5234813) · [Engadget — Discord](https://www.engadget.com/2168231/discord-is-down-for-some-users/) · 2026-05-07–08

### UK kills £35M Police National Database cloud move
Home Office abandoned the migration after discovering only ~20% of legacy code was reusable instead of the projected 80%; database stays on-prem with stability fixes only.
**Source:** The Register · [Read original](https://www.theregister.com/public-sector/2026/05/08/uk-abandons-police-database-cloud-move-after-35m-transformation-stalls/5235718) · 2026-05-08

## Hardware

### AMD MI350P PCIe AI accelerator launches
A slottable PCIe Instinct GPU: 144 GB HBM3e, 4.6 PFLOPS FP4, dual-slot. Pitched at enterprises that won't deploy OAM. AMD claims notable lead over Nvidia H200 NVL on FP16/FP8.
**Source:** Tom's Hardware · [Read original](https://www.tomshardware.com/pc-components/gpus/amd-announces-mi350p-pcie-ai-accelerator-card-with-144gb-of-hbm3e-roughly-40-percent-faster-in-fp16-and-fp8-theoretical-compute-compared-to-nvidias-h200-nvl-competitor) · 2026-05-07

### PCIe 8.0 draft 0.5 — 1 TB/s, new connector
PCI-SIG released the first PCIe 8.0 draft targeting ~1 TB/s aggregate bidirectional across 16 lanes, plus a new connector and 0.5V signalling. Final ratification slated for 2028; shipping silicon later.
**Source:** The Register · [Read original](https://www.theregister.com/storage/2026/05/07/official-pcie-80-draft-aims-for-1-tb/s-data-rate/5234648) · 2026-05-07

### Intel reportedly inks preliminary deal to fab Apple silicon
Intel Foundry will reportedly produce some Apple chips — a striking reversal of the post-Apple-Silicon dynamic. *(Reported, not officially confirmed.)* Intel shares are up ~490% YoY on the broader foundry-comeback narrative.
**Sources:** [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/apple-reportedly-strikes-deal-for-intel-to-make-some-of-its-chips-two-tech-giants-reached-a-preliminary-agreement-for-intel-to-make-processors-for-cupertino) · [TechCrunch — Intel rally](https://techcrunch.com/2026/05/08/intels-comeback-story-is-even-wilder-than-it-seems/) · 2026-05-08

### Sony + TSMC image-sensor JV
Sony and TSMC are forming a joint venture for image-sensor manufacturing including a new fab — unusual for Sony, which has historically run image-sensor fabs in-house.
**Source:** Engadget · [Read original](https://www.engadget.com/2167681/sony-tsmc-image-sensor-joint-venture/) · 2026-05-08

### Nintendo raising Switch 2 to $499 in September; Switch Online subs also up
Cited chip-supply pressure; pre-September buyers avoid the hike.
**Sources:** [Tom's Hardware](https://www.tomshardware.com/video-games/nintendo/nintendo-is-raising-the-price-of-the-switch-2-by-usd50-starting-in-september-console-will-soon-cost-usd499-but-you-can-avoid-the-price-hike-if-you-buy-now) · [Engadget](https://www.engadget.com/2167631/nintendo-raises-switch-2-prices/) · 2026-05-08

### SK hynix customers reportedly offering hundreds of millions to fund new fab lines
With memory capacity hitting effectively zero, large customers are reportedly offering to buy EUV machines outright and fund new fab lines to secure HBM supply. Vivid signal of the AI memory crunch.
**Source:** Tom's Hardware · [Read original](https://www.tomshardware.com/tech-industry/sk-hynix-customers-offer-to-buy-its-euv-machines-and-fund-new-fab-lines-as-memory-capacity-hits-zero) · 2026-05-08

### Other hardware in window
- **Motherboard sales** projected to drop 25%+ in 2026 as wafer/substrate capacity diverts to AI accelerators — 2026-05-07
- **HDD roadmap to 100 TB+** — Toshiba/Seagate/WD on three distinct technology paths (AI training-data storage demand) — 2026-05-07
- **Tesla Model Y first car** to clear NHTSA's new driver-assist benchmark — 2026-05-07
- **Lexus TZ** debuts as upscale three-row EV SUV — 2026-05-07
- **Qualcomm Snapdragon 6 Gen 5 / 4 Gen 5** for budget phones — 2026-05-07
- **HPE 723H** first Juniper-Aruba "self-driving" Wi-Fi 7 AP — 2026-05-08
- **Internet Archive / Wayback Machine** struggling under AI-driven HDD prices — 2026-05-08
- **Microsoft CTO** publicly acknowledges Win32 (mid-90s code) still anchors Windows 11 — 2026-05-08
- **DJI Osmo Pocket 4P** (dual-camera gimbal) teased; **Boox Tappy** wireless page-turner; **Blackmagic Camera** Apple Watch remote — 2026-05-08
- **FCC permits** banned drones/routers to receive security updates through Jan 2029 — 2026-05-09
- **Nvidia RTX Mega Geometry** tested — VRAM reduction for path-traced rendering — 2026-05-09

## Big Tech & Business

### Cloudflare cuts 20% framed as the "AI replaces these jobs" moment
Workforce -1,100, stock -19% on the news despite 34% YoY revenue growth. Coverage hardened over two days from "restructuring" to "AI made these jobs obsolete."
**Sources:** [The Register](https://www.theregister.com/off-prem/2026/05/08/cloudflare-to-fire-1100-staff-whose-jobs-just-arent-ai-enough/5235536) · [Tom's Hardware — 6× AI usage](https://www.tomshardware.com/tech-industry/big-tech/cloudflare-cuts-20-percent-of-its-jobs-due-to-ai-and-its-stock-takes-a-19-percent-spill-1-100-jobs-disappearing-as-company-increased-usage-of-ai-sixfold-over-past-months) · 2026-05-08–09

### Oracle refuses severance negotiations; many laid-off workers outside WARN protection
Oracle declined severance discussions with terminated staff, some classified as remote in ways that put them outside WARN Act protections.
**Source:** TechCrunch · [Read original](https://techcrunch.com/2026/05/08/laid-off-oracle-workers-tried-to-negotiate-better-severance-oracle-said-no/) · 2026-05-08

### Porsche shutters e-bike, battery, and software subsidiaries
Three subsidiaries (Porsche eBike Performance, V4Drive, Porsche Digital) closed; 500+ staff affected. Refocus on core auto operations.
**Sources:** [TechCrunch](https://techcrunch.com/2026/05/08/porsche-shutters-e-bike-battery-software-subsidiaries-as-part-of-company-overhaul/) · [Engadget — e-bike specifically](https://www.engadget.com/2168638/porsche-is-discontinuing-its-performance-ebike-division/) · 2026-05-08–09

### Lime files for Nasdaq IPO; InMusic acquires Native Instruments
Uber-backed Lime filed under ticker "LIME"; InMusic (Akai/Moog/M-Audio parent) acquired Native Instruments — major music-tech consolidation.
**Sources:** [TechCrunch — Lime](https://techcrunch.com/2026/05/08/lime-the-uber-backed-micromobility-company-files-for-ipo/) · [Engadget — InMusic](https://www.engadget.com/2168045/inmusic-will-acquire-native-instruments-putting-it-under-the-same-umbrella-as-akai/) · 2026-05-08

### Other big-tech / business in window
- **Disney "super-app"** consolidation reportedly under new CEO Josh D'Amaro — 2026-05-07
- **Twitch** announces viewbotting penalties — 2026-05-07
- **Bezos rep leaves Slate Auto's board** — 2026-05-07
- **Xbox CEO Asha Sharma** kills Copilot for Gaming, restructures with CoreAI veterans — 2026-05-06
- **Samsung chip workers** reject $340K bonus, demand annual payouts; threatened 18-day strike could cost $11.7B — 2026-05-07
- **Nvidia copyright suit over 197K pirated books** survives motion to dismiss — 2026-05-07
- **Nvidia $300M Corning investment** for three new US optical-fiber plants — 2026-05-06
- **SpaceX** files for $55B semiconductor fab in rural Texas (well above original $20B figure) — 2026-05-06
- **Truecaller** cuts 70 jobs after 44% ad-revenue drop — 2026-05-08
- **Avride** under NHTSA investigation after >12 self-driving crashes — 2026-05-08
- **Meta vs. Ofcom** dispute on UK fine math (UK revenue vs. global turnover) — 2026-05-08
- **GameStop CEO** eBay account briefly banned then restored mid-takeover stunt — 2026-05-08
- **Prime Video** adds a TikTok-like "Clips" feed — 2026-05-08

## Policy & Regulation

### EU AI Act high-risk rules pushed to Dec 2027
Council and Parliament agreed to delay Annex III enforcement from Aug 2026 to Dec 2, 2027 (Annex I to Aug 2028). Deepfake/AI-content transparency grace period was *cut* from 6 to 3 months (now Dec 2, 2026). Officials called this the last delay.
**Sources:** [Council of the EU](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/) · [The Register](https://www.theregister.com/ai-and-ml/2026/05/07/eu-hits-snooze-on-ai-act-rules-after-industry-backlash/5230530) · 2026-05-07

### Trump pivots: from deregulation to mandatory federal AI vetting
The Trump administration is reportedly drafting an EO requiring federal pre-release review of frontier AI models — a sharp reversal of earlier deregulatory directives. Widely tied to concern about Anthropic's Mythos. *(Reported, not finalised.)*
**Source:** The Register · [Read original](https://www.theregister.com/ai-and-ml/2026/05/08/trump-jumps-from-anything-goes-to-strict-regulation-ai-policy/5234687) · 2026-05-08

### EU pushes to close VPNs as an "age-verification loophole"
Regulators publicly call VPNs a loophole that needs closing as DSA-style age-verification rolls out. Tom's Hardware notes VPN downloads on one app surged ~1,800% in the UK after the Online Safety Act took effect.
**Sources:** [CyberInsider via HN](https://cyberinsider.com/eu-calls-vpns-a-loophole-that-needs-closing-in-age-verification-push/) · [Tom's Hardware](https://www.tomshardware.com/software/vpn/eu-research-arm-labels-vpns-a-loophole-as-age-verification-laws-drive-record-adoption) · 2026-05-09

### Other policy in window
- **Pentagon (now "Department of War") UFO files site** launches — 2026-05-08
- **AI data-center bans:** 50 active moratoriums, 69 jurisdictions; Michigan post-Stargate; Utah senator slaps reporter's phone over Box Elder fight — 2026-05-07–08
- **Maryland files complaint** over a $2B grid-upgrade bill being passed to ratepayers for out-of-state AI data-center load — 2026-05-09
- **NHS code clampdown** vs. open-source community — 2026-05-07
- **UK minister defends £330M Palantir NHS contract** — 2026-05-07
- **Canadian regulators** allege OpenAI broke federal/provincial privacy law — 2026-05-06
- **Academy** rules AI-generated performances and screenplays ineligible for Oscars — 2026-05-01
- **FCC bans Chinese certification labs** from certifying US-bound electronics — 2026-05-02

## Funding

- **Akamai signs $1.8B Anthropic inference deal**; stock +26% — 2026-05-09
- **Kalshi** raises $1B Series F at $22B (doubled in 5 months) — 2026-05-07
- **Ramp** in talks at $40B+ (up from $32B in November) — 2026-05-07
- **Kodiak AI** raises $100M at a discount; stock falls 37% — 2026-05-07
- **Pit (Voi founders' new AI startup)** raises $16M seed led by a16z — 2026-05-07
- **Gusto** crosses $1B revenue, eyeing IPO — 2026-05-07
- **IREN buys Mirantis** — 2026-05-07
- **Mother Ventures** launches with $10M debut fund targeting moms as consumers — 2026-05-08
- **Skyroot** becomes India's first space-tech unicorn — 2026-05-07
- **QuantWare** raises $178M for superconducting QPUs — 2026-05-06
- **Moonshot AI** raises $2B at $20B valuation — 2026-05-07

## Open Source / Dev

- **Mojo 1.0 Beta** released — 2026-05-08
- **jj 0.41** released — 2026-05-06
- **Go 1.x** earns NIST FIPS 140-3 certification — surfaced 2026-05-06
- **Stripe** publishes rubyfmt overnight-formatting writeup — surfaced 2026-05-06
- **Anthropic "Teaching Claude Why"** + Natural Language Autoencoders (interpretability) — 2026-05-07–08
- **Raspberry Pi Connect on Windows** enters limited test — 2026-05-08
- Various Lobsters / HN reads: NixOS secrets, Steering Zig fmt, SSH MITM mitigation, "I've banned query strings" — 2026-05-08–09

## Science

- **MIT TR — IVF tech feature pair** (vitrification, AI/robotics, gene editing); also **balcony solar boom in the US** — 2026-05-07–08
- **MIT TR — cruise-ship Andes virus outbreak** (8 passengers, 3 deaths, framed as limited if controlled) — 2026-05-08
- **IEEE Spectrum** profile of Ana Inês Inácio (RF-sensor IC design) — 2026-05-08
- **Sardinia clean-energy resistance** (long read) — 2026-05-07
- **Anaesthetised hippocampus** still processes language (Baylor) — 2026-05-07
- **3D-printed solid rocket fuel** tested at 1,800 PSI — 2026-05-07
- **NASA Curiosity drill stuck**; Arctic seafloor recordings (Engadget weekly science roundup) — 2026-05-09

---

## Notes
- This rollup synthesises five daily digests; it is not a fresh internet scan.
- For older items still in the rolling 30-day window (e.g., Ubuntu 26 / Canonical DDoS, KKR Helix $10B, Pentagon AI deals follow-up), see the daily digests at `digests/2026-05-02_1819` and earlier.
- Same upstream blockers as the daily digests: Verge / Ars Technica / Wired / CNET / Reuters / FT remain unreachable via WebFetch; VentureBeat AI feed stale; Bloomberg / The Information paywalled.

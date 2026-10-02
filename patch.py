import os, re, threading, time, gc, ctypes

# 🛡️ 1. Ultra RAM Guard (150 Bots Capacity)
def ram_guard():
    try:
        libc = ctypes.CDLL('libc.so.6')
        while True:
            time.sleep(60)
            gc.collect()
            libc.malloc_trim(0)
    except Exception:
        pass

t = threading.Thread(target=ram_guard, daemon=True)
t.start()
print("🚀 24/7 Monster RAM Guard Activated!")

# 🔒 2. Admin Password Protection for server.ts
admin_middleware = """
const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || "amrit@admin99";
app.use((req, res, next) => {
    const isInstanceRoute = req.path.includes("/api/instances") || req.path.includes("/api/bots");
    if (isInstanceRoute) {
        const clientPass = req.headers["x-admin-pass"] || req.query.adminPass;
        if (req.method === "POST") return next();
        if (clientPass !== ADMIN_PASSWORD) {
            if (req.method === "GET") return res.json([]);
            return res.status(403).json({ error: "Unauthorized! Only Admin can manage bots." });
        }
    }
    next();
});
"""

if os.path.exists("server.ts"):
    with open("server.ts", "r", encoding="utf-8", errors="ignore") as f:
        s = f.read()
    if "const ADMIN_PASSWORD" not in s:
        pattern = r"(app\s*=\s*express\(\);?)"
        if re.search(pattern, s):
            s = re.sub(pattern, r"\1\n" + admin_middleware, s, count=1)
            with open("server.ts", "w", encoding="utf-8") as f:
                f.write(s)

# 👹 3. Monster Intro Splash Screen & Powerful Beast Dark Theme
monster_theme_and_splash = """
<style id="mental-monster-theme">
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Rajdhani:wght@600;700&display=swap');

/* --- MONSTER BEAST THEME OVERRIDE --- */
body {
  background-color: #06080d !important;
  background-image: 
    radial-gradient(circle at 50% 5%, rgba(255, 0, 85, 0.18), transparent 45%),
    radial-gradient(circle at 90% 90%, rgba(0, 255, 136, 0.12), transparent 45%),
    linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px) !important;
  background-size: 100% 100%, 100% 100%, 28px 28px, 28px 28px !important;
  color: #e2e8f0 !important;
  font-family: 'Rajdhani', sans-serif !important;
}

/* Monster Armor Cards */
.bg-slate-800, .bg-slate-900, .bg-gray-800, .bg-gray-900, [class*="card"] {
  background: linear-gradient(135deg, rgba(13, 18, 30, 0.95), rgba(6, 8, 14, 0.98)) !important;
  border: 1px solid rgba(255, 0, 85, 0.45) !important;
  box-shadow: 0 0 25px rgba(255, 0, 85, 0.18), inset 0 0 15px rgba(0, 255, 136, 0.06) !important;
  border-radius: 14px !important;
}

h1, h2, h3, .font-bold {
  font-family: 'Orbitron', sans-serif !important;
}

h1 {
  color: #ffffff !important;
  text-shadow: 0 0 12px #ff0055, 0 0 25px rgba(255, 0, 85, 0.7) !important;
}

button, .btn-primary {
  font-family: 'Orbitron', sans-serif !important;
  letter-spacing: 1px !important;
}

/* --- MONSTER INTRO SPLASH --- */
#mental-splash {
  position: fixed;
  inset: 0;
  z-index: 9999999;
  background: radial-gradient(circle at center, #101422 0%, #030406 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: opacity 0.8s ease, visibility 0.8s ease;
  overflow: hidden;
  font-family: 'Orbitron', sans-serif;
  user-select: none;
}

#mental-splash.hide-splash {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.monster-beast-icon {
  width: 140px;
  height: 140px;
  animation: monster-pulse 2s infinite ease-in-out;
  filter: drop-shadow(0 0 25px #ff0055) drop-shadow(0 0 45px rgba(0, 255, 136, 0.5));
}

@keyframes monster-pulse {
  0%, 100% { transform: scale(1); filter: drop-shadow(0 0 25px #ff0055); }
  50% { transform: scale(1.08); filter: drop-shadow(0 0 40px #00ff88) drop-shadow(0 0 60px #ff0055); }
}

.monster-title {
  font-size: 42px;
  font-weight: 900;
  letter-spacing: 8px;
  color: #fff;
  text-shadow: 0 0 15px #ff0055, 0 0 35px #ff0055, 0 0 60px #00ff88;
  margin-top: 15px;
}

.monster-subtitle {
  font-family: 'Rajdhani', sans-serif;
  font-size: 14px;
  letter-spacing: 4px;
  color: #00ff88;
  font-weight: 700;
  margin-top: 4px;
  text-transform: uppercase;
  text-shadow: 0 0 10px rgba(0, 255, 136, 0.7);
}

.monster-progress-container {
  width: 220px;
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  margin-top: 25px;
  overflow: hidden;
  border: 1px solid rgba(255, 0, 85, 0.5);
  box-shadow: 0 0 15px rgba(255, 0, 85, 0.4);
}

.monster-progress-bar {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #ff0055, #00ff88);
  box-shadow: 0 0 12px #00ff88;
  transition: width 1.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.monster-status-text {
  font-size: 11px;
  color: #94a3b8;
  margin-top: 10px;
  letter-spacing: 2px;
}
</style>

<!-- MONSTER INTRO SPLASH HTML -->
<div id="mental-splash">
  <svg class="monster-beast-icon" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M50 5 L65 25 L85 20 L75 42 L92 52 L78 68 L82 92 L50 82 L18 92 L22 68 L8 52 L25 42 L15 20 L35 25 Z" fill="#0d111a" stroke="#ff0055" stroke-width="2.5"/>
    <path d="M15 20 L25 42 L35 25" stroke="#00ff88" stroke-width="2" stroke-linecap="round"/>
    <path d="M85 20 L75 42 L65 25" stroke="#00ff88" stroke-width="2" stroke-linecap="round"/>
    <polygon points="32,45 44,48 35,53" fill="#00ff88"/>
    <polygon points="68,45 56,48 65,53" fill="#00ff88"/>
    <circle cx="38" cy="49" r="1.5" fill="#fff"/>
    <circle cx="62" cy="49" r="1.5" fill="#fff"/>
    <polygon points="40,66 43,74 46,66" fill="#ff0055"/>
    <polygon points="47,66 50,76 53,66" fill="#00ff88"/>
    <polygon points="54,66 57,74 60,66" fill="#ff0055"/>
    <path d="M30 64 Q50 60 70 64" stroke="#ff0055" stroke-width="2"/>
    <polygon points="50,22 56,32 50,40 44,32" fill="#ff0055"/>
    <circle cx="50" cy="31" r="2.5" fill="#00ff88"/>
  </svg>

  <div class="monster-title">MENTAL</div>
  <div class="monster-subtitle">⚡ 24/7 ULTRA MONSTER CORE ⚡</div>

  <div class="monster-progress-container">
    <div class="monster-progress-bar" id="mental-bar"></div>
  </div>
  <div class="monster-status-text" id="mental-status">INITIALIZING MONSTER CORE...</div>
</div>

<script>
// Animate and Dismiss Splash Screen
(function(){
  var splash = document.getElementById('mental-splash');
  var bar = document.getElementById('mental-bar');
  var status = document.getElementById('mental-status');
  if(!splash || !bar) return;

  setTimeout(function(){
    bar.style.width = '65%';
    status.innerText = 'OVERCLOCKING MONSTER ENGINES...';
  }, 200);

  setTimeout(function(){
    bar.style.width = '100%';
    status.innerText = '⚡ MONSTER SYSTEM ONLINE 100% ⚡';
  }, 1100);

  setTimeout(function(){
    splash.classList.add('hide-splash');
    setTimeout(function(){ splash.remove(); }, 800);
  }, 2000);

  splash.onclick = function(){
    splash.classList.add('hide-splash');
    setTimeout(function(){ splash.remove(); }, 500);
  };
})();
</script>

<!-- Floating Admin Lock Button -->
<script>
(function(){
  var p = localStorage.getItem("amrit_admin_pass");
  var b = document.createElement("button");
  b.id = "amrit-admin-btn";
  b.innerHTML = p ? "🛡️ Monster Admin Active" : "🔒 Admin Access";
  b.style.cssText = "position:fixed;bottom:18px;right:18px;z-index:999999;padding:10px 18px;background:" + (p ? "linear-gradient(135deg, #059669, #10b981)" : "linear-gradient(135deg, #e11d48, #be123c)") + ";color:#ffffff;border-radius:30px;font-size:13px;font-weight:900;border:2px solid #ffffff;cursor:pointer;box-shadow:0 0 20px " + (p ? "#10b981" : "#e11d48") + ";font-family:'Orbitron',sans-serif;letter-spacing:1px;";
  b.onclick = function(){
    var cur = localStorage.getItem("amrit_admin_pass");
    if(cur){
      if(confirm("Logout from Monster Admin mode?")){
        localStorage.removeItem("amrit_admin_pass");
        location.href = location.pathname;
      }
    } else {
      var pass = prompt("Enter Master Admin Password:");
      if(pass === "amrit@admin99"){
        localStorage.setItem("amrit_admin_pass", pass);
        alert("⚡ WELCOME MASTER AMRIT! Monster Admin Panel Online.");
        location.search = "?adminPass=" + pass;
      } else if(pass){
        alert("❌ ACCESS DENIED! Invalid Password.");
      }
    }
  };
  window.addEventListener("DOMContentLoaded", function(){ document.body.appendChild(b); });
  if(document.body) document.body.appendChild(b);

  if(p && !location.search.includes("adminPass=")){
    location.search = "?adminPass=" + p;
  }
})();
</script>
"""

for h in ["index.html", "public/index.html"]:
    if os.path.exists(h):
        with open(h, "r", encoding="utf-8", errors="ignore") as f:
            hc = f.read()
        if "mental-monster-theme" not in hc:
            hc = hc.replace("</body>", monster_theme_and_splash + "\n</body>")
            with open(h, "w", encoding="utf-8") as f:
                f.write(hc)
            print("Monster Splash & UI Injected in", h)

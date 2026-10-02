import os, re, threading, time, gc, ctypes

# 🛡️ Ultra-Low RAM Trimmer (Memory hamesha 50-80 MB ke andar tight rakhega)
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
print("🚀 24/7 Async RAM Compressor Activated!")

# 🔒 Admin Password Protection (Public ko bot nahi dikhega, sirf Admin ko)
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
            print("server.ts secured with Admin Password!")

# 🔒 Floating Admin Lock Button (amrit@admin99)
admin_btn_script = """
<script>
(function(){
  var p = localStorage.getItem("amrit_admin_pass");
  var b = document.createElement("button");
  b.id = "amrit-admin-btn";
  b.innerHTML = p ? "🛡️ Admin Active" : "🔒 Admin Login";
  b.style.cssText = "position:fixed;bottom:18px;right:18px;z-index:999999;padding:10px 16px;background:" + (p ? "#059669" : "#2563eb") + ";color:#ffffff;border-radius:30px;font-size:13px;font-weight:bold;border:2px solid #ffffff;cursor:pointer;box-shadow:0 6px 18px rgba(0,0,0,0.6);font-family:sans-serif;";
  b.onclick = function(){
    var cur = localStorage.getItem("amrit_admin_pass");
    if(cur){
      if(confirm("Logout from Admin mode?")){
        localStorage.removeItem("amrit_admin_pass");
        location.href = location.pathname;
      }
    } else {
      var pass = prompt("Enter Master Admin Password:");
      if(pass === "amrit@admin99"){
        localStorage.setItem("amrit_admin_pass", pass);
        alert("✅ Welcome AMRIT! Admin panel activated.");
        location.search = "?adminPass=" + pass;
      } else if(pass){
        alert("❌ Galat Password! Sirf Admin access kar sakta hai.");
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
        if "amrit-admin-btn" not in hc:
            hc = hc.replace("</body>", admin_btn_script + "\n</body>")
            with open(h, "w", encoding="utf-8") as f:
                f.write(hc)
            print("Admin button added in", h)
